---
name: cocina-audiovisual-flow
description: "Diseño, generación, ensamblaje y packaging de episodios de cocina fotorrealista vertical (9:16) en Google Flow (Nano Banana Pro + Veo 3.1) y HyperFrames. Domina la Matriz 2x2: Formato 1 (POV Editorial ASMR, 18-30s) y Formato 2 (Recreación de Caricaturas en Split-Screen con expansión fullscreen, 18-25s), combinables con Estilo A (100% Video .mp4) o Estilo B (Híbrido: Imágenes Consecutivas Jump-Cuts + Clips de Video .mp4 con librería Foley). Aplica el protocolo de continuidad acumulativa (ANCHOR vacío al iniciar estación y Regla L17 Step-Anchor Chaining adjuntando el plano anterior S(N-1) cuando el plato va a mitad), normalización foley a -10 dB y Ficha de Publicación completa."
---

# Cocina Audiovisual Flow (`cocina-audiovisual-flow`) — v2.0

Manual maestro y especificación operativa en equipo para la producción, edición en HyperFrames y packaging de episodios de cocina fotorrealista de alto impacto visual y sonoro (YouTube Shorts, Instagram Reels y TikTok).

---

## 1. La Matriz 2×2: Formatos Editoriales × Estilos de Fabricación

Todo episodio debe definir desde el inicio qué combinación de la **Matriz 2×2** utilizará:

```
                  │ ESTILO DE FABRICACIÓN A          │ ESTILO DE FABRICACIÓN B
                  │ 100% Clips de Video (.mp4)       │ Híbrido Percusivo: Imágenes Consecutivas
                  │ (Fluidez Continua)               │ (Jump-Cuts 0.28s–0.40s) + Clips de Video (.mp4)
──────────────────┼──────────────────────────────────┼────────────────────────────────────────────────
FORMATO 1         │ Combinación 1A:                  │ Combinación 1B:
Receta Full 9:16  │ POV ASMR 100% Video              │ POV ASMR con Jump-Cuts en tabla + Video en fuego
(1080x1920)       │ Todos los planos son .mp4 con    │ Secuencias de 2-3 imágenes consecutivas (.png)
                  │ vapor y movimiento continuo      │ para picados/cortes rápidos con SFX CLACK +
                  │ (ej. Pasta Camarones, Rigatoni). │ videos .mp4 en sartén, salsas y payoff (ej. Pollo Toscano).
──────────────────┼──────────────────────────────────┼────────────────────────────────────────────────
FORMATO 2         │ Combinación 2A:                  │ Combinación 2B:
Split-Screen      │ Caricatura + 100% Video          │ Caricatura + Jump-Cuts + Video
Caricaturas       │ Caricatura arriba + todos los    │ Caricatura arriba + imágenes consecutivas rápidas
(35%/65% -> 100%) │ planos de abajo en .mp4 + cierre │ cuando el dibujo pica/apila + videos .mp4 en
                  │ Fullscreen (ej. Elmer, Osos).    │ fuego, salsas y Payoff Fullscreen.
```

### ¿Cuándo elegir Estilo A vs. Estilo B?
- **Estilo A (`100% Video .mp4`):** Ideal cuando toda la receta consiste en acciones fluidas (emulsiones, vertidos, salteados, deshebrado, estiramiento de queso).
- **Estilo B (`Híbrido Imágenes Consecutivas + Clips de Video`):** Ideal cuando la receta tiene pasos de picado rápido o transformación geométrica en tabla (ej. *pechuga entera → en tiras → en dados*; *ajo entero → aplastado → picado*; *tomates enteros → partidos*; *capas rápidas de un sándwich*).
  - **Ventaja 1:** Evita que la IA deforme los dedos al intentar picar rápido en video.
  - **Ventaja 2:** Crea el ritmo percusivo adictivo de `0.28 s – 0.35 s` con sonidos reales de `assets/sfx/` (`knife_chop_wood.wav`, `knife_slice.wav`, `bench_scraper.wav`).
  - **Ventaja 3:** Ahorra entre 35% y 45% de créditos de generación de video, reservando Veo 3.1 para los planos donde hay fuego, líquidos, vapor y el bocado final.

---

## 2. Las 5 Reglas de Oro Innegociables

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       LAS 5 REGLAS DE ORO CANÓNICAS                         │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. PROTOCOLO DE CONTINUIDAD EN 2 NIVELES (ANCHOR vs. PLANO ANTERIOR L17):   │
│    - 🟢 INICIO DE ESTACIÓN (Superficie limpia): Adjuntar en [+] el          │
│      ANCHOR_01 / 02 / 03 vacío cuando se inaugura la tabla, sartén o plato. │
│    - 🔗 PLATO EN PROGRESO (Mitad de receta, armado o Jump-Cuts): Cuando el  │
│      plato ya lleva ingredientes en la tabla, sartén o cuenco, NUNCA        │
│      adjuntar el Anchor vacío (porque la IA rehace los ingredientes y       │
│      presenta otra comida). Adjuntar en [+] la IMAGEN O FRAME DEL PLANO     │
│      ANTERIOR S(N-1) para conservar 100% idéntica la comida en curso.       │
│                                                                             │
│ 2. CERO FOTOS CONGELADAS LARGAS (ESTILO A o ESTILO B):                      │
│    O se usa 100% video .mp4 (Estilo A), o se usan Jump-Cuts percusivos      │
│    de imágenes consecutivas (0.28s–0.40s encadenadas con S(N-1) + SFX)      │
│    combinadas con clips de video .mp4 en fuego, salsas y payoff (Estilo B). │
│                                                                             │
│ 3. REGLA DEL ESTADO INICIAL Y MASTER HERO:                                  │
│    En cortes en video, el cuchillo empieza suspendido 2 cm arriba del       │
│    alimento entero. En vertidos, la botella empieza inclinada con la        │
│    primera gota asomando. El Master Hero mantiene las mismas capas siempre. │
│                                                                             │
│ 4. INGENIERÍA DE AUDIO FOLEY A -10 dB Y BALANCE DINÁMICO:                   │
│    Todo clip de Veo se respalda en originals_raw/ y se nivela a -10 dBFS    │
│    pico con `scripts/process_clips.py` (`aac_at` en macOS). En Formato 2,   │
│    el foley va a 0.28 durante el diálogo del cartoon y sube a 1.00 al       │
│    pasar a Pantalla Completa.                                               │
│                                                                             │
│ 5. PACKAGING Y FICHA DE PUBLICACIÓN OBLIGATORIA:                            │
│    Ningún episodio termina sin su `FICHA_PUBLICACION.md` (3 títulos de      │
│    alto CTR, receta bilingüe en gramos, comentario fijado y frame de        │
│    portada) y su registro en `episodes/`.                                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Matriz Histórica de las 19 Lecciones Canónicas (L01 – L19)

| Código | Área | Qué pasó en producción | Causa Raíz | Regla Canónica Incorporada |
|---|---|---|---|---|
| **L01** | Editorial | Imágenes fijas largas sin ritmo parecen diapositivas. | Uso de fotos sueltas sin percusión ni movimiento. | **Estilo A (100% `.mp4`) o Estilo B (Jump-cuts `0.28s–0.40s` con SFX + `.mp4`).** |
| **L02** | Editorial | Pérdida de retención al arrancar picando desde cero. | Falta de recompensa visual en los segundos 0–2. | **Doble Hook Obligatorio:** Mostrar el plato terminado (`Hero Reveal`) + acción táctil (`Dip` / `Corte` / `Cheese Pull`) en `0.0–2.8 s`. |
| **L03** | Editorial | En Formato 2, el video cortaba en seco al acabar la caricatura. | Falta de clímax de cocina propia. | **Payoff a Pantalla Completa:** Expansión automática a `1080x1920` en el segundo `SPLIT_END`. |
| **L04** | Editorial | Mutación caótica al inventar ingredientes distintos en cada plano. | Descripciones diferentes del plato entre escenas. | **ADN del Master Hero:** Describir exactamente los mismos ingredientes y capas en toda la guía. |
| **L05** | Producción | Encimera mutaba entre mármol blanco y madera rústica. | Generar el primer plano desde texto sin referencia. | **Uso de `ANCHOR_01 / 02 / 03`:** Generar estaciones vacías primero en `Nano Banana Pro (9:16)`. |
| **L06** | Producción | Cuchillo deformaba el ingrediente al pedir *"halfway slicing"*. | La IA dibuja el alimento ya partido y hace un corte extra. | **Regla del Estado Inicial (Corte):** Ingrediente entero y cuchillo suspendido 2 cm arriba antes de bajar. |
| **L07** | Producción | Mano aparecía de la nada o frasco flotaba al verter salsa. | No posicionar el recipiente en el fotograma inicial. | **Regla del Vertido Inicial:** Botella o jarra inclinada en `[IMG]` soltando la primera gota. |
| **L08** | Producción | Operador olvidaba qué adjuntar en guías largas. | Falta de indicador visible en cada escena. | **Recordatorio Inline `📎 ADJUNTAR EN [+]`:** Obligatorio en el encabezado de cada plano. |
| **L09** | Edición | Suspiros o voces fantasma de la IA en clips de Veo. | Audio crudo sin auditar. | **Inspección por Plano:** Silenciar (`data-volume="0.00"`) o limpiar cualquier ruido no culinario. |
| **L10** | Edición | Diferencias de hasta 15 dB entre planos de Veo. | Falta de normalización de picos. | **Nivelación Foley a `-10 dBFS` pico:** Procesar con `scripts/process_clips.py` antes de ensamblar. |
| **L11** | Edición | La música de fondo tapaba el crujido del pan y la sartén. | Choque de frecuencias medias-altas. | **Muesca de EQ (`EQ dip`):** Atenuar `-3.5 dB` en `2600 Hz` (`Q: 1.2`) en la pista musical. |
| **L12** | Edición | Inercia estática de `0.2s–0.4s` al arrancar clips de Veo. | Arranque lento de la física de IA. | **Calibración de `data-media-start`:** Recortar entre `0.30 s` y `0.35 s` iniciales en `assemble.py`. |
| **L13** | Packaging | Logos de canales de TV en el clip de caricatura. | Descarga cruda sin limpiar. | **Filtro `delogo`:** Limpiar marcas de agua antes de montar `cartoon_top.mp4`. |
| **L14** | Packaging | Bloqueos por canciones comerciales con copyright. | Uso de música comercial en el render. | **Pistas Libres o Audio Nativo de la App:** Exportar con foley limpio o cama libre a `-14 LUFS`. |
| **L15** | Packaging | Pocos "Guardados" en Shorts/Reels. | Descripción sin receta detallada. | **Receta Bilingüe en Gramos:** Incluir ingredientes exactos en gramos/ml en Español e Inglés. |
| **L16** | Packaging | Bajo CTR con títulos descriptivos planos. | Falta de curiosidad o nostalgia. | **Fórmula de Título:** `¡Recreé el [Plato Icónico] de [Caricatura]!` o gancho sensorial directo. |
| **L17** | Producción | **Cuando el plato ya va a mitad, adjuntar un `ANCHOR` vacío hace que la IA rehaga los ingredientes desde cero y presente otra comida distinta.** | Contradicción entre la foto vacía adjunta y el prompt con comida acumulada. | **Encadenamiento de Continuidad (`Step-Anchor Chaining`):** Cuando el plato está en progreso (en tabla, sartén, armado de taco/sándwich, emplatado o secuencia de imágenes consecutivas), **adjuntar en `[+]` la imagen/frame del plano anterior `S(N-1)`** en vez del Anchor vacío. |
| **L18** | Edición | En Formato 2, el foley de cocina a `0.80` tapaba el diálogo cómico de los personajes animados. | Volumen fijo en toda la línea de tiempo. | **Balance Dinámico Split/Full:** Foley inferior a `0.25–0.30` durante el diálogo del cartoon, y subida a `1.00` al expandir a Pantalla Completa en el corte final (`CRUNCH`). |
| **L19** | Producción | En secuencias de picado rápido en video, la IA deforma los dedos o el cuchillo. | Pedir múltiples cortes rápidos dentro de un clip de 4s de Veo. | **Jump-Cuts de Imágenes Consecutivas (Estilo B):** Usar 2–3 imágenes consecutivas de `0.28s–0.35s` encadenadas con `L17` + SFX `knife_chop_wood.wav` de `assets/sfx/`. |

---

## 4. Flujo de Trabajo en 6 Fases (Producción + Packaging + Equipo)

```
[ FASE 1: MATRIZ 2x2 ] ──> [ FASE 2: GUÍA + L17 ] ──> [ FASE 3: GENERACIÓN ] ──> [ FASE 4: AUDIO -10dB ] ──> [ FASE 5: RENDER ] ──> [ FASE 6: PACKAGING + GIT ]
Elegir Formato (1 o 2)     Anclas vacías al inicio    Nano Banana Pro +          process_clips.py +         assemble.py +          FICHA_PUBLICACION.md +
y Estilo (A o B)           + Encadenar S(N-1) [+]     Veo 3.1 / Jump-Cuts        SFX de assets/sfx/         hyperframes delivery   Subida + git push al repo
```

### Fase 1: Selección en la Matriz 2×2 y Escaleta
1. Definir la combinación del episodio:
   - **`1A`:** Formato 1 (Full 9:16 POV ASMR) + Estilo A (100% Video `.mp4`).
   - **`1B`:** Formato 1 (Full 9:16 POV ASMR) + Estilo B (Imágenes Consecutivas `0.30s` + Clips de Video `.mp4`).
   - **`2A`:** Formato 2 (Caricaturas Split-Screen) + Estilo A (100% Video `.mp4`).
   - **`2B`:** Formato 2 (Caricaturas Split-Screen) + Estilo B (Imágenes Consecutivas `0.30s` + Clips de Video `.mp4`).
2. Consultar [FORMATO_1_POV_ASMR.md](./references/FORMATO_1_POV_ASMR.md) o [FORMATO_2_SPLIT_CARICATURAS.md](./references/FORMATO_2_SPLIT_CARICATURAS.md).

### Fase 2: Redacción de la Guía con Protocolo de Continuidad (`ANCHOR` vs `L17 S(N-1)`)
1. Usar la plantilla [GUIA_GENERACION_TEMPLATE.md](./templates/GUIA_GENERACION_TEMPLATE.md) y las fórmulas de [PROMPT_PATTERNS.md](./references/PROMPT_PATTERNS.md).
2. En cada plano, especificar con precisión quirúrgica el campo **`📎 ADJUNTAR EN [+]`**:
   - Si la estación empieza limpia → **`🟢 ANCHOR_01 / 02 / 03` (Estación vacía)**.
   - Si el plato ya tiene ingredientes de la toma previa → **`🔗 Fotograma/Imagen de S(N-1)` (Regla L17: conserva la comida en curso sin rehacerla)**.
   - Si es una secuencia de *Jump-Cuts* de imágenes consecutivas (Estilo B) → **`🔗 Imagen de S(N-1)`** + indicar el archivo de sonido de `assets/sfx/` (ej. `knife_chop_wood.wav`).

### Fase 3: Generación en Google Flow y Recepción de Activos
1.Guardar los activos descargados en `projects/<nombre_proyecto>/assets_flow/`:
   - Videos: `S01.mp4`, `S04.mp4`, `S05.mp4`...
   - Imágenes consecutivas (si se usa Estilo B): `S02.png`, `S03.png`...
2. Ejecutar el procesador de clips:
   ```bash
   python3 scripts/process_clips.py --project projects/<nombre_proyecto>
   ```
   *(Crea backup inmutable en `originals_raw/` y nivela todos los `.mp4` a `-10.0 dBFS` usando aceleración por hardware `aac_at` en macOS).*

### Fase 4: Ensamblaje Híbrido o Puro en HyperFrames
1. Configurar `assemble.py` a partir de [ASSEMBLE_TEMPLATE.py](./templates/ASSEMBLE_TEMPLATE.py).
   - El script detecta automáticamente tanto `.mp4` como `.png/.jpg`, y en los planos de imagen inyecta automáticamente el efecto Foley de `assets/sfx/` (`knife_chop_wood.wav`, `knife_slice.wav`, `bench_scraper.wav`, `spice_sprinkle.wav`).
2. Generar `index.html` y verificar:
   ```bash
   python3 projects/<nombre_proyecto>/assemble.py
   npx hyperframes check projects/<nombre_proyecto>
   ```
   **Criterio:** `0 errors, 0 warnings`.

### Fase 5: Render Master de Entrega
```bash
npx hyperframes render projects/<nombre_proyecto> --quality delivery --output projects/<nombre_proyecto>/renders/<nombre_proyecto>_final.mp4
```

### Fase 6: Packaging del Canal, Subida y Sincronización Git en Equipo
1. Generar la ficha de subida usando [FICHA_PUBLICACION_TEMPLATE.md](./templates/FICHA_PUBLICACION_TEMPLATE.md) siguiendo las reglas de [PACKAGING_Y_PUBLICACION.md](./references/PACKAGING_Y_PUBLICACION.md).
2. La persona encargada del canal sube el `.mp4` desde su PC copiando el Título, Descripción bilingüe en gramos, Primer Comentario Fijado y eligiendo el segundo exacto de Portada (*Thumbnail*).
3. **Sincronización con el Equipo en GitHub:**
   - Copiar la carpeta ligera del episodio (solo `GUIA_GENERACION.md`, `assemble.py` y `FICHA_PUBLICACION.md`, **sin archivos `.mp4`**) dentro de `episodes/<codigo_episodio>/`.
   - Actualizar `episodes/README.md` y hacer `git add . && git commit -m "..." && git push origin main`.

---

## 5. Recursos de la Skill

- **[FORMATO_1_POV_ASMR.md](./references/FORMATO_1_POV_ASMR.md):** Especificación de Formato 1 (Estilo A y Estilo B).
- **[FORMATO_2_SPLIT_CARICATURAS.md](./references/FORMATO_2_SPLIT_CARICATURAS.md):** Especificación de Formato 2 Split-Screen (Estilo A y Estilo B).
- **[PROMPT_PATTERNS.md](./references/PROMPT_PATTERNS.md):** Fórmulas Nano Banana Pro, Veo 3.1, Regla `L17` (*Step-Anchor Chaining*) y Patrón G (*Jump-Cuts*).
- **[PACKAGING_Y_PUBLICACION.md](./references/PACKAGING_Y_PUBLICACION.md):** Manual de subida, títulos A/B, miniatura, comentario fijado y bitácora del encargado del canal.
- **[GUIA_GENERACION_TEMPLATE.md](./templates/GUIA_GENERACION_TEMPLATE.md):** Plantilla maestra de guías con soporte 2×2 y `L17`.
- **[ASSEMBLE_TEMPLATE.py](./templates/ASSEMBLE_TEMPLATE.py):** Ensamblador universal HyperFrames (Full/Split + Video/Imagen con SFX).
- **[FICHA_PUBLICACION_TEMPLATE.md](./templates/FICHA_PUBLICACION_TEMPLATE.md):** Plantilla lista para copiar y pegar al subir a YouTube/TikTok/Reels.
- **[assets/sfx/](./assets/sfx/):** Librería oficial de 8 efectos Foley percusivos en `.wav` para imágenes consecutivas.
- **[episodes/](./episodes/):** Biblioteca viva de episodios producidos por el equipo.
