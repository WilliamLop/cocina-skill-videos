# Guía Maestra de Generación en Google Flow — Piloto P002: Smash Tacos de Birria con Costra de Queso y Consomé Caliente

- **Fecha:** 2026-10-19
- **Formato:** Formato 1: Cocina POV Editorial ASMR (1080x1920 Full 9:16, 50mm f/2.0 a 4500K, foley envolvente a -10 dB, cero rostros).
- **Inspiración:** `@culturaglotona`, `@cookingWITHfred`, `@alenakhmil`.
- **Proyecto HyperFrames:** [`projects/P002_birria_tacos_cheese/`](file:///Users/leidycalderon/Documents/resetasfenbaru/projects/P002_birria_tacos_cheese/)
- **Duración final:** **`20.00 segundos`** (`16 planos de video .mp4` · promedio `1.25 s/corte` · `1080x1920` a `30 fps`).

---

## 1. Reglas Canónicas y Flujo de Trabajo en Google Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       DIRECTIVAS INNEGOCIABLES DE FLOW                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 100% VIDEO (.mp4): Prohibido usar fotos estáticas en el render final.    │
│ 2. ANCLAS MAESTRAS: Generar ANCHOR_01, ANCHOR_02 y ANCHOR_03 vacías primero. │
│ 3. REGLA L17 (STEP-ANCHOR CHAINING): En los pasos de emplatado final        │
│    (S14, S15, S16), adjuntar en [+] la imagen del plano anterior            │
│    para garantizar 100% de coherencia en los tacos, queso y consomé.        │
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
     `projects/P002_birria_tacos_cheese/assets_flow/`
   - Nómbralos exactamente: **`S01.mp4`, `S02.mp4` ... hasta `S16.mp4`**.

---

## 2. Imágenes Ancla de Escenario (Generar primero en `Nano Banana Pro`)

Genera estas 3 imágenes vacías antes de crear ningún alimento y tenlas descargadas para adjuntarlas en el botón **`[+]`**:

### `ANCHOR_01`: Estación de Corte y Deshebrado (Tabla de Nogal)
```text
Vertical 9:16, 45-degree high-angle POV shot of a warm rustic kitchen workstation. A thick dark end-grain walnut wooden cutting board resting on a matte warm-grey limestone countertop. Soft natural morning daylight coming from a window on the left (4500K), subtle warm shadows falling to the right, softly blurred warm-grey kitchen wall behind. 50mm f/2.0 lens, shallow depth of field, photorealistic editorial food photography. Empty center of the board ready for food, no food, no hands, no people, no text.
```

### `ANCHOR_02`: Estación de Plancha de Hierro Fundido (Fuego y Costra de Queso)
```text
Vertical 9:16, 45-degree high-angle close-up shot of a heavy seasoned 30cm black cast-iron flat griddle skillet sitting on a sleek black induction cooktop. Warm natural side lighting from the left (4500K), subtle oily sheen on the dark cast iron surface, shallow depth of field, 50mm f/2.0 lens, photorealistic culinary photography, empty hot griddle, no hands, no food, no text.
```

### `ANCHOR_03`: Estación de Emplatado (Plato Rústico y Cuenco para Consomé)
```text
Vertical 9:16, 45-degree high-angle shot of a handcrafted rustic terracotta clay platter resting beside an empty small ceramic bowl on a dark walnut wooden table. Soft warm morning side light from the left (4500K), subtle linen napkin in the blurred background, 50mm f/2.0 lens, photorealistic editorial food photography, empty plate and empty bowl, no hands, no food, no text.
```

---

## 3. Mapa Cronométrico Sincronizado (20.00 segundos)

| Clip | Tiempo en Short | Duración | Recorte (`media-start`) | Acción Clave | Foley Nativo Veo 3.1 |
|---|---|---|---|---|---|
| **`S01.mp4`** | `0.00 s – 1.40 s` | `1.40 s` | `0.35 s` | **Hook 1:** Hero reveal tacos de birria dorados + cuenco de consomé | Murmullo cálido y vapor subiendo |
| **`S02.mp4`** | `1.40 s – 2.80 s` | `1.40 s` | `0.30 s` | **Hook 2:** "The Dip" taco crujiente sumergiéndose en consomé | Inmersión húmeda y chapoteo de caldo |
| **`S03.mp4`** | `2.80 s – 4.00 s` | `1.20 s` | `0.30 s` | Dos tenedores deshebrando carne tierna humeante | Desgarre suave de carne tierna |
| **`S04.mp4`** | `4.00 s – 5.50 s` | `1.50 s` | `0.30 s` | Picado rápido y fino de cilantro y cebolla morada | Cortes rítmicos contra nogal |
| **`S05.mp4`** | `5.50 s – 6.80 s` | `1.30 s` | `0.35 s` | Montón de queso rallado cayendo en plancha caliente | `SIZZLE` burbujeante de queso |
| **`S06.mp4`** | `6.80 s – 8.10 s` | `1.30 s` | `0.30 s` | Tortilla de maíz sumergida en olla de birria roja | Chapoteo denso y goteo de grasa roja |
| **`S07.mp4`** | `8.10 s – 9.40 s` | `1.30 s` | `0.35 s` | Tortilla roja pegada sobre el queso burbujeante | Chisporroteo fuerte de contacto |
| **`S08.mp4`** | `9.40 s – 10.80 s` | `1.40 s` | `0.35 s` | Montículo de carne de birria depositado en el centro | Caída pesada y vapor aromático |
| **`S09.mp4`** | `10.80 s – 12.00 s` | `1.20 s` | `0.35 s` | Espátula metálica dobla el taco (costra dorada) | Raspado metálico y crujido seco |
| **`S10.mp4`** | `12.00 s – 13.20 s` | `1.20 s` | `0.35 s` | Espátula presiona el taco contra la plancha caliente | Prensado firme y chisporroteo rápido |
| **`S11.mp4`** | `13.20 s – 14.40 s` | `1.20 s` | `0.35 s` | Cucharón de acero sirve consomé rojo en cuenco | Vertido líquido caliente en cerámica |
| **`S12.mp4`** | `14.40 s – 15.60 s` | `1.20 s` | `0.30 s` | Cilantro y cebolla morada caen sobre el consomé | Salpicadura sutil de vegetales |
| **`S13.mp4`** | `15.60 s – 16.80 s` | `1.20 s` | `0.35 s` | Espátula coloca los dos tacos junto al consomé | Asentamiento crujiente en fuente |
| **`S14.mp4`** | `16.80 s – 17.90 s` | `1.10 s` | `0.30 s` | Exprimido de lima fresca sobre los tacos dorados | Chorrito cítrico sobre costra |
| **`S15.mp4`** | `17.90 s – 18.90 s` | `1.00 s` | `0.30 s` | Separación y *Cheese Pull* elástico humeante | Estiramiento gomoso y crujido |
| **`S16.mp4`** | `18.90 s – 20.00 s` | `1.10 s` | `0.35 s` | **Payoff:** The Ultimate Dip levantado hacia la cámara | Chapoteo de caldo y vapor vivo |

---

## 4. Prompts Exactos Plano por Plano (`S01` a `S16`)

---

### BLOQUE 1 — Doble Hook Sensorial (`0.00 s – 2.80 s`)

#### Plano `S01` (`0.00 s – 1.40 s`) — Hero Reveal de Tacos y Consomé
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_03` (Plato Rústico y Cuenco)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of two golden-crispy quesabirria tacos with crunchy toasted cheese skirts resting on a handcrafted rustic terracotta clay platter, beside a small ceramic bowl of steaming deep red birria consommé garnished with fresh cilantro and diced red onions. Lime wedges resting on the side, hot steam plumes rising into warm side window light (4500K), 50mm f/2.0 lens, shallow depth of field, photorealistic editorial food photography, no hands, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  Slow cinematic push-in toward the crispy quesabirria tacos and the steaming bowl of red consommé, as rich aromatic steam curls into the air and juices glisten on the golden toasted cheese crust. Crisp ASMR kitchen audio: faint sizzling warmth and quiet cozy room ambiance, no music, no voice, no glitches.
  ```

---

#### Plano `S02` (`1.40 s – 2.80 s`) — The Dip: Taco Sumergiéndose en Consomé
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_03` (Plato Rústico y Cuenco)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle macro close-up of a hand holding the tip of a crispy golden quesabirria taco, plunging it deeply into a steaming bowl of rich ruby-red birria broth topped with chopped green cilantro. Droplets of glossy red chili oil and melted cheese beginning to swirl at the surface, warm side lighting (4500K), 50mm f/2.0 lens, photorealistic culinary photography, no faces, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The crispy taco dips smoothly into the steaming red consommé, creating rich appetizing ripples and splashes of red broth, then slowly lifts showing glossy broth cascading off the melted cheese. Crisp ASMR kitchen audio: rich mouthwatering wet broth dip and gentle splash, no music, no voice, no glitches.
  ```

---

### BLOQUE 2 — Preparación y Físicas Táctiles (`2.80 s – 5.50 s`)

#### Plano `S03` (`2.80 s – 4.00 s`) — Deshebrado de Carne de Birria Tierna
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_01` (Tabla de Nogal)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a thick, ultra-tender chunk of slow-cooked red chili braised beef birria resting in the center of a dark walnut cutting board. Two stainless steel forks are poised with tines digging into the meat, ready to pull apart into juicy shredded strands. Plumes of hot steam rising, warm morning window light (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The two forks effortlessly shred the tender beef birria in opposite directions, revealing glistening juicy meat fibers and releasing puffs of hot aromatic steam. Crisp ASMR kitchen audio: soft succulent meat pulling apart and gentle steam breath, no music, no voice, no glitches.
  ```

---

#### Plano `S04` (`4.00 s – 5.50 s`) — Picado Rápido de Cilantro y Cebolla Morada
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_01` (Tabla de Nogal)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a bundle of vibrant green cilantro and half a peeled red onion resting on a dark walnut cutting board. A sharp chef's knife blade is held 2 centimeters above the cilantro in a ready cutting stance. Warm natural side light (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The chef's knife executes rapid, rhythmic chopping cuts through the cilantro and red onion, producing crisp clean dices that tap on the wooden cutting board. Crisp ASMR kitchen audio: fast rhythmic sharp knife chops on solid walnut wood, no music, no voice, no glitches.
  ```

---

### BLOQUE 3 — Plancha Caliente, Queso y Tortilla (`5.50 s – 10.80 s`)

#### Plano `S05` (`5.50 s – 6.80 s`) — Queso Rallado en Plancha de Hierro
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Plancha de Hierro)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a generous handful of freshly shredded white Oaxaca and Monterey Jack cheese landing in a round mound on a hot seasoned black cast-iron griddle, the edges already beginning to bubble into a golden melted skirt. Warm side lighting, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The shredded cheese rapidly melts on the scorching cast iron, vigorously sizzling and creating an expanding golden-brown crispy lace skirt with bubbling hot oil. Crisp ASMR kitchen audio: immediate punchy sizzling cheese crackle on hot cast iron, no music, no voice, no glitches.
  ```

---

#### Plano `S06` (`6.80 s – 8.10 s`) — Inmersión de Tortilla en Olla de Birria
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_01` (o vista cenital de olla)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of kitchen tongs dipping a yellow corn tortilla into the simmering top layer of a large pot of deep red birria broth, soaking the tortilla in glossy chili-infused oil. Warm kitchen lighting, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The tongs submerge the tortilla into the bright red spiced oil layer and immediately lift it, showing red chili oil dripping back into the pot. Crisp ASMR kitchen audio: gentle broth immersion and oily liquid drips, no music, no voice, no glitches.
  ```

---

#### Plano `S07` (`8.10 s – 9.40 s`) — Tortilla Roja sobre Costra de Queso Caliente
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Plancha de Hierro)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of the red-soaked corn tortilla being placed directly on top of the bubbling, golden-melting cheese mound on the hot cast-iron griddle. Wisps of aromatic smoke rising, warm side light, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The red tortilla makes contact with the hot bubbling cheese, producing a loud explosive sizzle as steam shoots out from the edges. Crisp ASMR kitchen audio: explosive high-heat contact sizzle and searing crackle, no music, no voice, no glitches.
  ```

---

#### Plano `S08` (`9.40 s – 10.80 s`) — Colocación de Carne de Birria en el Taco
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Plancha de Hierro)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of kitchen tongs placing a generous mound of steaming, juicy shredded beef birria down the center of the tortilla and melted cheese on the sizzling griddle. Warm side lighting (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The tongs release the juicy shredded beef onto the sizzling tortilla, with flavorful red juices bubbling around the meat as fragrant steam curls up. Crisp ASMR kitchen audio: rich wet sizzling meat landing on hot griddle and bubbling fat, no music, no voice, no glitches.
  ```

---

### BLOQUE 4 — Doblado, Fusión y Crujido (`10.80 s – 15.60 s`)

#### Plano `S09` (`10.80 s – 12.00 s`) — Espátula Dobla el Taco a la Mitad
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Plancha de Hierro)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a stainless steel chef spatula sliding under one half of the crispy cheese tortilla on the griddle, poised to fold it over into a half-moon taco shape. Glistening golden-brown toasted cheese crust visible, warm side light, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The spatula decisively lifts and folds the tortilla in half over the beef filling, with the ultra-crispy toasted cheese crust crunching distinctly as it bends. Crisp ASMR kitchen audio: metallic spatula scrape and loud crunchy toasted cheese crack, no music, no voice, no glitches.
  ```

---

#### Plano `S10` (`12.00 s – 13.20 s`) — Prensado Firme con Espátula Plana
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Plancha de Hierro)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of the flat blade of the stainless steel spatula pressing firmly down on the folded quesabirria taco against the smoking hot cast iron. Red juices and cheese bubbling furiously at the seams, warm side light, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The spatula firmly presses down, flattening the taco and forcing out a burst of sizzling red chili fat and golden bubbles around the crispy edges. Crisp ASMR kitchen audio: heavy firm press and loud sizzling fry hiss, no music, no voice, no glitches.
  ```

---

#### Plano `S11` (`13.20 s – 14.40 s`) — Cucharón Sirve Consomé en Cuenco
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_03` (Plato Rústico y Cuenco)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a stainless steel ladle tilted above a rustic ceramic bowl, with a steaming stream of deep ruby-red birria consommé pouring into the bowl. Tiny golden oil droplets glistening on the surface, warm side lighting (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The ladle smoothly pours the hot red broth into the bowl, creating swirling golden oil circles as dense aromatic steam rises into the air. Crisp ASMR kitchen audio: rich steaming liquid soup pour into ceramic bowl, no music, no voice, no glitches.
  ```

---

#### Plano `S12` (`14.40 s – 15.60 s`) — Lluvia de Cilantro y Cebolla Morada en Consomé
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_03` (o fotograma de S11 con cuenco lleno)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a hand sprinkling finely minced green cilantro and vibrant diced red onion into the steaming bowl of red birria consommé. Warm side light (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The fresh cilantro and red onion shower down into the hot consommé, floating on the glistening red surface as steam swirls gently. Crisp ASMR kitchen audio: delicate water drop splashes and quiet room steam ambiance, no music, no voice, no glitches.
  ```

---

### BLOQUE 5 — Emplatado, Cítrico y Clímax Payoff (`15.60 s – 20.00 s`)
*(Aplicando con rigor la Regla L17: Step-Anchor Chaining)*

#### Plano `S13` (`15.60 s – 16.80 s`) — Emplatado de Tacos junto al Consomé
- **📎 ADJUNTAR EN `[+]`:** Imagen de `S12` (el cuenco con consomé recién servido)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a chef spatula placing two crispy, golden-red folded quesabirria tacos with crunchy toasted cheese skirts onto the rustic clay platter, right beside the steaming bowl of red consommé with cilantro and onion. Warm side window daylight (4500K), 50mm f/2.0 lens, photorealistic editorial food photography, no faces, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The spatula smoothly slides the two crunchy tacos onto the clay plate, settling them with a satisfying crisp tap beside the steaming bowl of broth. Crisp ASMR kitchen audio: crispy taco crust tap on clay platter and gentle steam rustle, no music, no voice, no glitches.
  ```

---

#### Plano `S14` (`16.80 s – 17.90 s`) — Exprimido de Lima Fresca en los Tacos
- **📎 ADJUNTAR EN `[+]`:** Imagen de `S13` (Regla L17: para mantener exactamente los mismos tacos y cuenco)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle macro close-up of fingers squeezing a fresh green lime wedge directly over the two crispy quesabirria tacos resting on the terracotta platter beside the consommé. Shiny droplets of fresh lime juice cascading onto the golden toasted cheese crust and beef filling, warm side lighting (4500K), 50mm f/2.0 lens, photorealistic, no faces, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The lime wedge is squeezed firmly, releasing a glistening spray of fresh citrus juice that lands on the sizzling hot crispy cheese crust with tiny savory pops. Crisp ASMR kitchen audio: wet juicy citrus squeeze spray and subtle sizzle tap, no music, no voice, no glitches.
  ```

---

#### Plano `S15` (`17.90 s – 18.90 s`) — Separación y *Cheese Pull* Elástico
- **📎 ADJUNTAR EN `[+]`:** Imagen de `S14` (Regla L17: continuidad total con los tacos recién bañados en lima)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle macro close-up of two hands holding the two cut halves of a crispy quesabirria taco directly above the terracotta platter, pulling them apart to reveal thick strands of molten white Oaxaca cheese stretching between the juicy red shredded beef. Hot steam plumes rising into warm window light (4500K), 50mm f/1.8 lens, photorealistic, no faces, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The hands slowly pull the two halves apart, extending thick elastic strings of molten gooey cheese that stretch dramatically while hot steam billows out from the juicy beef interior. Crisp ASMR kitchen audio: soft crispy tortilla crunch and rich gooey melted cheese stretching sound, no music, no voice, no glitches.
  ```

---

#### Plano `S16` (`18.90 s – 20.00 s`) — Payoff: The Ultimate Dip hacia la Cámara
- **📎 ADJUNTAR EN `[+]`:** Imagen de `S15` (Regla L17: para conservar el mismo cuenco de consomé y tacos de fondo)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle macro close-up of one half of the quesabirria taco with molten cheese lifted straight out of the red consommé bowl, elevated toward the camera lens. Glossy red chili broth cascading off the crispy toasted cheese edge with wisps of hot steam rising into warm morning sunlight. 50mm f/1.8 lens, shallow depth of field, photorealistic editorial food photography, no faces, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The dripping taco slowly rises closer to the camera lens, showcasing hot red broth droplets falling back into the bowl while steam curls dance in the warm morning light. Crisp ASMR kitchen audio: mouthwatering warm broth splash, gentle drip, and cozy steam exhale, no music, no voice, no glitches.
  ```

---

## 5. Empaquetado SEO Bilingüe de Alto Impacto

### Título Optimizado (YouTube Shorts / Reels / TikTok):
> **Crispy Birria Quesatacos with Hot Consomé Dip 🌮🔥 #birria #quesabirria #tacos #asmrcooking #mexicanfood**

---

### Descripción con Gramajes Exactos (Bilingüe ES / EN):

```text
CRISPY BIRRIA QUESATACOS WITH HOT CONSOMÉ (POV ASMR)
The ultimate crispy, juicy street food experience with a golden toasted cheese skirt and rich beef dipping broth.

Ingredients (Makes 4 Tacos):
- 4 Corn tortillas
- 300g Slow-cooked beef chuck & short rib birria, shredded
- 250ml Hot birria consommé (spiced beef broth)
- 180g Oaxaca cheese (or Mozzarella), freshly shredded
- 1/2 Red onion, finely diced
- Fresh cilantro, finely chopped
- 2 Limes, cut into wedges
- Spiced birria chili oil (skimmed from the broth)

Steps:
1. Dip corn tortillas into the top chili oil layer of the hot birria broth.
2. Sprinkle shredded cheese directly onto a screaming-hot cast-iron griddle until a bubbling golden skirt forms.
3. Place the oiled tortilla on top of the cheese to fuse.
4. Add a generous mound of juicy shredded beef birria down the center.
5. Fold into a half-moon taco and press firmly with a flat spatula until ultra-crispy.
6. Ladle hot consommé into a ceramic bowl and garnish with cilantro and diced red onion.
7. Plate the tacos, squeeze fresh lime over the crispy crust, dip deep into the broth, and enjoy!

---

SMASH TACOS DE BIRRIA CON COSTRA DE QUESO Y CONSOMÉ (POV ASMR)
La combinación perfecta de tortilla crujiente, costra de queso dorada en hierro fundido y el baño irresistible en consomé caliente.

Ingredientes (Para 4 Tacos):
- 4 Tortillas de maíz
- 300 g de Carne de res para birria (costilla y morcillo), cocida y deshebrada
- 250 ml de Consomé caliente de birria (caldo de res especiado)
- 180 g de Queso Oaxaca (o Mozzarella), recién rallado
- 1/2 Cebolla morada, finamente picada en cubos
- Cilantro fresco, finamente picado
- 2 Limas verdes, cortadas en cuartos
- Grasa/aceite de birria (la capa roja superior del caldo)

Paso a paso:
1. Pasar las tortillas de maíz por la capa de grasa roja del caldo de birria.
2. Poner montículos de queso rallado en la plancha de hierro hirviendo hasta formar una costra dorada burbujeante.
3. Colocar la tortilla sobre el queso para sellar la costra.
4. Añadir un montículo generoso de carne de birria jugosa en el centro.
5. Doblar el taco por la mitad con espátula y prensar hasta dorar ambos lados.
6. Servir el consomé hirviendo en un cuenco con cilantro fresco y cebolla morada.
7. Emplatar los tacos, exprimir lima fresca sobre la costra crujiente, sumergir en el consomé y disfrutar.
```

---

## 6. Checklist de Ensamblaje y Render Final

Una vez descargues los 16 clips en `projects/P002_birria_tacos_cheese/assets_flow/`:

1. **Auditoría, Backup Inmutable y Nivelación de Audio a -10 dB:**
   ```bash
   python3 .agent/skills/cocina-audiovisual-flow/scripts/process_clips.py --project projects/P002_birria_tacos_cheese
   ```
2. **Auto-Ensamblaje en HyperFrames:**
   ```bash
   python3 projects/P002_birria_tacos_cheese/assemble.py
   ```
3. **Validación Estricta:**
   ```bash
   npx hyperframes check projects/P002_birria_tacos_cheese
   ```
4. **Render Master de Entrega (1080x1920 a 30 fps):**
   ```bash
   npx hyperframes render projects/P002_birria_tacos_cheese -o projects/P002_birria_tacos_cheese/renders/P002_birria_tacos_final.mp4
   ```
