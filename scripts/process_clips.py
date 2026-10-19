#!/usr/bin/env python3
"""
Herramienta de Auditoría Técnica, Respaldo Inmutable y Nivelación de Audio Foley
para la Skill de Producción: cocina-audiovisual-flow.

Funciones principales:
1. Inspección técnica de clips (resolución, framerate, duración y audio).
2. Respaldo inmutable automático en assets_flow/originals_raw/ (sin sobreescritura).
3. Detección de picos máximos con ffmpeg volumedetect.
4. Nivelación de audio por lotes al objetivo canónico (-10.0 dBFS) con `ffmpeg -c:v copy`
   (sin recodificar video, 100% fidelidad visual instantánea).

Uso:
  python3 process_clips.py --project projects/P006_poorboy_mega_sandwich
  python3 process_clips.py --dir path/to/assets_flow --target-peak -10.0
"""

import argparse
import os
import re
import shutil
import subprocess
import sys


def check_tool(tool_name):
    """Verifica si una herramienta CLI está disponible en el PATH."""
    path = shutil.which(tool_name)
    if not path:
        print(f"❌ Error: La herramienta obligatoria '{tool_name}' no está instalada o no está en el PATH.", file=sys.stderr)
        sys.exit(1)
    return path


def probe_clip(ffprobe_bin, file_path):
    """Extrae metadatos técnicos del clip de video."""
    cmd = [
        ffprobe_bin,
        "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height,r_frame_rate,duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        file_path,
    ]
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True).strip().splitlines()
        w = int(out[0]) if len(out) > 0 and out[0].isdigit() else 0
        h = int(out[1]) if len(out) > 1 and out[1].isdigit() else 0
        fps_str = out[2] if len(out) > 2 else "0/0"
        dur = float(out[3]) if len(out) > 3 else 0.0

        if "/" in fps_str:
            num, den = fps_str.split("/")
            fps = float(num) / float(den) if float(den) != 0 else 0.0
        else:
            fps = float(fps_str)
        return {"width": w, "height": h, "fps": round(fps, 2), "duration": round(dur, 2)}
    except Exception as e:
        return {"width": 0, "height": 0, "fps": 0.0, "duration": 0.0, "error": str(e)}


def detect_max_volume(ffmpeg_bin, file_path):
    """Mide el pico máximo de volumen (max_volume) usando el filtro volumedetect."""
    cmd = [
        ffmpeg_bin,
        "-hide_banner",
        "-nostats",
        "-i", file_path,
        "-af", "volumedetect",
        "-vn", "-sn", "-dn",
        "-f", "null",
        "/dev/null" if os.name != "nt" else "NUL",
    ]
    res = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.DEVNULL, text=True)
    match = re.search(r"max_volume:\s*(-?[\d\.]+)\s*dB", res.stderr)
    if match:
        return float(match.group(1))
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Audita, respalda y nivela audio a -10 dB pico en clips de cocina en Google Flow."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--project", "-p", help="Directorio raíz del proyecto (ej. projects/P006_poorboy_mega_sandwich)")
    group.add_argument("--dir", "-d", help="Directorio directo con los clips (ej. assets_flow/)")

    parser.add_argument("--target-peak", "-t", type=float, default=-10.0, help="Pico de audio objetivo en dBFS (default: -10.0 dBFS)")
    parser.add_argument("--tolerance", type=float, default=0.5, help="Tolerancia en dB para considerar nivelado (default: 0.5 dB)")
    parser.add_argument("--dry-run", action="store_true", help="Solo analiza e informa sin realizar cambios ni backups.")

    args = parser.parse_args()

    ffmpeg_bin = check_tool("ffmpeg")
    ffprobe_bin = check_tool("ffprobe")

    if args.project:
        flow_dir = os.path.join(args.project, "assets_flow")
    else:
        flow_dir = args.dir

    if not os.path.exists(flow_dir):
        print(f"❌ Error: La carpeta de assets '{flow_dir}' no existe.", file=sys.stderr)
        sys.exit(1)

    backup_dir = os.path.join(flow_dir, "originals_raw")

    # Buscar clips de video soportados
    valid_exts = {".mp4", ".mov", ".webm"}
    all_files = sorted(os.listdir(flow_dir))
    clip_files = [f for f in all_files if os.path.splitext(f)[1].lower() in valid_exts and os.path.isfile(os.path.join(flow_dir, f))]

    if not clip_files:
        print(f"⚠️  No se encontraron clips de video (.mp4/.mov) en: {flow_dir}")
        sys.exit(0)

    print("\n" + "=" * 80)
    print(f"🚀 INICIANDO AUDITORÍA Y NIVELACIÓN DE AUDIO FOLEY (cocina-audiovisual-flow)")
    print(f"   Carpeta activa: {flow_dir}")
    print(f"   Objetivo de pico: {args.target_peak:.1f} dBFS (Tolerancia: ±{args.tolerance:.1f} dB)")
    print(f"   Modo Dry-Run: {'ACTIVADO (sin modificaciones)' if args.dry_run else 'DESACTIVADO (procesamiento real)'}")
    print("=" * 80 + "\n")

    if not args.dry_run and not os.path.exists(backup_dir):
        os.makedirs(backup_dir, exist_ok=True)
        print(f"📁 Directorio de respaldo inmutable creado: {backup_dir}\n")

    report = []

    for fname in clip_files:
        curr_path = os.path.join(flow_dir, fname)
        backup_path = os.path.join(backup_dir, fname)

        # 1. Inspección técnica de video
        meta = probe_clip(ffprobe_bin, curr_path)

        # 2. Respaldo Inmutable (solo si no existe ya para proteger el crudo original)
        if not args.dry_run:
            if not os.path.exists(backup_path):
                shutil.copy2(curr_path, backup_path)
            # Tomamos siempre como fuente de procesamiento el archivo original en el backup
            source_for_processing = backup_path
        else:
            source_for_processing = curr_path

        # 3. Detección de Pico de Audio Original
        orig_peak = detect_max_volume(ffmpeg_bin, source_for_processing)

        if orig_peak is None:
            report.append({
                "file": fname,
                "meta": f"{meta['width']}x{meta['height']}@{meta['fps']}fps",
                "dur": f"{meta['duration']}s",
                "orig_peak": "SIN AUDIO",
                "adj": "0.0 dB",
                "final_peak": "N/A",
                "status": "⚠️ Sin pista de audio",
            })
            continue

        # 4. Cálculo de Ajuste
        diff = args.target_peak - orig_peak
        needs_adj = abs(diff) > args.tolerance

        if not needs_adj:
            report.append({
                "file": fname,
                "meta": f"{meta['width']}x{meta['height']}@{meta['fps']}fps",
                "dur": f"{meta['duration']}s",
                "orig_peak": f"{orig_peak:.1f} dB",
                "adj": "0.0 dB",
                "final_peak": f"{orig_peak:.1f} dB",
                "status": "✅ Ya nivelado",
            })
            continue

        # 5. Aplicar Nivelación sin recodificar video (-c:v copy)
        adj_db = round(diff, 2)
        if not args.dry_run:
            tmp_out = os.path.join(flow_dir, f"_tmp_{fname}")
            cmd_norm = [
                ffmpeg_bin,
                "-y",
                "-i", source_for_processing,
                "-af", f"volume={adj_db}dB",
                "-c:v", "copy",
                "-c:a", "aac",
                "-b:a", "192k",
                tmp_out,
            ]
            subprocess.run(cmd_norm, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            os.replace(tmp_out, curr_path)

            final_peak = detect_max_volume(ffmpeg_bin, curr_path)
            final_str = f"{final_peak:.1f} dB" if final_peak is not None else "Error"
            status_str = "🎉 Nivelado exitoso"
        else:
            final_str = f"{(orig_peak + adj_db):.1f} dB (est.)"
            status_str = "🔍 Requiere nivelación"

        report.append({
            "file": fname,
            "meta": f"{meta['width']}x{meta['height']}@{meta['fps']}fps",
            "dur": f"{meta['duration']}s",
            "orig_peak": f"{orig_peak:.1f} dB",
            "adj": f"{'+' if adj_db > 0 else ''}{adj_db:.1f} dB",
            "final_peak": final_str,
            "status": status_str,
        })

    # Imprimir Tabla Resumen
    header = f"{'Clip':<12} | {'Formato':<16} | {'Dur':<7} | {'Pico Orig':<10} | {'Ajuste':<9} | {'Pico Final':<11} | {'Estado'}"
    print(header)
    print("-" * len(header))
    for r in report:
        print(f"{r['file']:<12} | {r['meta']:<16} | {r['dur']:<7} | {r['orig_peak']:<10} | {r['adj']:<9} | {r['final_peak']:<11} | {r['status']}")

    print("-" * len(header))
    print(f"\n✅ Proceso completado sobre {len(clip_files)} clips.")
    if not args.dry_run:
        print(f"🔒 Todos los originales crudos están preservados de forma inmutable en:\n   {backup_dir}")
        print("💡 Ahora puedes ejecutar `python3 assemble.py` con audio perfectamente calibrado.")


if __name__ == "__main__":
    main()
