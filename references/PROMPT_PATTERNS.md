# Fórmulas Canónicas de Prompts: Nano Banana Pro y Veo 3.1

Guía de fórmulas estandarizadas de ingeniería de prompts para Google Flow. Validadas a través de los pilotos reales `P002` a `P006` para garantizar fotorrealismo óptico, física creíble de fluidos y vapor, y consistencia total de escenario.

---

## 1. Arquitectura de Generación en Google Flow

Cada plano se compone de una pareja sincronizada:
1. **`[IMG]` Start Frame:** Creado en `Create Image` con `Nano Banana Pro` en proporción `Portrait (9:16)`, adjuntando la imagen ancla del escenario en el botón `[+]`.
2. **`[VID]` Animación + Foley:** Creado en `Image to Video` con `Veo 3.1` (Fast o Quality) a partir del `[IMG]` con duración fija de `4 segundos`.

```
               ┌───────────────────────────────┐
               │    ANCHOR_01 (Escenario)      │
               └──────────────┬────────────────┘
                              │ Adjuntar en [+]
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ 1. [IMG] PROMPT (Nano Banana Pro · 9:16)                    │
│    - Óptica: 50mm f/2.0, luz natural lateral 4500K           │
│    - Estado Inicial: Cuchillo arriba o botella inclinada    │
│    - Resultado: Fotograma inicial estático perfecto         │
└─────────────────────────────┬───────────────────────────────┘
                              │ Seleccionar como Start Frame
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. [VID] PROMPT (Veo 3.1 Fast o Quality · 4s)               │
│    - Acción física concisa (tajo, chisporroteo, vertido)    │
│    - Audio nativo: "Crisp ASMR kitchen audio: [foley]"      │
│    - Negativas: "no music, no voice, no glitches"           │
│    - Resultado: Video .mp4 con sonido foley sincronizado    │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Prompts para Imágenes Ancla de Escenario (`ANCHOR`)

Las imágenes ancla se generan **una sola vez al inicio del proyecto** y se guardan como referencia fija:

### `ANCHOR_01`: Estación de Trabajo Rústica de Nogal (Vista General)
```text
Vertical 9:16, 45-degree high-angle POV shot of a warm rustic kitchen workstation. A thick dark end-grain walnut wooden cutting board resting on a matte warm-grey limestone countertop. Soft natural morning daylight coming from a window on the left (4500K), subtle warm shadows falling to the right, softly blurred warm-grey kitchen wall behind. 50mm f/2.0 lens, shallow depth of field, photorealistic editorial food photography. Empty center of the board ready for food, no food, no hands, no people, no text.
```

### `ANCHOR_02`: Sartén Caliente / Estación de Fuego
- **Sartén de Acero Inoxidable:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up shot of a heavy 28cm brushed stainless steel chef skillet with copper-core rim sitting on a sleek black induction cooktop. Warm natural side lighting from the left (4500K), realistic metallic reflections, shallow depth of field, 50mm f/2.0 lens, photorealistic, empty pan, no hands, no text.
  ```
- **Sartén de Hierro Fundido Negro:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up shot of a heavy seasoned 26cm black cast-iron skillet sitting on a sleek black gas stovetop grate. Warm side lighting from the left (4500K), subtle oil sheen on the cast iron surface, shallow depth of field, 50mm f/2.0 lens, photorealistic, empty pan, no hands, no text.
  ```

### `ANCHOR_03`: Plato Artesanal de Emplatado
```text
Vertical 9:16, 45-degree high-angle shot of a handcrafted matte warm-cream ceramic stoneware plate resting on a dark walnut wooden table. Soft warm side window light from the left (4500K), subtle linen napkin in the blurred background, 50mm f/2.0 lens, photorealistic editorial food photography, empty plate, no food, no hands, no text.
```

---

## 3. Fórmulas para el Prompt de Imagen (`[IMG]` — Nano Banana Pro)

### Patrón A: Corte de Ingredientes (Regla del Estado Inicial)
> **Principio (L06):** NUNCA pedir el alimento partido a la mitad en la imagen inicial. La imagen debe contener el ingrediente **entero**, con el cuchillo suspendido **2 cm por encima**, listo para iniciar el corte descendente.

```text
Vertical 9:16, 45-degree high-angle close-up of a whole, uncut [INGREDIENTE COMPLETO] resting on a dark end-grain walnut cutting board. One hand holds the side of the [INGREDIENTE] steady while the other hand holds a sharp stainless steel chef's knife poised 2 centimeters in the air directly above the center, ready to slice down. Warm side window light (4500K), 50mm f/2.0 lens, shallow depth of field, photorealistic editorial food photography, no text.
```

### Patrón B: Vertido de Líquidos y Salsas
> **Principio (L07):** La botella, jarra o salsera debe aparecer ya inclinada en el aire, con la primera gota asomando o rozando la punta.

```text
Vertical 9:16, 45-degree high-angle close-up of a hand holding a [BOTELLA / JARRA DE CRISTAL] tilted above [SUPERFICIE O ALIMENTO BASE], with the very first glossy drop of [SALSA / ACEITE / NATA] forming at the spout ready to pour down. Warm side window lighting, 50mm f/2.0 lens, photorealistic culinary photography, no text.
```

### Patrón C: Sellado y Sartén Caliente
> **Principio:** Describir la grasa (mantequilla espumosa o aceite brillante) en contacto con la proteína caliente, con vapor sutil elevándose.

```text
Vertical 9:16, 45-degree high-angle close-up of [PROTEÍNA: CAMARONES / FILETE / POLLO] being placed into a hot [SARTÉN DE ACERO / HIERRO FUNDIDO] coated with shimmering extra virgin olive oil and bubbling golden melted butter with fine white foam. Wisps of aromatic steam rising, warm side light (4500K), 50mm f/2.0 lens, photorealistic, no text.
```

### Patrón D: El Master Hero (Torres y Sándwiches Complejos)
> **Principio (L04):** No reinventar los ingredientes. Describir exactamente las mismas capas en todos los planos de la receta.

```text
Vertical 9:16, eye-level front view of a [NOMBRE DEL PLATO HERO] resting on a dark walnut cutting board. [DESCRIPCIÓN MINUCIOSA DE CAPAS: ej. two thick slices of golden toasted artisan brioche bread packed with melted orange cheddar oozing from the edges, folded pink smoked ham, crisp green lettuce, and red tomatoes]. Delicate wisps of hot steam rising, warm side window light (4500K), 50mm f/2.0 lens, photorealistic editorial food photography, no hands, no text.
```

### Patrón E: Clímax de Separación (*Cheese Pull* / Fusión)
```text
Vertical 9:16, 45-degree high-angle close-up of two hands holding the two freshly cut halves of a [SÁNDWICH / PLATO CON QUESO] pressed gently together on a dark walnut board, with molten glossy [TIPO DE QUESO] beginning to stretch between the two halves. Warm side lighting, 50mm f/2.0 lens, photorealistic, no text.
```

---

## 4. Fórmulas para el Prompt de Video (`[VID]` — Veo 3.1)

### Selección del Modelo: Fast vs Quality

| Modelo | Cuándo Utilizarlo | Ejemplo de Planos |
|---|---|---|
| **Veo 3.1 Fast** | Planos cortos (`0.5 s` a `1.2 s`), acciones físicas directas, caídas por gravedad o movimientos rápidos de herramientas. | Corte limpio de cuchillo, aplastado de ajo (`CRACK`), caída de especias en polvo, colocación de panes. |
| **Veo 3.1 Quality** | Planos estelares (`1.2 s` a `2.0 s`), físicas de fluidos densos, burbujeo térmico, fusión elástica y movimiento de cámara lento. | Estiramiento elástico de queso (*cheese pull*), remolino de crema espesa, emulsión de salsa en sartén, enrollado de pasta (*pasta twirl*), paneo macro. |

---

### Anatomía del Prompt en Veo 3.1:

```text
[ACCIÓN FÍSICA CLARA EN TERCERA PERSONA]. 
[COMPORTAMIENTO DEL ALIMENTO: vapor, derretimiento, fluidos, crujido]. 
[MOVIMIENTO DE CÁMARA: static, slow push-in, macro tilt-down]. 
Crisp ASMR kitchen audio: [DESCRIPCIÓN DEL SONIDO EXACTO: crunch, sizzle, chop, pour], no music, no voice, no glitches.
```

---

### Catálogo de Directivas de Audio ASMR Validadas:

| Acción | Directiva Canónica de Audio ASMR |
|---|---|
| **Corte de Pan Tostado** | `Crisp ASMR kitchen audio: loud ultra-crispy toasted bread crust crunch followed by a clean wooden cutting board tap, no music, no voice.` |
| **Corte Húmedo de Cítrico** | `Crisp ASMR kitchen audio: crisp wet citrus slice and dull thud of the wooden board, no music, no voice.` |
| **Aplastado de Ajo** | `Crisp ASMR kitchen audio: one loud sharp resonant garlic crunch and heavy wooden thud, no music, no voice.` |
| **Sellado en Sartén Caliente** | `Crisp ASMR kitchen audio: immediate punchy high-heat pan sizzle as food hits hot foaming butter, no music, no voice.` |
| **Vertido de Líquido Espeso** | `Crisp ASMR kitchen audio: rich velvety liquid pour meeting a warm simmering pan with gentle bubbles, no music, no voice.` |
| **Lluvia de Queso Rallado** | `Crisp ASMR kitchen audio: soft airy snowfall of grated cheese landing on hot bubbling sauce, no music, no voice.` |
| **Estiramiento de Queso (*Cheese Pull*)**| `Crisp ASMR kitchen audio: soft crispy bread crackle and rich gooey melted cheese stretching sound, no music, no voice.` |
| **Enrollado de Pasta con Pinzas**| `Crisp ASMR kitchen audio: rich mouthwatering creamy pasta folding and glossy sauce slosh, no music, no voice.` |
| **Picado Rápido de Hierbas** | `Crisp ASMR kitchen audio: rhythmic sharp knife chops on solid wood followed by a clean metallic blade scrape, no music, no voice.` |

---

## 5. Reglas Negativas Obligatorias

Para blindar las generaciones contra deformaciones típicas de los modelos generativos:
- **En `[IMG]`:** Siempre añadir al final `, no text, no watermark, no logo, no distorted elements`.
- **En planos sin manos:** Añadir explícitamente `, no hands, no people`.
- **En `[VID]`:** Terminar invariablemente con `, no music, no voice, no glitches, no extra fingers, no morphing`.
