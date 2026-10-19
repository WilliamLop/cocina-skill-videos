# Referencia Técnica: Formato 1 — Cocina POV Editorial ASMR

- **Inspiración editorial:** `@alenakhmil` (`R020`–`R022`), `@namcook` (`R017`–`R019`), `@moribyan`.
- **Pilotos de referencia comprobados:** [`P002` (Pollo Cremoso Toscano)](file:///Users/fenbsru/Documents/ChatGPT/social%20automatization/projects/P002_pollo_cremoso_toscano/) y [`P003` (Pasta Cremosa con Camarones al Ajillo)](file:///Users/fenbsru/Documents/ChatGPT/social%20automatization/projects/P003_pasta_camarones_ajillo/).
- **Lienzo:** `1080x1920 px` (Vertical 9:16 Pantalla Completa).
- **Duración estándar:** `18.0 a 22.0 segundos` (`15 a 18 planos` · promedio `1.1 a 1.3 s/plano`).

---

## 1. Concepto y Promesa Editorial

Una experiencia sensorial inmersiva, hiperrealista y de alta gastronomía casera (*comfort food gourmet*). 
- **La comida es la única protagonista:** Se prescinde de presentadores en pantalla, caras y voz en off explicativa.
- **Narrativa puramente visual y táctil:** Manos expertas ejecutan acciones precisas (masaje de especias, sellado de proteínas, vertido de salsas, rallado de queso, enrollado de pasta).
- **Ritmo hipnótico:** El tempo lo dictan el corte crujiente, el chisporroteo del fuego y el sonido de los fluidos, respaldados por una base musical instrumental suave y elegante.

---

## 2. Especificaciones Ópticas y Dirección de Arte

| Parámetro | Valor Canónico | Justificación Técnica |
|---|---|---|
| **Lienzo** | `1080x1920 px` (9:16) | Cobertura total de la pantalla vertical en dispositivos móviles. |
| **Óptica simulada** | `50mm f/2.0` (o `f/1.8` en payoff) | Profundidad de campo muy estrecha (*shallow DOF*) con *bokeh* suave en el fondo para centrar la mirada en la textura del alimento. |
| **Temperatura de color** | `4500K` (Luz natural cálida) | Evita los tonos fríos y clínicos; resalta el dorado de la mantequilla, el rojo de las especias y la calidez de la madera. |
| **Fuente de luz** | Ventana lateral izquierda | Genera sombras suaves y orgánicas hacia la derecha, esculpiendo el volumen tridimensional de la comida. |
| **Encuadres clave** | Macro cenital 60° y Frontal 45° | Ángulos cómodos y naturales desde la perspectiva de quien cocina. |
| **Superficie de trabajo** | Tabla de nogal oscuro sobre piedra caliza | Contraste cromático premium con proteínas, quesos y vegetales verdes. |

---

## 3. Estructura de Retención y Pacing Segundo a Segundo (18–22s)

| Bloque | Rango de Tiempo | Duración | Función Dramática | Ejemplo Visual en P003 |
|---|---|---|---|---|
| **Bloque 1: Doble Hook** | `0.00 s – 2.00 s` | `2.0 s` | Impacto sensorial instantáneo; muestra el alimento terminado antes de retroceder al inicio. | Caída pesada de camarones frescos en la tabla + lluvia de pimentón rojo y sal marina. |
| **Bloque 2: Preparación y Físicas** | `2.00 s – 5.00 s` | `3.0 s` | Físicas táctiles: masaje, corte contundente y desprendimiento. | Masaje con aceite de oliva brillante + golpe seco de cuchillo aplastando ajo (`CRACK`). |
| **Bloque 3: Cocción y Chispazo** | `5.00 s – 11.50 s` | `6.5 s` | Transformación térmica: fuego, grasa, humo y color. | Cubo de mantequilla fundiéndose en sartén de acero inox + sellado coral de camarones (`SIZZLE`) + corte de limón y desglasado. |
| **Bloque 4: Fusión y Textura** | `11.50 s – 16.50 s` | `5.0 s` | Espesamiento y emulsión cremosa. | Vertido en espiral de nata espesa + lluvia de Parmesano fundiéndose + caída de pasta fettuccine al dente. |
| **Bloque 5: Payoff Gourmet** | `16.50 s – 21.00 s` | `4.5 s` | La gran recompensa visual (*Hero Twirl* / Bocado). | Emplatado en nido en cuenco artesanal de cerámica + tenedor levantando bocado humeante hacia la lente con vapor vivo. |

---

## 4. Ingeniería de Sonido (ASMR Puro + Cama Musical)

El diseño sonoro es responsable de al menos el 50% del éxito en el Formato 1.

```
Pista 1: Audio Foley Nativo de Veo 3.1
  [S01 wet thud] ── [S02 sprinkle] ── [S04 crack] ── [S06 SIZZLE] ── [S11 pour] ── [S18 steam]
  Nivelación obligatoria: -10 dBFS a -12 dBFS pico por clip

Pista 2: Cama Musical Suave (Lo-Fi Beats / Neo-Soul / Chill Jazz)
  Volumen base: 0.32 - 0.36
  Muesca de EQ paramétrico (Notch): Frecuencia 2600 Hz, Ganancia -3.5 dB, Q 1.2
  (Abre espacio espectral para que el crujido del pan y la sartén brillen sin ensuciar la música)
```

### Parámetros de Mezcla y Masterización:
1. **Nivelación por clip:** Cada clip en `assets_flow/` se procesa previamente con el script `scripts/process_clips.py` para fijar picos máximos a `-10 dBFS`.
2. **Cadena de efectos en la música (HyperFrames Web Audio FX):**
   ```json
   {
     "version": 1,
     "nodes": [
       {
         "type": "peaking",
         "id": "n1",
         "label": "Foley Transient Pocket",
         "params": { "frequency": 2600, "gain": -3.5, "q": 1.2 }
       }
     ]
   }
   ```
3. **Master de Salida:** `-14.0 LUFS` integrado con un limitador a `-1.0 dBFS`.

---

## 5. Las 3 Anclas de Escenario Recomendadas para Formato 1

Para mantener consistencia de iluminación y materiales en las 5 fases:

1. **`ANCHOR_01` (Tabla de Nogal — Estación de Corte y Preparación):**
   ```text
   Vertical 9:16, 45-degree high-angle POV shot of a warm rustic kitchen workstation. A thick dark end-grain walnut wooden cutting board resting on a matte warm-grey limestone countertop. Soft natural morning daylight coming from a window on the left (4500K), subtle warm shadows, shallow depth of field, 50mm f/2.0 lens, photorealistic editorial food photography, empty center ready for ingredients, no hands, no text.
   ```
2. **`ANCHOR_02` (Sartén de Acero Inoxidable / Hierro — Estación de Fuego):**
   ```text
   Vertical 9:16, 45-degree high-angle close-up shot of a heavy 28cm brushed stainless steel chef skillet with copper-core rim sitting on a sleek black induction cooktop. Warm natural side lighting from the left (4500K), realistic metallic reflections, shallow depth of field, 50mm f/2.0 lens, photorealistic, empty pan, no hands, no text.
   ```
3. **`ANCHOR_03` (Plato Cerámico Artesanal — Estación de Emplatado):**
   ```text
   Vertical 9:16, 45-degree high-angle shot of a handcrafted matte cream stoneware pasta bowl resting on a dark walnut wooden table. Soft warm side window light from the left, linen napkin edge in the blurred background, 50mm f/2.0 lens, photorealistic editorial food photography, empty bowl, no hands, no text.
   ```

---

## 6. Lista de Verificación de Entrega para Formato 1

- [ ] Todos los planos son 100% video `.mp4` (cero imágenes fijas o zooms simulados).
- [ ] El Hook arranca con un impacto fuerte en los primeros 1.5 segundos.
- [ ] Se utilizó `ANCHOR_01`, `ANCHOR_02` o `ANCHOR_03` en el botón `[+]` de cada toma de Google Flow.
- [ ] Los clips crudos fueron respaldados en `assets_flow/originals_raw/`.
- [ ] Los picos de audio de cada clip están nivelados a `-10 dBFS`.
- [ ] Se configuró `data-media-start` en `assemble.py` (0.25s–0.45s) para eliminar la inercia del arranque de Veo.
- [ ] Validación `npx hyperframes check` arroja 0 errores y 0 advertencias.
- [ ] Render final validado a `1080x1920`, `30 fps` constante y pista estéreo limpia.
