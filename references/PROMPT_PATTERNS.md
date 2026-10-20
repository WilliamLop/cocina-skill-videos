# Fórmulas Canónicas de Prompts: Nano Banana Pro, Veo 3.1 y Continuidad L17

Guía de fórmulas estandarizadas de ingeniería de prompts para Google Flow. Validadas en los pilotos originales y en los episodios de producción del equipo para garantizar fotorrealismo óptico, física creíble de fluidos/vapor, y **100% de continuidad acumulativa** tanto en **Estilo A (100% Video)** como en **Estilo B (Híbrido: Imágenes Consecutivas + Clips de Video)**.

---

## 1. El Árbol de Decisión de Continuidad: ¿Qué adjuntar en `[+]`? (Regla L17)

El error más grave en generación culinaria ocurre cuando el plato ya va a mitad de preparación (ej. el pan ya tiene jamón y queso, la sartén ya tiene carne dorada, o la concha de ramen ya está formada) y el operador adjunta en `[+]` el `ANCHOR` vacío: **la IA ve una superficie vacía y vuelve a rehacer los ingredientes desde cero, presentando una comida distinta en el siguiente clip.**

Para evitarlo al 100%, cada plano sigue esta regla de decisión:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│             ¿QUÉ DEBO ADJUNTAR EN EL BOTÓN [+] DE NANO BANANA PRO?          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ CASO 1: 🟢 INICIO DE ESTACIÓN (Superficie limpia o ingrediente nuevo solo)  │
│   ¿La tabla, la sartén o el cuenco empiezan limpios en este plano?          │
│   👉 ADJUNTAR EN [+]: `ANCHOR_01`, `ANCHOR_02` o `ANCHOR_03` (Vacío).       │
│                                                                             │
│ CASO 2: 🔗 PLATO EN PROGRESO (Mitad de receta, cocción, armado o emplatado) │
│   ¿En este plano vas a añadir un ingrediente, salsa, corte o acción sobre   │
│   la comida que YA estaba en la tabla, sartén o plato en el plano anterior? │
│   👉 ADJUNTAR EN [+]: `Fotograma/Imagen del Plano Anterior S(N-1)` (L17).   │
│      (Ej: Usar S08 para generar S09; usar S09 para generar S10...).         │
│      ¡PROHIBIDO adjuntar el Anchor vacío aquí!                              │
│                                                                             │
│ CASO 3: ⚡ SECUENCIA DE IMÁGENES CONSECUTIVAS (Jump-Cuts de Estilo B)       │
│   ¿Vas a hacer un corte percusivo de 2 o 3 imágenes seguidas de 0.30s       │
│   (ej. Entero -> En tiras -> En dados, o Ajo entero -> Aplastado -> Picado)?│
│   👉 Imagen 1 (`S01`): Adjuntar `ANCHOR_01` (Tabla vacía).                  │
│   👉 Imagen 2 (`S02`): Adjuntar la imagen `S01` en [+].                     │
│   👉 Imagen 3 (`S03`): Adjuntar la imagen `S02` en [+].                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Prompts para Imágenes Ancla de Escenario (`ANCHOR` Vacíos)

Las imágenes ancla se generan **una sola vez al inicio del proyecto** en `Create Image` → `Nano Banana Pro (9:16)` y se usan únicamente cuando se inaugura una estación limpia (Caso 1):

### `ANCHOR_01`: Estación de Trabajo Rústica de Nogal (Tabla Vacía)
```text
Vertical 9:16, 45-degree high-angle POV shot of a warm rustic kitchen workstation. A thick dark end-grain walnut wooden cutting board resting on a matte warm-grey limestone countertop. Soft natural morning daylight coming from a window on the left (4500K), subtle warm shadows falling to the right, softly blurred warm-grey kitchen wall behind. 50mm f/2.0 lens, shallow depth of field, photorealistic editorial food photography. Empty center of the board ready for food, no food, no hands, no people, no text.
```

### `ANCHOR_02`: Estación de Fuego (Sartén o Plancha Vacía)
- **Sartén de Acero Inoxidable:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up shot of a heavy 28cm brushed stainless steel chef skillet with copper-core rim sitting on a sleek black induction cooktop. Warm natural side lighting from the left (4500K), realistic metallic reflections, shallow depth of field, 50mm f/2.0 lens, photorealistic, empty pan, no hands, no food, no text.
  ```
- **Sartén / Plancha de Hierro Fundido Negro:**
  ```text
  Vertical 9:16, 45-degree high-angle close-up shot of a heavy seasoned 28cm black cast-iron skillet sitting on a sleek black stovetop grate. Warm side lighting from the left (4500K), subtle oil sheen on the cast iron surface, shallow depth of field, 50mm f/2.0 lens, photorealistic, empty pan, no hands, no food, no text.
  ```

### `ANCHOR_03`: Estación de Emplatado (Cuenco o Plato Artesanal Vacío)
```text
Vertical 9:16, 45-degree high-angle shot of a handcrafted matte warm-cream ceramic stoneware plate resting on a dark walnut wooden table. Soft warm side window light from the left (4500K), subtle linen napkin in the blurred background, 50mm f/2.0 lens, photorealistic editorial food photography, empty plate, no food, no hands, no text.
```

---

## 3. Fórmulas para el Prompt de Imagen (`[IMG]` — Nano Banana Pro)

### Patrón A: Corte en Video (Regla del Estado Inicial — L06)
> **Principio:** NUNCA pedir el alimento partido a la mitad en la imagen inicial si el corte se hará en video. La imagen muestra el ingrediente **entero**, con el cuchillo suspendido **2 cm por encima**, listo para bajar.

```text
Vertical 9:16, 45-degree high-angle close-up of a whole, uncut [INGREDIENTE O PLATO COMPLETO] resting on a dark end-grain walnut cutting board. One hand holds the side steady while the other hand holds a sharp stainless steel chef's knife poised 2 centimeters in the air directly above the center, ready to slice down. Warm side window light (4500K), 50mm f/2.0 lens, shallow depth of field, photorealistic editorial food photography, no text.
```

### Patrón B: Vertido de Líquidos y Salsas (L07)
> **Principio:** La botella, jarra o cucharón aparece ya inclinado en el aire, con la primera gota asomando en la boquilla.

```text
Vertical 9:16, 45-degree high-angle close-up of a hand holding a [BOTELLA / JARRA / CUCHARÓN] tilted above [SUPERFICIE O ALIMENTO EN PROGRESO], with the very first glossy drop of [SALSA / ACEITE / NATA] forming at the spout ready to pour down. Warm side window lighting (4500K), 50mm f/2.0 lens, photorealistic culinary photography, no text.
```

### Patrón C: Sellado y Sartén Caliente
```text
Vertical 9:16, 45-degree high-angle close-up of [PROTEÍNA / INGREDIENTE] being placed into a hot [SARTÉN DE ACERO / HIERRO FUNDIDO] coated with shimmering extra virgin olive oil and bubbling golden melted butter with fine white foam. Wisps of aromatic steam rising, warm side light (4500K), 50mm f/2.0 lens, photorealistic, no text.
```

### Patrón D: El Master Hero (Torres, Tacos y Sándwiches Complejos — L04)
```text
Vertical 9:16, 45-degree high-angle close-up of a complete gourmet [NOMBRE DEL PLATO HERO] resting on a dark walnut cutting board. [DESCRIPCIÓN EXACTA DE CAPAS DE ABAJO HACIA ARRIBA]. Delicate wisps of hot steam rising, warm side window light (4500K), 50mm f/2.0 lens, photorealistic editorial food photography, no hands, no text.
```

### Patrón E: Clímax de Separación (*Cheese Pull* / Corte Transversal)
```text
Vertical 9:16, 45-degree high-angle close-up of two hands holding the two freshly cut halves of a [SÁNDWICH / TACO / PLATO] pressed gently together on a dark walnut board, with molten glossy [QUESO / RELLENO JUGOSO] beginning to stretch between the two halves. Warm side lighting (4500K), 50mm f/2.0 lens, photorealistic, no text.
```

### Patrón F: Encadenamiento de Continuidad Acumulativa (*Step-Anchor Chaining* — L17)
> **Principio Crítico (L17):** Cuando el plato ya está a mitad de preparación (en la sartén con ingredientes previos, en la tabla armando capas de un taco/sándwich, o en el cuenco añadiendo toppings finales), **adjuntar en `[+]` el fotograma/imagen del plano inmediatamente anterior `S(N-1)`**. En el prompt se pide explícitamente mantener intacta la base de la imagen de referencia y añadir únicamente el nuevo elemento.

```text
Vertical 9:16, 45-degree high-angle close-up keeping the exact same [PLATO / SARTÉN / CONCHA DE TACO CON SUS INGREDIENTES ACTUALES] from the reference image intact on the surface, as [HERRAMIENTA O MANO: ej. a silver spoon / stainless steel tongs / a squeeze bottle] positioned right above adds [NUEVO INGREDIENTE O CAPA: ej. finely shredded green cabbage / heavy cream / freshly grated Parmesan] on top. Warm side window lighting (4500K), 50mm f/2.0 lens, photorealistic editorial food photography, no faces, no text.
```

### Patrón G: Secuencias de Imágenes Consecutivas (*Jump-Cuts Percusivos* — Estilo B, L19)
> **Principio (Estilo B como en `P002_pollo_cremoso_toscano`):** Para transformaciones rápidas en tabla (`0.28 s` a `0.35 s` por imagen, sin generar video), se crean 2 o 3 imágenes consecutivas encadenando la anterior en `[+]` y se sincronizan en `assemble.py` con la librería `assets/sfx/`:

1. **Imagen 1 (`S0X` — Estado Entero, adjuntando `ANCHOR_01` en `[+]`):**
   ```text
   Vertical 9:16, 45-degree high-angle close-up of whole raw [INGREDIENTE: ej. chicken breast / 4 peeled garlic cloves / cherry tomatoes] resting on the center of the dark end-grain walnut cutting board, with a sharp chef's knife blade resting gently on top. Warm side window light (4500K), 50mm f/2.0 lens, photorealistic, no text.
   ```
2. **Imagen 2 (`S0(X+1)` — Transformación 1, adjuntando `S0X` en `[+]` + SFX `knife_chop_wood.wav`):**
   ```text
   Vertical 9:16, 45-degree high-angle close-up keeping the exact same dark walnut cutting board and lighting from the reference image, now showing the exact same [INGREDIENTE] cleanly sliced into [long even strips / crushed flat garlic cloves / clean halves] in the exact same spot on the board. Photorealistic, 50mm f/2.0 lens, no hands, no text.
   ```
3. **Imagen 3 (`S0(X+2)` — Transformación 2, adjuntando `S0(X+1)` en `[+]` + SFX `bench_scraper.wav` o `knife_chop_wood.wav`):**
   ```text
   Vertical 9:16, 45-degree high-angle close-up keeping the exact same dark walnut cutting board and lighting from the reference image, now showing the exact same [INGREDIENTE] cut into [neat bite-sized cubes / finely minced garlic beside a steel bench scraper] in the exact same position. Photorealistic, 50mm f/2.0 lens, no hands, no text.
   ```

#### Catálogo de Efectos Foley en `assets/sfx/` para Imágenes Consecutivas (Estilo B):
| Archivo en `assets/sfx/` | Uso en Jump-Cuts de Imagen (`.png` / `.jpg`) | Duración recomendada |
|---|---|---|
| `knife_chop_wood.wav` | Golpe seco de cuchillo sobre madera (tiras, dados, ajo aplastado) | `0.28 s – 0.35 s` |
| `knife_slice.wav` | Corte húmedo deslizado (pechuga, tomates cherry, limón, carnes) | `0.30 s – 0.40 s` |
| `bench_scraper.wav` | Raspado metálico recogiendo ajo o hierbas picadas en la tabla | `0.30 s – 0.38 s` |
| `spice_sprinkle.wav` | Golpe visual de montaña de queso rallado, especias o hierbas | `0.32 s – 0.40 s` |
| `oil_pour_foam.wav` | Refuerzo sonoro de aceite/mantequilla espumando | `0.50 s – 0.85 s` |
| `pan_sizzle.wav` | Refuerzo de chisporroteo intenso al sellar proteínas | `0.80 s – 1.20 s` |
| `cream_pour_swirl.wav` | Refuerzo de vertido cremoso en sartén o plato | `0.80 s – 1.40 s` |
| `simmer_stir.wav` | Refuerzo de hervor espeso y cuchara removiendo | `0.80 s – 1.50 s` |

---

## 4. Fórmulas para el Prompt de Video (`[VID]` — Veo 3.1)

### Selección del Modelo: Fast vs Quality

| Modelo | Cuándo Utilizarlo | Ejemplo de Planos |
|---|---|---|
| **Veo 3.1 Fast** | Planos cortos (`0.6 s` a `1.3 s`), acciones físicas directas, caídas por gravedad o cortes limpios. | Corte vertical de cuchillo, aplastado de ajo (`CRACK`), caída de especias, prensado en sartén. |
| **Veo 3.1 Quality** | Planos estelares (`1.3 s` a `2.0 s`), físicas de fluidos densos, burbujeo térmico, fusión elástica y payoff. | Estiramiento de queso (*cheese pull*), rotura de burrata/yema, remolino de nata, bocado final con vapor. |

### Anatomía del Prompt en Veo 3.1:
```text
[ACCIÓN FÍSICA CLARA EN TERCERA PERSONA]. [COMPORTAMIENTO DEL ALIMENTO: vapor, derretimiento, fluidos, crujido]. Crisp ASMR kitchen audio: [DESCRIPCIÓN DEL SONIDO EXACTO: crunch, sizzle, chop, pour], no music, no voice, no glitches.
```
