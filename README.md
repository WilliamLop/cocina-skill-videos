# Cocina Audiovisual Flow (`cocina-audiovisual-flow`)

[![Agent Skill](https://img.shields.io/badge/Antigravity-Agent%20Skill-blue.svg)](https://github.com/WilliamLop/cocina-skill-videos.git)
[![Pipeline](https://img.shields.io/badge/Pipeline-Google%20Flow%20%2B%20HyperFrames-green.svg)](https://github.com/WilliamLop/cocina-skill-videos.git)
[![Resolution](https://img.shields.io/badge/Format-1080x1920%20(9%3A16)-orange.svg)](https://github.com/WilliamLop/cocina-skill-videos.git)

Agent Skill profesional e instalable para diseñar, generar y ensamblar episodios de **cocina fotorrealista vertical (9:16)** en **Google Flow (`Nano Banana Pro` + `Veo 3.1`)** y **HyperFrames**.

Esta skill codifica y automatiza las **16 reglas canónicas de producción** derivadas de los pilotos reales `P002` a `P006`, erradicando por completo los errores clásicos de la IA audiovisual (mutación de encimeras, cortes deformes, botellas flotantes, disparidades de volumen y desincronización).

---

## 📋 Tabla de Contenidos

1. [Formatos Soportados](#-formatos-soportados)
2. [Las 4 Reglas de Oro Canónicas](#-las-4-reglas-de-oro-canónicas)
3. [Requisitos del Sistema](#-requisitos-del-sistema)
4. [Instalación Paso a Paso](#-instalación-paso-a-paso)
5. [Cómo Invocar y Usar la Skill](#-cómo-invocar-y-usar-la-skill)
6. [Estructura del Repositorio](#-estructura-del-repositorio)
7. [Pipeline Operativo en 5 Fases](#-pipeline-operativo-en-5-fases)
8. [Créditos y Mantenimiento](#-créditos-y-mantenimiento)

---

## 🍳 Formatos Soportados

| Criterio | Formato 1: POV Editorial ASMR | Formato 2: Recreación de Caricaturas en Split-Screen |
|---|---|---|
| **Inspiración** | `@alenakhmil`, `@namcook`, `@moribyan` | `@culturaglotona`, `@cookingWITHfred` |
| **Pilotos probados** | `P002` (Pollo Toscano), `P003` (Pasta con Camarones) | `P004` (Elmer Gruñón), `P005` (Knuckles), `P006` (Poor Boy Scooby) |
| **Lienzo** | `1080x1920 px` (Fullscreen continuo) | Split-Screen dual (35%/65%) con cierre a Pantalla Completa |
| **Duración** | `18 a 22 segundos` (15–18 planos) | `18 a 25 segundos` (12–15 planos) |
| **Audio líder** | Foley culinario ASMR nativo + Cama Lo-Fi/Jazz con muesca EQ | Diálogo / Canción doblada de la caricatura + Foley suplementario |
| **Peculiaridad** | Cero rostros, f/2.0 a 4500K, foley puro a -10 dB | Sincronización espejo 1:1 + Expansión fullscreen en el clímax |

---

## ⚡ Las 4 Reglas de Oro Canónicas

Cualquier agente o editor que opere bajo esta skill debe respetar estas directivas:

1. **100% Video (`.mp4`), Cero Fotos Fijas (L01):** Prohibido usar imágenes congeladas o zooms simulados. Cada toma debe tener micro-movimiento, física de fluidos real y vapor vivo.
2. **Uso Obligatorio de Ancla de Escenario (`ANCHOR_01` en `[+]`) (L05, L08):** Antes de crear comida, se genera la tabla vacía en `Nano Banana Pro (9:16)` y se adjunta obligatoriamente en `+` en cada toma subsiguiente.
3. **Regla del Estado Inicial y Master Hero (L04, L06, L07):** En planos de corte, el cuchillo se suspende 2 cm por encima del ingrediente entero; en vertidos, la botella se inclina rozando la primera gota. Para pilas o sándwiches, el Master Hero se describe idéntico en cada toma.
4. **Ingeniería de Audio Foley a `-10 dB` (L09, L10, L11):** Todo clip descargado se audita, se respalda inmutablemente en `originals_raw/` y se nivela a `-10.0 dBFS` pico con `ffmpeg -c:v copy` sin alterar la calidad del video.

---

## 🛠️ Requisitos del Sistema

- **Python 3.8+** (con biblioteca estándar: `os`, `sys`, `shutil`, `subprocess`, `argparse`).
- **FFmpeg y FFprobe** instalados y accesibles en la terminal (`ffmpeg -version`).
- **Node.js 18+** y **HyperFrames CLI** (`npm i -g hyperframes` o vía `npx hyperframes`).
- Acceso a **Google Flow** con modelos `Nano Banana Pro` y `Veo 3.1 Fast / Quality`.

---

## 📦 Instalación Paso a Paso

Puedes instalar esta Agent Skill de forma global (para todos tus proyectos) o a nivel de workspace (para un proyecto específico):

### Opción 1: Instalación Global en Antigravity / Gemini CLI (Recomendado)
Instala la skill en tu directorio de configuración global para que cualquier asistente la reconozca automáticamente:

```bash
# Crear directorio de skills si no existe
mkdir -p ~/.gemini/config/skills

# Clonar la skill oficial
git clone https://github.com/WilliamLop/cocina-skill-videos.git ~/.gemini/config/skills/cocina-audiovisual-flow
```

### Opción 2: Instalación Local en Workspace (Equipo / Repositorio Compartido)
Si deseas que la skill viaje dentro del repositorio de tu equipo:

```bash
# En la raíz de tu proyecto o workspace:
mkdir -p .agent/skills

# Clonar dentro de la carpeta de agentes del proyecto:
git clone https://github.com/WilliamLop/cocina-skill-videos.git .agent/skills/cocina-audiovisual-flow
```

### Opción 3: Actualizar una Instalación Existente
Para sincronizar las últimas lecciones y mejoras del equipo:

```bash
cd ~/.gemini/config/skills/cocina-audiovisual-flow
git pull origin main
```

---

## 🤖 Cómo Invocar y Usar la Skill

Una vez instalada, los asistentes de IA compatibles con Agent Skills (Antigravity, Gemini CLI, Claude Code, Cursor) detectarán automáticamente la skill a través de su frontmatter en `SKILL.md`.

### Ejemplos de Solicitudes al Asistente:

#### 1. Planificar un nuevo episodio y redactar la Guía de Generación:
> *"Activa la skill `cocina-audiovisual-flow` y redacta la Guía Maestra de Generación para el Piloto P007 en Formato 2: La Cangreburger de Bob Esponja. Incluye los 12 planos con recordatorios inline `[📎 ADJUNTAR EN +]`, tabla cronométrica al segundo y empaquetado SEO bilingüe."*

#### 2. Nivelar y respaldar clips descargados:
> *"Acabo de descargar los 14 clips de Veo en `projects/P007_cangreburger/assets_flow/`. Usa el script de la skill `cocina-audiovisual-flow` para verificar resolución, respaldar originales en `originals_raw/` y nivelar picos de audio a -10 dB."*

#### 3. Auto-ensamblar en HyperFrames:
> *"Genera el script `assemble.py` a partir de la plantilla de `cocina-audiovisual-flow`, calibra el `data-media-start` a 0.35 s y valida el proyecto con `npx hyperframes check`."*

---

## 📂 Estructura del Repositorio

```text
cocina-skill-videos/
├── SKILL.md                              # Instrucciones maestras y YAML frontmatter
├── README.md                             # Documentación de instalación y uso
├── .gitignore                            # Ignora temporales, backups y videos pesados
├── references/                           # Especificaciones canónicas de referencia
│   ├── FORMATO_1_POV_ASMR.md             # Guía completa de Formato 1 (18-22s, 4500K, f/2.0)
│   ├── FORMATO_2_SPLIT_CARICATURAS.md    # Geometría Split-Screen (35%/65%) y Payoff Fullscreen
│   └── PROMPT_PATTERNS.md                # Fórmulas de prompts para Nano Banana Pro y Veo 3.1
├── templates/                            # Plantillas listas para producción
│   ├── GUIA_GENERACION_TEMPLATE.md       # Plantilla de redacción con [📎 ADJUNTAR EN +] inline
│   └── ASSEMBLE_TEMPLATE.py              # Script de ensamblaje modular para HyperFrames
└── scripts/                              # Herramientas de automatización
    └── process_clips.py                  # Auditoría, backup inmutable y nivelación a -10 dB
```

---

## 🔄 Pipeline Operativo en 5 Fases

```
[ FASE 1: DESGLOSE ] ──> [ FASE 2: PROMPTING ] ──> [ FASE 3: RECEPCIÓN ] ──> [ FASE 4: ENSAMBLAJE ] ──> [ FASE 5: MASTER RENDER ]
Escaleta al segundo      Anchor vacía +         Inspección + Backup    assemble.py con          npx hyperframes render
y sincronización         Inline [📎 ADJUNTAR]   Nivelar a -10 dB       data-media-start         + Empaque SEO bilingüe
```

1. **Fase 1 (Desglose):** Escaleta segundo a segundo según la duración meta (18–22s para POV ASMR o 18–25s para Split-Screen).
2. **Fase 2 (Prompting):** Generación de `ANCHOR_01`, `ANCHOR_02` y redacción de la guía usando `templates/GUIA_GENERACION_TEMPLATE.md` con fórmulas de `references/PROMPT_PATTERNS.md`.
3. **Fase 3 (Recepción y Audio):** Ejecución de `python3 scripts/process_clips.py --project projects/<proyecto>`. Los picos quedan automáticamente en `-10.0 dBFS` sin alterar el video.
4. **Fase 4 (Ensamblaje):** Ejecución de `python3 assemble.py` y comprobación de `0 errors, 0 warnings` con `npx hyperframes check projects/<proyecto>`.
5. **Fase 5 (Master Render):** Render final con `npx hyperframes render projects/<proyecto> --quality delivery --output renders/<proyecto>_final.mp4`.

---

## 👥 Créditos y Mantenimiento

- **Autor / Arquitectura:** William López (`@WilliamLop`) & Equipo de Automatización Audiovisual.
- **Repositorio Oficial:** [https://github.com/WilliamLop/cocina-skill-videos.git](https://github.com/WilliamLop/cocina-skill-videos.git)
- **Licencia:** MIT. Libre para uso interno y comercial en flujos de producción audiovisual con IA.
