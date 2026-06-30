# Guía de Contribución

¡Gracias por tu interés en contribuir al proyecto de Data Mart de Palta Hass!

## Cómo contribuir

1. **Haz un Fork del repositorio**: Crea tu propia copia para trabajar.
2. **Crea una rama (branch)**: Nómbrala según la característica que vas a desarrollar (`git checkout -b feature/nueva-metrica`).
3. **Haz tus cambios**:
   - Sigue los estándares de código definidos en `.editorconfig`.
   - Documenta cualquier nuevo script en la carpeta `docs/`.
4. **Haz commit de tus cambios**: Usa mensajes claros y descriptivos (`git commit -m "feat: agregar nueva dimensión de calidad"`).
5. **Haz push a la rama**: Sube tus cambios a tu fork (`git push origin feature/nueva-metrica`).
6. **Abre un Pull Request**: Describe detalladamente qué cambios realizaste y por qué.

## Estándares del Código

- **Scripts SQL**: Nombres de tablas en mayúsculas, palabras reservadas en mayúsculas, formato legible.
- **Python**: Sigue las guías de estilo PEP 8.
- **Power BI**: Asegúrate de no incluir credenciales embebidas ni datos en crudo que excedan los límites antes de hacer un commit del archivo `.pbix` o `.pbit`.

¡Toda ayuda para mejorar el modelo analítico es bienvenida!
