#!/usr/bin/env python3
"""Proyecta los contornos de los estados alrededor de Concá y los guarda
simplificados en mapa.json. Solo se corre si cambia el alcance del mapa.
Uso: python3 prepara_mapa.py estados.geojson   (GeoJSON de estados de México)
"""
import json, math, sys, os
CONCA = (21.4467, -99.6356)   # Concá, Arroyo Seco, Qro.
RADIO_KM = 330
REGION = {"Querétaro", "Guanajuato", "San Luis Potosí", "Hidalgo", "México"}

def proyecta(lat, lon, c=CONCA):
    """Acimutal equidistante centrada en Concá: devuelve (x, y) en km."""
    la1, lo1, la2, lo2 = map(math.radians, (c[0], c[1], lat, lon))
    dlo = lo2 - lo1
    a = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin(dlo/2)**2
    d = 6371.0 * 2 * math.asin(math.sqrt(a))
    y = math.sin(dlo)*math.cos(la2)
    x = math.cos(la1)*math.sin(la2) - math.sin(la1)*math.cos(la2)*math.cos(dlo)
    t = math.atan2(y, x)
    return d*math.sin(t), -d*math.cos(t)

def simplifica(p, tol):
    if len(p) < 3: return p
    (x1, y1), (x2, y2) = p[0], p[-1]
    dx, dy = x2-x1, y2-y1; n = math.hypot(dx, dy) or 1e-9
    imax, dmax = 0, 0
    for i in range(1, len(p)-1):
        d = abs(dy*(p[i][0]-x1) - dx*(p[i][1]-y1))/n
        if d > dmax: imax, dmax = i, d
    if dmax <= tol: return [p[0], p[-1]]
    return simplifica(p[:imax+1], tol)[:-1] + simplifica(p[imax:], tol)

def main(src):
    sys.setrecursionlimit(100000)
    g = json.load(open(src, encoding="utf-8"))
    out = []
    for f in g["features"]:
        nombre = f["properties"].get("name") or f["properties"].get("state_name")
        geom = f["geometry"]
        polis = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
        caminos = []
        for poli in polis:
            anillo = [proyecta(lat, lon) for lon, lat in poli[0]]
            if min(math.hypot(x, y) for x, y in anillo) > RADIO_KM*1.15: continue
            mitad = len(anillo)//2
            s = simplifica(anillo[:mitad+1], 2.2)[:-1] + simplifica(anillo[mitad:], 2.2)
            if len(s) >= 4:
                caminos.append([[round(x, 1), round(y, 1)] for x, y in s])
        if caminos:
            out.append({"nombre": nombre, "region": nombre in REGION, "caminos": caminos})
    dst = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mapa.json")
    json.dump({"centro": CONCA, "radio_km": RADIO_KM, "estados": out}, open(dst, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print(dst, os.path.getsize(dst), "bytes;", [(e["nombre"], sum(len(c) for c in e["caminos"])) for e in out])

if __name__ == "__main__":
    main(sys.argv[1])
