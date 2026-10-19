---
name: cocina-audiovisual-flow
description: "Diseño, generación y ensamblaje de episodios de cocina fotorrealista vertical (9:16) en Google Flow (Nano Banana Pro + Veo 3.1) y HyperFrames. Soporta Formato 1 (POV Editorial ASMR, 18-22s) y Formato 2 (Recreación de Caricaturas en Split-Screen con expansión fullscreen, 18-25s). Aplica las 16 reglas canónicas de producción (100% video .mp4, ancla de escenario ANCHOR_01 en [+], estado inicial de cortes/vertidos, y normalización foley a -10 dB)."
---

# Cocina Audiovisual Flow (`cocina-audiovisual-flow`)

Manual maestro y especificación operativa para la producción sistemática de episodios de cocina fotorrealista de alto impacto visual y sonoro, optimizados para YouTube Shorts, Instagram Reels y TikTok.

---

## 1. Activación y Alcance de la Skill

Esta skill se activa automáticamente cuando se requiere:
- **Redactar Guías Maestras de Generación** para Google Flow (`Nano Banana Pro` + `Veo 3.1 Fast/Quality`).
- **Planificar y Estructurar Episodios** en cualquiera de los dos formatos canónicos:
  - **Formato 1: Cocina POV Editorial ASMR** (18 a 22 segundos, full 9:16, foley envolvente, cero rostros).
  - **Formato 2: Recreación de Caricaturas en Split-Screen** (18 a 25 segundos, pantalla dual 35%/65% con expansión a pantalla completa).
- **Inspeccionar y Nivelar Clips** descargados en `assets_flow/` mediante copia de seguridad inmutable y normalización de picos de audio a `-10 dBFS`.
- **Ensamblar Proyectos en HyperFrames** generando `index.html` calibrado con recortes de inercia (`data-media-start`) y validación estricta de 0 errores con `npx hyperframes check`.

---

## 2. Las 4 Reglas de Oro Innegociables

Derivadas de los pilotos reales `P002` a `P006`, estas reglas son de obligado cumplimiento para evitar repeticiones de errores:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       LAS 4 REGLAS DE ORO CANÓNICAS                         │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 100% VIDEO (.mp4), CERO FOTOS FIJAS:                                     │
│    Prohibido usar imágenes estáticas en el render final. Cada plano debe    │
│    tener micro-movimiento, vapor vivo, fluidos físicos y audio nativo.       │
│                                                                             │
│ 2. ANCLA DE ESCENARIO OBLIGATORIA (ANCHOR_01 en [+]):                       │
│    Antes de generar alimentos, se fija la estación de trabajo vacía en       │
│    Nano Banana Pro (9:16) y se adjunta en [+] en cada toma subsiguiente.    │
│                                                                             │
│ 3. REGLA DEL ESTADO INICIAL Y MASTER HERO:                                  │
│    En cortes, el cuchillo se sitúa 2 cm suspendido sobre el alimento antes  │
│    de bajar. En vertidos, la botella se inclina soltando la primera gota.   │
│    En torres o sándwiches, se describe el Master Hero intacto una sola vez. │
│                                                                             │
│ 4. INGENIERÍA DE AUDIO FOLEY A -10 dB:                                      │
│    Todo clip de Veo 3.1 se respalda en originals_raw/ y se nivela a -10 dB  │
│    pico con `ffmpeg -af "volume=..." -c:v copy` sin recodificar video.      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Matriz de las 16 Lecciones de Producción (L01 – L16)

Toda decisión técnica en la skill responde directamente a la matriz histórica de errores y soluciones probadas:

| Código | Área | Error Original Identificado | Causa Raíz | Solución Canónica Incorporada |
|---|---|---|---|---|
| **L01** | Editorial | 8 imágenes fijas con zoom digital (`P002`). | Falta de generación de video en acciones intermedias. | **100% video `.mp4`:** Ningún plano fijo en el render final. |
| **L02** | Editorial | Pérdida de retención al arrancar desde cero (`P002`). | Falta de impacto en los segundos 0–2. | **Doble Hook Obligatorio:** Mostrar el resultado terminado o el corte más crujiente en los primeros 1.5–2.0 s. |
| **L03** | Editorial | Video terminado en seco al terminar la caricatura (`P004`). | Falta de recompensa final. | **Payoff a Pantalla Completa:** Expansión inmediata a `1080x1920` cuando concluye el dibujo animado. |
| **L04** | Editorial | Mutación caótica al apilar un sándwich capa por capa. | La IA reinventa pan, lechuga y cocina en cada toma. | **La Trampa del Apilado:** Se define el Master Hero completo una sola vez y se usa en planos de corte y salsas. |
| **L05** | Producción | Encimera mutaba entre mármol blanco y madera (`P003`). | Prompts generados directamente desde texto. | **Uso Obligatorio de `ANCHOR_01`:** Generar encimera vacía y adjuntarla siempre en `+`. |
| **L06** | Producción | Cuchillo deformaba mantequilla a medio cortar (`P003`). | Solicitar "halfway slicing" en `[IMG]`. | **Regla del Estado Inicial:** Cuchillo suspendido 2 cm encima del ingrediente antes de iniciar el tajo. |
| **L07** | Producción | Mano aparecía de la nada o frasco flotaba al verter salsa. | No posicionar la botella en el frame inicial. | **Regla del Vertido Inicial:** La botella aparece inclinada justo tocando la primera gota. |
| **L08** | Producción | Operador olvidaba adjuntar el anchor en guías largas (`P006`). | Falta de contexto local en cada escena. | **Recordatorio Inline `📎 ADJUNTAR EN [+]`:** Cada plano lleva explícitamente el nombre del Anchor en su encabezado. |
| **L09** | Edición | Suspiros y artefactos extraños de la IA en audio (`P004`). | Audio nativo de Veo sin auditar. | **Inspección de Audio por Plano:** Silenciar o limpiar ruidos no culinarios antes de ensamblar. |
| **L10** | Edición | Diferencias de hasta 15 dB entre planos de Veo. | Falta de normalización de picos. | **Nivelación Foley a `-10 dB` a `-12 dB` pico:** Con `ffmpeg -c:v copy` por lotes. |
| **L11** | Edición | Música de fondo tapaba el crujido del pan y la sartén. | Frecuencias medias-altas competían con el Foley. | **Muesca de EQ (`EQ dip`):** Atenuar `-3.5 dB` en los `2500 Hz – 3200 Hz` en la pista musical. |
| **L12** | Edición | Inercia estática de 0.2s–0.5s en los arranques de Veo. | Arranque lento de la física de IA. | **Calibración de `data-media-start`:** Recortar los fotogramas lentos iniciales en `assemble.py`. |
| **L13** | Packaging | Marcas de agua y logos de canales de TV en cartoons. | Descarga cruda de transmisiones de cable. | **Filtro `delogo` obligatorio:** Limpiar coordenadas antes de montar en HyperFrames. |
| **L14** | Packaging | Bloqueos de copyright por música comercial conocida. | Uso de tracks comerciales en el master. | **Pistas Propias o Librería Nativa:** Camas libres masterizadas a `-14 LUFS` o selección de audio en tendencia al publicar. |
| **L15** | Packaging | Bajas tasas de "Guardar" en Shorts de cocina. | Falta de valor utilitario para el espectador. | **Receta Completa en Descripción:** Ingredientes y cantidades exactas en gramos (ES + EN). |
| **L16** | Packaging | Bajo CTR con títulos genéricos tipo "Haciendo pasta". | Falta de curiosidad y gancho emocional. | **Estructura de Titulación Probada:** `¡Recreé el [Plato Icónico] de [Personaje / Caricatura]!` con hashtags de nicho. |

---

## 4. Flujo de Trabajo en 5 Fases

```
[ FASE 1: DESGLOSE ] ──> [ FASE 2: PROMPTING ] ──> [ FASE 3: RECEPCIÓN ] ──> [ FASE 4: ENSAMBLAJE ] ──> [ FASE 5: MASTER RENDER ]
Escaleta al segundo      Anchor vacía +         Inspección + Backup    assemble.py con          npx hyperframes render
y sincronización         Inline [📎 ADJUNTAR]   Nivelar a -10 dB       data-media-start         + Empaque SEO bilingüe
```

### Fase 1: Desglose y Escaleta Sincronizada
1. Elegir el formato editorial:
   - **Formato 1 (POV ASMR):** Consultar [FORMATO_1_POV_ASMR.md](./references/FORMATO_1_POV_ASMR.md). Duración objetivo: `18 a 22 s` (15 a 18 planos de ~1.1s).
   - **Formato 2 (Split-Screen Caricaturas):** Consultar [FORMATO_2_SPLIT_CARICATURAS.md](./references/FORMATO_2_SPLIT_CARICATURAS.md). Duración objetivo: `18 a 25 s` (12 a 15 planos de ~1.5s).
2. Si es Formato 2:
   - Extraer clip animado con `yt-dlp` a máxima resolución.
   - Limpiar marcas de agua con filtro `delogo` de `ffmpeg`.
   - Establecer el segundo exacto de finalización de la caricatura para programar la transición a pantalla completa.

### Fase 2: Protocolo de Prompts e Imágenes Ancla
1. Utilizar la plantilla [GUIA_GENERACION_TEMPLATE.md](./templates/GUIA_GENERACION_TEMPLATE.md).
2. Generar en `Nano Banana Pro (9:16)` las imágenes ancla vacías del escenario (`ANCHOR_01`, `ANCHOR_02`, `ANCHOR_03`).
3. Aplicar las fórmulas canónicas de [PROMPT_PATTERNS.md](./references/PROMPT_PATTERNS.md) tanto para `[IMG]` (estado inicial) como para `[VID]` (Veo 3.1 con directiva ASMR).
4. **Obligatorio:** Cada plano de la guía debe contener el bloque inline:
   `- 📎 ADJUNTAR EN [+]: ANCHOR_0X (Descripción)`

### Fase 3: Recepción, Backup y Nivelación de Audio
Cuando el operador descargue los videos generados (`S01.mp4`, `S02.mp4`...) en la carpeta `assets_flow/` del proyecto:
1. Ejecutar el script automatizado:
   ```bash
   python3 scripts/process_clips.py --project projects/<nombre_proyecto>
   ```
2. El script realiza automáticamente:
   - Inspección técnica de códec, resolución (`1080x1920`) y framerate (`30 fps`).
   - Copia de respaldo inmutable en `assets_flow/originals_raw/`.
   - Detección de picos máximos con filtro `volumedetect`.
   - Normalización de audio a **`-10.0 dBFS` pico** con `ffmpeg -c:v copy` (sin recodificar video, ultrarrápido).

### Fase 4: Calibración y Ensamblaje en HyperFrames
1. Configurar y ejecutar el ensamblador a partir de [ASSEMBLE_TEMPLATE.py](./templates/ASSEMBLE_TEMPLATE.py):
   ```bash
   python3 projects/<nombre_proyecto>/assemble.py
   ```
2. Calibrar `data-media-start` en cada plano (típicamente `0.25 s` a `0.45 s`) para eliminar el lag o inercia inicial del modelo Veo.
3. Validar la composición con el motor de HyperFrames:
   ```bash
   npx hyperframes check projects/<nombre_proyecto>
   ```
   **Criterio de aprobación:** `0 errors, 0 warnings`.

### Fase 5: Render Master de Entrega y Empaquetado
1. Renderizar en calidad máxima de entrega (*delivery quality*):
   ```bash
   npx hyperframes render projects/<nombre_proyecto> --quality delivery --output projects/<nombre_proyecto>/renders/<nombre_proyecto>_final.mp4
   ```
2. Verificar el archivo final con `ffprobe`:
   - Resolución exacta: `1080x1920` (9:16 vertical).
   - Tasa de fotogramas: `30.0 fps` constante.
   - Pista de audio: Estéreo AAC a `48 kHz`, integrado a `-14 LUFS`.
3. Publicar con el bloque de empaquetado SEO bilingüe generado en la Fase 2 (ingredientes en gramos, inglés y español, y títulos de alto CTR).

---

## 5. Estructura Canónica de un Proyecto

Todo proyecto de producción creado con esta skill debe mantener este árbol de directorios:

```text
projects/<nombre_proyecto>/
├── assets/                          # Medios externos (cartoon_top.mp4, música)
│   └── cartoon_top.mp4              # Clip 16:9 HD limpio (en Formato 2)
├── assets_flow/                     # Videos generados en Google Flow
│   ├── S01.mp4                      # Video procesado con audio nivelado a -10 dB
│   ├── S02.mp4
│   └── originals_raw/               # BACKUP INMUTABLE de descargas crudas
│       ├── S01.mp4
│       └── S02.mp4
├── renders/                         # Renders finales de HyperFrames
│   └── <nombre_proyecto>_final.mp4  # Master final 1080x1920 a 30 fps
├── assemble.py                      # Script de generación de index.html
├── GUIA_GENERACION.md               # Guía con prompts e inline [📎 ADJUNTAR]
├── hyperframes.json                 # Descriptor del proyecto HyperFrames
└── index.html                       # Composición HTML + GSAP renderizable
```

---

## 6. Recursos Relacionados en la Skill

- **[FORMATO_1_POV_ASMR.md](./references/FORMATO_1_POV_ASMR.md):** Especificación completa de Cocina POV Editorial ASMR.
- **[FORMATO_2_SPLIT_CARICATURAS.md](./references/FORMATO_2_SPLIT_CARICATURAS.md):** Especificación de Split-Screen y expansión Fullscreen.
- **[PROMPT_PATTERNS.md](./references/PROMPT_PATTERNS.md):** Fórmulas exactas para Nano Banana Pro y Veo 3.1.
- **[GUIA_GENERACION_TEMPLATE.md](./templates/GUIA_GENERACION_TEMPLATE.md):** Plantilla para redactar guías de producción.
- **[ASSEMBLE_TEMPLATE.py](./templates/ASSEMBLE_TEMPLATE.py):** Script de ensamblaje base para HyperFrames.
- **[process_clips.py](./scripts/process_clips.py):** Script de inspección, backup y nivelación a -10 dB.
