#!/usr/bin/env python3
"""
Script de Auto-Ensamblaje para HyperFrames.
Proyecto: P002_birria_tacos_cheese
Formato: FORMATO 1 - Cocina POV Editorial ASMR (1080x1920 Fullscreen continuo)

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
PROJECT_NAME = "Smash Tacos de Birria con Costra de Queso y Consomé Caliente"
TOTAL_DURATION = 20.00
DEFAULT_MEDIA_START = 0.35  # Recorte de inercia para arranque ágil de Veo 3.1

# ==============================================================================
# 2. MAPA DE PLANOS (SHOTS) — FORMATO 1 POV ASMR
# Tupla: (shot_code, mode, start_t, end_t, media_start, label, cue)
# ==============================================================================
SHOTS = [
    # (code, mode, start, end, media_start, label, cue)
    ("S01", "full", 0.000, 1.400, 0.35, "S01 · Hero Reveal de Tacos y Consomé", "Hook inicial sensorial"),
    ("S02", "full", 1.400, 2.800, 0.30, "S02 · The Dip: Taco sumergiéndose en Consomé", "Inmersión jugosa en caldo rojo"),
    ("S03", "full", 2.800, 4.000, 0.30, "S03 · Deshebrado de Carne de Birria Tierna", "Tenedores separando hebras jugosas"),
    ("S04", "full", 4.000, 5.500, 0.30, "S04 · Picado Rápido de Cilantro y Cebolla", "Cortes rítmicos en tabla de nogal"),
    ("S05", "full", 5.500, 6.800, 0.35, "S05 · Queso Rallado en Plancha de Hierro", "Costra de queso burbujeante"),
    ("S06", "full", 6.800, 8.100, 0.30, "S06 · Inmersión de Tortilla en Olla de Birria", "Tortilla impregnada en grasa roja"),
    ("S07", "full", 8.100, 9.400, 0.35, "S07 · Tortilla sobre Costra de Queso Caliente", "Chasquido y sellado en plancha"),
    ("S08", "full", 9.400, 10.800, 0.35, "S08 · Colocación de Carne de Birria en Taco", "Montículo generoso humeante"),
    ("S09", "full", 10.800, 12.000, 0.35, "S09 · Espátula Dobla el Taco a la Mitad", "Costra tostada crujiente"),
    ("S10", "full", 12.000, 13.200, 0.35, "S10 · Prensado con Espátula Plana", "Chisporroteo de grasa roja"),
    ("S11", "full", 13.200, 14.400, 0.35, "S11 · Cucharón Sirve Consomé en Cuenco", "Caldo rojo rubí con vapor vivo"),
    ("S12", "full", 14.400, 15.600, 0.30, "S12 · Lluvia de Cilantro y Cebolla en Consomé", "Frescura verde y morada en caldo"),
    ("S13", "full", 15.600, 16.800, 0.35, "S13 · Emplatado de Tacos junto al Cuenco", "Asentamiento crujiente en fuente"),
    ("S14", "full", 16.800, 17.900, 0.30, "S14 · Exprimido de Lima Fresca en los Tacos", "Chorrito cítrico brillante"),
    ("S15", "full", 17.900, 18.900, 0.30, "S15 · Separación y Cheese Pull Elástico", "Queso estirándose entre la carne"),
    ("S16", "full", 18.900, 20.000, 0.35, "S16 · Payoff: The Ultimate Dip hacia Cámara", "Taco goteando consomé con vapor vivo"),
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
    # Planos de Cocina Flow (S01 ... S16)
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
