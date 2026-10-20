# Cocina Audiovisual Flow (`cocina-audiovisual-flow`) — v2.0

[![Agent Skill](https://img.shields.io/badge/Antigravity-Agent%20Skill%20v2.0-blue.svg)](https://github.com/WilliamLop/cocina-skill-videos.git)
[![Pipeline](https://img.shields.io/badge/Pipeline-Google%20Flow%20%2B%20HyperFrames-green.svg)](https://github.com/WilliamLop/cocina-skill-videos.git)
[![Resolution](https://img.shields.io/badge/Format-1080x1920%20(9%3A16)-orange.svg)](https://github.com/WilliamLop/cocina-skill-videos.git)

Agent Skill profesional e instalable en equipo para diseñar, generar, ensamblar y empaquetar episodios de **cocina fotorrealista vertical (9:16)** en **Google Flow (`Nano Banana Pro` + `Veo 3.1`)** y **HyperFrames**.

---

## 🍳 La Matriz 2×2: 2 Formatos × 2 Estilos de Fabricación

Esta skill permite producir combinando cualquiera de los **2 Formatos Editoriales** con cualquiera de los **2 Estilos de Fabricación Visual**:

| Formato \ Estilo | **Estilo A: 100% Video Continuo (`.mp4`)** | **Estilo B: Híbrido Percusivo (`Jump-Cuts` de Imágenes Consecutivas `.png` + Clips `.mp4`)** |
|---|---|---|
| **Formato 1: Cocina POV Editorial ASMR** (`1080x1920` Full 9:16) | **Combinación `1A`:** Todos los planos son clips `.mp4` con vapor y movimiento continuo (ej. `P001` Rigatoni, `P002` Birria, `P003` Ramen). | **Combinación `1B`:** Secuencias de 2–3 imágenes consecutivas (`0.28s–0.40s` encadenadas con `L17` + SFX `knife_chop_wood.wav`) para picados rápidos + clips `.mp4` en fuego, salsas y payoff. |
| **Formato 2: Recreación de Caricaturas en Split-Screen** (`35%/65%` → `100% Fullscreen`) | **Combinación `2A`:** Caricatura arriba + todos los planos inferiores en `.mp4` + expansión Fullscreen en el clímax (ej. `P004` Tacos de Ramen de Escandalosos). | **Combinación `2B`:** Caricatura arriba + *Jump-Cuts* de imágenes consecutivas con SFX cuando el personaje pica o apila rápido + clips `.mp4` en sartén, salsas y cierre Fullscreen. |

---

## ⚡ Las 5 Reglas de Oro Canónicas (v2.0)

1. **Protocolo de Continuidad en 2 Niveles (`🟢 ANCHOR Vacío` vs. `🔗 Regla L17 Plano Anterior S(N-1)`):**
   - **🟢 Inicio de Estación:** Adjuntar `ANCHOR_01 / 02 / 03` vacío en `[+]` **únicamente** cuando la tabla, la sartén o el cuenco empiezan limpios.
   - **🔗 Plato en Progreso (Regla `L17` — *Step-Anchor Chaining*):** Cuando el plato ya va a mitad de preparación (en sartén, armando capas en la tabla, decorando el cuenco o en secuencias de imágenes consecutivas), **NUNCA adjuntar el Anchor vacío** (evita que la IA rehaga los ingredientes desde cero y presente otra comida). **Adjuntar en `[+]` la imagen o fotograma del plano inmediatamente anterior `S(N-1)`**.
2. **Estilo A (`100% .mp4`) o Estilo B (`Jump-Cuts 0.30s` con SFX + `.mp4`):**
   - En cortes rápidos de cuchillo donde Veo podría deformar los dedos, usar el **Estilo B** con 2–3 imágenes consecutivas encadenadas con `L17` y sincronizadas automáticamente con la librería `assets/sfx/`.
3. **Regla del Estado Inicial y Master Hero (`L04, L06, L07`):**
   - En cortes en video, el cuchillo empieza suspendido 2 cm arriba del ingrediente entero. En vertidos, la botella empieza inclinada soltando la primera gota.
4. **Ingeniería de Audio Foley a `-10 dBFS` y Balance Dinámico (`L10, L18`):**
   - `scripts/process_clips.py` respalda en `originals_raw/` y nivela todos los `.mp4` a `-10 dB` con aceleración por hardware (`aac_at` en macOS). En Formato 2, el foley va a `0.28` durante el diálogo de la caricatura y sube a `1.00` en la expansión a Pantalla Completa.
5. **Packaging y Ficha de Publicación Obligatoria (`Fase 6`):**
   - Todo episodio se entrega con su `FICHA_PUBLICACION.md` (frame exacto de portada, 3 títulos de alto CTR, descripción bilingüe en gramos y primer comentario fijado) lista para subir desde el PC del encargado del canal.

---

## 🔄 Flujo de Sincronización en Equipo (Git Sync)

### 1. Bajar la última versión de la Skill antes de producir (`git pull`):
```bash
git -C .agent/skills/cocina-audiovisual-flow pull origin main
# (O en instalación global: git -C ~/.gemini/config/skills/cocina-audiovisual-flow pull origin main)
```

### 2. Subir nuevos episodios documentados o mejoras de la Skill (`git push`):
- Guardar en `episodes/<codigo_episodio>/` únicamente los archivos de texto (`GUIA_GENERACION.md`, `assemble.py` y `FICHA_PUBLICACION.md` — **nunca videos `.mp4`**).
- Ejecutar commit y push a `origin main` para que todo el equipo reciba la actualización.

---

## 📂 Estructura del Repositorio (v2.0)

```text
cocina-skill-videos/
├── SKILL.md                              # Instrucciones maestras v2.0 (Matriz 2x2 + 19 Reglas L01–L19)
├── README.md                             # Guía de instalación, Matriz 2x2 y sincronización en equipo
├── .gitignore                            # Bloquea videos .mp4 pesados; permite librería assets/sfx/*.wav
├── assets/
│   └── sfx/                              # Librería oficial de 8 efectos Foley (.wav) para Estilo B (Jump-Cuts)
├── references/
│   ├── FORMATO_1_POV_ASMR.md             # Especificación de Formato 1 (18-30s, 4500K, f/2.0)
│   ├── FORMATO_2_SPLIT_CARICATURAS.md    # Geometría Split-Screen (35%/65%) y Payoff Fullscreen
│   ├── PROMPT_PATTERNS.md                # Fórmulas Nano Banana Pro, Veo 3.1, Regla L17 y Jump-Cuts
│   └── PACKAGING_Y_PUBLICACION.md        # Protocolo de subida, títulos A/B, miniatura y comentario fijado
├── templates/
│   ├── GUIA_GENERACION_TEMPLATE.md       # Plantilla con Matriz 2x2 e indicador [🟢 ANCHOR vs 🔗 S(N-1)]
│   ├── ASSEMBLE_TEMPLATE.py              # Ensamblador universal HyperFrames (Video .mp4 + Imagen .png con SFX)
│   └── FICHA_PUBLICACION_TEMPLATE.md     # Plantilla lista para copiar y pegar al subir el video
├── scripts/
│   └── process_clips.py                  # Auditoría, backup inmutable y nivelación a -10 dB (aac_at en macOS)
└── episodes/                             # Bitácora viva de episodios producidos por el equipo (P001, P002, P003, P004...)
```
