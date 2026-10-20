# Guía Maestra de Generación en Google Flow — Episodio `[CÓDIGO]`: [NOMBRE DEL PLATO / RECETA]

- **Fecha:** [YYYY-MM-DD]
- **Combinación Matriz 2×2:** `[1A | 1B | 2A | 2B]`
  - **Formato Editorial:** `[Formato 1: Cocina POV Editorial ASMR (Full 9:16) | Formato 2: Recreación de Caricaturas en Split-Screen (35%/65% -> Fullscreen)]`
  - **Estilo de Fabricación:** `[Estilo A: 100% Video Continuo (.mp4) | Estilo B: Híbrido Percusivo (Imágenes Consecutivas Jump-Cuts 0.28s–0.40s + Clips de Video .mp4)]`
- **Referencia / Caricatura base:** `[Referencia editorial o episodio animado de origen]`
- **Proyecto HyperFrames asociado:** `projects/[NOMBRE_PROYECTO]/`
- **Duración final del Short:** **`[XX.XX] segundos`** (`[NN] planos` · `1080x1920` a `30 fps`)
- **Clip animado superior (si aplica Formato 2):** `projects/[NOMBRE_PROYECTO]/assets/cartoon_top.mp4` (`1080x612` o `1080x792`, `30 fps`, finaliza en `SPLIT_END = [XX.XX] s`)

---

## 1. Reglas de Oro y Protocolo de Continuidad (`ANCHOR` vs. `Regla L17`)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                REGLA DE CONTINUIDAD ACUMULATIVA EN [+] (L17)                │
├─────────────────────────────────────────────────────────────────────────────┤
│ 🟢 INICIO DE ESTACIÓN (Superficie limpia):                                  │
│    Usa `ANCHOR_01`, `ANCHOR_02` o `ANCHOR_03` vacío SOLO cuando la tabla,   │
│    la sartén o el plato se estrenan vacíos en ese bloque.                   │
│                                                                             │
│ 🔗 PLATO EN PROGRESO (Mitad de receta, cocción, armado o Jump-Cuts):        │
│    Si la sartén, la tabla o el plato YA tienen ingredientes del paso        │
│    anterior, NUNCA adjuntes el Anchor vacío (porque la IA rehace los        │
│    ingredientes desde cero). Adjunta en [+] la IMAGEN O FRAME DEL PLANO     │
│    ANTERIOR `S(N-1)` para mantener 100% idéntica la comida que ya llevas.   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Flujo por cada plano (`S01` a `S[NN]`):
- **Si el plano es `VIDEO (.mp4)`:**
  1. **Paso A (`[IMG]`):** `Create Image` → `Nano Banana Pro (9:16)` → Adjunta en **`[+]`** la referencia indicada (`🟢 ANCHOR` o `🔗 S(N-1)`).
  2. **Paso B (`[VID]`):** Selecciona la imagen como **Start Frame** → `Image to Video` → `Veo 3.1 Fast` o `Quality` (`4s`) → Pega el prompt `[VID]`. Descarga como `SXX.mp4` en `assets_flow/`.
- **Si el plano es `IMAGEN CONSECUTIVA / JUMP-CUT (.png)` (Solo en Estilo B):**
  1. **Paso Único (`[SOLO IMG]`):** `Create Image` → `Nano Banana Pro (9:16)` → Adjunta en **`[+]`** la imagen del plano inmediatamente anterior `S(N-1)` → Pega el prompt `[IMG]`.
  2. Descarga únicamente la imagen como `SXX.png` en `assets_flow/` *(NO generes video; `assemble.py` le aplicará el corte seco de `0.30 s` y el sonido Foley de `assets/sfx/`)*.

---

## 2. Imágenes Ancla de Escenario (Generar una sola vez al inicio en `Nano Banana Pro`)

### `ANCHOR_01` (Estación Principal — Tabla de Nogal Vacía)
```text
Vertical 9:16, 45-degree high-angle POV shot of a warm rustic kitchen workstation. A thick dark end-grain walnut wooden cutting board resting on a matte warm-grey limestone countertop. Soft natural morning daylight coming from a window on the left (4500K), subtle warm shadows, shallow depth of field, 50mm f/2.0 lens, photorealistic editorial food photography, empty center ready for ingredients, no hands, no food, no text.
```

### `ANCHOR_02` (Estación de Fuego — Sartén o Plancha Vacía)
```text
Vertical 9:16, 45-degree high-angle close-up shot of a heavy 28cm brushed stainless steel chef skillet with copper-core rim sitting on a sleek black induction cooktop. Warm natural side lighting from the left (4500K), realistic metallic reflections, shallow depth of field, 50mm f/2.0 lens, photorealistic, empty pan, no hands, no food, no text.
```

### `ANCHOR_03` (Estación de Emplatado — Plato o Cuenco Vacío)
```text
Vertical 9:16, 45-degree high-angle shot of a handcrafted matte warm-cream ceramic dinner plate resting on a dark walnut wooden table. Soft warm side window light from the left (4500K), subtle linen napkin in the blurred background, 50mm f/2.0 lens, photorealistic editorial food photography, empty plate, no hands, no food, no text.
```

---

## 3. Mapa Cronométrico Sincronizado Segundo a Segundo

| Plano | Tipo (`video`/`image`) | Tiempo en Short | Duración | Referencia en `[+]` | Contexto / Caricatura (ARRIBA) | Acción en Cocina Flow (ABAJO) | Audio Foley / SFX |
|---|---|---|---|---|---|---|---|
| **`S01`** | `video` (`.mp4`) | `0.00s – 1.40s` | `1.40s` | 🟢 `ANCHOR_03` | [Hook 1] | **Hero Reveal:** Plato terminado humeante | Foley nativo Veo |
| **`S02`** | `video` (`.mp4`) | `1.40s – 2.70s` | `1.30s` | 🔗 `Frame S01` | [Hook 2] | **Acción Hook:** Corte / Dip / Rotura sobre `S01` | `CRUNCH` / `SLOSH` |
| **`S03`** | `image` o `video` | `2.70s – 3.00s` | `0.30s` | 🟢 `ANCHOR_01` | [Preparación 1] | Ingrediente entero bajo el cuchillo en tabla | `knife_chop_wood.wav` |
| **`S04`** | `image` o `video` | `3.00s – 3.30s` | `0.30s` | 🔗 `Imagen S03` | [Preparación 2] | Mismo ingrediente cortado en tiras sobre `S03` | `knife_chop_wood.wav` |
| **`S05`** | `image` o `video` | `3.30s – 3.60s` | `0.30s` | 🔗 `Imagen S04` | [Preparación 3] | Mismo ingrediente cortado en dados sobre `S04` | `bench_scraper.wav` |
| **`S06`** | `video` (`.mp4`) | `3.60s – 5.00s` | `1.40s` | 🟢 `ANCHOR_02` | [Fuego 1] | Entrada de mantequilla y proteína a sartén limpia | `SIZZLE` nativo Veo |
| **`S07`** | `video` (`.mp4`) | `5.00s – 6.40s` | `1.40s` | 🔗 `Frame S06` | [Fuego 2] | Vertido de salsa sobre la proteína ya dorada de `S06` | Vertido y burbujeo |
| **...** | ... | ... | ... | ... | ... | ... | ... |
| **`S[NN]`**| `video` (`.mp4`) | `[XX.X]s – [FIN]s`| `1.80s` | 🔗 `Frame S(N-1)`| **PANTALLA COMPLETA** | **Payoff:** Bocado humeante levantado hacia cámara | Vapor y bocado final |

---

## 4. Prompts Exactos Plano por Plano (`S01` a `S[NN]`)

### BLOQUE 1 — Doble Hook Sensorial (`0.00 s – [X.XX] s`)

#### Plano `S01` (`0.00 s – 1.40 s`) — Hero Reveal del Plato Terminado `[VIDEO .mp4]`
- **📎 ADJUNTAR EN `[+]`:** 🟢 `ANCHOR_03` (Plato/Cuenco Vacío)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of [DESCRIPCIÓN DEL MASTER HERO TERMINADO] resting on the handcrafted ceramic plate on a dark walnut table. Glistening textures, delicate wisps of hot steam rising, warm side window light (4500K), shallow depth of field, 50mm f/2.0 lens, photorealistic editorial food photography, no hands, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  Slow cinematic push-in toward the steaming [PLATO TERMINADO] as delicate steam rises and glossy juices glisten under warm window light. Crisp ASMR kitchen audio: faint warm sizzle and cozy room ambiance, no music, no voice, no glitches.
  ```

---

#### Plano `S02` (`1.40 s – 2.70 s`) — Acción Táctil del Hook `[VIDEO .mp4]`
- **📎 ADJUNTAR EN `[+]`:** 🔗 `Fotograma de S01` *(Regla L17: Mantiene el mismo plato del Hook 1)*
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up keeping the exact same [PLATO TERMINADO] from the reference image intact, with a [CUCHILLO / TENEDOR / MANO] poised 2 centimeters above the center ready to [slice straight down / break open / dip]. Warm side lighting (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast/Quality, Image-to-Video, 4s)`:**
  ```text
  The [CUCHILLO / TENEDOR] presses down cleanly into the [PLATO], revealing the steaming juicy interior. Crisp ASMR kitchen audio: loud ultra-crispy crunch and juicy texture sound, no music, no voice, no glitches.
  ```

---

### BLOQUE 2 — Ejemplo de Secuencia en Tabla (Adaptar según Estilo A o Estilo B)

#### *(Si es Estilo B: Jump-Cut de Imágenes Consecutivas `0.30s` con `L17`)*
#### Plano `S03` (`2.70 s – 3.00 s`) — Estado 1: Ingrediente Entero `[SOLO IMAGEN .png + SFX knife_chop_wood.wav]`
- **📎 ADJUNTAR EN `[+]`:** 🟢 `ANCHOR_01` (Tabla de Nogal Vacía)
- **`[SOLO IMG] Prompt (Nano Banana Pro, 9:16 — NO generar video)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of whole fresh [INGREDIENTE] resting in the center of the dark end-grain walnut cutting board, with a sharp stainless steel chef's knife blade resting gently on top. Warm side window light (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```

#### Plano `S04` (`3.00 s – 3.30 s`) — Estado 2: Cortado en Tiras/Mitades `[SOLO IMAGEN .png + SFX knife_chop_wood.wav]`
- **📎 ADJUNTAR EN `[+]`:** 🔗 `Imagen de S03` *(Regla L17: Mantiene la misma tabla e ingrediente)*
- **`[SOLO IMG] Prompt (Nano Banana Pro, 9:16 — NO generar video)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up keeping the exact same dark walnut cutting board and lighting from the reference image, now showing the exact same [INGREDIENTE] cleanly sliced into [long even strips / clean halves] in the exact same spot on the board. Photorealistic, 50mm f/2.0 lens, no hands, no text.
  ```

---

### BLOQUE 3 — Cocción y Armado Progresivo con Regla `L17`

#### Plano `S06` (`[XX.XX] s – [XX.XX] s`) — Inicio en Sartén Caliente `[VIDEO .mp4]`
- **📎 ADJUNTAR EN `[+]`:** 🟢 `ANCHOR_02` (Sartén Vacía)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of [INGREDIENTE 1] entering the hot skillet coated with foaming golden butter. Warm side lighting (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  [INGREDIENTE 1] sizzles vigorously in the hot foaming butter as aromatic steam rises. Crisp ASMR kitchen audio: immediate punchy high-heat pan sizzle, no music, no voice, no glitches.
  ```

#### Plano `S07` (`[XX.XX] s – [XX.XX] s`) — Adición sobre Comida en Progreso `[VIDEO .mp4]`
- **📎 ADJUNTAR EN `[+]`:** 🔗 `Fotograma de S06` *(Regla L17: Conserva exactamente la comida que ya está en la sartén/tabla)*
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up keeping the exact same browned [INGREDIENTE 1] sizzling inside the skillet from the reference image intact, as a [JARRA / CUCHARA / MANO] tilted right above begins pouring [SALSA / CREMA / INGREDIENTE 2] over it. Warm side lighting (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The [SALSA / CREMA] pours smoothly over the sizzling [INGREDIENTE 1] in the skillet, bubbling and blending into a glossy rich sauce. Crisp ASMR kitchen audio: velvety liquid pour meeting a hot simmering pan, no music, no voice, no glitches.
  ```

---

## 5. Comandos de Procesamiento, Ensamblaje y Packaging

```bash
# 1. Nivelar audios de clips .mp4 a -10 dB y respaldar originales
python3 .agent/skills/cocina-audiovisual-flow/scripts/process_clips.py --project projects/[NOMBRE_PROYECTO]

# 2. Generar index.html en HyperFrames (monta videos .mp4 e imágenes .png con SFX automáticos)
python3 projects/[NOMBRE_PROYECTO]/assemble.py

# 3. Validar 0 errores y 0 advertencias
npx hyperframes check projects/[NOMBRE_PROYECTO]

# 4. Render Master Final 1080x1920 a 30 fps
npx hyperframes render projects/[NOMBRE_PROYECTO] --quality delivery --output projects/[NOMBRE_PROYECTO]/renders/[NOMBRE_PROYECTO]_final.mp4
```
*(A continuación, completar y entregar `FICHA_PUBLICACION.md` para la subida al canal).*
