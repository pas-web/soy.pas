# Sitio web · Licenciatura en Producción Agropecuaria Sustentable (PAS)

Sitio informativo para estudiantes de la Licenciatura en Producción Agropecuaria Sustentable de la Universidad Autónoma de Querétaro, Facultad de Ciencias Naturales, Campus Concá, en la Sierra Gorda de Querétaro.

Reúne en un solo lugar horarios, becas, titulación, servicio social, prácticas profesionales y los demás trámites de la carrera. Sustituye gradualmente al sitio anterior en Google Sites.

## Estructura del sitio

| Archivo | Sección | Estado |
|---|---|---|
| `index.html` | Portada con accesos rápidos, Procedimientos e Información | ✅ Rediseñada |
| `practicas.html` | Prácticas profesionales (proceso en 2 etapas: Alta y Conclusión) | ✅ Rediseñada |
| `horas.html` | Horas extracurriculares (150 h CIDAF + 5 créditos) | ✅ Rediseñada |
| `egresados.html` | Egresados (cédula, CV, LinkedIn, OCCMundial) | ✅ Rediseñada |
| `servicio-social.html` | Servicio Social (proceso en 4 etapas) | ✅ Rediseñada |
| `consejo.html` | Consejo interno (solicitudes, plazos, actas, calendario) | ✅ Rediseñada |
| Becas, Titulación, Horarios, Inscripción, Movilidad, Salidas de campo, Certificaciones, Seminarios | Enlazadas al Google Sites original | ⏳ Pendientes de migrar |

Cada archivo HTML es **autocontenido**: lleva incrustados sus estilos, el logo y el favicon. No hay dependencias de compilación ni carpetas de recursos — subir el archivo es publicar la página.

## Cómo funciona el contenido (arquitectura híbrida)

El sitio separa dos tipos de contenido:

- **Lo estable** (estructura, textos permanentes, diseño) vive en estos archivos HTML. Solo cambia cuando se rediseña algo.
- **Lo volátil** (horarios del semestre, convocatorias, bases de datos de avance, formatos, actas) vive en Google Drive y plataformas de la UAQ. **El personal lo actualiza ahí, como siempre, sin tocar este repositorio.** Los enlaces del sitio apuntan a esos documentos y reflejan los cambios automáticamente.

## Cómo actualizar el sitio

**Para cambiar documentos de Drive (horarios, convocatorias, formatos):** no se toca el repositorio. Se edita el documento en Drive y listo.

**Para reemplazar o agregar una página:** en GitHub, botón `Add file` → `Upload files`, arrastrar el archivo HTML y `Commit changes`. GitHub Pages republica solo en uno o dos minutos. Los archivos nuevos quedan disponibles en `https://<usuario>.github.io/<repositorio>/<archivo>.html`.

**Nombres de archivo:** en minúsculas, sin espacios ni acentos (`servicio-social.html`, no `Servicio Social.html`). La portada debe llamarse exactamente `index.html`.

## Convenciones del sitio

Decisiones de diseño y técnica que las páginas nuevas deben respetar (cada archivo documenta las suyas en el comentario inicial del código):

- **Identidad:** paleta Sierra Gorda — verde monte `#0E3B2E`, teal `#14706B`, verde milpa `#2E9E4F`, azul PAS `#1D4D77` (tomado del logo), crema `#FAF7F0`. Tipografías Fraunces (títulos) e Instrument Sans (cuerpo), vía Google Fonts. Ornamentos SVG de grabado serrano (sotol, milpa, correcaminos, biznaga, cerros, sol) dibujados en el propio código.
- **Enlaces externos** (Drive, Forms, plataformas UAQ): abren en pestaña nueva (`target="_blank" rel="noopener"`) y se señalan con flecha **↗**; los internos usan **→**.
- **Formatos que el estudiante llena** (cartas, informes): se enlazan en modo `/copy` de Google Docs, para que cada quien obtenga su copia y el documento maestro quede protegido.
- **Bases de datos de consulta** (registros de horas, créditos): se enlazan en modo `/preview` (solo lectura). El blindaje de fondo es fijar el permiso "Lector" en Drive.
- **URLs limpias:** sin redirectores de Google (`google.com/url?q=...`) ni identificadores de sesión (`jsessionid`), que caducan y rompen los enlaces.

## Pendientes

- [ ] Activar `og:image` en las seis páginas: descomentar la línea correspondiente en cada `<head>` y poner la URL pública del logo (requiere subir `logo_PAS_transparente.png` al repositorio).
- [ ] Fijar permiso "Lector" en Drive a las dos bases de datos de Horas extracurriculares.
- [ ] Plantilla de solicitud de "Créditos" del Consejo: en el sitio original es una imagen sin documento; falta la URL del documento real para integrarla.
- [ ] Correo de contacto de coordinación en las cajas de ayuda de Prácticas y Horas.
- [ ] Migrar las ocho secciones restantes (Titulación es la prioritaria).

## Créditos

Sitio de la **Licenciatura en Producción Agropecuaria Sustentable** · Universidad Autónoma de Querétaro · Facultad de Ciencias Naturales · Campus Concá, Sierra Gorda, Querétaro.

El contenido académico y los documentos enlazados pertenecen a la UAQ y sus dependencias. Diseño desarrollado en 2026 sobre el inventario de contenidos del sitio original.
