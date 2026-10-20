#!/usr/bin/env python3
"""
Plantilla Universal de Auto-Ensamblaje para HyperFrames (cocina-audiovisual-flow v2.0).
Soporta la Matriz 2x2 completa:
  - FORMATO 1 ('formato_1'): Cocina POV Editorial ASMR (1080x1920 Fullscreen continuo).
  - FORMATO 2 ('formato_2'): Recreación de Caricaturas en Split-Screen + Expansión Fullscreen en SPLIT_END.
  - ESTILO A ('100% Video'): Todos los planos son .mp4 con su audio Foley nativo nivelado a -10 dB.
  - ESTILO B ('Híbrido Imágenes Consecutivas + Video'): Combina Jump-Cuts de imágenes (.png/.jpg de 0.28s–0.40s)
    sincronizadas automáticamente con efectos Foley de `assets/sfx/` (knife_chop_wood.wav, etc.) + clips .mp4.

Uso:
  python3 assemble.py [--no-bgm]
"""

import os
import shutil
import sys

# ==============================================================================
# 1. CONFIGURACIÓN DEL PROYECTO Y MATRIZ 2x2
# ==============================================================================
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_FLOW_DIR = os.path.join(PROJECT_DIR, "assets_flow")
PROJECT_SFX_DIR = os.path.join(PROJECT_DIR, "assets", "sfx")

# Selector de Formato: 'formato_1' (Full 9:16 POV ASMR) o 'formato_2' (Split-Screen Caricaturas)
FORMAT_MODE = "formato_2"
# Selector de Estilo: 'estilo_a' (100% Video) o 'estilo_b' (Híbrido Imágenes Consecutivas + Video)
PRODUCTION_STYLE = "estilo_a"

PROJECT_NAME = "Mi Episodio de Cocina Flow"
TOTAL_DURATION = 18.10
DEFAULT_MEDIA_START = 0.35  # Recorte de inercia inicial para Veo 3.1

# ==============================================================================
# 2. CONFIGURACIÓN ESPECÍFICA DE FORMATO 2 (SPLIT-SCREEN)
# ==============================================================================
CARTOON_REL = "assets/cartoon_top.mp4"
CARTOON_DURATION = 14.215
SPLIT_END = 14.215  # Segundo exacto en que termina el cartoon y se expande a Fullscreen

TOP_HEIGHT = 612          # Altura de la ventana animada (612 o 792 px)
DIVIDER_TOP = 612         # Posición Y del divisor (px)
DIVIDER_HEIGHT = 32       # Altura del divisor (px)
BOTTOM_TOP = 644          # Posición Y de la cocina (px)
BOTTOM_HEIGHT = 1276      # Altura de la ventana inferior (1276 o 1096 px)

# Volúmenes canónicos (Regla L18):
CARTOON_VOL = "0.95"      # Diálogo/canción líder en ventana superior
SPLIT_FOLEY_VOL = "0.28"  # Foley secundario bajo el diálogo durante el split-screen
FULL_FOLEY_VOL = "1.00"   # Foley al 100% cuando pasa a Pantalla Completa o en Formato 1

# ==============================================================================
# 3. MAPA DE PLANOS (SHOTS)
# Soporta tuplas de 7 elementos (Estándar) o 9 elementos (con preferred_kind y sfx_file para Estilo B):
#   7-tupla: (code, mode, start_t, end_t, media_start, label, cue)
#   9-tupla: (code, mode, preferred_kind, start_t, end_t, media_start, label, cue, sfx_file)
#   - mode: 'split' o 'full' (en Formato 1 se fuerza a 'full' automáticamente)
#   - preferred_kind: 'video' (.mp4) o 'image' (.png/.jpg para Jump-Cuts de 0.28s-0.40s)
#   - sfx_file: nombre del archivo en assets/sfx/ cuando el plano es 'image' (ej. 'knife_chop_wood.wav')
# ==============================================================================
SHOTS = [
    ("S01", "split", "video", 0.000, 1.500, 0.35, "S01 · Hero Reveal del Plato Terminado", "Hook 1", None),
    ("S02", "split", "video", 1.500, 2.800, 0.30, "S02 · Acción Táctil del Hook (CRUNCH)", "Hook 2", None),
    # Ejemplo de Jump-Cuts si usas Estilo B (cambia 'video' a 'image' y asigna duraciones de ~0.30s):
    ("S03", "split", "video", 2.800, 4.100, 0.30, "S03 · Preparación en Tabla 1", "Paso 1", "knife_chop_wood.wav"),
    ("S04", "split", "video", 4.100, 5.500, 0.35, "S04 · Entrada a Sartén Caliente (SIZZLE)", "Paso 2", None),
    ("S05", "split", "video", 5.500, 6.900, 0.35, "S05 · Glaseado o Salsa en Sartén (L17)", "Paso 3", None),
    ("S06", "split", "video", 6.900, 8.200, 0.30, "S06 · Cocción / Textura Principal", "Paso 4", None),
    ("S07", "split", "video", 8.200, 9.600, 0.35, "S07 · Transformación / Dorado", "Paso 5", None),
    ("S08", "split", "video", 9.600, 10.900, 0.30, "S08 · Base Lista para Armar", "Paso 6", None),
    ("S09", "split", "video", 10.900, 12.500, 0.35, "S09 · Relleno Principal sobre S08 (L17)", "Paso 7", None),
    ("S10", "split", "video", 12.500, 14.215, 0.30, "S10 · Topping Final y Salsa sobre S09 (L17)", "Paso 8", None),
    # Planos finales a PANTALLA COMPLETA (Payoff gourmet tras SPLIT_END):
    ("S11", "full", "video", 14.215, 16.150, 0.35, "S11 · Corte Transversal Crujiente (CRUNCH)", "Payoff Fullscreen", None),
    ("S12", "full", "video", 16.150, 18.100, 0.35, "S12 · Bocado Humeante hacia Cámara (L17)", "Cierre épico", None),
]


# ==============================================================================
# 4. FUNCIONES DE DETECCIÓN Y PROVISIÓN DE SFX
# ==============================================================================
def normalize_shot_tuple(row):
    """Permite usar tuplas de 7 elementos o de 9 elementos indistintamente."""
    if len(row) == 7:
        code, mode, start_t, end_t, media_start, label, cue = row
        return code, mode, "video", start_t, end_t, media_start, label, cue, "knife_chop_wood.wav"
    elif len(row) == 9:
        return row
    else:
        raise ValueError(f"Formato de tupla inválido en SHOTS: {row}")


def ensure_sfx_file(sfx_name):
    """Busca el archivo SFX en el proyecto o lo copia automáticamente desde la Skill."""
    if not sfx_name:
        sfx_name = "knife_chop_wood.wav"
    local_sfx = os.path.join(PROJECT_SFX_DIR, sfx_name)
    if os.path.exists(local_sfx):
        return f"assets/sfx/{sfx_name}"

    # Buscar en ubicaciones estándar de la skill cocina-audiovisual-flow
    candidates = [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "sfx", sfx_name),
        os.path.join(PROJECT_DIR, "..", "..", ".agent", "skills", "cocina-audiovisual-flow", "assets", "sfx", sfx_name),
        os.path.expanduser(f"~/.gemini/config/skills/cocina-audiovisual-flow/assets/sfx/{sfx_name}"),
    ]
    for cand in candidates:
        if os.path.exists(cand):
            os.makedirs(PROJECT_SFX_DIR, exist_ok=True)
            shutil.copy2(cand, local_sfx)
            return f"assets/sfx/{sfx_name}"
    return None


def find_asset(code, preferred_kind="video"):
    """Prioriza .mp4 si preferred_kind=='video', y .png/.jpg si preferred_kind=='image'."""
    if not os.path.exists(ASSETS_FLOW_DIR):
        return None, None
    files = sorted(os.listdir(ASSETS_FLOW_DIR))
    code_lower = code.lower()
    video_exts = (".mp4", ".mov", ".webm")
    image_exts = (".png", ".jpg", ".jpeg", ".webp")

    order = (
        [(video_exts, "video"), (image_exts, "image")]
        if preferred_kind == "video"
        else [(image_exts, "image"), (video_exts, "video")]
    )
    for exts, kind in order:
        for fname in files:
            nl = fname.lower()
            if (nl.startswith(code_lower + ".") or nl.startswith(code_lower + "_")) and os.path.splitext(nl)[1] in exts:
                return f"assets_flow/{fname}", kind
    return None, None


def build_html(include_bgm=False):
    clip_blocks = []
    audio_blocks = []
    found_videos = 0
    found_images = 0

    # --------------------------------------------------------------------------
    # FORMATO 2: Pistas de Ventana Superior (Cartoon) y Barra Divisoria
    # --------------------------------------------------------------------------
    if FORMAT_MODE == "formato_2":
        clip_blocks.append(
            f'      <video id="cartoon-top" class="clip" src="{CARTOON_REL}" data-start="0" data-duration="{CARTOON_DURATION}" data-media-start="0" data-track-index="0" playsinline data-has-audio="true" data-volume="{CARTOON_VOL}" style="position:absolute;left:0;top:0px;width:1080px;height:{TOP_HEIGHT}px;object-fit:cover;z-index:20"></video>'
        )
        clip_blocks.append(
            f'      <div id="split-divider" class="clip" data-start="0" data-duration="{SPLIT_END}" data-track-index="1" style="position:absolute;left:0;top:{DIVIDER_TOP}px;width:1080px;height:{DIVIDER_HEIGHT}px;background:#090807;border-top:2px solid rgba(245,158,11,0.28);border-bottom:2px solid rgba(245,158,11,0.28);z-index:19"></div>'
        )

    # --------------------------------------------------------------------------
    # Planos de Cocina Flow (S01 ... SNN)
    # --------------------------------------------------------------------------
    for idx, raw_row in enumerate(SHOTS, start=1):
        code, mode, pref_kind, start_t, end_t, media_start, label, cue, sfx_file = normalize_shot_tuple(raw_row)
        dur = round(end_t - start_t, 3)
        asset_path, kind = find_asset(code, pref_kind)
        shot_id = f"shot-{code.lower()}"
        track_idx = idx + (1 if FORMAT_MODE == "formato_2" else -1)
        z_idx = idx

        if FORMAT_MODE == "formato_2" and mode == "split":
            geo = f"position:absolute;left:0;top:{BOTTOM_TOP}px;width:1080px;height:{BOTTOM_HEIGHT}px;object-fit:cover;z-index:{z_idx}"
            ph_geo = f"position:absolute;left:0;top:{BOTTOM_TOP}px;width:1080px;height:{BOTTOM_HEIGHT}px"
            foley_vol = SPLIT_FOLEY_VOL
        else:
            geo = f"position:absolute;left:0;top:0px;width:1080px;height:1920px;object-fit:cover;z-index:{z_idx}"
            ph_geo = "position:absolute;left:0;top:0px;width:1080px;height:1920px"
            foley_vol = FULL_FOLEY_VOL

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
            # En Estilo B (Jump-Cuts de imagen), inyectar automáticamente el SFX percusivo
            sfx_rel = ensure_sfx_file(sfx_file)
            if sfx_rel:
                sfx_dur = round(max(0.15, dur - 0.02), 2)
                audio_blocks.append(
                    f'      <audio id="sfx-{code.lower()}" class="clip" src="{sfx_rel}" data-start="{start_t}" data-duration="{sfx_dur}" data-track-index="{50 + idx}" data-volume="{foley_vol}"></audio>'
                )
        else:
            label_clean = f"{code} ({pref_kind.upper()}) · ({start_t:.2f}s–{end_t:.2f}s) | {label}"
            clip_blocks.append(
                f'      <div id="{shot_id}" class="clip" data-start="{start_t}" data-duration="{dur}" data-track-index="{track_idx}" style="{ph_geo};background:#1c1917;color:#f59e0b;font-family:sans-serif;font-size:30px;font-weight:700;display:flex;align-items:center;justify-content:center;text-align:center;padding:50px;z-index:{z_idx}">{label_clean}</div>'
            )

    # --------------------------------------------------------------------------
    # FORMATO 1: Cama Musical Opcional con Muesca de EQ (2600 Hz, -3.5 dB)
    # --------------------------------------------------------------------------
    if FORMAT_MODE == "formato_1" and include_bgm:
        bgm_rel = "assets/music-video.mp3"
        if os.path.exists(os.path.join(PROJECT_DIR, bgm_rel)):
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
    print(f"Matriz 2x2: {FORMAT_MODE} + {PRODUCTION_STYLE} | Duración total: {TOTAL_DURATION}s")
    print(f"Assets detectados: {found_videos} videos (.mp4), {found_images} imágenes (.png/.jpg) de {len(SHOTS)} planos")
    print(f"Generado exitosamente: {out_file}")


if __name__ == "__main__":
    use_bgm = "--no-bgm" not in sys.argv
    build_html(include_bgm=use_bgm)
