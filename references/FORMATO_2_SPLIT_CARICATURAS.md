# Referencia Técnica: Formato 2 — Recreaciones de Caricaturas en Split-Screen

- **Inspiración editorial:** `@culturaglotona` (`R024`–`R028`), `@cookingWITHfred` (`R029`).
- **Pilotos de referencia comprobados:** [`P004` (Sándwich Elmer Gruñón)](file:///Users/fenbsru/Documents/ChatGPT/social%20automatization/projects/P004_elmer_sandwich_queso/), [`P005` (Chili Dog Knuckles Pirata)](file:///Users/fenbsru/Documents/ChatGPT/social%20automatization/projects/P005_sonic_chilidog_guacamole/) y [`P006` (Poor Boy Gigante Scooby-Doo)](file:///Users/fenbsru/Documents/ChatGPT/social%20automatization/projects/P006_poorboy_mega_sandwich/).
- **Lienzo base:** `1080x1920 px` (Vertical 9:16).
- **Duración estándar:** `18.0 a 25.0 segundos` (`12 a 15 planos de cocina` · promedio `1.4 a 1.6 s/plano`).

---

## 1. Concepto y Promesa Editorial

Traer a la realidad física, con el máximo apetito visual y fotorrealismo gastronómico, los platos disparatados, monumentales e icónicos que marcaron la infancia de millones en series animadas clásicas y contemporáneas (Looney Tunes, Scooby-Doo, Sonic Prime, Bob Esponja, Los Simpson, Steven Universe, Studio Ghibli).

- **El contraste humor/apetito:** El delirio cómico del dibujo animado arriba se contrapone abajo con ingredientes tangibles, técnicas culinarias creíbles y texturas hiperapetitosas.
- **Sincronización espejo:** Cada ingrediente que lanza, corta o añade el personaje animado tiene su reflejo inmediato en la cocina inferior.
- **Payoff a Pantalla Completa:** Al finalizar el fragmento animado, la cocina propia invade el 100% de la pantalla para mostrar el corte transversal jugoso y el vapor caliente.

---

## 2. Geometría de Pantalla Dual y Transición Fullscreen

La composición se diseña en HyperFrames dividida en dos ventanas principales con una barra divisoria estética:

```text
┌────────────────────────────────────────────────────────────────────────┐  y = 0 px
│                                                                        │
│  VENTANA SUPERIOR (CARTOON ANIMADO)                                    │
│  Resolución: 1080 x 612 px (o hasta 1080 x 792 px)                     │  32% a 41% de pantalla
│  Clip 16:9 HD limpio, sin marcas de agua (filtro delogo)               │  z-index: 20
│  Audio original latino con canción o diálogos (volumen 0.90 – 0.95)   │
│                                                                        │
├────────────────────────────────────────────────────────────────────────┤  y = 612 px / 792 px
│  FRANJA DIVISORIA ELEGANTE (Alto: 32 px)                               │
│  Fondo oscuro #090807 + bordes dorados rgba(245, 158, 11, 0.28)        │  z-index: 19
├────────────────────────────────────────────────────────────────────────┤  y = 644 px / 824 px
│                                                                        │
│  VENTANA INFERIOR (COCINA FOTORREALISTA EN GOOGLE FLOW)                │
│  Resolución: 1080 x 1170 px (o 1080 x 1096 px)                         │  59% a 61% de pantalla
│  Videos generados en 9:16 con object-fit: cover (centro en macro)      │  z-index: 1 a N
│  Foley nativo ASMR nivelado a -10 dB (mezclado a 0.75 – 0.82)          │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘  y = 1920 px

>>> TRANSICIÓN CANÓNICA EN EL SEGUNDO DE CORTE (SPLIT_END, ej. 14.21 s):
    Cuando la caricatura concluye en la ventana superior:
    1. La ventana superior y el divisor se retiran.
    2. Los planos finales de cocina (S11, S12...) se renderizan a PANTALLA COMPLETA
       (1080 x 1920 px, y = 0) para el clímax gourmet: separación de mitades y bocado.
```

---

## 3. Estructura de Retención y Pacing Segundo a Segundo (18–25s)

| Bloque | Rango de Tiempo | Duración | Comportamiento Arriba (Cartoon) | Comportamiento Abajo (Cocina) |
|---|---|---|---|---|
| **Bloque 1: Doble Hook** | `0.00 s – 3.50 s` | `3.5 s` | El personaje animado presume, nombra o lanza el plato icónico. | **Hero Reveal** de la recreación terminada sobre nogal + **Macro Paneo** por las capas más atractivas. |
| **Bloque 2: Sincronización Espejo** | `3.50 s – 12.00 s` | `8.5 s` | El personaje agrega ingredientes disparatados o enciende el fuego. | Reflejo inmediato: colocación de panes, cascadas de queso, mantequilla en sartén, salsas espesas (`~1.4 a 1.6 s por plano`). |
| **Bloque 3: Clímax de Corte** | `12.00 s – 14.50 s` | `2.5 s` | El chef de la caricatura o el personaje corta el plato. | Cuchillo de chef largo corta verticalmente el sándwich/plato con un contundente **`CRUNCH`** hasta la madera. |
| **Bloque 4: Payoff a Pantalla Completa** | `14.50 s – Final` | `3.5 a 5.0 s` | *(Caricatura finaliza y se oculta)* | **PANTALLA COMPLETA (1080x1920):** Dos manos separan las mitades mostrando el interior jugoso y humeante; acercamiento final directo a cámara. |

---

## 4. Tratamiento Técnico del Clip Animado Superior

Para garantizar calidad profesional y evitar sanciones de derechos o estética amateur:

1. **Extracción en Máxima Calidad:**
   ```bash
   yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]" --output "assets/cartoon_raw.mp4" "<URL_ORIGEN>"
   ```
2. **Limpieza Obligatoria de Logos de Canales (`delogo`):**
   Si el video fuente contiene marcas de agua en esquinas (ej. Boomerang, Cartoon Network, logos de canales de cable), se aplica el filtro `delogo` de `ffmpeg`:
   ```bash
   ffmpeg -i assets/cartoon_raw.mp4 -vf "delogo=x=920:y=40:w=120:h=60" -c:a copy assets/cartoon_clean.mp4
   ```
3. **Escalado y Recorte a la Ventana Superior:**
   Se formatea exactamente a `1080x792` (o `1080x612`) a 30 fps con audio estéreo:
   ```bash
   ffmpeg -i assets/cartoon_clean.mp4 -ss 00:00:04.500 -t 14.215 -vf "scale=1080:792:force_original_aspect_ratio=increase,crop=1080:792" -r 30 -c:v libx264 -crf 18 -c:a aac -b:a 192k assets/cartoon_top.mp4
   ```

---

## 5. Ingeniería de Sonido para Formato 2

```
Pista Primaria (Líder): Audio de la Caricatura
  - Canción en español latino, diálogos cómicos o efectos clásicos de animación.
  - Nivel de mezcla en HyperFrames: data-volume="0.90" a "0.95".

Pista Secundaria (Refuerzo Táctil): Foley de Cocina en Veo 3.1
  - Crunch al cortar pan, sizzle de mantequilla, splash de salsa.
  - Nivelación en scripts/process_clips.py: picos a -10 dBFS.
  - Nivel de mezcla en HyperFrames: data-volume="0.75" a "0.82"
  - Permite que el espectador "sienta" el peso y la textura sin enmascarar los diálogos cómicos.

Master Integrado:
  - -14.0 LUFS integrado con limitador de picos a -1.0 dBFS.
```

---

## 6. Lista de Verificación de Entrega para Formato 2

- [ ] El clip animado superior está limpio de marcas de agua o logos de TV.
- [ ] La tabla temporal de sincronización alinea cada ingrediente de la caricatura con su réplica en video.
- [ ] Cada plano de cocina fue generado a partir del `ANCHOR_01` correspondiente.
- [ ] Se aplicó la Regla del Master Hero: no se inventan ingredientes nuevos en cada corte.
- [ ] En el segundo exacto `SPLIT_END`, la composición se expande a `1080x1920` (Fullscreen).
- [ ] Los clips crudos están respaldados en `assets_flow/originals_raw/` y nivelados a `-10 dBFS`.
- [ ] `assemble.py` genera el `index.html` sin solapamientos indebidos.
- [ ] Verificación con `npx hyperframes check` arroja 0 errores y 0 advertencias.
- [ ] El título sigue la fórmula de alto CTR: `¡Recreé el [Plato] de [Personaje]!` y contiene la receta en gramos en la descripción.
