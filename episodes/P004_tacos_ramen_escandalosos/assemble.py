#!/usr/bin/env python3
"""
Script de Auto-Ensamblaje para HyperFrames (cocina-audiovisual-flow).
Proyecto: P004_tacos_ramen_escandalosos
Formato: FORMATO 2 — Recreación de Caricaturas en Split-Screen
         (Escandalosos / We Bare Bears: Tacos de Ramen)

Geometría:
  - Ventana Cartoon Superior: 1080 x 612 px (0.00s a 16.20s)
  - Franja Divisoria: 1080 x 32 px en y = 612 px (0.00s a 16.20s)
  - Ventana Cocina Inferior: 1080 x 1276 px en y = 644 px (0.00s a 16.20s)
  - Transición SPLIT_END a Pantalla Completa: 16.20s a 20.00s (1080x1920 Fullscreen)

Uso:
  python3 assemble.py
"""

import os
import sys

# ==============================================================================
# 1. CONFIGURACIÓN DEL PROYECTO
# ==============================================================================
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_FLOW_DIR = os.path.join(PROJECT_DIR, "assets_flow")

# Selector de Formato: 'formato_2' (Split-Screen Caricaturas)
FORMAT_MODE = "formato_2"

# Metadatos del Short
PROJECT_NAME = "¡Recreé los Tacos de Ramen de Escandalosos!"
TOTAL_DURATION = 20.00
DEFAULT_MEDIA_START = 0.35  # Recorte de inercia para arranque ágil de Veo 3.1

# ==============================================================================
# 2. CONFIGURACIÓN DE FORMATO 2 (SPLIT-SCREEN)
# ==============================================================================
CARTOON_REL = "assets/cartoon_top.mp4"
CARTOON_DURATION = 16.200
SPLIT_END = 16.200  # Segundo exacto en que termina el cartoon y se expande a Fullscreen

TOP_HEIGHT = 612          # Altura de la ventana animada (px)
DIVIDER_TOP = 612         # Posición Y del divisor (px)
DIVIDER_HEIGHT = 32       # Altura del divisor (px)
BOTTOM_TOP = 644          # Posición Y de la cocina (px)
BOTTOM_HEIGHT = 1276      # Altura de la ventana inferior (px)

# ==============================================================================
# 3. MAPA DE PLANOS (SHOTS) — FORMATO 2
# Formato de tupla: (shot_code, mode, start_t, end_t, media_start, label, cartoon_cue)
# ==============================================================================
SHOTS = [
    # (code, mode, start, end, media_start, label, cue)
    ("S01", "split", 0.000, 1.500, 0.35, "S01 · Hero Reveal del Taco de Ramen", "Pardo: ¡Por favor, señor, tacos de ramen!"),
    ("S02", "split", 1.500, 2.800, 0.30, "S02 · Crujido de la Concha de Ramen (CRUNCH)", "Pardo apoyado en el mostrador"),
    ("S03", "split", 2.800, 4.100, 0.30, "S03 · Aceite de Sésamo y Cebolla en Sartén", "Panda: ¡Hemos esperado mucho!..."),
    ("S04", "split", 4.100, 5.500, 0.35, "S04 · Carne Picada de Res en Sartén Caliente", "Panda: ...¡Muero de hambre!"),
    ("S05", "split", 5.500, 6.900, 0.35, "S05 · Glaseado de Soya, Mirin y Ajo Rallado", "Fila enorme en el festival"),
    ("S06", "split", 6.900, 8.200, 0.30, "S06 · Fideos de Ramen Hirviendo en Olla", "Chica entrega plato: Pardo: ¿Solo uno?"),
    ("S07", "split", 8.200, 9.600, 0.35, "S07 · Prensado del Disco de Fideos en Sartén", "Chica del camión: ¡Siguiente!"),
    ("S08", "split", 9.600, 10.900, 0.30, "S08 · Pliegue de Concha de Taco Dorada", "Pardo contempla el mini taco"),
    ("S09", "split", 10.900, 12.200, 0.35, "S09 · Relleno de Carne Jugosa en Concha", "Pardo: Bien, hermanos..."),
    ("S10", "split", 12.200, 13.500, 0.30, "S10 · Col Verde Crujiente Rallada", "Pardo: ...bocados pequeños..."),
    ("S11", "split", 13.500, 14.800, 0.30, "S11 · Pico de Gallo Fresco Brillante", "Pardo: ...sabórenlo..."),
    ("S12", "split", 14.800, 16.200, 0.35, "S12 · Zigzag de Mayonesa Spicy Sriracha", "¡Los 3 osos devoran: NOM NOM NOM!"),
    # Planos finales a PANTALLA COMPLETA (Payoff gourmet):
    ("S13", "full", 16.200, 18.100, 0.35, "S13 · Corte Transversal Crujiente (CRUNCH)", "FULLSCREEN: Interior jugoso humeante"),
    ("S14", "full", 18.100, 20.000, 0.35, "S14 · Payoff: Bocado Supremo hacia Cámara", "FULLSCREEN: Cierre épico gourmet"),
]

# ==============================================================================
# 4. FUNCIONES DE APOYO
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


def build_html():
    clip_blocks = []
    found_videos = 0
    found_images = 0

    # --------------------------------------------------------------------------
    # FORMATO 2: Split-Screen Tracks
    # --------------------------------------------------------------------------
    if FORMAT_MODE == "formato_2":
        # Track 0: Cartoon Superior (Audio Primario a 0.95)
        clip_blocks.append(
            f'      <video id="cartoon-top" class="clip" src="{CARTOON_REL}" data-start="0" data-duration="{CARTOON_DURATION}" data-media-start="0" data-track-index="0" playsinline data-has-audio="true" data-volume="0.95" style="position:absolute;left:0;top:0px;width:1080px;height:{TOP_HEIGHT}px;object-fit:cover;z-index:20"></video>'
        )
        # Track 1: Barra Divisoria Elegante
        clip_blocks.append(
            f'      <div id="split-divider" class="clip" data-start="0" data-duration="{SPLIT_END}" data-track-index="1" style="position:absolute;left:0;top:{DIVIDER_TOP}px;width:1080px;height:{DIVIDER_HEIGHT}px;background:#090807;border-top:2px solid rgba(245,158,11,0.28);border-bottom:2px solid rgba(245,158,11,0.28);z-index:19"></div>'
        )

    # --------------------------------------------------------------------------
    # Planos de Cocina Flow (S01 ... S14)
    # --------------------------------------------------------------------------
    for idx, (code, mode, start_t, end_t, media_start, label, cue) in enumerate(SHOTS, start=1):
        dur = round(end_t - start_t, 3)
        asset_path, kind = find_asset(code)
        shot_id = f"shot-{code.lower()}"
        track_idx = idx + 1  # Track 0 = cartoon, Track 1 = divider
        z_idx = idx

        # Geometría y volumen según el modo del plano
        if FORMAT_MODE == "formato_2" and mode == "split":
            geo = f"position:absolute;left:0;top:{BOTTOM_TOP}px;width:1080px;height:{BOTTOM_HEIGHT}px;object-fit:cover;z-index:{z_idx}"
            ph_geo = f"position:absolute;left:0;top:{BOTTOM_TOP}px;width:1080px;height:{BOTTOM_HEIGHT}px"
            foley_vol = "0.28"
        else:
            # Fullscreen en Clímax (S13, S14)
            geo = f"position:absolute;left:0;top:0px;width:1080px;height:1920px;object-fit:cover;z-index:{z_idx}"
            ph_geo = "position:absolute;left:0;top:0px;width:1080px;height:1920px"
            foley_vol = "1.00" if code == "S13" else "0.00"

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
                f'      <div id="{shot_id}" class="clip" data-start="{start_t}" data-duration="{dur}" data-track-index="{track_idx}" style="{ph_geo};background:#1c1917;color:#f59e0b;font-family:sans-serif;font-size:30px;font-weight:700;display:flex;align-items:center;justify-content:center;text-align:center;padding:50px;z-index:{z_idx}">{label_clean}</div>'
            )

    all_clips = "\n".join(clip_blocks)

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
    print(f"Cartoon superior: {CARTOON_REL} ({CARTOON_DURATION}s)")
    print(f"Transición Fullscreen en: {SPLIT_END}s")
    print(f"Assets detectados: {found_videos}/{len(SHOTS)} videos (.mp4), {found_images} imágenes")
    print(f"Generado exitosamente: {out_file}")


if __name__ == "__main__":
    build_html()
