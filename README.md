# 📦 Generador de Inventario Inteligente (Web & Excel)

## 1. Introducción
Bienvenido al **Generador de Inventario Automatizado**. Esta herramienta es una solución web diseñada para simular, visualizar y exportar grandes volúmenes de datos de inventario de manera instantánea. 

El sistema permite generar registros aleatorios y realistas (fechas, regiones, encargados con foto, productos con foto, entradas y salidas) para facilitar pruebas de bases de datos, análisis de stock o simplemente para automatizar la gestión administrativa sin necesidad de servidores complejos.

## 2. Planteamiento del Problema
En el entorno empresarial y de desarrollo, a menudo nos enfrentamos a los siguientes desafíos:
*   **Creación de Datos de Prueba:** Generar miles de filas de datos realistas para Excel manualmente es tedioso y propenso a errores.
*   **Gestión de Archivos Dispersos:** Cuando se manejan inventarios por fechas, guardar archivo por archivo (Enero, Febrero, Marzo...) consume demasiado tiempo.
*   **Visualización Pobre:** Las hojas de cálculo tradicionales no suelen mostrar visualmente a los responsables ni los productos de forma amigable.
*   **Pérdida de Información:** Al exportar a Excel desde la web, a menudo se pierden los enlaces a las imágenes de los productos o encargados.

## 3. Solución Propuesta
Este proyecto resuelve estos problemas mediante una interfaz web ágil e interactiva que ofrece:

1.  **Generación Automática:** Crea registros inteligentes basados en rangos de fechas definidos por el usuario.
2.  **Cálculos en Tiempo Real:** Calcula automáticamente el Stock Final (Entradas - Salidas) y valida la lógica de negocio.
3.  **Interfaz Visual Premium:** Una tabla paginada (7 registros por página) con avatares de encargados e imágenes de productos visibles directamente en el navegador.
4.  **Exportación Masiva Avanzada:** Utiliza la *File System Access API* para permitir al usuario **elegir una carpeta local** y guardar automáticamente múltiples archivos Excel (uno por cada mes) con un solo clic, incluyendo los enlaces (URLs) a las imágenes correspondientes.

## 4. Tecnologías Utilizadas
El proyecto ha sido construido utilizando estándares web modernos y librerías optimizadas:

*   **Lenguajes:**
    *   ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) **HTML5:** Estructura semántica.
    *   ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white) **CSS3:** Diseño responsivo y estilizado.
    *   ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black) **JavaScript (ES6+):** Lógica de generación de datos, manipulación del DOM y manejo de archivos.

*   **Frameworks & Librerías:**
    *   **Bootstrap 5:** Para el sistema de rejilla, componentes UI (tablas, botones, inputs) y diseño *Mobile-First*.
    *   **SheetJS (xlsx):** La librería líder para la creación y manipulación de hojas de cálculo Excel desde el navegador.
    *   **Bootstrap Icons:** Iconografía vectorial ligera.

*   **APIs del Navegador:**
    *   **File System Access API:** Para interactuar con el sistema de archivos local y guardar múltiples archivos en directorios específicos.

## 5. Llamado a la Acción (Call to Action)
🚀 **¡Deja de perder tiempo creando Excels manualmente!**

Descarga este código, abre el archivo `index.html` en tu navegador y genera reportes de todo un año en segundos. Personaliza la lista de productos y encargados en el código y adapta la herramienta a tu negocio hoy mismo.

> *¡Pruébalo ahora y automatiza tu flujo de trabajo!*

## 6. Conclusión
El **Generador de Inventario Inteligente** demuestra cómo las tecnologías web modernas pueden reemplazar tareas manuales complejas. Al combinar una interfaz visual atractiva con la potencia de `SheetJS` y el acceso al sistema de archivos local, hemos eliminado la fricción entre la visualización de datos en la web y el almacenamiento de reportes en el escritorio. Es una herramienta ligera, sin instalación y altamente efectiva.

## 7. Redes Sociales
Si te gustó este proyecto o tienes sugerencias, ¡conéctate conmigo!

*   👤 **GitHub:** [github.com/tu-usuario](https://github.com/)
*   💼 **LinkedIn:** [linkedin.com/in/tu-usuario](https://linkedin.com/)
*   🐦 **Twitter/X:** [@tu-usuario](https://twitter.com/)
*   🌐 **Portafolio:** [tu-web.com](https://google.com)

---
*Desarrollado con ❤️ y código limpio.*
