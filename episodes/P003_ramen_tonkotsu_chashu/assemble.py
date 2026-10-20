#!/usr/bin/env python3
"""
Script de Auto-Ensamblaje para HyperFrames.
Proyecto: P003_ramen_tonkotsu_chashu
Formato: FORMATO 1 - Cocina POV Editorial ASMR (1080x1920 Fullscreen continuo)
Duración: 30.00 segundos (21 planos)

Uso:
  python3 assemble.py [--no-bgm]
"""

import os
import subprocess
import sys

# ==============================================================================
# 1. CONFIGURACIÓN DEL PROYECTO
# ==============================================================================
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_FLOW_DIR = os.path.join(PROJECT_DIR, "assets_flow")

# Selector de Formato: 'formato_1' (POV ASMR)
FORMAT_MODE = "formato_1"

# Metadatos del Short
PROJECT_NAME = "Ramen Tonkotsu Cremoso con Chashu Sopleteado y Huevo Nitamago"
TOTAL_DURATION = 30.00
DEFAULT_MEDIA_START = 0.35  # Recorte de inercia para arranque ágil de Veo 3.1

# ==============================================================================
# 2. MAPA DE PLANOS (SHOTS) — FORMATO 1 POV ASMR (30 SEGUNDOS)
# Tupla: (shot_code, mode, start_t, end_t, media_start, label, cue)
# ==============================================================================
SHOTS = [
    # (code, mode, start, end, media_start, label, cue)
    ("S01", "full", 0.000, 1.400, 0.35, "S01 · Hero Reveal del Cuenco de Ramen", "Hook sensorial inicial con vapor vivo"),
    ("S02", "full", 1.400, 2.800, 0.30, "S02 · Hook del Huevo Nitamago (Yema Fundente)", "Rotura suave y desborde dorado"),
    ("S03", "full", 2.800, 4.000, 0.30, "S03 · Corte de Chashu en Tabla de Nogal", "Corte limpio de panceta glaseada"),
    ("S04", "full", 4.000, 5.300, 0.35, "S04 · Sopleteado de Chashu con Fuego Vivo", "Llama caramelizando grasa burbujeante"),
    ("S05", "full", 5.300, 6.500, 0.30, "S05 · Picado Rápido de Cebollín Negi", "Cortes rítmicos acelerados en nogal"),
    ("S06", "full", 6.500, 7.800, 0.30, "S06 · Corte de Lámina de Alga Nori", "Crujido fibroso y seco de nori"),
    ("S07", "full", 7.800, 9.200, 0.35, "S07 · Olla de Caldo Tonkotsu Hirviendo", "Borboteo espeso blanco marfil"),
    ("S08", "full", 9.200, 10.600, 0.30, "S08 · Inmersión de Fideos Frescos en Agua", "Fideos entrando en agua hirviendo"),
    ("S09", "full", 10.600, 12.200, 0.35, "S09 · Noodle Shake: Escurrido Enérgico", "Golpes secos sacudiendo el agua"),
    ("S10", "full", 12.200, 13.800, 0.35, "S10 · Tare y Aceite Aromático en Cuenco", "Fondo concentrado en cerámica negra"),
    ("S11", "full", 13.800, 15.300, 0.35, "S11 · Cucharón Vierte Caldo Tonkotsu", "Remolino blanco sedoso en el cuenco"),
    ("S12", "full", 15.300, 16.800, 0.35, "S12 · Entrada de Fideos en el Caldo", "Fideos humeantes entrando al caldo"),
    ("S13", "full", 16.800, 18.300, 0.35, "S13 · Peinado de Fideos con Palillos", "Plegado simétrico formando nido"),
    ("S14", "full", 18.300, 19.800, 0.35, "S14 · Gotas de Aceite Negro Mayu", "Gotas de ajo negro creando círculos"),
    ("S15", "full", 19.800, 21.300, 0.35, "S15 · Colocación de Lonchas de Chashu", "Panceta dorada sobre los fideos"),
    ("S16", "full", 21.300, 22.800, 0.30, "S16 · Colocación del Huevo Nitamago", "Medio huevo con yema fundente al lado"),
    ("S17", "full", 22.800, 24.300, 0.30, "S17 · Lluvia de Cebollín Verde al Centro", "Frescura verde en el cuenco"),
    ("S18", "full", 24.300, 25.800, 0.30, "S18 · Inserción de Alga Nori en el Borde", "Toque crujiente negro en cerámica"),
    ("S19", "full", 25.800, 27.200, 0.30, "S19 · Macro Presión de la Yema Fundente", "Yema cremosa desbordando en caldo"),
    ("S20", "full", 27.200, 28.600, 0.35, "S20 · Cuchara Sopera Levantando Caldo", "Cuchara negra con caldo, fideos y Mayu"),
    ("S21", "full", 28.600, 30.000, 0.35, "S21 · Payoff: Bocado con Chashu y Fideos", "Palillos elevando bocado humeante"),
]

# ==============================================================================
# 3. FUNCIONES DE APOYO
# ==============================================================================
def find_asset(code):
    """Busca en assets_flow/ archivos que comiencen por el código (ej. S01.mp4)."""
    if not os.path.exists(ASSETS_FLOW_DIR):
        return None, None
    files = sorted(os.listdir(ASSETS_FLOW_DIR))
    code_lower = code.lower()
    video_exts = (".mp4", ".mov", ".webm")
    image_exts = (".png", ".jpg", ".jpeg", ".webp")

    for fname in files:
        nl = fname.lower()
        if (nl.startswith(code_lower + ".") or nl.startswith(code_lower + "_")) and os.path.splitext(nl)[1] in video_exts:
            return f"assets_flow/{fname}", "video"
    for fname in files:
        nl = fname.lower()
        if (nl.startswith(code_lower + ".") or nl.startswith(code_lower + "_")) and os.path.splitext(nl)[1] in image_exts:
            return f"assets_flow/{fname}", "image"
    return None, None


def build_html(include_bgm=False):
    clip_blocks = []
    audio_blocks = []
    found_videos = 0
    found_images = 0

    # --------------------------------------------------------------------------
    # Planos de Cocina Flow (S01 ... S21)
    # --------------------------------------------------------------------------
    for idx, (code, mode, start_t, end_t, media_start, label, cue) in enumerate(SHOTS, start=1):
        dur = round(end_t - start_t, 3)
        asset_path, kind = find_asset(code)
        shot_id = f"shot-{code.lower()}"
        track_idx = idx
        z_idx = idx

        geo = f"position:absolute;left:0;top:0px;width:1080px;height:1920px;object-fit:cover;z-index:{z_idx}"
        ph_geo = "position:absolute;left:0;top:0px;width:1080px;height:1920px"
        foley_vol = "1.00"

        m_start = media_start if media_start is not None else DEFAULT_MEDIA_START

        if asset_path and kind == "video":
            found_videos += 1
            clip_blocks.append(
                f'      <video id="{shot_id}" class="clip" src="{asset_path}" data-start="{start_t}" data-duration="{dur}" data-media-start="{m_start}" data-track-index="{track_idx}" playsinline data-has-audio="true" data-volume="{foley_vol}" style="{geo}"></video>'
            )
        elif asset_path and kind == "image":
            found_images += 1
            clip_blocks.append(
                f'      <img id="{shot_id}" class="clip" src="{asset_path}" alt="{code}" data-start="{start_t}" data-duration="{dur}" data-track-index="{track_idx}" style="{geo}" />'
            )
        else:
            # Placeholder visual estilizado (0 advertencias en HyperFrames)
            label_clean = f"{code} · ({start_t:.2f}s–{end_t:.2f}s) | {label}"
            clip_blocks.append(
                f'      <div id="{shot_id}" class="clip" data-start="{start_t}" data-duration="{dur}" data-track-index="{track_idx}" style="{ph_geo};background:#1c1917;color:#f59e0b;font-family:sans-serif;font-size:32px;font-weight:700;display:flex;align-items:center;justify-content:center;text-align:center;padding:60px;z-index:{z_idx}">{label_clean}</div>'
            )

    # --------------------------------------------------------------------------
    # Cama Musical Opcional con Muesca de EQ (Notch a 2600 Hz para proteger Foley)
    # --------------------------------------------------------------------------
    bgm_path = os.path.join(PROJECT_DIR, "assets", "music-video.mp3")
    if include_bgm and os.path.exists(bgm_path):
        bgm_rel = "assets/music-video.mp3"
        bgm_fx_chain = (
            "{&quot;version&quot;:1,&quot;nodes&quot;:["
            "{&quot;type&quot;:&quot;peaking&quot;,&quot;id&quot;:&quot;n1&quot;,&quot;label&quot;:&quot;Foley Transient Pocket&quot;,&quot;params&quot;:{&quot;frequency&quot;:2600,&quot;gain&quot;:-3.5,&quot;q&quot;:1.2}}"
            "]}"
        )
        try:
            cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", bgm_path]
            bgm_dur = float(subprocess.check_output(cmd, text=True).strip())
        except Exception:
            bgm_dur = TOTAL_DURATION

        if bgm_dur > 0 and bgm_dur < TOTAL_DURATION:
            t = 0.0
            b_idx = 1
            while t < TOTAL_DURATION:
                slot_dur = round(min(bgm_dur, TOTAL_DURATION - t), 3)
                audio_blocks.append(
                    f'      <audio id="bgm-main-{b_idx}" class="clip" src="{bgm_rel}" data-start="{t:.3f}" data-duration="{slot_dur:.3f}" data-track-index="99" data-volume="0.32" data-fx-chain="{bgm_fx_chain}"></audio>'
                )
                t += bgm_dur
                b_idx += 1
        else:
            audio_blocks.append(
                f'      <audio id="bgm-main" class="clip" src="{bgm_rel}" data-start="0" data-duration="{TOTAL_DURATION}" data-track-index="99" data-volume="0.32" data-fx-chain="{bgm_fx_chain}"></audio>'
            )

    all_clips = "\n".join(clip_blocks)
    all_audios = "\n".join(audio_blocks)

    html = f"""<!doctype html>
<html lang="es" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>{PROJECT_NAME} ({TOTAL_DURATION}s)</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: #090807; font-family: Inter, ui-sans-serif, system-ui, sans-serif; }}
      #root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background: #090807; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL_DURATION}" data-width="1080" data-height="1920">
{all_clips}
{all_audios}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
"""
    out_file = os.path.join(PROJECT_DIR, "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"=== Ensamblaje completado para: {PROJECT_NAME} ===")
    print(f"Formato: {FORMAT_MODE} | Duración total: {TOTAL_DURATION}s")
    print(f"Assets detectados: {found_videos}/{len(SHOTS)} videos (.mp4), {found_images} imágenes")
    print(f"Generado exitosamente: {out_file}")


if __name__ == "__main__":
    use_bgm = "--no-bgm" not in sys.argv
    build_html(include_bgm=use_bgm)
