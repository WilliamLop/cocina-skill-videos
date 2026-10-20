# Protocolo de Packaging, Pre-Vuelo y Publicación para el Encargado del Canal

Este documento rige la **Fase 6** del flujo de trabajo en `cocina-audiovisual-flow`. Todo video renderizado en HyperFrames debe ir acompañado obligatoriamente de su **`FICHA_PUBLICACION.md`** para que la persona encargada del canal suba el episodio desde su ordenador maximizando el **CTR (Tasa de Clic / No-Swipe)**, la **Retención (>85%)**, los **Guardados (Saves)** y los **Comentarios**.

---

## 1. Las 4 Palancas Algorítmicas en Shorts, Reels y TikTok

| Palanca | Métrica que Dispara | Cómo la optimizamos en el Packaging |
|---|---|---|
| **1. Frame de Portada (*Thumbnail*)** | CTR en el Feed de Shorts y Perfil | Seleccionar en el deslizador de la app el fotograma exacto del **Doble Hook (`0.5s – 1.8s`)** o del **Payoff (`Cheese Pull` / `Dip` / `Corte`)** con máxima saturación cálida y vapor visible. |
| **2. Título con Gancho Emocional** | Retención en los primeros 2 segundos | Aplicar las fórmulas probadas de curiosidad/nostalgia (Formato 2) o hiper-apetito sensorial (Formato 1) en menos de 60 caracteres + 4 hashtags estratégicos. |
| **3. Descripción Bilingüe con Gramajes** | **Tasa de "Guardados" (Saves) y Compartidos** | Incluir la lista exacta de ingredientes en **gramos / ml** y el paso a paso en **Español e Inglés**. Cuando el espectador ve cantidades reales, guarda el video para cocinarlo después. |
| **4. Primer Comentario Fijado (*Pinned*)** | **Debate en Comentarios (Tiempo de sesión)** | Mientras el espectador lee o escribe un comentario, el video de `18–22 s` se reproduce en bucle (*loop*) 2 o 3 veces en el fondo, disparando la retención por encima del **120%**. |

---

## 2. Fórmulas Canónicas de Títulos (A/B)

### Para Formato 1 (Recetas POV Editorial ASMR — 9:16 Completo):
- **Opción A (Directa Sensorial / Bilingüe):**
  `[Nombre del Plato] [Adjetivo Textural: Ultra Cremoso / Crujiente] 🧀🍝 #recetas #asmrcooking #[ingrediente1] #foodporn`
  *(Ej: Rigatoni Cremoso al Vodka con Burrata Fundente 🧀🍝 #pasta #burrata #asmrcooking #recetasfaciles)*
- **Opción B (Promesa de Tiempo / Antojo):**
  `Cuando tienes antojo de [Plato] a las 11 PM 🤤🔥 #[ingrediente] #asmrfood #recetasvirales #cocina`

### Para Formato 2 (Recreación de Caricaturas en Split-Screen):
- **Opción A (Clásica de Alto CTR — Estilo Cultura Glotona):**
  `¡Recreé el [Plato Icónico] de [Nombre de la Caricatura / Personaje]! 🍔🔥 #[caricatura] #recetasdecaricaturas #foodporn #viral`
  *(Ej: ¡Recreé los Tacos de Ramen de Escandalosos! 🍜🌮 #escandalosos #webarebears #ramentaco #recetasvirales)*
- **Opción B (Reto / Curiosidad):**
  `¿A qué sabe realmente el [Plato] de [Caricatura]? Lo hicimos en la vida real 🤯🥪 #[caricatura] #cocina #shorts`

---

## 3. Estrategia del Primer Comentario Fijado (*Pinned Comment*)

Inmediatamente después de publicar el video desde el PC, la persona encargada del canal debe escribir y **fijar (Pin)** el primer comentario usando una de estas 2 fórmulas:

- **En Formato 2 (Caricaturas):**
  > *"¿Del 1 al 10 qué tan idéntico nos quedó al de [Personaje/Caricatura]? 👀👇 ¿Cuál es el siguiente plato de caricatura o anime que deberíamos cocinar?"*
- **En Formato 1 (POV ASMR):**
  > *"📌 Les dejé la receta exacta en gramos en la descripción para que la guarden. ¿Le pondrían [Ingrediente extra polémico: ej. más picante / tocino / sin cebolla] o así está perfecto? 👇"*

---

## 4. Checklist de Pre-Vuelo (Antes de darle a "Publicar")

Antes de subir el archivo `renders/<proyecto>_final.mp4`, el encargado del canal verifica estos 6 puntos:

- [ ] **1. Verificación Visual Completa:** Reproducir el `.mp4` de principio a fin. Cero cortes negros, cero textos deformes, y en Formato 2 el clip superior no tiene logos de TV y pasa a Pantalla Completa en el segundo exacto.
- [ ] **2. Verificación Acústica:** Escuchar con audífonos. El foley cruje limpio sin saturar (`-10 dB`), no hay suspiros extraños de IA, y en Formato 2 el diálogo de la caricatura se entiende con claridad total.
- [ ] **3. Frame de Portada Seleccionado:** Al subir en YouTube/TikTok/Reels, mover el selector de miniatura al segundo exacto indicado en `FICHA_PUBLICACION.md`.
- [ ] **4. Título + Descripción con Gramos Copiados:** Pegar desde `FICHA_PUBLICACION.md` sin errores de ortografía.
- [ ] **5. Comentario Fijado Publicado:** Publicar y fijar la pregunta gatillo en la caja de comentarios.
- [ ] **6. Sincronización Git con el Equipo:** Guardar `GUIA_GENERACION.md`, `assemble.py` y `FICHA_PUBLICACION.md` en `episodes/<codigo_episodio>/`, actualizar `episodes/README.md` y ejecutar `git push origin main`.
