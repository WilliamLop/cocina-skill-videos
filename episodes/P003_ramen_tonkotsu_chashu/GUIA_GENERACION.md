# Guía Maestra de Generación en Google Flow — Piloto P003: Ramen Tonkotsu Cremoso con Chashu Sopleteado y Huevo Nitamago

- **Fecha:** 2026-10-20
- **Formato:** Formato 1: Cocina POV Editorial ASMR (1080x1920 Full 9:16, 50mm f/2.0 a 4500K, foley envolvente a -10 dB, cero rostros).
- **Duración final:** **`30.00 segundos`** (`21 planos de video .mp4` · promedio `1.43 s/corte` · `1080x1920` a `30 fps`).
- **Proyecto HyperFrames:** [`projects/P003_ramen_tonkotsu_chashu/`](file:///Users/leidycalderon/Documents/resetasfenbaru/projects/P003_ramen_tonkotsu_chashu/)

---

## 1. Reglas Canónicas y Flujo de Trabajo en Google Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       DIRECTIVAS INNEGOCIABLES DE FLOW                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 100% VIDEO (.mp4): Cero imágenes fijas en el ensamblaje.                │
│ 2. ANCLAS MAESTRAS: Generar ANCHOR_01, ANCHOR_02 y ANCHOR_03 vacías primero. │
│ 3. REGLA L17 (STEP-ANCHOR CHAINING): En los pasos de emplatado final        │
│    (S15 a S21), adjuntar en [+] la imagen del plano anterior para           │
│    garantizar 100% de coherencia en el cuenco, fideos y toppings.           │
│ 4. DURACIÓN DE VEO: Siempre generar 4 segundos en Image-to-Video.           │
│    HyperFrames recortará la inercia inicial (data-media-start).             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Protocolo de Trabajo en 2 Pasos por Plano:
1. **Paso A — Fotograma Inicial (`[IMG]`):**
   - Modo: `Create Image` → Modelo: `Nano Banana Pro` (o `Nano Banana 2.1`) → Formato: `Portrait (9:16)`.
   - Adjuntar en el botón **`[+]`** la referencia indicada (`ANCHOR_0X` o plano anterior por regla L17).
   - Pegar el prompt `[IMG]`.
2. **Paso B — Animación y Sonido Foley (`[VID]`):**
   - Seleccionar la imagen generada como **Start Frame**.
   - Modo: `Image to Video` → Modelo: `Veo 3.1 Fast` o `Veo 3.1 Quality` (según se indica).
   - Duración: `4s`.
   - Pegar el prompt `[VID]`.
3. **Descarga y Nombres de Archivo:**
   - Descarga los videos generados directamente en:
     `projects/P003_ramen_tonkotsu_chashu/assets_flow/`
   - Nómbralos exactamente: **`S01.mp4`, `S02.mp4` ... hasta `S21.mp4`**.

---

## 2. Imágenes Ancla de Escenario (Generar primero en `Nano Banana Pro`)

Genera estas 3 imágenes vacías antes de crear ningún alimento y tenlas descargadas para adjuntarlas en el botón **`[+]`**:

### `ANCHOR_01`: Estación de Corte y Sopleteado (Tabla de Nogal)
```text
Vertical 9:16, 45-degree high-angle POV shot of a warm rustic kitchen workstation. A thick dark end-grain walnut wooden cutting board resting on a matte warm-grey limestone countertop. Soft natural morning daylight coming from a window on the left (4500K), subtle warm shadows falling to the right, softly blurred warm-grey kitchen wall behind. 50mm f/2.0 lens, shallow depth of field, photorealistic editorial food photography. Empty center of the board ready for food, no food, no hands, no people, no text.
```

### `ANCHOR_02`: Estación de Fuego y Olla de Caldo
```text
Vertical 9:16, 45-degree high-angle close-up shot of a heavy stainless steel ramen stockpot with boiling water on a sleek commercial induction burner. Metallic reflections, rising atmospheric steam, warm side lighting from the left (4500K), shallow depth of field, 50mm f/2.0 lens, photorealistic, empty frame ready for tools, no hands, no text.
```

### `ANCHOR_03`: Estación de Emplatado (Cuenco Cerámico Japonés Negro Mate)
```text
Vertical 9:16, 45-degree high-angle shot of a handcrafted matte black ceramic ramen bowl resting on a dark walnut wooden table. Soft warm morning side light from the left (4500K), subtle linen napkin in the blurred background, 50mm f/2.0 lens, photorealistic editorial food photography, empty bowl, no food, no hands, no text.
```

---

## 3. Mapa Cronométrico Sincronizado (30.00 segundos)

| Clip | Tiempo en Short | Duración | Recorte (`media-start`) | Acción Clave | Foley Nativo Veo 3.1 |
|---|---|---|---|---|---|
| **`S01.mp4`** | `0.00 s – 1.40 s` | `1.40 s` | `0.35 s` | **Hook 1:** Hero reveal del cuenco de ramen humeante | Murmullo cálido y vapor vivo |
| **`S02.mp4`** | `1.40 s – 2.80 s` | `1.40 s` | `0.30 s` | **Hook 2:** Huevo nitamago cortado en dos (yema fundente) | Rotura suave y desborde dorado |
| **`S03.mp4`** | `2.80 s – 4.00 s` | `1.20 s` | `0.30 s` | Corte de rollo de chashu glaseado en la tabla | Corte limpio y golpe en madera |
| **`S04.mp4`** | `4.00 s – 5.30 s` | `1.30 s` | `0.35 s` | Soplete caramelizando las lonchas de chashu con llama | Soplido de soplete y chisporroteo |
| **`S05.mp4`** | `5.30 s – 6.50 s` | `1.20 s` | `0.30 s` | Picado rápido y fino de cebollín verde negi | Cortes rítmicos acelerados |
| **`S06.mp4`** | `6.50 s – 7.80 s` | `1.30 s` | `0.30 s` | Corte de lámina de alga nori crujiente | Crujido fibroso seco de alga |
| **`S07.mp4`** | `7.80 s – 9.20 s` | `1.40 s` | `0.35 s` | Olla de caldo Tonkotsu lechoso hirviendo | Borboteo profundo y espeso |
| **`S08.mp4`** | `9.20 s – 10.60 s` | `1.40 s` | `0.30 s` | Fideos frescos entrando en colador en agua hirviendo | Inmersión y chapoteo de pasta |
| **`S09.mp4`** | `10.60 s – 12.20 s` | `1.60 s` | `0.35 s` | Noodle Shake: colador sacudiéndose con golpes secos | Sacudida de colador y goteo |
| **`S10.mp4`** | `12.20 s – 13.80 s` | `1.60 s` | `0.35 s` | Tare y manteca aromatizada vertiéndose en cuenco | Vertido espeso en fondo de cuenco |
| **`S11.mp4`** | `13.80 s – 15.30 s` | `1.50 s` | `0.35 s` | Cucharón vierte caldo Tonkotsu hirviendo | Cascada fluida y remolino cremoso |
| **`S12.mp4`** | `15.30 s – 16.80 s` | `1.50 s` | `0.35 s` | Entrada de fideos escurridos en el caldo | Entrada suave de fideos humeantes |
| **`S13.mp4`** | `16.80 s – 18.30 s` | `1.50 s` | `0.35 s` | Palillos peinan y pliegan los fideos en el caldo | Peinado y fricción sedosa |
| **`S14.mp4`** | `18.30 s – 19.80 s` | `1.50 s` | `0.35 s` | Gotas de aceite negro Mayu flotando sobre el caldo | Goteo de aceite y círculos oscuros |
| **`S15.mp4`** | `19.80 s – 21.30 s` | `1.50 s` | `0.35 s` | Colocación de lonchas de chashu dorado sopleteado | Asentamiento suave sobre fideos |
| **`S16.mp4`** | `21.30 s – 22.80 s` | `1.50 s` | `0.30 s` | Colocación de medio huevo nitamago con yema | Asentamiento húmedo del huevo |
| **`S17.mp4`** | `22.80 s – 24.30 s` | `1.50 s` | `0.30 s` | Lluvia de cebollín fresco al centro | Lluvia ligera de vegetales |
| **`S18.mp4`** | `24.30 s – 25.80 s` | `1.50 s` | `0.30 s` | Inserción de alga nori en el borde interior | Roce seco de alga en cuenco |
| **`S19.mp4`** | `25.80 s – 27.20 s` | `1.40 s` | `0.30 s` | Palillos presionan la yema y se desborda en el caldo | Desborde cremoso y vapor vivo |
| **`S20.mp4`** | `27.20 s – 28.60 s` | `1.40 s` | `0.35 s` | Cuchara sopera levantando caldo cremoso y fideos | Cuchara sumergiéndose y subiendo |
| **`S21.mp4`** | `28.60 s – 30.00 s` | `1.40 s` | `0.35 s` | **Payoff:** Palillos elevan bocado de fideos y chashu | Levantamiento apetitoso con vapor vivo |

---

## 4. Prompts Exactos Plano por Plano (`S01` a `S21`)

---

### BLOQUE 1 — Doble Hook Sensorial (`0.00 s – 2.80 s`)

#### Plano `S01` (`0.00 s – 1.40 s`) — Hero Reveal del Cuenco de Ramen
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_03` (Cuenco Cerámico Negro Mate)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a steaming handcrafted matte black ceramic bowl of authentic Tonkotsu ramen resting on a dark walnut table. Rich creamy ivory pork bone broth, neatly folded yellow ramen noodles, two torched chashu pork belly slices with caramelized edges, half a ramen egg with glistening jammy orange yolk, a mound of chopped green scallions, crispy black nori seaweed sheet, and swirls of black garlic oil on top. Delicate wisps of hot steam rising into warm side window light (4500K), 50mm f/2.0 lens, photorealistic editorial food photography, no hands, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  Slow cinematic push-in toward the steaming ramen bowl as thick clouds of aromatic steam rise and glossy oil droplets glisten on the ivory broth. Crisp ASMR kitchen audio: faint bubbling warmth and quiet cozy room ambiance, no music, no voice, no glitches.
  ```

---

#### Plano `S02` (`1.40 s – 2.80 s`) — Hook del Huevo Nitamago (Yema Fundente)
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_01` (Tabla de Nogal)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle macro close-up of a soy-marinated soft-boiled ramen egg resting on a dark walnut cutting board. A thin cutting wire / sharp knife blade is held horizontally 2 centimeters above the center, positioned to slice cleanly through the middle. Warm side lighting (4500K), 50mm f/2.0 lens, photorealistic culinary photography, no faces, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The cutting wire slices decisively down through the center of the marinated egg, parting the tender white halves to reveal an ultra-glossy, rich molten jammy orange yolk that slowly oozes forward with warm steam curls. Crisp ASMR kitchen audio: clean wet slice and soft lush jammy yolk ooze, no music, no voice, no glitches.
  ```

---

### BLOQUE 2 — Preparación, Corte y Sopleteado (`2.80 s – 7.80 s`)

#### Plano `S03` (`2.80 s – 4.00 s`) — Corte de Chashu en Tabla de Nogal
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_01` (Tabla de Nogal)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a rolled braised pork belly chashu log resting on a dark walnut cutting board. A sharp Japanese chef's knife blade is poised 2 centimeters above the front edge, ready to slice a thick medallion of tender caramelized pork. Warm natural side light (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The sharp knife slices smoothly through the tender chashu roll in one continuous draw, dropping a juicy round slice of braised pork belly onto the board with a clean wooden tap. Crisp ASMR kitchen audio: clean sharp knife slice through tender meat and dull wooden cutting board tap, no music, no voice, no glitches.
  ```

---

#### Plano `S04` (`4.00 s – 5.30 s`) — Sopleteado de Chashu con Fuego Vivo
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_01` (Tabla de Nogal)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of two thick slices of pork chashu resting on a dark metal prep tray on the wooden workstation. The brass nozzle of a culinary blowtorch is angled 5 centimeters above the meat, with a sharp blue and bright orange flame just beginning to ignite towards the pork belly fat. Warm side light, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The roaring blue flame of the culinary torch sweeps across the pork chashu slices, instantly blistering the pork fat into sizzling golden bubbles and caramelizing the sweet soy glaze with wisps of aromatic white smoke. Crisp ASMR kitchen audio: roaring gas blowtorch flame whoosh and aggressive crackling fat sizzle, no music, no voice, no glitches.
  ```

---

#### Plano `S05` (`5.30 s – 6.50 s`) — Picado Rápido de Cebollín Negi
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_01` (Tabla de Nogal)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a bundle of vibrant green Japanese scallions (negi) resting on a dark walnut cutting board. A chef's knife blade is poised 2 centimeters above the scallions in a ready chopping stance. Warm morning side light (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The chef's knife executes ultra-fast, rhythmic push cuts through the green scallions, spraying delicate paper-thin circular green rings across the dark wood surface. Crisp ASMR kitchen audio: rapid rhythmic crisp knife taps against solid walnut wood, no music, no voice, no glitches.
  ```

---

#### Plano `S06` (`6.50 s – 7.80 s`) — Corte de Lámina de Alga Nori
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_01` (Tabla de Nogal)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a whole dark-green toasted nori seaweed sheet resting on the cutting board. Stainless steel kitchen shears are positioned 2 centimeters above, ready to snip the sheet into rectangular strips. Warm natural side light, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The shears cleanly snip through the brittle nori sheet in one crisp motion, separating a perfect crisp rectangular piece. Crisp ASMR kitchen audio: dry brittle paper-crisp nori crackle and clean metallic snip, no music, no voice, no glitches.
  ```

---

### BLOQUE 3 — Olla de Caldo, Fideos y Escurrido (`7.80 s – 13.80 s`)

#### Plano `S07` (`7.80 s – 9.20 s`) — Olla de Caldo Tonkotsu Hirviendo
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Olla de Acero Inoxidable)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a stainless steel stockpot filled with bubbling, velvety rich ivory-white Tonkotsu pork broth on a commercial induction burner. A stainless steel ladle is partially submerged in the broth, dense clouds of steam billowing upwards into warm kitchen light. 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The rich milky pork broth bubbles vigorously with rolling waves of white froth, sending dense aromatic plumes of steam curling toward the ceiling as the ladle gently scoops through the liquid. Crisp ASMR kitchen audio: deep rolling heavy broth boil and bubbling liquid warmth, no music, no voice, no glitches.
  ```

---

#### Plano `S08` (`9.20 s – 10.60 s`) — Inmersión de Fideos Frescos en Agua
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Olla de Acero Inoxidable)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a cylindrical stainless steel noodle boiling basket holding a portion of fresh yellow crinkled ramen noodles, held 2 centimeters directly above boiling clear water. Rising steam, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The basket plunges swiftly into the rolling boiling water, with long wooden chopsticks immediately stirring the noodles into swirling submerged motion. Crisp ASMR kitchen audio: fast boiling water splash and wooden chopsticks swirling submerged noodles, no music, no voice, no glitches.
  ```

---

#### Plano `S09` (`10.60 s – 12.20 s`) — Noodle Shake: Escurrido Enérgico
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Olla de Acero Inoxidable)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of the noodle basket lifted high above the pot, holding steaming, cooked yellow ramen noodles glistening with hot water droplets, paused right before a downward shaking snap. Warm side light, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The chef executes two sharp, powerful downward snaps with the basket (te-kiri noodle shake), expelling airborne droplets of water with clouds of steam shooting out. Crisp ASMR kitchen audio: two loud sharp basket downward snaps and water droplets showering onto the metal grate, no music, no voice, no glitches.
  ```

---

#### Plano `S10` (`12.20 s – 13.80 s`) — Tare y Manteca Aromatizada en Cuenco
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_03` (Cuenco Cerámico Negro Mate)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a stainless steel sauce spoon tilted above the empty matte black ceramic bowl, with a glossy spoonful of dark soy ramen tare seasoning and golden rendered pork lard beginning to pour onto the bottom of the bowl. Warm side lighting (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The dark tare seasoning and aromatic golden fat pour into the base of the black ceramic bowl with a glossy splatter, pooling smoothly in the bottom. Crisp ASMR kitchen audio: thick glossy sauce drip and gentle ceramic bottom tap, no music, no voice, no glitches.
  ```

---

### BLOQUE 4 — Fusión de Caldo y Nido de Fideos (`13.80 s – 19.80 s`)

#### Plano `S11` (`13.80 s – 15.30 s`) — Cucharón Vierte Caldo Tonkotsu Hirviendo
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_03` (Cuenco Cerámico Negro Mate)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a round stainless steel ladle tilted above the black ceramic bowl, with a thick cascade of steaming, creamy ivory Tonkotsu broth pouring in, blending into the dark tare at the bottom. Dense steam rising, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  A generous stream of steaming milky pork broth pours smoothly from the ladle, swirling into the dark seasoning and creating a silky, creamy latte-colored ramen broth with golden fat bubbles floating on top. Crisp ASMR kitchen audio: rich heavy steaming soup pour into ceramic bowl and gentle swirling slosh, no music, no voice, no glitches.
  ```

---

#### Plano `S12` (`15.30 s – 16.80 s`) — Entrada de Fideos en el Caldo
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_03` (Cuenco Cerámico Negro Mate)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of the stainless steel noodle basket tilted right over the filled black bowl, with steaming hot yellow noodles beginning to slide out into the creamy broth. Warm side light (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The steaming noodles slide cleanly out of the basket and plunge into the warm creamy broth with a gentle, satisfying splash. Crisp ASMR kitchen audio: soft wet noodle bundle landing in warm broth and subtle splash, no music, no voice, no glitches.
  ```

---

#### Plano `S13` (`16.80 s – 18.30 s`) — Peinado de Fideos con Palillos
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_03` (Cuenco Cerámico Negro Mate)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of two long dark wooden cooking chopsticks inserted into the noodles in the creamy broth, lifting slightly to fold and arrange the noodles into a neat, straight parallel nest. Warm side light, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The wooden chopsticks smoothly comb and fold the noodles back and forth through the creamy broth, forming a neat, elegant rectangular noodle bed with hot steam swirling. Crisp ASMR kitchen audio: mouthwatering wet noodle friction and gentle broth fold, no music, no voice, no glitches.
  ```

---

#### Plano `S14` (`18.30 s – 19.80 s`) — Gotas de Aceite Negro Mayu
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_03` (o fotograma del cuenco con fideos peinados)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a small porcelain spoon tilted above the creamy ivory ramen broth, dripping glossy pitch-black roasted garlic oil (Mayu) onto the surface beside the noodles. Warm side lighting (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  Slow glossy droplets of dark black garlic oil fall onto the milky surface, expanding into striking ebony marbled rings that contrast beautifully against the ivory broth. Crisp ASMR kitchen audio: delicate oil droplet taps and quiet cozy room steam ambiance, no music, no voice, no glitches.
  ```

---

### BLOQUE 5 — Emplatado y Toppings Finales — Regla L17 Step-Anchor Chaining (`19.80 s – 25.80 s`)

#### Plano `S15` (`19.80 s – 21.30 s`) — Colocación de Lonchas de Chashu
- **📎 ADJUNTAR EN `[+]`:** Imagen de `S14` (Regla L17: para mantener exactamente el mismo cuenco, caldo y gotas de Mayu)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of chef kitchen tongs carefully placing two thick, torched and caramelized pork chashu slices onto the left side of the folded noodle bed in the matte black ramen bowl filled with creamy Tonkotsu broth. Charred edges glistening, warm side light (4500K), 50mm f/2.0 lens, photorealistic, no faces, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The tongs gently rest the torched chashu slices on top of the noodles, with the pork settling into the broth as juices glisten under the window light. Crisp ASMR kitchen audio: soft succulent meat settling on wet noodles and subtle steam exhale, no music, no voice, no glitches.
  ```

---

#### Plano `S16` (`21.30 s – 22.80 s`) — Colocación del Huevo Nitamago
- **📎 ADJUNTAR EN `[+]`:** Imagen de `S15` (Regla L17: para mantener el chashu ya colocado)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of chef tongs placing half a soy-marinated ramen egg with its radiant jammy orange yolk facing upwards, resting gently next to the torched chashu in the black ceramic bowl. Steam rising, warm side lighting (4500K), 50mm f/2.0 lens, photorealistic, no faces, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The egg half settles tenderly onto the noodle bed beside the chashu, with its molten orange yolk wobbling softly under the warm light. Crisp ASMR kitchen audio: gentle soft wet egg settle and quiet warm room ambiance, no music, no voice, no glitches.
  ```

---

#### Plano `S17` (`22.80 s – 24.30 s`) — Lluvia de Cebollín Verde al Centro
- **📎 ADJUNTAR EN `[+]`:** Imagen de `S16` (Regla L17: continuidad con chashu y huevo)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of fingers dropping a neat, vibrant green mound of finely sliced negi scallions directly into the center of the ramen bowl between the egg and chashu. Warm side lighting (4500K), 50mm f/2.0 lens, photorealistic, no faces, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The fresh green scallion rings scatter neatly over the center of the bowl, resting crisply against the creamy broth and noodles. Crisp ASMR kitchen audio: delicate airy scatter of fresh chopped scallions, no music, no voice, no glitches.
  ```

---

#### Plano `S18` (`24.30 s – 25.80 s`) — Inserción de Alga Nori en el Borde
- **📎 ADJUNTAR EN `[+]`:** Imagen de `S17` (Regla L17: tazón completamente montado)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of tongs sliding a crisp, dark rectangular sheet of toasted nori seaweed vertically into the back inner rim of the matte black ramen bowl, standing upright behind the chashu. Warm side window light, 50mm f/2.0 lens, photorealistic, no faces, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The nori sheet slides smoothly into the broth at the edge of the bowl, standing proud and crisp against the dark ceramic rim as rising steam envelops it. Crisp ASMR kitchen audio: crisp dry nori tuck into ceramic bowl and gentle broth whisper, no music, no voice, no glitches.
  ```

---

### BLOQUE 6 — Payoff Supremo Multi-Ángulo (`25.80 s – 30.00 s`)

#### Plano `S19` (`25.80 s – 27.20 s`) — Macro Presión de la Yema Fundente
- **📎 ADJUNTAR EN `[+]`:** Imagen de `S18` (Regla L17: cuenco completo de ramen terminado)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle macro close-up of wooden chopsticks gently pressing the edge of the jammy orange egg yolk inside the black ramen bowl, with the molten yolk beginning to break and seep into the creamy white Tonkotsu broth. Hot steam rising, 50mm f/1.8 lens, photorealistic, no faces, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The chopsticks nudge the egg, causing a rich, thick ribbon of golden jammy yolk to slowly bleed into the milky pork broth and wrap around the noodles. Crisp ASMR kitchen audio: soft velvety yolk break and luscious creamy slosh, no music, no voice, no glitches.
  ```

---

#### Plano `S20` (`27.20 s – 28.60 s`) — Cuchara Sopera Levantando Caldo
- **📎 ADJUNTAR EN `[+]`:** Imagen de `S18` (o `S19`)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle macro close-up of a traditional black ceramic Asian soup spoon dipped deep into the bowl, lifting a full spoonful of rich ivory Tonkotsu broth with marbled black Mayu garlic oil and chopped green scallions. Steam curls rising into warm 4500K window light, 50mm f/1.8 lens, photorealistic, no faces, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The soup spoon rises smoothly from the bowl, lifting glistening creamy broth with black garlic oil droplets dancing on the spoon's edge as warm steam billows. Crisp ASMR kitchen audio: deep appetizing soup spoon lift and gentle liquid drip, no music, no voice, no glitches.
  ```

---

#### Plano `S21` (`28.60 s – 30.00 s`) — Payoff Final: Palillos Elevando Fideos y Chashu
- **📎 ADJUNTAR EN `[+]`:** Imagen de `S18` (para conservar el cuenco de fondo)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle macro close-up of dark wooden chopsticks lifting a steaming, generous clump of glistening yellow ramen noodles alongside a slice of torched chashu pork belly directly above the black ceramic bowl. Strings of broth dripping down, intense plumes of hot aromatic steam curling into warm morning sunlight. 50mm f/1.8 lens, shallow depth of field, photorealistic editorial food photography, no faces, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The chopsticks smoothly elevate the steaming noodles and glistening chashu slice toward the camera lens, showcasing rich sauce clinging to every noodle strand while wisps of hot steam dance in the light. Crisp ASMR kitchen audio: mouthwatering warm noodle lift and lush quiet steam breath, no music, no voice, no glitches.
  ```

---

## 5. Empaquetado SEO Bilingüe de Alto Impacto

### Título Optimizado (YouTube Shorts / Reels / TikTok):
> **Authentic Tonkotsu Ramen with Torched Chashu 🍜🔥 #ramen #tonkotsu #chashu #asmrcooking #japanesefood #noodles**

---

### Descripción con Gramajes Exactos (Bilingüe ES / EN):

```text
RAMEN TONKOTSU CREMOSO CON CHASHU SOPLETEADO Y HUEVO NITAMAGO (POV ASMR)
La ceremonia japonesa definitiva: caldo blanco lechoso de 12 horas, fideos al dente peinados a mano, panceta caramelizada con fuego vivo y la yema fundente perfecta.

Ingredientes (2 Porciones):
- 260 g de Fideos ramen frescos artesanales
- 600 ml de Caldo Tonkotsu espeso (huesos de cerdo reducidos)
- 4 lonchas de Panceta Chashu glaseada (aprox. 180 g)
- 2 Huevos Nitamago marinados en salsa de soja, mirin y dashi
- 40 ml de Tare shoyu / shio concentrado
- 20 g de Manteca aromatizada de cerdo
- 15 ml de Aceite negro de ajo tostado (Mayu)
- 4 tallos de Cebollín japonés fresco (Negi), finamente picado
- 2 láminas de Alga Nori tostada

Paso a paso:
1. Cortar las lonchas de panceta chashu y sopletear con fuego vivo hasta caramelizar la grasa.
2. Cocer los fideos frescos en agua hirviendo durante 90 segundos; sacudir enérgicamente con colador de bambú.
3. Servir el tare concentrado y la manteca aromatizada en el fondo del cuenco cerámico negro.
4. Verter el caldo Tonkotsu hirviendo y mezclar con cuchara.
5. Introducir los fideos y peinar con palillos formando un nido simétrico.
6. Coronar con gotas de aceite negro Mayu, las lonchas de chashu sopleteadas, medio huevo nitamago, cebollín y alga nori.
7. Romper la yema dorada sobre el caldo y disfrutar del bocado humeante.

---

AUTHENTIC CREAMY TONKOTSU RAMEN WITH TORCHED CHASHU (POV ASMR)
The ultimate Japanese culinary ceremony: 12-hour rich ivory pork bone broth, hand-folded noodles, blowtorch-caramelized chashu pork belly, and a molten jammy ramen egg.

Ingredients (2 Servings):
- 260g Fresh artisanal ramen noodles
- 600ml Rich Tonkotsu pork bone broth
- 4 slices Braised Chashu pork belly (approx. 180g)
- 2 Nitamago soft-boiled eggs marinated in soy, mirin & dashi
- 40ml Concentrated ramen tare seasoning
- 20g Aromatic rendered pork lard
- 15ml Black garlic oil (Mayu)
- 4 stalks Fresh Japanese scallions (Negi), thinly sliced
- 2 sheets Crispy toasted nori seaweed

Steps:
1. Slice the braised pork chashu and torch with a culinary blowtorch until fat is bubbly and caramelized.
2. Boil fresh ramen noodles for 90 seconds; execute a firm noodle shake to drain thoroughly.
3. Pour tare seasoning and aromatic fat into the bottom of the black ceramic bowl.
4. Ladle in boiling Tonkotsu broth and stir gently into an ivory latte-colored soup.
5. Add noodles and comb with chopsticks into an elegant folded nest.
6. Garnish with swirls of black garlic oil, torched chashu, half jammy egg, green negi, and nori.
7. Break the molten yolk into the broth, lift steaming noodles, and enjoy!
```

---

## 6. Checklist de Ensamblaje y Render Final

Una vez descargues los 21 clips en `projects/P003_ramen_tonkotsu_chashu/assets_flow/`:

1. **Auditoría, Backup Inmutable y Nivelación de Audio a -10 dB:**
   ```bash
   python3 .agent/skills/cocina-audiovisual-flow/scripts/process_clips.py --project projects/P003_ramen_tonkotsu_chashu
   ```
2. **Auto-Ensamblaje en HyperFrames:**
   ```bash
   python3 projects/P003_ramen_tonkotsu_chashu/assemble.py
   ```
3. **Validación Estricta:**
   ```bash
   npx hyperframes check projects/P003_ramen_tonkotsu_chashu
   ```
4. **Render Master de Entrega (1080x1920 a 30 fps):**
   ```bash
   npx hyperframes render projects/P003_ramen_tonkotsu_chashu -o projects/P003_ramen_tonkotsu_chashu/renders/P003_ramen_tonkotsu_final.mp4
   ```
