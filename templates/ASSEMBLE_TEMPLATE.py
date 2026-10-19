#!/usr/bin/env python3
"""
Plantilla Base de Auto-Ensamblaje para HyperFrames (cocina-audiovisual-flow).
Soporta:
  1. FORMATO 1: Cocina POV Editorial ASMR (1080x1920 Fullscreen continuo, Foley puro o BGM con Notch EQ).
  2. FORMATO 2: Split-Screen Caricaturas (Ventana Cartoon superior 16:9 + Franja divisoria + Cocina inferior
                + Transición a Pantalla Completa en clímax SPLIT_END).

Uso:
  python3 assemble.py [--no-bgm]
"""

import os
import sys

# ==============================================================================
# 1. CONFIGURACIÓN DEL PROYECTO
# ==============================================================================
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_FLOW_DIR = os.path.join(PROJECT_DIR, "assets_flow")

# Selector de Formato: 'formato_1' (POV ASMR) o 'formato_2' (Split-Screen)
FORMAT_MODE = "formato_2"

# Metadatos del Short
PROJECT_NAME = "Mi Proyecto de Cocina Flow"
TOTAL_DURATION = 18.10
DEFAULT_MEDIA_START = 0.35  # Recorte de arranque para evitar inercia del modelo de IA

# ==============================================================================
# 2. CONFIGURACIÓN ESPECÍFICA DE FORMATO 2 (SPLIT-SCREEN)
# ==============================================================================
# Si FORMAT_MODE == 'formato_2':
CARTOON_REL = "assets/cartoon_top.mp4"
CARTOON_DURATION = 14.215
SPLIT_END = 14.215  # Segundo exacto en que termina el cartoon y se expande a Fullscreen

TOP_HEIGHT = 792          # Altura de la ventana animada (px)
DIVIDER_TOP = 792         # Posición Y del divisor (px)
DIVIDER_HEIGHT = 32       # Altura del divisor (px)
BOTTOM_TOP = 824          # Posición Y de la cocina (px)
BOTTOM_HEIGHT = 1096      # Altura de la ventana inferior (px)

# ==============================================================================
# 3. MAPA DE PLANOS (SHOTS)
# Formato de tupla: (shot_code, mode, start_t, end_t, media_start, label, cartoon_cue)
#   - mode: 'split' o 'full' (en Formato 1 todos son 'full')
# ==============================================================================
SHOTS = [
    # (code, mode, start, end, media_start, label, cue)
    ("S01", "split", 0.000, 1.600, 0.35, "S01 · Hero Reveal del Plato Terminado", "Hook inicial"),
    ("S02", "split", 1.600, 3.200, 0.30, "S02 · Macro Paneo por las Texturas", "Pase visual"),
    ("S03", "split", 3.200, 4.800, 0.35, "S03 · Manos en la Base / Escala", "Diálogo inicial"),
    ("S04", "split", 4.800, 6.150, 0.30, "S04 · Base y Aceite de Oliva", "Preparación base"),
    ("S05", "split", 6.150, 7.500, 0.35, "S05 · Montaña de Ingredientes / Proteína", "Ingrediente 1"),
    ("S06", "split", 7.500, 8.800, 0.30, "S06 · Ingrediente Secundario / Salsa", "Ingrediente 2"),
    ("S07", "split", 8.800, 10.250, 0.35, "S07 · Especias o Toque Especial", "Ingrediente 3"),
    ("S08", "split", 10.250, 11.710, 0.30, "S08 · Cascada de Salsa / Emulsión", "Salsa abundante"),
    ("S09", "split", 11.710, 12.800, 0.35, "S09 · Tapa / Toque Final", "Cierre del plato"),
    ("S10", "split", 12.800, 14.215, 0.30, "S10 · Corte con Cuchillo (CRUNCH)", "Clímax de corte"),
    # Planos finales a Pantalla Completa (Payoff):
    ("S11", "full", 14.215, 16.150, 0.35, "S11 · Separación de Mitades (Interior)", "Payoff Fullscreen"),
    ("S12", "full", 16.150, 18.100, 0.35, "S12 · Bocado Humeante hacia Cámara", "Cierre épico"),
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


def build_html(include_bgm=False):
    clip_blocks = []
    audio_blocks = []
    found_videos = 0
    found_images = 0

    # --------------------------------------------------------------------------
    # FORMATO 2: Split-Screen Tracks
    # --------------------------------------------------------------------------
    if FORMAT_MODE == "formato_2":
        # Track 0: Cartoon Superior
        clip_blocks.append(
            f'      <video id="cartoon-top" class="clip" src="{CARTOON_REL}" data-start="0" data-duration="{CARTOON_DURATION}" data-media-start="0" data-track-index="0" playsinline data-has-audio="true" data-volume="0.92" style="position:absolute;left:0;top:0px;width:1080px;height:{TOP_HEIGHT}px;object-fit:cover;z-index:20"></video>'
        )
        # Track 1: Barra Divisoria Elegante
        clip_blocks.append(
            f'      <div id="split-divider" class="clip" data-start="0" data-duration="{SPLIT_END}" data-track-index="1" style="position:absolute;left:0;top:{DIVIDER_TOP}px;width:1080px;height:{DIVIDER_HEIGHT}px;background:#090807;border-top:2px solid rgba(245,158,11,0.28);border-bottom:2px solid rgba(245,158,11,0.28);z-index:19"></div>'
        )

    # --------------------------------------------------------------------------
    # Planos de Cocina Flow (S01 ... SNN)
    # --------------------------------------------------------------------------
    for idx, (code, mode, start_t, end_t, media_start, label, cue) in enumerate(SHOTS, start=1):
        dur = round(end_t - start_t, 3)
        asset_path, kind = find_asset(code)
        shot_id = f"shot-{code.lower()}"
        track_idx = idx + (1 if FORMAT_MODE == "formato_2" else -1)
        z_idx = idx

        # Geometría según el modo del plano
        if FORMAT_MODE == "formato_2" and mode == "split":
            geo = f"position:absolute;left:0;top:{BOTTOM_TOP}px;width:1080px;height:{BOTTOM_HEIGHT}px;object-fit:cover;z-index:{z_idx}"
            ph_geo = f"position:absolute;left:0;top:{BOTTOM_TOP}px;width:1080px;height:{BOTTOM_HEIGHT}px"
            foley_vol = "0.80"
        else:
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
            clip_blocks.append(
                f'      <div id="{shot_id}" class="clip" data-start="{start_t}" data-duration="{dur}" data-track-index="{track_idx}" style="{ph_geo};background:#1c1917;color:#fafaf9;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:60px;text-align:center;z-index:{z_idx}"><span style="color:#f59e0b;font-size:28px;font-weight:800;margin-bottom:12px">{code} · ({start_t:.2f}s–{end_t:.2f}s)</span><h2 style="font-size:42px;font-weight:700;line-height:1.25">{label}</h2><p style="color:#a8a29e;font-size:24px;margin-top:16px">{cue}</p></div>'
            )

    # --------------------------------------------------------------------------
    # FORMATO 1: Cama Musical Opcional con Muesca de EQ
    # --------------------------------------------------------------------------
    if FORMAT_MODE == "formato_1" and include_bgm:
        bgm_rel = "assets/music-video.mp3"
        bgm_fx_chain = (
            "{&quot;version&quot;:1,&quot;nodes&quot;:["
            "{&quot;type&quot;:&quot;peaking&quot;,&quot;id&quot;:&quot;n1&quot;,&quot;label&quot;:&quot;Foley Transient Pocket&quot;,&quot;params&quot;:{&quot;frequency&quot;:2600,&quot;gain&quot;:-3.5,&quot;q&quot;:1.2}}"
            "]}"
        )
        audio_blocks.append(
            f'      <audio id="bgm-main" class="clip" src="{bgm_rel}" data-start="0" data-duration="{TOTAL_DURATION}" data-track-index="99" data-volume="0.35" data-fx-chain="{bgm_fx_chain}"></audio>'
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
    print(f"Generado: {out_file}")


if __name__ == "__main__":
    use_bgm = "--no-bgm" not in sys.argv
    build_html(include_bgm=use_bgm)
