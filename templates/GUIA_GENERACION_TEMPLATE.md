# Guía Maestra de Generación en Google Flow — Piloto `[CÓDIGO_PILOTO]`: [NOMBRE DEL PLATO / RECETA]

- **Fecha:** [YYYY-MM-DD]
- **Formato:** [Formato 1: Cocina POV Editorial ASMR | Formato 2: Recreación de Caricaturas en Split-Screen]
- **Referencia base:** [Referencia editorial o clip animado de origen, ej. R029 / @culturaglotona]
- **Proyecto HyperFrames asociado:** `projects/[NOMBRE_PROYECTO]/`
- **Duración final del Short:** **`[XX.XX] segundos`** (`[NN] planos de video .mp4` · promedio `[X.XX] s/corte` · `1080x1920` a `30 fps`)
- **Clip animado superior (si aplica Formato 2):** `projects/[NOMBRE_PROYECTO]/assets/cartoon_top.mp4` (`[W]x[H]`, `30 fps`, `[XX.XX] s`)

---

## 1. Configuración Base en Google Flow

1. **Relación de Aspecto:** `Portrait (9:16)` en absolutamente todas las generaciones.
2. **Flujo por cada plano (`S01` a `S[NN]`):**
   - **Paso A (Imagen Inicial — Start Frame):** Modo `Create Image` → Modelo `Nano Banana Pro` → Pega el **Prompt de Imagen (`[IMG]`)** adjuntando en el botón **`[+]`** la imagen ancla correspondiente (`ANCHOR_01`, `ANCHOR_02` o `ANCHOR_03`).
   - **Paso B (Animación y Audio ASMR):** Selecciona la imagen generada como **Start Frame** → Modo `Image to Video` → Modelo `Veo 3.1 - Fast` (para cortes, caídas de especias y acciones dinámicas) o `Veo 3.1 - Quality` (para emulsiones de salsas, quesos fundidos y payoff) → Duración `4s` → Pega el **Prompt de Video (`[VID]`)**.
3. **Nombres de archivo al descargar:**
   - Guarda los videos descargados en:
     `projects/[NOMBRE_PROYECTO]/assets_flow/`
   - Nómbralos exactamente: **`S01.mp4`, `S02.mp4`, `S03.mp4` ... hasta `S[NN].mp4`**.
   - *(No necesitas guardar imágenes .jpg: el video es 100% .mp4 sin fotos estáticas).*

---

## 2. Las Imágenes Ancla de Escenario (Generar primero en `Nano Banana Pro`)

Genera estas imágenes vacías antes de crear ningún alimento y tenlas descargadas para adjuntarlas en el botón **`[+]`**:

### `ANCHOR_01` (Estación Principal — Tabla de Nogal Oscuro)
```text
Vertical 9:16, 45-degree high-angle POV shot of a warm rustic kitchen workstation. A thick dark end-grain walnut wooden cutting board resting on a matte warm-grey limestone countertop. Soft natural morning daylight coming from a window on the left (4500K), subtle warm shadows, shallow depth of field, 50mm f/2.0 lens, photorealistic editorial food photography, empty center ready for ingredients, no hands, no food, no text.
```

### `ANCHOR_02` (Estación de Fuego — Sartén Caliente)
```text
Vertical 9:16, 45-degree high-angle close-up shot of a heavy 28cm brushed stainless steel chef skillet with copper-core rim sitting on a sleek black induction cooktop. Warm natural side lighting from the left (4500K), realistic metallic reflections, shallow depth of field, 50mm f/2.0 lens, photorealistic, empty pan, no hands, no food, no text.
```

### `ANCHOR_03` (Estación de Emplatado — Plato Artesanal Cerámico)
```text
Vertical 9:16, 45-degree high-angle shot of a handcrafted matte warm-cream ceramic dinner plate resting on a dark walnut wooden table. Soft warm side window light from the left (4500K), subtle linen napkin in the blurred background, 50mm f/2.0 lens, photorealistic editorial food photography, empty plate, no hands, no food, no text.
```

---

## 3. Mapa Cronométrico y Sincronización Segundo a Segundo

| Plano | Tiempo en el Short | Duración | Ventana (`media-start`) | Lo que ocurre ARRIBA / Contexto | Lo que ocurre ABAJO (Cocina en Flow) | Sonido Foley Nativo (Veo) |
|---|---|---|---|---|---|---|
| **`S01.mp4`** | `0.00 s – 1.50 s` | `1.50 s` | `0.35 s` | [Contexto inicial o Cartoon Hook] | **Hero Reveal:** [Plato terminado o corte crujiente] | Crujido inicial o golpe sólido |
| **`S02.mp4`** | `1.50 s – 2.80 s` | `1.30 s` | `0.30 s` | [Paso 1 del personaje / Caricatura] | [Ingrediente 1 / Preparación base] | [Sonido de corte o especias] |
| **`S03.mp4`** | `2.80 s – 4.20 s` | `1.40 s` | `0.35 s` | [Paso 2] | [Ingrediente 2 / Masaje o fuego] | [Chisporroteo o crujido] |
| **...** | ... | ... | ... | ... | ... | ... |
| **`S[NN].mp4`**| `[XX.XX] s – [XX.XX] s` | `[X.XX] s` | `0.35 s` | [Payoff Final / Pantalla Completa] | **Payoff:** [Bocado humeante o cheese pull hacia cámara] | Vapor cálido y crujido final |

---

## 4. Prompts Exactos Plano por Plano (`S01` a `S[NN]`)

### BLOQUE 1 — Doble Hook Inicial (`0.00 s – [X.XX] s`)

#### Plano `S01` (`0.00 s – 1.50 s`) — Hero Reveal
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_01` (Tabla de Nogal Oscuro)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of [DESCRIPCIÓN DEL PLATO COMPLETO TERMINADO] resting on a dark end-grain walnut wooden cutting board. Glistening textures, delicate wisps of hot steam rising, warm natural side window light from the left (4500K), shallow depth of field, 50mm f/2.0 lens, photorealistic editorial food photography, no hands, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  Slow cinematic push-in toward the [PLATO TERMINADO] on the dark walnut cutting board as delicate steam rises and juices glisten on the surface. Crisp ASMR kitchen audio: [SONIDO ESPECÍFICO: faint buttery sizzle / warm room ambiance], no music, no voice, no glitches.
  ```

---

#### Plano `S02` (`1.50 s – 2.80 s`) — El Corte Diagonal Crujiente
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_01` (Tabla de Nogal Oscuro)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a whole, completely uncut [ALIMENTO] on a dark walnut cutting board. One hand holds the side of the [ALIMENTO] steady while the other hand holds a sharp stainless steel chef's knife poised 2 centimeters in the air directly above, ready to slice down. Warm side lighting (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The chef's knife presses down firmly through the [ALIMENTO] in one decisive slice, cutting cleanly through to the wooden board. Crisp ASMR kitchen audio: loud ultra-crispy crunch followed by a clean wooden tap on the cutting board, no music, no voice, no glitches.
  ```

---

### BLOQUE 2 — Preparación y Cocción (`[X.XX] s – [XX.XX] s`)

#### Plano `S03` (`[XX.XX] s – [XX.XX] s`) — [Acción de Cocción / Fuego]
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Sartén Caliente)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of [INGREDIENTE] entering a hot [SARTÉN DE ACERO / HIERRO] coated with foaming melted butter and extra virgin olive oil. Warm side lighting, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast/Quality, Image-to-Video, 4s)`:**
  ```text
  [INGREDIENTE] sizzles vigorously upon contacting the hot foaming butter in the skillet, sending up lively golden bubbles and aromatic steam. Crisp ASMR kitchen audio: immediate punchy high-heat pan sizzle as food hits hot foaming butter, no music, no voice, no glitches.
  ```

---

### BLOQUE 3 — Fusión y Payoff Final (`[XX.XX] s – [FINAL] s`)

#### Plano `S[NN]` (`[XX.XX] s – [FINAL] s`) — Bocado Final (*Hero Payoff*)
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_03` (Plato Cerámico Artesanal)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle macro close-up of a fork / hands holding a steaming, juicy bite of [PLATO] lifted directly above the plate. Glossy sauce clinging, melted cheese stretching, hot steam curls rising into warm window light, 50mm f/1.8 lens, shallow depth of field, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The fork / hand slowly moves the steaming bite slightly closer to the camera lens, showcasing the rich glistening textures and escaping curls of warm steam. Crisp ASMR kitchen audio: subtle savory lift and quiet warm room ambiance, no music, no voice, no glitches.
  ```

---

## 5. Empaquetado SEO Bilingüe

**Título Optimizado para CTR y Búsqueda:**
`[Título Principal con Gancho] #receta #[palave_clave1] #[palabra_clave2] #foodporn`

*(Ejemplo Formato 1: Creamy Garlic Butter Shrimp Pasta 🍤 #shrimppasta #easyrecipes)*  
*(Ejemplo Formato 2: ¡Recreé el Poor Boy Gigante de Scooby-Doo! 🥪 #scoobydoo #sandwichgigante)*

**Descripción para YouTube Shorts / Reels (Inglés + Español con Gramajes Exactos):**

```text
[NOMBRE DEL PLATO EN INGLÉS]

Ingredients:
- [Ingrediente 1] — [Cantidad en gramos/ml]
- [Ingrediente 2] — [Cantidad en gramos/ml]
- [Ingrediente 3] — [Cantidad en gramos/ml]

Step-by-step instructions:
1. [Instrucción breve 1]
2. [Instrucción breve 2]
3. [Instrucción breve 3]

---

[NOMBRE DEL PLATO EN ESPAÑOL]

Ingredientes:
- [Ingrediente 1] — [Cantidad en gramos/ml]
- [Ingrediente 2] — [Cantidad en gramos/ml]
- [Ingrediente 3] — [Cantidad en gramos/ml]

Paso a paso:
1. [Instrucción breve 1]
2. [Instrucción breve 2]
3. [Instrucción breve 3]
```
