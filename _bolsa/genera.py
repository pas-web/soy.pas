#!/usr/bin/env python3
"""Genera bolsa.html a partir de los datos del mes.

    python3 _bolsa/genera.py _bolsa/datos/2026-11.json

Lee estilos.css, bolsa.js, mapa.json, logo.b64 y favicon.b64 de esta carpeta y
escribe ../bolsa.html, autocontenido (como el resto del sitio). El archivo de
datos del mes es la memoria de la bolsa: cada oportunidad lleva "desde" (mes de
primera publicación).
"""
import json, math, os, sys, html, re

AQUI = os.path.dirname(os.path.abspath(__file__))
CONCA = (21.4467, -99.6356)
RADIO = 310          # km que abarca el mapa
EJE = (8000, 26000)  # eje de la gráfica de sueldos
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
         "septiembre", "octubre", "noviembre", "diciembre"]
MES3 = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]

# Cabeceras municipales (lat, lon). Añadir aquí las que hagan falta.
LUGARES = {
    "Concá": (21.4467, -99.6356), "Arroyo Seco": (21.547, -99.688), "Jalpan de Serra": (21.217, -99.473),
    "Landa de Matamoros": (21.183, -99.320), "Pinal de Amoles": (21.134, -99.627), "Peñamiller": (21.052, -99.815),
    "Tolimán": (20.908, -99.930), "Cadereyta": (20.694, -99.815), "San Joaquín": (20.916, -99.565),
    "Querétaro": (20.588, -100.389), "El Marqués": (20.625, -100.280), "Corregidora": (20.533, -100.443),
    "Huimilpan": (20.374, -100.275), "Pedro Escobedo": (20.502, -100.141), "Colón": (20.787, -100.049),
    "Ezequiel Montes": (20.665, -99.899), "Tequisquiapan": (20.522, -99.892), "San Juan del Río": (20.389, -99.996),
    "Amealco": (20.187, -100.145),
    "Celaya": (20.523, -100.815), "Apaseo el Grande": (20.546, -100.685), "Apaseo el Alto": (20.457, -100.621),
    "Cortazar": (20.483, -100.962), "Salamanca": (20.571, -101.195), "Irapuato": (20.677, -101.347),
    "León": (21.122, -101.682), "Silao": (20.944, -101.427), "Guanajuato": (21.019, -101.257),
    "San Miguel de Allende": (20.914, -100.744), "Dolores Hidalgo": (21.156, -100.932),
    "San Luis de la Paz": (21.298, -100.516), "San José Iturbide": (21.001, -100.385), "Victoria": (21.211, -100.214),
    "Xichú": (21.300, -100.055), "Acámbaro": (20.030, -100.722), "Pénjamo": (20.431, -101.722),
    "Valle de Santiago": (20.393, -101.191), "Comonfort": (20.722, -100.760), "Villagrán": (20.515, -100.997),
    "San Luis Potosí": (22.156, -100.985), "Soledad de Graciano Sánchez": (22.187, -100.937),
    "Rioverde": (21.932, -99.995), "Ciudad Valles": (21.997, -99.011), "Tamazunchale": (21.262, -98.789),
    "Xilitla": (21.386, -98.990), "Cárdenas": (22.001, -99.650), "Ciudad del Maíz": (22.400, -99.602),
    "Tamuín": (22.005, -98.778), "Ébano": (22.218, -98.378), "Matehuala": (23.648, -100.644),
    "Villa de Reyes": (21.803, -100.933), "Aquismón": (21.622, -99.020), "Tamasopo": (21.921, -99.394),
    "Pachuca": (20.101, -98.759), "Tulancingo": (20.084, -98.363), "Ixmiquilpan": (20.482, -99.218),
    "Huichapan": (20.375, -99.650), "Tula": (20.054, -99.342), "Zimapán": (20.738, -99.381),
    "Jacala": (21.006, -99.190), "Huejutla": (21.140, -98.420), "Actopan": (20.268, -98.943),
    "Tizayuca": (19.840, -98.980), "Apan": (19.711, -98.451), "Mixquiahuala": (20.230, -99.213),
    "Toluca": (19.283, -99.655), "Metepec": (19.251, -99.605), "Texcoco": (19.512, -98.882),
    "Atlacomulco": (19.798, -99.875), "Jilotepec": (19.952, -99.533), "Ixtlahuaca": (19.569, -99.767),
    "Tenancingo": (18.961, -99.591), "Villa Guerrero": (18.960, -99.641), "Zumpango": (19.797, -99.099),
    "Tepotzotlán": (19.716, -99.223), "Cuautitlán Izcalli": (19.647, -99.246), "Valle de Bravo": (19.193, -100.131),
    "Santa María Rayón": (19.148, -99.580), "Tultitlán": (19.645, -99.169), "San Francisco del Rincón": (21.018, -101.855), "Lerma": (19.285, -99.512), "Ciudad de México": (19.433, -99.133),
    "Morelia": (19.706, -101.195), "Aguascalientes": (21.882, -102.296), "Ciudad Victoria": (23.737, -99.146),
    "Tampico": (22.255, -97.868),
}
ETIQUETAS_ESTADO = {"S.L.P.": (22.75, -100.55), "GTO.": (20.86, -101.05), "QRO.": (20.93, -99.93),
                    "HGO.": (20.52, -98.82), "EDOMEX": (19.55, -100.0)}
CATS = [
    ("empleo", "c-empleos", "Empleos", "Ver vacante"),
    ("beca", "c-becas", "Becas y primer empleo", "Ver convocatoria"),
    ("apoyo", "c-apoyos", "Apoyos para proyectos", "Ver convocatoria"),
    ("curso", "c-capacitaciones", "Capacitaciones", "Ver curso"),
    ("registro", "c-registros", "Convocatorias y registros", "Abrir"),
]
ICO_GUARDAR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" aria-hidden="true"><path d="M6 3h12v18l-6-4.5L6 21z"/></svg>'
ICO_COMPARTIR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="18" cy="5" r="2.6"/><circle cx="6" cy="12" r="2.6"/><circle cx="18" cy="19" r="2.6"/><path d="M8.3 10.8l7.4-4.4M8.3 13.2l7.4 4.4"/></svg>'

e = lambda s: html.escape(str(s), quote=True)


def proyecta(lat, lon):
    la1, lo1, la2, lo2 = map(math.radians, (CONCA[0], CONCA[1], lat, lon))
    dlo = lo2 - lo1
    a = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin(dlo / 2) ** 2
    d = 6371.0 * 2 * math.asin(math.sqrt(a))
    t = math.atan2(math.sin(dlo) * math.cos(la2),
                   math.cos(la1) * math.sin(la2) - math.sin(la1) * math.cos(la2) * math.cos(dlo))
    return d * math.sin(t), -d * math.cos(t), d


def pesos(n):
    return "${:,.0f}".format(n)


def fecha_larga(s, con_anio=False):
    a, m, d = map(int, s.split("-"))
    t = "{} de {}".format(d, MESES[m - 1])
    return t + (" de {}".format(a) if con_anio else "")


def sueldo_texto(it):
    lo, hi = it["sueldo"]
    return pesos(lo) if lo == hi else "{} a {}".format(pesos(lo), pesos(hi))


# ───────────────────────── tarjetas ─────────────────────────
def tarjeta(it, mes, ver):
    km = it.get("km")
    attrs = ['class="vacante"', 'id="v-{}"'.format(e(it["id"])), 'data-desde="{}"'.format(e(it["desde"])),
             'data-cat="{}"'.format(it["cat"]), 'data-perfil="{}"'.format(" ".join(it.get("perfil", []))),
             'data-href="{}"'.format(e(it["url"]))]
    if km is not None:
        attrs.append('data-km="{}"'.format(km))
    if it.get("sueldo"):
        attrs.append('data-sueldo="{}"'.format(it["sueldo"][1]))
    limite = it.get("cierre") or it.get("evento")
    if limite:
        attrs.append('data-cierre="{}"'.format(limite))
    nueva = it["desde"] == mes
    if nueva:
        attrs.append("data-nueva")
    marca = '<span class="v-nuevo">Nuevo</span>' if nueva else '<span class="v-segundo">Sigue abierta</span>'
    o = ['<article {}>'.format(" ".join(attrs)),
         '<div class="v-top"><span class="v-sector">{}</span>{}</div>'.format(e(it["sector"]), marca),
         '<h4><a href="{}" target="_blank" rel="noopener">{}</a></h4>'.format(e(it["url"]), e(it["titulo"])),
         '<p class="v-org">{}</p>'.format(e(" · ".join(x for x in (it.get("org"), it.get("lugar")) if x)))]
    if it.get("linea"):
        o.append('<p class="v-linea">{}</p>'.format(e(it["linea"])))
    if it.get("sueldo"):
        o.append('<p class="v-sueldo"><b>{}</b> <span>{}</span></p>'.format(
            sueldo_texto(it), e(it.get("sueldo_nota") or "al mes")))
    elif it.get("monto"):
        o.append('<p class="v-sueldo"><b>{}</b> <span>{}</span></p>'.format(e(it["monto"]), e(it.get("monto_nota", ""))))
    elif it["cat"] == "empleo":
        o.append('<p class="v-sueldo no"><span>Sueldo no publicado: pregúntalo en la entrevista</span></p>')
    chips = []
    perfil = it.get("perfil", [])
    if "recien" in perfil:
        chips.append('<li class="c-recien">Recién egresado</li>')
    if "estudiante" in perfil:
        chips.append('<li class="c-estudiante">Estudiantes</li>')
    if it.get("exp"):
        chips.append('<li class="c-exp">{}</li>'.format(e(it["exp"])))
    if km is not None:
        chips.append('<li class="c-km">a {} km de Concá</li>'.format(km))
    c = it.get("contrato")
    if c:
        chips.append('<li class="{}">{}</li>'.format("c-hon" if it.get("contrato_alerta") else "c-prest", e(c)))
    for extra in it.get("chips", []):
        chips.append("<li>{}</li>".format(e(extra)))
    if it.get("cierre"):
        chips.append('<li class="c-cierre" data-verbo="Cierra">Cierra el {}</li>'.format(fecha_larga(it["cierre"])))
    elif it.get("evento"):
        chips.append('<li class="c-cierre" data-verbo="Es">{}</li>'.format(e(it.get("evento_txt") or "Es el " + fecha_larga(it["evento"]))))
    elif it.get("permanente"):
        chips.append("<li>Permanente</li>")
    o.append('<ul class="v-chips">{}</ul>'.format("".join(chips)))
    o.append('<div class="v-pie"><span class="v-ir">{} ↗</span>'
             '<button type="button" class="v-btn v-guardar" aria-pressed="false" aria-label="Guardar para después">{}</button>'
             '<button type="button" class="v-btn v-compartir" aria-label="Compartir esta oportunidad">{}</button></div>'.format(ver, ICO_GUARDAR, ICO_COMPARTIR))
    o.append("</article>")
    return "\n".join(o)


# ───────────────────────── mapa ─────────────────────────
def mapa(items):
    geo = json.load(open(os.path.join(AQUI, "mapa.json"), encoding="utf-8"))
    pts = {}
    for it in items:
        if it.get("muni"):
            pts.setdefault(it["muni"], []).append(it)
    # agrupa cabeceras a menos de 26 km para que los puntos no se encimen
    grupos = []
    for muni in sorted(pts, key=lambda m: -len(pts[m])):
        x, y, d = proyecta(*LUGARES[muni])
        for g in grupos:
            if math.hypot(g["x"] - x, g["y"] - y) < 26:
                g["munis"].append(muni); g["items"] += pts[muni]
                break
        else:
            grupos.append({"x": x, "y": y, "d": d, "munis": [muni], "items": list(pts[muni])})
    grupos = [g for g in grupos if g["d"] <= RADIO]
    grupos.sort(key=lambda g: g["d"])
    V = RADIO + 8
    s = ['<svg class="mapa-svg" viewBox="{0} {0} {1} {1}" role="group" aria-label="Mapa de oportunidades alrededor de Concá">'.format(-V, 2 * V),
         '<defs><clipPath id="disco"><circle r="{}"/></clipPath>'
         '<linearGradient id="haz" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7FE0A3" stop-opacity="0"/><stop offset="1" stop-color="#7FE0A3" stop-opacity=".22"/></linearGradient></defs>'.format(RADIO),
         '<circle r="{}" fill="rgba(0,0,0,.16)"/>'.format(RADIO), '<g clip-path="url(#disco)">']
    for est in geo["estados"]:
        d = "".join("M" + "L".join("{} {}".format(x, y) for x, y in c) + "Z" for c in est["caminos"])
        s.append('<path class="estado{}" d="{}"/>'.format(" region" if est["region"] else "", d))
    for t, (la, lo) in ETIQUETAS_ESTADO.items():
        x, y, _ = proyecta(la, lo)
        s.append('<text class="edo-t" x="{:.0f}" y="{:.0f}">{}</text>'.format(x, y, t))
    a = math.radians(38)
    s.append('<path class="barrido" d="M0 0L0 {r}A{R} {R} 0 0 0 {x:.1f} {y:.1f}Z" fill="url(#haz)"/>'.format(
        r=-RADIO, R=RADIO, x=-RADIO * math.sin(a), y=-RADIO * math.cos(a)))
    s.append("</g>")
    for r in (100, 200, 300):
        s.append('<circle class="anillo" r="{}"/><text class="anillo-t" x="6" y="{}">{} km</text>'.format(r, -r + 19, r))
    filas, cajas = [], [(0, -30, 110, 8)]
    radios = [14 + 3.2 * min(len(g["items"]), 6) for g in grupos]
    def libre(c, yo):
        for o in cajas:
            if c[0] < o[2] and o[0] < c[2] and c[1] < o[3] and o[1] < c[3]:
                return False
        for j, o in enumerate(grupos):
            if j != yo and c[0] - radios[j] < o["x"] < c[2] + radios[j] and c[1] - radios[j] < o["y"] < c[3] + radios[j]:
                return False
        return abs(c[0]) < RADIO and abs(c[2]) < RADIO
    for i, g in enumerate(grupos):
        n = len(g["items"])
        nombre = g["munis"][0] + (" y alrededores" if len(g["munis"]) > 1 else "")
        clave = "l{}".format(i)
        r = 14 + 3.2 * min(n, 6)
        ancho = 9.6 * len(g["munis"][0])
        der = (g["x"] + r + 6, g["y"] - 13, g["x"] + r + 6 + ancho, g["y"] + 9)
        izqc = (g["x"] - r - 6 - ancho, g["y"] - 13, g["x"] - r - 6, g["y"] + 9)
        orden = [(True, izqc), (False, der)] if g["x"] > 120 else [(False, der), (True, izqc)]
        izq, corto = False, ""
        for lado, caja in orden:
            if libre(caja, i):
                izq, corto = lado, g["munis"][0]; cajas.append(caja); break
        s.append('<g class="pt" data-l="{c}" tabindex="0" role="button" aria-label="{nom}: {n} oportunidades, a {km} km" transform="translate({x:.1f} {y:.1f})">'
                 '<circle r="30" fill="transparent"/><circle class="halo" r="{r:.1f}" style="animation-delay:{dl:.1f}s"/><circle class="c" r="{r:.1f}"/>'
                 '<text y="6">{n}</text><text class="pt-t" x="{tx:.0f}" y="6" text-anchor="{ta}">{corto}</text></g>'.format(
                     c=clave, nom=e(nombre), n=n, km=round(g["d"]), x=g["x"], y=g["y"], r=r, dl=(i % 5) * .5,
                     tx=(-r - 6) if izq else (r + 6), ta="end" if izq else "start", corto=e(corto)))
        ligas = "".join('<li><a href="#v-{}">{}<span>{} · {}</span></a></li>'.format(
            e(it["id"]), e(it["titulo"]), e(it.get("org", "")), e(it["muni"])) for it in g["items"])
        filas.append('<li><details class="lugar" data-l="{}"><summary><span class="km">{}<small> km</small></span>'
                     '<span class="nom">{}</span><span class="cu">{}</span></summary><ul>{}</ul></details></li>'.format(
                         clave, round(g["d"]), e(nombre), n, ligas))
    s.append('<g><circle class="conca" r="9"/><circle r="17" fill="none" stroke="#F2C14E" stroke-width="2"/>'
             '<text class="conca-t" x="24" y="-12">Concá</text></g>')
    s.append("</svg>")
    return "\n".join(s), "\n".join(filas), grupos


# ───────────────────────── sueldos ─────────────────────────
def sueldos(datos, items):
    lo, hi = EJE
    pos = lambda v: max(0.0, min(100.0, (v - lo) / (hi - lo) * 100))
    puntos = []
    for it in items:
        if it.get("sueldo") and it.get("familia"):
            puntos.append({"fam": it["familia"], "s": it["sueldo"], "t": "{} · {}".format(it["titulo"], it.get("org", "")),
                           "viva": True, "id": it["id"], "cuando": "abierta este mes"})
    for h in datos.get("historico_sueldos", []):
        puntos.append({"fam": h["familia"], "s": h["sueldo"], "t": "{} · {}".format(h["titulo"], h["org"]),
                       "viva": False, "cuando": "publicada en " + h["mes"]})
    filas = []
    for clave, nombre in datos["familias"]:
        ps = sorted((p for p in puntos if p["fam"] == clave), key=lambda p: p["s"][0])
        if not ps:
            continue
        carriles, marcas = [], []
        for p in ps:
            a, b = pos(p["s"][0]), pos(p["s"][1])
            c = 0
            while c < len(carriles) and carriles[c] > a - 4.6:
                c += 1
            if c == len(carriles):
                carriles.append(b)
            else:
                carriles[c] = b
            fuera = " fuera" if p["s"][1] > hi else ""
            est = "left:{:.2f}%;width:calc({:.2f}% + 12px);top:{}px".format(a, b - a, c * 17)
            rango = pesos(p["s"][0]) if p["s"][0] == p["s"][1] else "{} a {}".format(pesos(p["s"][0]), pesos(p["s"][1]))
            comun = 'style="{}" data-s="{}" data-t="{} <br><i>{}</i>"'.format(est, rango, e(p["t"]), e(p["cuando"]))
            if p["viva"]:
                marcas.append('<a class="sl-p viva{}" href="#v-{}" {} aria-label="{}: {}"></a>'.format(fuera, e(p["id"]), comun, e(p["t"]), rango))
            else:
                marcas.append('<span class="sl-p{}" tabindex="0" {} role="img" aria-label="{}: {}"></span>'.format(fuera, comun, e(p["t"]), rango))
        todos = [v for p in ps for v in p["s"]]
        filas.append('<div class="sl-fila"><p class="sl-nombre">{} <span>{} · de {} a {}</span></p>'
                     '<div class="sl-pista" style="height:{}px">{}</div></div>'.format(
                         e(nombre), "1 vacante" if len(ps) == 1 else "{} vacantes".format(len(ps)),
                         pesos(min(todos)), pesos(max(todos)), len(carriles) * 17, "".join(marcas)))
    refs = "".join('<div class="sl-ref{}" style="left:{:.2f}%;--c:{}"><span style="top:{}rem">{}</span></div>'.format(
        " izq" if r.get("izq") else "", pos(r["valor"]), r.get("color", "#9C3B1E"), r.get("alto", 0), r["texto_html"])
        for r in datos["referencias_sueldo"])
    eje = "".join('<span style="left:{:.2f}%">{}</span>'.format(pos(v), "$" + str(v // 1000) + " mil") for v in range(10000, hi + 1, 5000))
    mids = sorted((p["s"][0] + p["s"][1]) / 2 for p in puntos)
    n = len(mids)
    q = lambda f: mids[min(n - 1, int(round(f * (n - 1))))]
    return {"filas": "\n".join(filas), "refs": refs, "eje": eje, "n": n, "q1": q(.25), "q2": q(.5), "q3": q(.75),
            "vivas": sum(1 for p in puntos if p["viva"])}


# ───────────────────────── página ─────────────────────────
def construye(ruta):
    datos = json.load(open(ruta, encoding="utf-8"))
    mes = datos["mes"]
    anio, m = map(int, mes.split("-"))
    mes_txt = "{} {}".format(MESES[m - 1].capitalize(), anio)
    items = datos["items"]
    for it in items:
        if it.get("muni"):
            if it["muni"] not in LUGARES:
                sys.exit("Falta la coordenada de «{}» en LUGARES".format(it["muni"]))
            it["km"] = int(round(proyecta(*LUGARES[it["muni"]])[2]))
    ids = [it["id"] for it in items]
    assert len(ids) == len(set(ids)), "ids repetidos"

    css = open(os.path.join(AQUI, "estilos.css"), encoding="utf-8").read()
    js = open(os.path.join(AQUI, "bolsa.js"), encoding="utf-8").read()
    logo = open(os.path.join(AQUI, "logo.b64")).read().strip()
    fav = open(os.path.join(AQUI, "favicon.b64")).read().strip()

    # categorías
    secciones, nav = [], []
    for cat, cid, nombre, ver in CATS:
        los = [it for it in items if it["cat"] == cat]
        if not los:
            continue
        nav.append('<li><a href="#{}">{} <span class="n">{}</span></a></li>'.format(cid, nombre, len(los)))
        secciones.append('<section class="categoria" id="{cid}"><div class="cat-cab"><h3 class="cat-titulo">{n}</h3>'
                         '<span class="cat-n">{k}</span><span class="cat-regla" aria-hidden="true"></span></div>'
                         '<p class="cat-nota">{nota}</p><div class="vacantes">\n{t}\n</div></section>'.format(
                             cid=cid, n=nombre, k=len(los), nota=datos["notas_categoria"].get(cat, ""),
                             t="\n".join(tarjeta(it, mes, ver) for it in los)))

    svg, lugares, grupos = mapa(items)
    sl = sueldos(datos, items)
    en_mapa = sum(len(g["items"]) for g in grupos)

    # destacadas
    porid = {it["id"]: it for it in items}
    dest = []
    for i, d in enumerate(datos["destacadas"], 1):
        it = porid[d["id"]]
        dest.append('<a class="dest d{i}" href="#v-{id}"><span class="lema">{lema}</span><span class="grande">{g}</span>'
                    '<h3>{t}</h3><p>{p}</p><span class="ir">Verla en la lista ↓</span></a>'.format(
                        i=i, id=e(it["id"]), lema=e(d["lema"]), g=d["grande_html"].format(km=it.get("km", "")), t=e(it["titulo"]),
                        p=e(" · ".join(x for x in (it.get("org"), it.get("lugar")) if x))))

    # qué piden
    piden = []
    for p in datos["piden"]["lista"]:
        n = datos["piden"]["n"]
        puntos = "".join('<i class="si"></i>' if k < p["k"] else "<i></i>" for k in range(n))
        piden.append('<div class="pide"><div class="num">{k}<small>de {n}</small></div><h3>{t}</h3>'
                     '<div class="puntos" aria-hidden="true">{pts}</div><p class="como">{c}</p></div>'.format(
                         k=p["k"], n=n, t=e(p["titulo"]), pts=puntos, c=p["como_html"]))

    # rutas
    NIVEL = {3: "Alcanzable", 2: "Alcanzable con preparación", 1: "Difícil", 0: "No es para egresados"}
    rutas = []
    for r in datos.get("rutas", {}).get("lista", []):
        dl = "".join("<dt>{}</dt><dd>{}</dd>".format(e(k), v) for k, v in r["datos_html"])
        rutas.append('<article class="ruta"><p class="pais">{pais}</p><h3>{t}</h3>'
                     '<p class="medidor a{a}"><span class="b"><i></i><i></i><i></i></span>{nivel}</p><dl>{dl}</dl>'
                     '<a class="mas" href="{u}" target="_blank" rel="noopener">{f} ↗</a></article>'.format(
                         pais=e(r["pais"]), t=e(r["titulo"]), a=r["alcance"], nivel=NIVEL[r["alcance"]], dl=dl,
                         u=e(r["url"]), f=e(r["fuente"])))

    # fechas
    fechas = []
    for it in items:
        f = it.get("cierre") or it.get("evento")
        if f and not it.get("sin_fecha_en_lista"):
            fechas.append((f, "Cierra" if it.get("cierre") else "", it["titulo"], it.get("org", ""), "#v-" + it["id"]))
    for v in datos.get("ventanas", []):
        fechas.append((v["fecha"], "", v["titulo"], v["nota"], v.get("url", "")))
    fechas.sort()
    fh = []
    for f, pre, t, nota, u in fechas:
        a, mm, d = map(int, f.split("-"))
        ext = u and not u.startswith("#")
        tag, cierre = ("a", "</a>") if u else ("div", "</div>")
        href = ' href="{}"{}'.format(e(u), ' target="_blank" rel="noopener"' if ext else "") if u else ""
        fh.append('<li><{tag} class="fecha" data-fecha="{f}"{href}><span class="dia"><b>{d}</b><span>{m}{an}</span></span>'
                  '<span class="que">{pre}{t}<span>{nota}</span></span><span class="faltan"></span>{c}</li>'.format(
                      tag=tag, f=f, href=href, d=d, m=MES3[mm - 1], an=" " + str(a)[2:] if a != anio else "",
                      pre=(pre + ": ") if pre else "", t=e(t), nota=e(nota), c=cierre))

    rad = datos["radar"]
    radar_cols = "".join('<div class="radar-col"><h3>{}</h3><ul>{}</ul></div>'.format(
        e(c["titulo"]), "".join("<li>{}</li>".format(x) for x in c["puntos_html"])) for c in rad["columnas"])
    cm = datos["cifra_media"]
    hoy_txt = fecha_larga(datos["actualizado"], True)

    pagina = PLANTILLA.format(
        css=css, js=js, logo=logo, fav=fav, mes_txt=mes_txt, edicion="{:02d}".format(datos["edicion"]),
        gancho=datos["gancho_html"], bajada=datos["bajada_html"], total=len(items),
        cm_valor=cm["valor"], cm_pre=cm.get("pre", ""), cm_texto=cm["texto_html"], cm_href=cm["href"],
        nav="".join(nav), destacadas="\n".join(dest), svg=svg, lugares=lugares, en_mapa=en_mapa,
        fuera_mapa=len(items) - en_mapa, intro=datos["intro_lista_html"], secciones="\n".join(secciones),
        sl_titular=datos["sueldos_titular_html"].format(n=sl["n"], q1=pesos(round(sl["q1"], -2)), q2=pesos(round(sl["q2"], -2)),
                                                       q3=pesos(round(sl["q3"], -2)), vivas=sl["vivas"]),
        sl_filas=sl["filas"], sl_refs=sl["refs"], sl_eje=sl["eje"], sl_nota=datos["sueldos_nota_html"].format(n=sl["n"]),
        piden_intro=datos["piden"]["intro_html"], piden="\n".join(piden), piden_nota=datos["piden"]["nota_html"],
        rutas_seccion=RUTAS.format(intro=datos["rutas"]["intro_html"], rutas="\n".join(rutas), alerta=datos["rutas"]["alerta_html"]) if rutas else "",
        rutas_nav='    <li><a href="#rutas">EUA y Canadá</a></li>\n' if rutas else "",
        fechas="\n".join(fh), radar_nota=e(rad["nota"]), radar_cols=radar_cols, hoy_txt=hoy_txt)
    destino = os.path.join(os.path.dirname(AQUI), "bolsa.html")
    open(destino, "w", encoding="utf-8").write(pagina)
    print("{} · {} oportunidades · {} en el mapa · {} sueldos · {:.0f} KB".format(
        destino, len(items), en_mapa, sl["n"], os.path.getsize(destino) / 1024))


RUTAS = """<section class="seccion" id="rutas" aria-labelledby="t-rutas">
  <div class="cab aparece"><p class="sobre">Sin cuentos</p><h2 id="t-rutas">Trabajar en Estados Unidos o Canadá</h2><p>{intro}</p></div>
  <div class="rutas aparece">
{rutas}
  </div>
  <div class="alerta aparece">{alerta}</div>
</section>"""

PLANTILLA = """<!DOCTYPE html>
<html lang="es">
<head>
<!--
  bolsa.html · Bolsa de trabajo PAS
  NO EDITAR A MANO. Esta página la genera _bolsa/genera.py a partir de
  _bolsa/datos/AAAA-MM.json (una vez al mes, con el skill bolsa-pas).
  La memoria de la bolsa es ese archivo de datos y el atributo data-desde
  de cada tarjeta (mes de primera publicación).
-->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bolsa de trabajo PAS · {mes_txt}</title>
<meta name="description" content="Bolsa de trabajo mensual para estudiantes y egresad@s de la Licenciatura PAS (UAQ Campus Concá): empleos, becas, apoyos y cursos del sector agropecuario y ambiental, con sueldos, distancias desde Concá y fechas de cierre.">
<meta name="theme-color" content="#1D4D77">
<link rel="icon" type="image/png" href="data:image/png;base64,{fav}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_MX">
<meta property="og:title" content="Bolsa de trabajo PAS · {mes_txt}">
<meta property="og:description" content="Empleos, becas, apoyos y cursos del sector agropecuario y ambiental. Con sueldos, distancias desde Concá y fechas de cierre.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;0,9..144,900;1,9..144,600&family=Instrument+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--logo:url(data:image/png;base64,{logo})}}
{css}
</style>
<!-- Microsoft Clarity · medición anónima de uso del sitio (proyecto soy.pas) -->
<script type="text/javascript">
  (function(c,l,a,r,i,t,y){{
    c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
    t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
    y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
  }})(window, document, "clarity", "script", "xr967ke69r");
</script>
</head>
<body>

<header class="topbar">
  <div class="topbar-inner">
    <a class="logo-pas" href="index.html" aria-label="Inicio · Licenciatura PAS"></a>
    <a class="volver" href="egresados.html">← Egresados</a>
  </div>
</header>

<section class="hero">
  <svg class="hero-ondas" viewBox="0 0 640 640" aria-hidden="true">
    <circle cx="320" cy="320" r="60"/><circle cx="320" cy="320" r="130"/><circle cx="320" cy="320" r="200"/><circle cx="320" cy="320" r="270"/><circle cx="320" cy="320" r="318"/>
    <path class="barrido" d="M320 320L320 2A318 318 0 0 0 124 70Z" fill="#9DC4E4" opacity=".16"/>
    <circle cx="320" cy="320" r="6" style="fill:#F2C14E;stroke:none"/>
  </svg>
  <div class="hero-inner">
    <p class="eyebrow"><span class="ed">N.º {edicion}</span> {mes_txt}</p>
    <h1>Bolsa de trabajo <em>PAS</em></h1>
    <p class="hero-gancho">{gancho}</p>
    <p class="hero-bajada">{bajada}</p>
    <div class="cifras">
      <a class="cifra" href="#lista"><b id="cifra-total" data-a="{total}">{total}</b><span>oportunidades abiertas hoy <span class="ir">↓</span></span></a>
      <a class="cifra" href="{cm_href}"><b data-a="{cm_valor}" data-pre="{cm_pre}">{cm_pre}{cm_valor:,}</b><span>{cm_texto} <span class="ir">↓</span></span></a>
      <a class="cifra" href="#fechas"><b id="cifra-cierran" data-a="0">0</b><span>cierran en las próximas tres semanas <span class="ir">↓</span></span></a>
    </div>
  </div>
</section>

<nav class="nav-bolsa" aria-label="Secciones de la bolsa">
  <ul>
    <li><a href="#mapa">Mapa</a></li>
    {nav}
    <li class="sep" aria-hidden="true"></li>
    <li><a href="#sueldos">Cuánto pagan</a></li>
    <li><a href="#piden">Qué piden</a></li>
{rutas_nav}    <li><a href="#fechas">Fechas</a></li>
    <li><a href="#radar">Radar</a></li>
  </ul>
</nav>

<section class="seccion" aria-labelledby="t-tres">
  <div class="cab aparece"><p class="sobre">Si solo tienes un minuto</p><h2 id="t-tres">Tres para empezar</h2></div>
  <div class="tres aparece">
{destacadas}
  </div>
</section>

<section class="seccion" id="mapa" aria-labelledby="t-mapa">
  <div class="cab aparece"><p class="sobre">Desde Concá</p><h2 id="t-mapa">¿Qué tan lejos queda?</h2>
  <p>Cada punto es un lugar con oportunidades abiertas; los anillos marcan la distancia en línea recta desde el campus. Toca un punto para ver qué hay ahí.</p></div>
  <div class="mapa-caja aparece">
    {svg}
    <div class="mapa-lista">
      <h3>De lo más cerca a lo más lejos</h3>
      <p class="nota">{en_mapa} oportunidades tienen sede en el mapa.</p>
      <ul class="lugares">
{lugares}
      </ul>
    </div>
    <p class="mapa-pie">Las otras {fuera_mapa} son en línea, de alcance nacional o están a más de 300 km: aparecen en la lista de abajo. Las distancias son en línea recta; por carretera en la Sierra, calcula bastante más.</p>
  </div>
</section>

<section class="seccion" id="lista" aria-labelledby="t-lista">
  <div class="cab aparece"><p class="sobre">Actualizada el {hoy_txt}</p><h2 id="t-lista">Todo lo que está abierto</h2>
  <p>{intro}</p></div>

<!-- BOLSA:INICIO — este bloque lo genera _bolsa/genera.py cada mes; no editar a mano -->
  <div class="filtros" role="group" aria-label="Filtrar oportunidades">
    <span class="tit">Muéstrame solo</span>
    <button type="button" class="f" data-f="recien" aria-pressed="false">Para recién egresados <span class="n"></span></button>
    <button type="button" class="f" data-f="estudiante" aria-pressed="false">Para estudiantes <span class="n"></span></button>
    <button type="button" class="f" data-f="cerca" aria-pressed="false">A menos de 130 km <span class="n"></span></button>
    <button type="button" class="f" data-f="sueldo" aria-pressed="false">Con sueldo publicado <span class="n"></span></button>
    <button type="button" class="f" data-f="pronto" aria-pressed="false">Cierran pronto <span class="n"></span></button>
    <button type="button" class="f" data-f="nuevas" aria-pressed="false">Nuevas este mes <span class="n"></span></button>
    <button type="button" class="f" data-f="guardadas" id="f-guardadas" aria-pressed="false">Mis guardadas <span class="n"></span></button>
  </div>
  <p class="f-estado" id="f-estado" aria-live="polite"></p>
{secciones}
<!-- BOLSA:FIN -->
</section>

<section class="seccion" id="sueldos" aria-labelledby="t-sueldos">
  <div class="cab aparece"><p class="sobre">Lo que nadie te dice</p><h2 id="t-sueldos">¿Cuánto pagan?</h2></div>
  <div class="panel aparece">
    <p class="sl-titular">{sl_titular}</p>
    <div class="sl">
      <div class="sl-globo" role="status"></div>
      <div class="sl-area" style="position:relative;margin:0 8px">
        <div class="sl-refs" aria-hidden="true">{sl_refs}</div>
        <div class="sl-filas">
{sl_filas}
        </div>
        <div class="sl-eje" aria-hidden="true">{sl_eje}</div>
      </div>
    </div>
    <p class="sl-leyenda"><span><i class="viva"></i>Abierta este mes: tócala para ir a la vacante</span><span><i></i>Publicada en meses anteriores</span><span><i class="rango"></i>Rango de sueldo</span></p>
    <p class="nota-fina">{sl_nota}</p>
  </div>
</section>

<section class="seccion" id="piden" aria-labelledby="t-piden">
  <div class="cab aparece"><p class="sobre">Leímos las vacantes completas</p><h2 id="t-piden">¿Qué piden?</h2><p>{piden_intro}</p></div>
  <div class="piden">
{piden}
  </div>
  <p class="nota-fina">{piden_nota}</p>
</section>

{rutas_seccion}

<section class="seccion" id="fechas" aria-labelledby="t-fechas">
  <div class="cab aparece"><p class="sobre">Que no se te pase</p><h2 id="t-fechas">Fechas que vienen</h2><p>La cuenta de días se actualiza sola cada vez que abres la página.</p></div>
  <ul class="fechas aparece">
{fechas}
  </ul>
</section>

<section class="seccion" id="radar" aria-labelledby="t-radar">
<!-- RADAR:INICIO — este bloque lo genera _bolsa/genera.py cada mes; no editar a mano -->
  <div class="radar aparece">
    <h2 id="t-radar">Radar del mes</h2>
    <p class="radar-nota">{radar_nota}</p>
    <div class="radar-cols">{radar_cols}</div>
  </div>
<!-- RADAR:FIN -->
</section>

<section class="seccion">
  <div class="aviso"><strong>Cómo funciona esta bolsa.</strong> La coordinación revisa una vez al mes portales de empleo, comités de sanidad, dependencias, universidades y empresas del sector, lee cada convocatoria completa y publica aquí lo que sirve a perfiles PAS. Todos los enlaces se comprobaron el {hoy_txt}. Las postulaciones son directas con quien convoca; la UAQ solo difunde. Si buscas plantilla de CV y consejos para tu perfil, están en <a href="egresados.html">Egresados</a>.</div>
</section>

<footer>
  <div class="pie-inner">
    <span class="logo-pas" role="img" aria-label="Logo PAS"></span>
    <div class="pie-texto">
      <strong>Licenciatura en Producción Agropecuaria Sustentable</strong><br>
      Universidad Autónoma de Querétaro · Facultad de Ciencias Naturales<br>
      Campus Concá · Sierra Gorda, Querétaro
    </div>
  </div>
  <p class="aviso-analitica">Este sitio mide de forma anónima qué páginas se consultan y en qué se hace clic, con el único fin de mejorar su contenido. No se recopila información que identifique a las personas. Las oportunidades que guardas se quedan solo en tu teléfono.</p>
</footer>

<script>
{js}
</script>
</body>
</html>
"""

if __name__ == "__main__":
    construye(sys.argv[1])
