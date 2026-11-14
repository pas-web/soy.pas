# Cómo se genera la bolsa

`bolsa.html` no se edita a mano: sale de los datos del mes.

    python3 _bolsa/datos/arma_AAAA_MM.py      # escribe _bolsa/datos/AAAA-MM.json
    python3 _bolsa/genera.py _bolsa/datos/AAAA-MM.json

- `datos/AAAA-MM.json` es la memoria de la bolsa: cada oportunidad lleva `desde` (mes de primera publicación) y `historico_sueldos` acumula los sueldos leídos en meses anteriores.
- `genera.py` arma la página completa (mapa, sueldos, filtros, fechas, radar) e incrusta `estilos.css`, `bolsa.js`, el logo y el favicon, para que `bolsa.html` siga siendo autocontenido.
- Si una oportunidad lleva `muni`, aparece en el mapa; la cabecera debe existir en `LUGARES` de `genera.py`.
- `mapa.json` (contornos de los estados alrededor de Concá) solo se regenera con `prepara_mapa.py` si cambia el alcance.
- La cuenta regresiva y el aviso de «cerró» los calcula el navegador con la fecha de quien abre la página.
