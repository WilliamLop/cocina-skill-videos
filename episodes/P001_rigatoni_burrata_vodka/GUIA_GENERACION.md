# Guía Maestra de Generación en Google Flow — Piloto P001: Rigatoni Cremoso al Vodka con Burrata Trufada

- **Fecha:** 2026-10-19
- **Formato:** Formato 1: Cocina POV Editorial ASMR (1080x1920 Full 9:16, 50mm f/2.0 a 4500K, foley envolvente a -10 dB, cero rostros).
- **Inspiración:** `@alenakhmil`, `@namcook`, `@moribyan` (Pilotos de referencia: `P002`, `P003`).
- **Proyecto HyperFrames:** [`projects/P001_rigatoni_burrata_vodka/`](file:///Users/leidycalderon/Documents/resetasfenbaru/projects/P001_rigatoni_burrata_vodka/)
- **Duración final:** **`20.00 segundos`** (`16 planos de video .mp4` · promedio `1.25 s/corte` · `1080x1920` a `30 fps`).

---

## 1. Reglas Canónicas y Flujo de Trabajo en Google Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       DIRECTIVAS INNEGOCIABLES DE FLOW                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 100% VIDEO (.mp4): Prohibido usar fotos fijas en el ensamblaje.          │
│ 2. ANCLAS OBLIGATORIAS: Generar ANCHOR_01, ANCHOR_02 y ANCHOR_03 primero    │
│    y adjuntarlas siempre en el botón [+] de cada toma en Nano Banana Pro.   │
│ 3. REGLA DEL ESTADO INICIAL: En cortes, el cuchillo se suspende 2 cm arriba;│
│    en vertidos, la jarra o botella se inclina tocando la primera gota.      │
│ 4. DURACIÓN DE VEO: Siempre generar 4 segundos en Image-to-Video.           │
│    HyperFrames recortará los fotogramas lentos iniciales (media-start).     │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Protocolo de Trabajo en 2 Pasos por Plano:
1. **Paso A — Fotograma Inicial (`[IMG]`):**
   - Modo: `Create Image` → Modelo: `Nano Banana Pro` → Formato: `Portrait (9:16)`.
   - Adjuntar en el botón **`[+]`** la imagen ancla indicada en la guía.
   - Pegar el prompt `[IMG]`.
2. **Paso B — Animación y Sonido Foley (`[VID]`):**
   - Seleccionar la imagen generada como **Start Frame**.
   - Modo: `Image to Video` → Modelo: `Veo 3.1 Fast` o `Veo 3.1 Quality` (según se indica).
   - Duración: `4s`.
   - Pegar el prompt `[VID]`.
3. **Descarga y Nombres de Archivo:**
   - Descarga los videos generados directamente en:
     `projects/P001_rigatoni_burrata_vodka/assets_flow/`
   - Nómbralos exactamente: **`S01.mp4`, `S02.mp4` ... hasta `S16.mp4`**.

---

## 2. Imágenes Ancla de Escenario (Generar primero en `Nano Banana Pro`)

Genera estas 3 imágenes vacías antes de crear ningún ingrediente. Descárgalas a tu ordenador para adjuntarlas en el botón **`[+]`**:

### `ANCHOR_01`: Estación de Corte y Preparación (Tabla de Nogal)
```text
Vertical 9:16, 45-degree high-angle POV shot of a warm rustic kitchen workstation. A thick dark end-grain walnut wooden cutting board resting on a matte warm-grey limestone countertop. Soft natural morning daylight coming from a window on the left (4500K), subtle warm shadows falling to the right, softly blurred warm-grey kitchen wall behind. 50mm f/2.0 lens, shallow depth of field, photorealistic editorial food photography. Empty center of the board ready for food, no food, no hands, no people, no text.
```

### `ANCHOR_02`: Estación de Fuego (Sartén de Acero Inoxidable)
```text
Vertical 9:16, 45-degree high-angle close-up shot of a heavy 28cm brushed stainless steel chef skillet with copper-core rim sitting on a sleek black induction cooktop. Warm natural side lighting from the left (4500K), realistic metallic reflections, shallow depth of field, 50mm f/2.0 lens, photorealistic, empty pan, no hands, no food, no text.
```

### `ANCHOR_03`: Estación de Emplatado (Cuenco Cerámico Artesanal)
```text
Vertical 9:16, 45-degree high-angle shot of a handcrafted matte warm-cream ceramic stoneware pasta bowl resting on a dark walnut wooden table. Soft warm side window light from the left (4500K), subtle linen napkin in the blurred background, 50mm f/2.0 lens, photorealistic editorial food photography, empty bowl, no hands, no food, no text.
```

---

## 3. Mapa Cronométrico Sincronizado (20.00 segundos)

| Clip | Tiempo en Short | Duración | Recorte (`media-start`) | Acción Clave | Foley Nativo Veo 3.1 |
|---|---|---|---|---|---|
| **`S01.mp4`** | `0.00 s – 1.40 s` | `1.40 s` | `0.35 s` | **Hook 1:** Hero reveal del plato terminado | Vapor vivo y murmullo cálido |
| **`S02.mp4`** | `1.40 s – 2.80 s` | `1.40 s` | `0.30 s` | **Hook 2:** Tenedor abre la burrata y brota crema | Rotura suave y desborde húmedo |
| **`S03.mp4`** | `2.80 s – 4.00 s` | `1.20 s` | `0.30 s` | Hoja plana de cuchillo aplasta ajo en seco | `CRACK` resonante en madera |
| **`S04.mp4`** | `4.00 s – 5.50 s` | `1.50 s` | `0.30 s` | Picado rápido y fino de hojas de albahaca | Cortes rítmicos sobre nogal |
| **`S05.mp4`** | `5.50 s – 6.80 s` | `1.30 s` | `0.35 s` | Hilo de AOVE y ajo entran a sartén caliente | `SIZZLE` chisporroteante dorado |
| **`S06.mp4`** | `6.80 s – 8.10 s` | `1.30 s` | `0.35 s` | Hojuelas de chile y pasta de tomate doble | Chisporroteo denso especiado |
| **`S07.mp4`** | `8.10 s – 9.40 s` | `1.30 s` | `0.35 s` | Chupito de vodka desglasa la base caliente | Silbido fuerte y vapor aromático |
| **`S08.mp4`** | `9.40 s – 10.80 s` | `1.40 s` | `0.35 s` | Chorro de crema espesa en espiral | Vertido líquido aterciopelado |
| **`S09.mp4`** | `10.80 s – 12.00 s` | `1.20 s` | `0.35 s` | Remolino espátula uniendo salsa naranja | Borboteo espeso y untuoso |
| **`S10.mp4`** | `12.00 s – 13.20 s` | `1.20 s` | `0.30 s` | Lluvia de Parmigiano Reggiano rallado | Nieve de queso fundiéndose |
| **`S11.mp4`** | `13.20 s – 14.40 s` | `1.20 s` | `0.35 s` | Rigatonis al dente caen a la sartén | Caída y chapoteo de pasta |
| **`S12.mp4`** | `14.40 s – 15.60 s` | `1.20 s` | `0.35 s` | Cubo de mantequilla y salteo envolvente | Salteo fluido y brillo cremoso |
| **`S13.mp4`** | `15.60 s – 16.80 s` | `1.20 s` | `0.35 s` | Pinzas sirven rigatonis en cuenco cerámico | Asentamiento suave en cerámica |
| **`S14.mp4`** | `16.80 s – 17.90 s` | `1.10 s` | `0.35 s` | Colocación de burrata e hilo de AOVE | Toque húmedo y goteo de aceite |
| **`S15.mp4`** | `17.90 s – 18.90 s` | `1.00 s` | `0.30 s` | Molinillo de pimienta negra y albahaca | Crujido aromático de molinillo |
| **`S16.mp4`** | `18.90 s – 20.00 s` | `1.10 s` | `0.35 s` | **Payoff:** Tenedor levanta bocado con vapor | Levantamiento cremoso y vapor vivo |

---

## 4. Prompts Exactos Plano por Plano (`S01` a `S16`)

---

### BLOQUE 1 — Doble Hook Sensorial (`0.00 s – 2.80 s`)

#### Plano `S01` (`0.00 s – 1.40 s`) — Hero Reveal del Plato Terminado
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_03` (Cuenco Cerámico Artesanal)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a steaming bowl of glossy orange creamy vodka rigatoni pasta crowned with a whole fresh silky white burrata cheese ball in the center. Fresh torn dark green basil leaves and crushed black peppercorns scattered on top, resting in a handcrafted matte cream ceramic bowl on a dark walnut wooden table. Soft warm morning window light from the left (4500K), gentle wisps of hot steam rising, shallow depth of field, 50mm f/2.0 lens, photorealistic editorial food photography, no hands, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  Slow cinematic push-in toward the steaming pasta bowl as delicate plumes of aromatic steam curl upwards and glossy tomato-cream sauce glistens under warm window light. Crisp ASMR kitchen audio: faint bubbling warmth and quiet cozy room ambiance, no music, no voice, no glitches.
  ```

---

#### Plano `S02` (`1.40 s – 2.80 s`) — Perforación y Rotura de la Burrata
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_03` (Cuenco Cerámico Artesanal)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle macro close-up of a sleek golden fork gently piercing the center of a soft fresh white burrata ball resting on steaming vodka rigatoni pasta. The thin outer skin has just split open, revealing rich glossy cream and stracciatella cheese curd beginning to ooze outwards. Warm side lighting (4500K), 50mm f/2.0 lens, photorealistic culinary photography, no faces, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The fork presses gently into the burrata, causing the delicate sphere to part smoothly as a thick, velvety river of fresh cream and stracciatella cheese slowly cascades over the hot orange rigatoni with rising steam. Crisp ASMR kitchen audio: soft wet creamy tear and lush gentle slosh, no music, no voice, no glitches.
  ```

---

### BLOQUE 2 — Preparación y Físicas Táctiles (`2.80 s – 5.50 s`)

#### Plano `S03` (`2.80 s – 4.00 s`) — Aplastado de Ajo en Seco
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_01` (Tabla de Nogal Oscuro)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a large whole peeled white garlic clove resting in the center of a dark walnut end-grain cutting board. A wide stainless steel chef's knife blade is held horizontally flat 2 centimeters directly above the garlic clove, ready to smash it down. Warm side window daylight (4500K), 50mm f/2.0 lens, shallow depth of field, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The palm firmly strikes the flat blade of the knife down onto the garlic clove, decisively crushing it into rustic flattened pieces against the wooden board. Crisp ASMR kitchen audio: one loud sharp resonant garlic crunch and heavy solid wooden thud, no music, no voice, no glitches.
  ```

---

#### Plano `S04` (`4.00 s – 5.50 s`) — Picado Rítmico de Albahaca Fresca
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_01` (Tabla de Nogal Oscuro)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a tightly rolled bundle of vibrant fresh green basil leaves resting on a dark walnut cutting board. One hand holds the basil roll in a chef claw grip while the sharp tip of a stainless steel chef's knife is poised 2 centimeters above the edge, ready to chiffonade. Warm natural side light (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The chef's knife executes rapid, rhythmic slicing motions through the rolled basil, creating clean thin ribbons that tumble onto the dark wood. Crisp ASMR kitchen audio: rapid rhythmic crisp knife chops tapping against solid walnut wood, no music, no voice, no glitches.
  ```

---

### BLOQUE 3 — Cocción y Chispazo en Sartén (`5.50 s – 10.80 s`)

#### Plano `S05` (`5.50 s – 6.80 s`) — Aceite de Oliva y Ajo en Sartén Caliente
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Sartén de Acero Inox)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of crushed fresh garlic entering a hot brushed stainless steel skillet coated with shimmering golden extra virgin olive oil. The first tiny bubbles are forming around the edges of the garlic. Warm metallic reflections, soft side lighting (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The crushed garlic vigorously sizzles in the shimmering olive oil, rapidly releasing lively golden foam and gentle wisps of fragrant steam. Crisp ASMR kitchen audio: immediate punchy sizzling olive oil crackle as garlic cooks, no music, no voice, no glitches.
  ```

---

#### Plano `S06` (`6.80 s – 8.10 s`) — Hojuelas de Chile y Pasta de Tomate Concentrada
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Sartén de Acero Inox)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a stainless steel spoon pressing a thick dollop of rich dark red concentrated tomato paste into the sizzling garlic and olive oil in the skillet, with red chili pepper flakes scattered across the bubbling surface. Warm side light, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The tomato paste caramelizes and darkens slightly as it fries in the hot oil, sizzling densely and releasing aromatic red oil droplets. Crisp ASMR kitchen audio: deep rich frying sizzle with subtle popping oil bubbles, no music, no voice, no glitches.
  ```

---

#### Plano `S07` (`8.10 s – 9.40 s`) — Desglasado con Vodka y Golpe de Vapor
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Sartén de Acero Inox)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a small clear glass shot tilted above the hot skillet, with a clear stream of vodka beginning to pour directly onto the caramelized red tomato paste. Warm side window light, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The clear vodka splashes into the sizzling hot pan, instantly creating an intense burst of white steam that billows upwards while deglazing the caramelized red tomato paste. Crisp ASMR kitchen audio: sharp explosive hiss and vigorous pan steam rush, no music, no voice, no glitches.
  ```

---

#### Plano `S08` (`9.40 s – 10.80 s`) — Vertido en Espiral de Crema Densa
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Sartén de Acero Inox)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a clear glass pitcher tilted above the skillet, pouring a thick ribbon of heavy whipping cream in a spiral pattern over the simmering glossy red tomato reduction. Soft warm light (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  A thick velvety stream of rich white cream smoothly flows into the simmering red sauce, creating mesmerizing swirling patterns as it blends into the gentle bubbles. Crisp ASMR kitchen audio: rich velvety heavy liquid pour meeting a warm bubbling pan, no music, no voice, no glitches.
  ```

---

### BLOQUE 4 — Fusión, Textura y Emulsión (`10.80 s – 15.60 s`)

#### Plano `S09` (`10.80 s – 12.00 s`) — Emulsión y Remolino Naranja Sedoso
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Sartén de Acero Inox)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a wooden spoon stirring the sauce in the stainless steel skillet, effortlessly blending the white cream and red tomato paste into a luminous, silky orange vodka sauce with glossy ripples. Warm side lighting, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The wooden spoon traces smooth circular motions through the sauce, forming a perfectly emulsified, velvety bright orange vodka cream sauce that softly bubbles at the edges. Crisp ASMR kitchen audio: mouthwatering thick creamy simmering slosh and warm bubbling, no music, no voice, no glitches.
  ```

---

#### Plano `S10` (`12.00 s – 13.20 s`) — Lluvia de Parmigiano Reggiano Rallado
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Sartén de Acero Inox)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a stainless steel microplane grater held over the skillet, with a cloud of finely grated Parmigiano Reggiano cheese falling like light white snow onto the hot bubbling orange vodka sauce. Warm side light, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The fine airy shavings of Parmesan cheese shower down onto the surface of the hot sauce, instantly melting into creamy golden ribbons with delicate steam rising. Crisp ASMR kitchen audio: soft airy snowfall of grated cheese landing on hot bubbling sauce, no music, no voice, no glitches.
  ```

---

#### Plano `S11` (`13.20 s – 14.40 s`) — Caída de Rigatoni al Dente en Cascada
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Sartén de Acero Inox)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a colander suspended directly over the skillet, poised as a cascade of hot, perfectly al dente rigatoni pasta cylinders begins to tumble into the bubbling orange vodka sauce. Warm steam rising, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The steaming rigatoni pasta tubes tumble into the hot orange vodka sauce, making a wet, satisfying splash as the sauce coats the ridged pasta surfaces. Crisp ASMR kitchen audio: wet thud of tender pasta tumbling into rich sauce and gentle splash, no music, no voice, no glitches.
  ```

---

#### Plano `S12` (`14.40 s – 15.60 s`) — Salteo con Mantequilla Fría y Brillo
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Sartén de Acero Inox)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a square pat of cold yellow butter melting against hot coated rigatoni pasta in the skillet, with the pan tilted slightly forward as if mid-toss. Shiny sauce clinging to every ridge, warm side light, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The skillet is vigorously tossed back and forth, flipping the rigatoni in the air as the melting butter coats the pasta in a high-gloss, ultra-creamy orange glaze. Crisp ASMR kitchen audio: energetic chef pan toss and glossy wet pasta folding sound, no music, no voice, no glitches.
  ```

---

### BLOQUE 5 — Emplatado y Clímax Gourmet (`15.60 s – 20.00 s`)

#### Plano `S13` (`15.60 s – 16.80 s`) — Emplatado con Pinzas en Cuenco Cerámico
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_03` (Cuenco Cerámico Artesanal)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of chef kitchen tongs releasing a mound of glossy, steaming vodka rigatoni pasta into the center of a handcrafted matte cream ceramic bowl on a dark walnut table. Warm side lighting (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The tongs gently twist and release the steaming pasta mound into the center of the ceramic bowl, with hot sauce settling into the base and wisps of aromatic steam rising. Crisp ASMR kitchen audio: soft wet pasta settling into ceramic bowl and gentle steam breath, no music, no voice, no glitches.
  ```

---

#### Plano `S14` (`16.80 s – 17.90 s`) — Corona con Burrata Fresca y Hilo de AOVE
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_03` (Cuenco Cerámico Artesanal)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a hand carefully placing a pristine fresh white burrata ball onto the crown of the steaming rigatoni pasta, while a slender spout pours a thin golden stream of extra virgin olive oil over the top of the cheese. Warm side daylight, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The burrata ball settles softly into the hot pasta as a glistening ribbon of golden olive oil pools in the delicate folds of the white cheese. Crisp ASMR kitchen audio: gentle squish of fresh cheese settling and delicate oil drizzle tap, no music, no voice, no glitches.
  ```

---

#### Plano `S15` (`17.90 s – 18.90 s`) — Pimienta Negra Molida y Albahaca Fresca
- **📎 ADJUNTAR EN `[+]`:** Imagen de `S14` (o `ANCHOR_03` con referencia de pasta)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle macro close-up of a dark wooden pepper mill held directly above the fresh white burrata ball that is resting on the crown of steaming, glossy orange vodka rigatoni pasta in the handcrafted cream ceramic bowl. Freshly cracked black pepper flecks showering over the white burrata, beside fresh dark green basil leaves on the pasta. Warm side lighting (4500K), 50mm f/2.0 lens, photorealistic editorial food photography, no faces, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The wooden pepper mill twists with two sharp clicks, depositing fragrant black pepper grains across the glossy burrata surface and steaming orange rigatoni pasta as fresh basil ribbons settle on the side. Crisp ASMR kitchen audio: two crisp sharp pepper mill ratchet clicks and subtle wood tap, no music, no voice, no glitches.
  ```

---

#### Plano `S16` (`18.90 s – 20.00 s`) — Bocado Hero Humeante hacia Cámara (*Payoff Final*)
- **📎 ADJUNTAR EN `[+]`:** Imagen de `S14` o `S15` (para mantener la pasta de fondo en el cuenco)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle macro close-up of a golden fork lifting a steaming, perfectly coated rigatoni pasta tube directly above the bowl filled with pasta and molten burrata. Strands of molten white stracciatella cheese and glossy orange vodka sauce cling to the ridges, with hot steam curls billowing upwards into warm window light. 50mm f/1.8 lens, shallow depth of field, photorealistic editorial food photography, no faces, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The fork slowly and smoothly elevates the steaming rigatoni toward the camera lens, showcasing the glistening texture of the sauce and strands of creamy cheese stretching into the warm morning light. Crisp ASMR kitchen audio: lush creamy lift sound and soft warm breath of rising steam, no music, no voice, no glitches.
  ```

---

## 5. Empaquetado SEO Bilingüe de Alto Impacto

### Título Optimizado (YouTube Shorts / Reels / TikTok):
> **Creamy Vodka Rigatoni with Molten Burrata 🧀🍝 #pasta #burrata #asmrcooking #vodkapasta #easyrecipes**

---

### Descripción con Gramajes Exactos (Bilingüe ES / EN):

```text
CREAMY VODKA RIGATONI WITH BURRATA (POV ASMR)
The ultimate creamy, glossy Italian comfort food with a molten fresh burrata crown.

Ingredients (2 Servings):
- 250g Rigatoni pasta (Bronze-cut)
- 1 fresh Burrata cheese ball (approx. 150g)
- 3 cloves Garlic, crushed
- 30ml Extra virgin olive oil
- 1 tsp Red chili flakes
- 70g Double concentrated tomato paste
- 40ml Vodka (unflavored)
- 160ml Heavy whipping cream (35% fat)
- 45g Parmigiano Reggiano, freshly grated
- 25g Cold unsalted butter
- Fresh basil leaves
- Freshly cracked black pepper & flaky sea salt

Steps:
1. Sauté crushed garlic and chili flakes in extra virgin olive oil until fragrant.
2. Add double concentrated tomato paste and fry for 2 minutes until deep rust red.
3. Deglaze with vodka and let it simmer for 60 seconds to evaporate alcohol.
4. Pour in heavy cream and stir into a velvety bright orange sauce.
5. Stir in Parmigiano Reggiano and cold butter until glossy.
6. Toss al dente rigatoni into the sauce with a splash of pasta water.
7. Plate in a warm ceramic bowl, top with the fresh burrata, torn basil, and cracked pepper. Slice open and enjoy!

---

RIGATONI CREMOSO AL VODKA CON BURRATA TRUFADA (POV ASMR)
Pasta italiana ultra sedosa, salsa naranja brillante y el desborde irresistible de una burrata fresca.

Ingredientes (2 Porciones):
- 250 g de Pasta Rigatoni (trefilada en bronce)
- 1 bola de Queso Burrata fresco (aprox. 150 g)
- 3 dientes de Ajo, aplastados
- 30 ml de Aceite de oliva virgen extra
- 1 cdta de Hojuelas de chile rojo
- 70 g de Pasta de tomate concentrada
- 40 ml de Vodka clásico
- 160 ml de Crema de leche / Nata para cocinar (35% M.G.)
- 45 g de Parmigiano Reggiano recién rallado
- 25 g de Mantequilla fría sin sal
- Hojas frescas de albahaca
- Pimienta negra recién molida y sal marina en escamas

Paso a paso:
1. Dorar los ajos aplastados y las hojuelas de chile en aceite de oliva virgen extra.
2. Incorporar el concentrado de tomate y sofreír 2 minutos hasta obtener un tono carmesí oscuro.
3. Desglasar con el vodka dejando reducir 1 minuto hasta evaporar el alcohol.
4. Verter la crema de leche y emulsionar hasta lograr una salsa naranja aterciopelada.
5. Agregar el Parmigiano Reggiano y la mantequilla fría para darle brillo espejo.
6. Incorporar los rigatonis al dente con un toque de agua de cocción y saltear.
7. Servir en cuenco cerámico, coronar con la burrata fresca, albahaca y pimienta recién molida. ¡Abrir la burrata y disfrutar!
```

---

## 6. Checklist de Ensamblaje y Render Final

Una vez que tengas los 16 clips descargados en `projects/P001_rigatoni_burrata_vodka/assets_flow/`:

1. **Auditoría, Backup Inmutable y Nivelación de Audio a -10 dB:**
   ```bash
   python3 .agent/skills/cocina-audiovisual-flow/scripts/process_clips.py --project projects/P001_rigatoni_burrata_vodka
   ```
2. **Auto-Ensamblaje en HyperFrames:**
   ```bash
   python3 projects/P001_rigatoni_burrata_vodka/assemble.py
   ```
3. **Validación Estricta:**
   ```bash
   npx hyperframes check projects/P001_rigatoni_burrata_vodka
   ```
4. **Render Master de Entrega (1080x1920 a 30 fps):**
   ```bash
   npx hyperframes render projects/P001_rigatoni_burrata_vodka --quality delivery --output projects/P001_rigatoni_burrata_vodka/renders/P001_rigatoni_burrata_final.mp4
   ```
