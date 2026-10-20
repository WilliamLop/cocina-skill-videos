# Episodios Producidos y Guías Maestras

Este directorio reúne la documentación técnica, guías de generación para Google Flow (`Nano Banana Pro` + `Veo 3.1`) y los scripts de ensamblado de HyperFrames (`assemble.py`) correspondientes a los episodios producidos con la skill `cocina-audiovisual-flow`.

---

## Estructura de Episodios

### Formato 1: POV Editorial ASMR (Pantalla Completa 9:16)
- **`P001_rigatoni_burrata_vodka/`**: *Rigatoni Cremoso al Vodka con Burrata Trufada* (20.0s).
  - **Hito Técnico:** Implementación de la **Regla L17 (*Step-Anchor Chaining*)** para evitar la mutación del plato final durante la fase de adición de toppings/emplatado.
- **`P002_birria_tacos_cheese/`**: *Smash Tacos de Birria con Costra de Queso y Consomé Caliente* (20.0s).
- **`P003_ramen_tonkotsu_chashu/`**: *Ramen Tonkotsu Cremoso con Chashu Sopleteado* (30.0s, versión extendida de 21 planos).

### Formato 2: Recreación de Caricaturas en Split-Screen
- **`P004_tacos_ramen_escandalosos/`**: *Tacos de Ramen de Escandalosos (We Bare Bears)* (20.0s).
  - **Hito Técnico:** Split-screen dual (35% caricatura arriba / 65% cocina fotorrealista abajo) con transición automática a pantalla completa (1080x1920) al segundo 16.20, filtrado de frecuencias graves con filtro paso alto (High-Pass) y balance de foley secundario frente al diálogo original.
