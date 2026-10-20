# Guía Maestra de Generación en Google Flow — Piloto P004: Tacos de Ramen de Escandalosos (We Bare Bears)

- **Fecha:** 2026-10-20
- **Formato:** Formato 2: Recreación de Caricaturas en Split-Screen (Dual-Screen 1080x612 arriba + 1080x1276 abajo con transición a Pantalla Completa 1080x1920 en el segundo 16.20).
- **Episodio de origen:** *Escandalosos* (*We Bare Bears*), Temporada 1: "El Camión de Comida" (*Food Truck*). Diálogo original latino con Pardo, Panda y Polar intentando conseguir tacos de ramen en la feria gastronómica.
- **Duración final:** **`20.00 segundos`** (`14 planos de cocina en video .mp4` · promedio `1.43 s/corte` · `1080x1920` a `30 fps`).
- **Clip animado superior:** [`projects/P004_tacos_ramen_escandalosos/assets/cartoon_top.mp4`](file:///Users/leidycalderon/Documents/resetasfenbaru/projects/P004_tacos_ramen_escandalosos/assets/cartoon_top.mp4) (`1080x612 px`, `30 fps`, audio estéreo latino a `volumen 0.95`, finaliza exactamente en `16.20 s`).
- **Proyecto HyperFrames:** [`projects/P004_tacos_ramen_escandalosos/`](file:///Users/leidycalderon/Documents/resetasfenbaru/projects/P004_tacos_ramen_escandalosos/)

---

## 1. Reglas Canónicas y Flujo de Trabajo en Google Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       DIRECTIVAS INNEGOCIABLES DE FLOW                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 100% VIDEO (.mp4): Prohibido usar fotos fijas en el ensamblaje.          │
│ 2. ANCLAS MAESTRAS: Generar ANCHOR_01, ANCHOR_02 y ANCHOR_03 vacías primero. │
│ 3. REGLA L17 (STEP-ANCHOR CHAINING): En los pasos de armado final (S09 a     │
│    S14), adjuntar en [+] la imagen del plano anterior para mantener         │
│    idéntica la forma, grosor y curvatura de la concha de ramen.             │
│ 4. DURACIÓN DE VEO: Siempre generar 4 segundos en Image-to-Video.           │
│    HyperFrames recortará la inercia inicial (data-media-start = 0.30–0.35s).│
│ 5. PANTALLA COMPLETA EN 16.20s: Cuando los osos terminan de devorar arriba, │
│    la cocina invade el 100% de la pantalla para el clímax crujiente.        │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Protocolo Operativo en 2 Pasos por Plano:
1. **Paso A — Fotograma Inicial (`[IMG]`):**
   - Modo: `Create Image` → Modelo: `Nano Banana Pro` (o `Nano Banana 2.1`) → Formato: `Portrait (9:16)`.
   - Adjuntar en el botón **`[+]`** la referencia indicada (`ANCHOR_0X` o el plano previo por regla L17).
   - Pegar el prompt `[IMG]`.
2. **Paso B — Animación y Sonido Foley (`[VID]`):**
   - Seleccionar la imagen generada como **Start Frame**.
   - Modo: `Image to Video` → Modelo: `Veo 3.1 Fast` o `Veo 3.1 Quality` (según se especifica).
   - Duración: `4s`.
   - Pegar el prompt `[VID]`.
3. **Descarga y Nombres de Archivo:**
   - Descarga los videos generados directamente en:
     `projects/P004_tacos_ramen_escandalosos/assets_flow/`
   - Nómbralos exactamente: **`S01.mp4`, `S02.mp4` ... hasta `S14.mp4`**.

---

## 2. Imágenes Ancla de Escenario (Generar primero en `Nano Banana Pro`)

Genera estas 3 imágenes vacías antes de crear ningún alimento y tenlas descargadas para adjuntarlas en el botón **`[+]`**:

### `ANCHOR_01`: Estación Principal de Ensamblaje y Corte (Tabla de Nogal)
```text
Vertical 9:16, 45-degree high-angle POV shot of a warm rustic kitchen workstation. A thick dark end-grain walnut wooden cutting board resting on a matte warm-grey limestone countertop. Soft natural morning daylight coming from a window on the left (4500K), subtle warm shadows falling to the right, softly blurred warm-grey kitchen wall behind. 50mm f/2.0 lens, shallow depth of field, photorealistic editorial food photography. Empty center of the board ready for food, no food, no hands, no people, no text.
```

### `ANCHOR_02`: Estación de Fuego y Sartén (Hierro Fundido / Plancha)
```text
Vertical 9:16, 45-degree high-angle close-up shot of a heavy seasoned 28cm black cast-iron skillet sitting on a sleek commercial induction cooktop. Warm natural side lighting from the left (4500K), subtle metallic oil sheen, shallow depth of field, 50mm f/2.0 lens, photorealistic, empty pan ready for cooking, no hands, no food, no text.
```

### `ANCHOR_03`: Olla Hirviendo de Caldo / Fideos
```text
Vertical 9:16, 45-degree high-angle close-up shot of a heavy stainless steel soup pot filled with rapidly boiling clear water on a commercial induction burner. Metallic reflections, rolling white steam rising into warm side light (4500K), shallow depth of field, 50mm f/2.0 lens, photorealistic, empty frame ready for tools, no hands, no text.
```

---

## 3. Mapa Cronométrico Sincronizado Segundo a Segundo (20.00 s)

| Plano | Tiempo Short | Duración | Ventana | Diálogo / Acción Caricatura (ARRIBA) | Acción Cocina en Flow (ABAJO) | Foley Nativo Veo 3.1 |
|---|---|---|---|---|---|---|
| **`S01.mp4`** | `0.00s – 1.50s` | `1.50s` | `0.35s` | Pardo: *"¡Por favor, señor, tacos de ramen!"* | **Hook 1 (Hero Reveal):** Taco de ramen dorado, relleno de carne humeante | Murmullo cálido de cocina y chisporroteo suave |
| **`S02.mp4`** | `1.50s – 2.80s` | `1.30s` | `0.30s` | Pardo apoyado en mostrador esperando | **Hook 2 (Textura):** Pinzas presionan concha de ramen crujiente (**CRUNCH**) | Crujido nítido de fideos tostados sobre madera |
| **`S03.mp4`** | `2.80s – 4.10s` | `1.30s` | `0.30s` | Panda: *"¡Hemos esperado mucho!..."* | Chorro de aceite de sésamo y cebolla picada a sartén | Chisporroteo inmediato y enérgico de cebolla |
| **`S04.mp4`** | `4.10s – 5.50s` | `1.40s` | `0.35s` | Panda: *"...¡Muero de hambre!"* | Carne picada de res entra a sartén caliente con vapor vivo | Golpe sordo de carne y chisporroteo profundo |
| **`S05.mp4`** | `5.50s – 6.90s` | `1.40s` | `0.35s` | Fila enorme de gente en el parque | Cascada de soya oscura, mirin y ajo caramelizando la carne | Chapoteo de salsa espesa y reducción chisporroteante |
| **`S06.mp4`** | `6.90s – 8.20s` | `1.30s` | `0.30s` | Chica desliza plato con 1 taco. Pardo: *"¿Solo uno?"* | Palillos elevan fideos de ramen ondulados hirviendo | Borboteo de agua y escurrido de fideos calientes |
| **`S07.mp4`** | `8.20s – 9.60s` | `1.40s` | `0.35s` | Chica del camión grita: *"¡Siguiente!"* | Prensa metálica aplana fideos en sartén dorando disco | Prensado metálico y crujido burbujeante en mantequilla |
| **`S08.mp4`** | `9.60s – 10.90s` | `1.30s` | `0.30s` | Pardo mira el mini taco resignado | Espátula dobla disco dorado en forma de taco (**CRUNCH**) | Crujido de flexión de concha tostada y raspado de espátula |
| **`S09.mp4`** | `10.90s – 12.20s` | `1.30s` | `0.35s` | Pardo: *"Bien, hermanos..."* | Cuchara colma la concha de ramen con carne picada jugosa | Asentamiento jugoso de carne caliente en concha |
| **`S10.mp4`** | `12.20s – 13.50s` | `1.30s` | `0.30s` | Pardo: *"...bocados pequeños..."* | Pinzas colocan cama de col verde crujiente rallada | Crujido vegetal fresco sobre carne caliente |
| **`S11.mp4`** | `13.50s – 14.80s` | `1.30s` | `0.30s` | Pardo: *"...sabórenlo..."* (Ponen patitas) | Cuchara vierte pico de gallo brillante con cilantro | Toque húmedo de verduras y goteo cítrico |
| **`S12.mp4`** | `14.80s – 16.20s` | `1.40s` | `0.35s` | ¡Los tres osos devoran: *"NOM NOM NOM!"*! | Hilo de mayonesa spicy en zigzag + semillas de sésamo | Chorro suave de salsa cremosa y lluvia de sésamo |
| **`S13.mp4`** | `16.20s – 18.10s` | `1.90s` | `0.35s` | **PANTALLA COMPLETA (1080x1920)** | Cuchillo parte el taco verticalmente (**MEGA CRUNCH**) | Crujido explosivo de concha y golpe en madera |
| **`S14.mp4`** | `18.10s – 20.00s` | `1.90s` | `0.35s` | **PANTALLA COMPLETA (1080x1920)** | **Payoff:** Manos elevan mitad con vapor hacia la cámara | Levantamiento apetitoso, goteo de salsa y vapor vivo |

---

## 4. Prompts Exactos Plano por Plano (`S01` a `S14`)

---

### BLOQUE 1 — Doble Hook Sensorial en Split-Screen (`0.00 s – 2.80 s`)

#### Plano `S01` (`0.00 s – 1.50 s`) — Hero Reveal del Taco de Ramen
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_01` (Tabla de Nogal Oscuro)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a complete, gourmet Master Hero Ramen Taco resting on a dark end-grain walnut cutting board. The taco shell is made of golden-brown crispy fried ramen noodles formed into a curved taco shell. It is generously filled with glistening glazed savory minced beef, crisp shredded green cabbage, vibrant red and white pico de gallo, chopped scallions, toasted sesame seeds, and a fine zigzag drizzle of orange spicy sriracha mayo. Delicate wisps of hot steam rising, warm side morning window lighting (4500K), shallow depth of field, 50mm f/2.0 lens, photorealistic editorial food photography, no hands, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  Cinematic slow push-in toward the gourmet ramen taco on the dark walnut board. Delicate curls of aromatic hot steam rise steadily into the warm window light as glossy juices on the beef glisten. Crisp ASMR kitchen audio: faint warm room ambiance and quiet savory sizzle, no music, no voice, no glitches.
  ```

---

#### Plano `S02` (`1.50 s – 2.80 s`) — El Crujido de la Concha de Ramen
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_01` (Tabla de Nogal Oscuro)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle macro close-up of a pair of sleek stainless steel kitchen tongs gently pinching the top golden-brown crispy ridge of the fried ramen noodle taco shell resting on the dark walnut board. The noodle strands show golden caramelized edges and crisp texture. Warm side lighting (4500K), 50mm f/2.0 lens, photorealistic editorial food photography, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The metal tongs press down firmly on the golden ramen noodle shell, producing a decisive ultra-crisp crackle as tiny golden noodle flakes scatter gently onto the dark wood. Crisp ASMR kitchen audio: loud sharp crispy ramen noodle shell crackle and wooden cutting board resonance, no music, no voice, no glitches.
  ```

---

### BLOQUE 2 — Fuego, Salteado y Fideos (`2.80 s – 8.20 s`)

#### Plano `S03` (`2.80 s – 4.10 s`) — Aceite de Sésamo y Cebolla en Sartén
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Sartén de Hierro Fundido)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a hand pouring a thin glossy stream of golden toasted sesame oil from a glass bottle into a hot black cast-iron skillet, with finely diced white onions already hitting the hot shimmering oil. Warm side light (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The diced onions sizzle instantly upon hitting the hot sesame oil, forming active golden bubbles and releasing a fragrant puff of white steam across the cast iron surface. Crisp ASMR kitchen audio: immediate punchy high-heat sizzle as diced onions hit shimmering hot sesame oil in cast iron skillet, no music, no voice, no glitches.
  ```

---

#### Plano `S04` (`4.10 s – 5.50 s`) — Carne Picada de Res a Fuego Vivo
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Sartén de Hierro Fundido)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a hand placing a fresh portion of seasoned ground beef (80/20) directly into the hot black cast-iron skillet next to translucent golden onions. Warm side lighting (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The ground beef hits the roaring hot cast-iron skillet with an explosive sizzle, rendering savory juices and creating a rich caramelized sear with thick wisps of steam. Crisp ASMR kitchen audio: heavy meat thud and aggressive roaring skillet sizzle with aromatic steam release, no music, no voice, no glitches.
  ```

---

#### Plano `S05` (`5.50 s – 6.90 s`) — Glaseado Umami de Soya y Mirin
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Sartén de Hierro Fundido)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a ceramic ramekin tilted above the browned bubbling ground beef in the black skillet, pouring a rich dark glossy mixture of soy sauce, mirin, and grated garlic into the center of the meat. Warm side lighting, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The dark soy glaze cascades onto the hot meat, instantly bubbling into a thick fragrant reduction that coats every beef morsel in glistening umami shine. Crisp ASMR kitchen audio: rich glossy soy sauce splash meeting bubbling hot meat with rapid sizzling reduction, no music, no voice, no glitches.
  ```

---

#### Plano `S06` (`6.90 s – 8.20 s`) — Fideos de Ramen Hirviendo al Dente
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_03` (Olla de Agua Hirviendo)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of long wooden cooking chopsticks lifting a bundle of wavy ramen noodles 5 centimeters out of a stainless steel pot of rolling boiling water. Hot steam billowing, water droplets glistening on noodles, warm side lighting, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The wooden chopsticks smoothly lift the al dente wavy ramen noodles higher from the boiling water, with boiling bubbles rolling below and hot drops splashing back into the pot. Crisp ASMR kitchen audio: deep rolling water boil, soft wet noodle lift and hot water dripping splash, no music, no voice, no glitches.
  ```

---

### BLOQUE 3 — Formación de la Concha y Armado del Taco (`8.20 s – 16.20 s`)

#### Plano `S07` (`8.20 s – 9.60 s`) — Prensado del Disco de Fideos en Sartén
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_02` (Sartén de Hierro Fundido)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of cooked ramen noodles compacted into a round flat tortilla disc sizzling in golden melted butter inside a black skillet. A round stainless steel burger press is poised 1 cm above the noodles, ready to press down. Warm side lighting, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The heavy metal press firmly pushes down on the ramen disc, compressing the noodles into a cohesive flat round cake as golden butter froths vigorously around the perimeter. Crisp ASMR kitchen audio: heavy metallic press flattening sizzling buttered noodles with energetic crackling bubbles, no music, no voice, no glitches.
  ```

---

#### Plano `S08` (`9.60 s – 10.90 s`) — Pliegue de la Concha de Taco (CRUNCH)
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_01` (Tabla de Nogal Oscuro)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a golden crispy fried ramen noodle disc on a dark walnut board. A stainless steel chef's spatula gently lifts and bends one half upward, folding it into a classic U-shaped taco shell. Golden caramelized crunchy edges, warm side light (4500K), 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The metal spatula crisply folds the warm golden noodle disc in half, locking the curved taco shell shape with a satisfying crunchy crackle along the toasted exterior. Crisp ASMR kitchen audio: crisp noodle shell fold crackle and metallic spatula scrape, no music, no voice, no glitches.
  ```

---

#### Plano `S09` (`10.90 s – 12.20 s`) — Relleno de Carne Jugosa
- **📎 ADJUNTAR EN `[+]`:** Fotograma inicial de `S08` *(Regla L17: Step-Anchor Chaining)*
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a stainless steel soup spoon laden with glistening, juicy glazed minced beef held directly above the hollow center of the crispy ramen noodle taco shell resting on the dark walnut board. Wisps of steam escaping from the hot meat, warm side lighting, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The spoon drops the steaming, glossy minced beef into the center of the crispy ramen shell, filling the cavity generously as hot juices coat the golden noodles. Crisp ASMR kitchen audio: rich savory meat settling softly into crispy shell with faint escaping sizzle, no music, no voice, no glitches.
  ```

---

#### Plano `S10` (`12.20 s – 13.50 s`) — Cama de Col Verde Crujiente
- **📎 ADJUNTAR EN `[+]`:** Fotograma inicial de `S09` *(Regla L17: Step-Anchor Chaining)*
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of stainless steel culinary tweezers holding a light bundle of finely shredded crisp green cabbage poised right above the steaming beef filling inside the ramen taco on the dark walnut board. Warm side lighting, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The tweezers gently release the crisp shredded cabbage, creating a delicate airy green layer over the hot dark beef. Crisp ASMR kitchen audio: light delicate rustle of crisp shredded cabbage landing on hot savory meat, no music, no voice, no glitches.
  ```

---

#### Plano `S11` (`13.50 s – 14.80 s`) — Pico de Gallo Fresco y Brillante
- **📎 ADJUNTAR EN `[+]`:** Fotograma inicial de `S10` *(Regla L17: Step-Anchor Chaining)*
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a silver spoon tilted above the ramen taco, spooning vibrant red diced tomatoes, white onions, and green cilantro (fresh pico de gallo) right over the shredded cabbage layer. Warm side window lighting, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The spoon deposits the juicy diced pico de gallo evenly over the taco, with tiny glistening drops of lime juice splashing onto the vibrant colors. Crisp ASMR kitchen audio: wet juicy vegetable tap and fresh citrus liquid drip, no music, no voice, no glitches.
  ```

---

#### Plano `S12` (`14.80 s – 16.20 s`) — Zigzag de Salsa Spicy Sriracha
- **📎 ADJUNTAR EN `[+]`:** Fotograma inicial de `S11` *(Regla L17: Step-Anchor Chaining)*
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of a clear plastic squeeze bottle nozzle angled above the fully assembled ramen taco on the dark walnut board, with the tip releasing a glossy orange stream of creamy spicy sriracha mayo. Warm side lighting, 50mm f/2.0 lens, photorealistic, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The squeeze bottle executes a swift, satisfying zigzag motion across the top of the ramen taco, laying down smooth glossy ribbons of orange spicy mayo, while white sesame seeds sprinkle over the top. Crisp ASMR kitchen audio: smooth velvety sauce squeeze and faint sesame seeds sprinkling sound, no music, no voice, no glitches.
  ```

---

### BLOQUE 4 — Clímax y Payoff a PANTALLA COMPLETA (`16.20 s – 20.00 s`)

> **>>> TRANSICIÓN A PANTALLA COMPLETA EN 16.20 s <<<**  
> En este segundo exacto concluye la caricatura animada en la ventana superior. La ventana de arriba y la franja divisoria se retiran por completo, expandiendo los planos finales a **1080 x 1920 px (Fullscreen 9:16)** para la máxima recompensa visual.

---

#### Plano `S13` (`16.20 s – 18.10 s`) — Corte Transversal Crujiente (CRUNCH) — FULLSCREEN
- **📎 ADJUNTAR EN `[+]`:** `ANCHOR_01` (Tabla de Nogal Oscuro)
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up of the complete Master Hero Ramen Taco resting on the dark end-grain walnut cutting board. A heavy Damascus steel chef's knife is poised 2 centimeters vertically above the exact center of the taco, ready to slice straight down through the crispy ramen shell and juicy filling. Warm side morning light (4500K), shallow depth of field, 50mm f/2.0 lens, photorealistic editorial food photography, no faces, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Fast, Image-to-Video, 4s)`:**
  ```text
  The chef's knife cuts straight down through the ramen taco in one decisive vertical chop, cleaving cleanly through the crunchy noodle shell to strike the wooden board firmly, revealing the steaming juicy interior layers. Crisp ASMR kitchen audio: explosive loud crispy ramen noodle shell crunch followed by a solid wooden cutting board thud, no music, no voice, no glitches.
  ```

---

#### Plano `S14` (`18.10 s – 20.00 s`) — Hero Payoff: Bocado Supremo hacia Cámara — FULLSCREEN
- **📎 ADJUNTAR EN `[+]`:** Fotograma final de `S13` *(Regla L17: Step-Anchor Chaining)*
- **`[IMG] Prompt (Nano Banana Pro, 9:16)`:**
  ```text
  Vertical 9:16, eye-level macro close-up of two hands holding one freshly sliced half of the crispy ramen taco on the dark walnut board, turning the cross-section to face the camera. The interior reveals glistening savory beef, crunchy green cabbage, diced red tomatoes, and molten sauce, with thick curls of hot steam rising into the warm window light. 50mm f/1.8 lens, shallow depth of field, photorealistic culinary masterpiece, no faces, no text.
  ```
- **`[VID] Prompt (Veo 3.1 Quality, Image-to-Video, 4s)`:**
  ```text
  The hands slowly move the steaming half of the ramen taco closer toward the camera lens, showcasing the glistening beef juices, crunchy noodle shell edges, and escaping ribbons of warm fragrant steam. Crisp ASMR kitchen audio: quiet mouthwatering lift, soft juicy drip, and warm ambient room presence, no music, no voice, no glitches.
  ```

---

## 5. Empaquetado SEO Bilingüe

**Título Optimizado para Alto CTR (YouTube Shorts / Reels / TikTok):**
`¡Recreé los Tacos de Ramen de Escandalosos! 🍜🌮 #escandalosos #webarebears #ramentaco #recetasvirales`

---

**Descripción Optimizada (Español + Inglés) con Gramajes Exactos:**

```text
¡Recreé el icónico Taco de Ramen de Escandalosos (We Bare Bears)! 🍜🌮
Pardo, Panda y Polar esperaron 4 horas en la fila por un solo taco... ¡así que hoy lo hicimos realidad con concha de ramen ultra crujiente, carne salteada al wok y pico de gallo fresco!

Ingredientes (para 2 tacos):
- Fideos ramen instantáneos: 2 paquetes (170 g)
- Huevo (para ligar la concha): 1 unidad (50 g)
- Mantequilla sin sal: 25 g
- Aceite de sésamo tostado: 15 ml
- Carne picada de res (80/20): 250 g
- Cebolla blanca en cubitos: 60 g
- Ajo rallado: 2 dientes (10 g)
- Salsa de soya oscura: 20 ml
- Mirin o vino de arroz: 15 ml
- Col verde finamente rallada: 60 g
- Tomate rojo picado en cubos: 80 g
- Cilantro fresco picado: 10 g
- Zumo de lima fresca: 15 ml
- Mayonesa spicy sriracha: 30 g
- Semillas de sésamo tostadas: 5 g

Paso a paso:
1. Cocina los fideos ramen en agua hirviendo durante 2.5 minutos. Escurre bien y mezcla con el huevo batido.
2. En sartén con mantequilla, aplasta los fideos en un disco plano con una prensa y dora por ambos lados hasta que esté crujiente.
3. Dobla el disco caliente sobre una rejilla para fijar la forma de concha de taco.
4. En sartén caliente con aceite de sésamo, dora la cebolla y saltea la carne picada con soya, mirin y ajo hasta glasear.
5. Rellena la concha con la carne caliente, la col crujiente, el pico de gallo fresco y termina con zigzag de mayonesa spicy y sésamo.

---

I recreated the iconic Ramen Taco from We Bare Bears! 🍜🌮
Grizz, Panda, and Ice Bear waited 4 hours in line for just one taco... so today we brought it to life with an ultra-crisp ramen shell, savory wok-seared beef, and fresh toppings!

Ingredients (2 tacos):
- Instant ramen noodles: 2 packs (170g)
- Egg (to bind the shell): 1 large (50g)
- Unsalted butter: 25g
- Toasted sesame oil: 15ml
- Ground beef (80/20): 250g
- Diced white onion: 60g
- Grated garlic: 2 cloves (10g)
- Dark soy sauce: 20ml
- Mirin: 15ml
- Finely shredded green cabbage: 60g
- Diced ripe tomatoes: 80g
- Fresh chopped cilantro: 10g
- Fresh lime juice: 15ml
- Spicy sriracha mayo: 30g
- Toasted sesame seeds: 5g
```
