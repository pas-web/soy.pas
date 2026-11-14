#!/usr/bin/env python3
"""Datos de la bolsa de noviembre de 2026. Corre: python3 arma_2026_11.py  → 2026-11.json"""
import json, os
CT = "https://mx.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-"
I = []
def add(**k): I.append(k)

# ── Empleos nuevos ──
add(id="calidad-pimientos-slpaz", cat="empleo", sector="Calidad e inocuidad", desde="2026-11",
    titulo="Supervisor de calidad · empaque de pimiento de exportación", org="Agrícola Los Pimientos (AGRIZAR)",
    lugar="San Luis de la Paz, Gto.", muni="San Luis de la Paz",
    url=CT+"supervisor-de-calidad-en-san-luis-de-la-paz-81A9334D03394A8861373E686DCF3405",
    linea="Revisas líneas, etiquetado, trazabilidad y buenas prácticas, y decides qué producto sale y cuál se retiene.",
    perfil=["recien"], exp="Pide 1 año en calidad")
add(id="linea-pimientos-slpaz", cat="empleo", sector="Agroindustria", desde="2026-11", familia="calidad",
    titulo="Coordinador de línea de producción · empaque de pimiento", org="Agrícola Los Pimientos (AGRIZAR)",
    lugar="San Luis de la Paz, Gto.", muni="San Luis de la Paz",
    url=CT+"coordinador-de-linea-de-produccion-en-san-luis-de-la-paz-0F37A5D79B1387C261373E686DCF3405",
    linea="Das seguimiento a una línea de empaque: tareas del personal, registros de producción y mermas, inventarios.",
    sueldo=[13028, 13028], perfil=["recien", "estudiante"], exp="Basta bachillerato y 6 meses")
add(id="hidroponia-jilotepec", cat="empleo", sector="Producción agrícola", desde="2026-11",
    titulo="Ingeniero agrónomo · hidroponía en invernadero", org="Finca Pombriego",
    lugar="Jilotepec, Méx.", muni="Jilotepec",
    url=CT+"ingeniero-agronomo-produccion-hidroponica-e-invernaderos-con-experiencia-en-hidroponia-en-jilotepec-8379AF1EA39C3B3461373E686DCF3405",
    linea="Llevas la producción de lechuga, espinaca, arúgula y aromáticas: soluciones nutritivas, plagas y personal.",
    perfil=["recien"], exp="Pide 1 año", chips=["Pide cambio de residencia"])
add(id="calidad-dongu-sma", cat="empleo", sector="Calidad e inocuidad", desde="2026-11",
    titulo="Analista de calidad · vegetales frescos", org="Frescos Don Gu",
    lugar="San Miguel de Allende, Gto.", muni="San Miguel de Allende",
    url=CT+"analista-de-calidad-en-san-miguel-de-allende-0AFC9586EEF0D00361373E686DCF3405",
    linea="Inspeccionas el vegetal al recibirlo y durante el empaque: muestreos, peso, etiquetado y trazabilidad.",
    perfil=["recien"], exp="Sin años mínimos", contrato="Prestaciones, comedor y transporte")
add(id="sanidad-aguilares-salamanca", cat="empleo", sector="Sanidad vegetal", desde="2026-11",
    titulo="Especialista de sanidad vegetal · invernaderos orgánicos", org="Aguilares",
    lugar="Salamanca, Gto.", muni="Salamanca",
    url=CT+"especialista-de-sanidad-vegetal-invernaderos-de-produccion-organicos-aguilares-en-salamanca-3355246B2C0B4B6561373E686DCF3405",
    linea="Coordinas el control de plagas, el control biológico, la polinización con abejorros y el clima del invernadero.",
    perfil=["experiencia"], exp="Pide 2 años", chips=["Pide vehículo propio"])
add(id="plantula-aguilares-villagran", cat="empleo", sector="Producción agrícola", desde="2026-11",
    titulo="Coordinador de producción · invernaderos de plántula", org="Aguilares",
    lugar="Villagrán, Gto.", muni="Villagrán",
    url=CT+"coordinador-de-produccion-invernaderos-de-plantula-en-villagran-398F24F661C35F1261373E686DCF3405",
    linea="Coordinas la producción de plántula: calidad, inocuidad, rendimientos, presupuesto y personal a cargo.",
    perfil=["experiencia"], exp="Pide 2 años")
add(id="grower-santodomingo", cat="empleo", sector="Producción agrícola", desde="2026-11",
    titulo="Grower Jr. · pimiento en invernadero de alta tecnología", org="Agrícola Santo Domingo",
    lugar="San Francisco del Rincón, Gto.", muni="San Francisco del Rincón",
    url=CT+"grower-jr-en-san-francisco-del-rincon-3C7579316354CBA461373E686DCF3405",
    linea="Planeas las labores del cultivo y ejecutas las estrategias de clima, riego, nutrición y manejo de plagas.",
    perfil=["experiencia"], exp="Pide 2 años en pimiento")
add(id="inspector-herdez-slp", cat="empleo", sector="Calidad e inocuidad", desde="2026-11", familia="calidad",
    titulo="Inspector de control de calidad · planta de alimentos", org="Grupo Herdez",
    lugar="San Luis Potosí, S.L.P.", muni="San Luis Potosí",
    url=CT+"inspector-control-de-calidad-herdez-slp-en-san-luis-potosi-9561A6EA870D149C61373E686DCF3405",
    linea="Recorres piso para asegurar calidad e inocuidad del proceso, con análisis microbiológicos y documentación.",
    sueldo=[11550, 11550], perfil=["recien"], exp="Pide 6 meses", contrato="Prestaciones superiores a las de ley", chips=["Tres turnos"])
add(id="supervisor-herdez-slp", cat="empleo", sector="Agroindustria", desde="2026-11", familia="calidad",
    titulo="Supervisor de producción · planta de alimentos", org="Grupo Herdez",
    lugar="San Luis Potosí, S.L.P.", muni="San Luis Potosí",
    url=CT+"supervisor-de-produccion-planta-herdez-slp-en-san-luis-potosi-4CD102685FE6321E61373E686DCF3405",
    linea="Supervisas una línea de producción: personal, programa semanal, indicadores e inocuidad.",
    sueldo=[14000, 14000], perfil=["recien"], exp="Pide de 6 meses a 1 año", contrato="Prestaciones superiores a las de ley", chips=["Tres turnos"])
add(id="materiales-capistrano-celaya", cat="empleo", sector="Calidad e inocuidad", desde="2026-11", familia="calidad",
    titulo="Inspector de materiales · calidad en planta cárnica", org="Grupo Alimentario Capistrano",
    lugar="Celaya, Gto.", muni="Celaya",
    url=CT+"inspector-de-materiales-calidad-en-celaya-221BF994B0C1295661373E686DCF3405",
    linea="Inspeccionas en recepción la materia prima, los empaques y los aditivos, y documentas las desviaciones.",
    sueldo=[12000, 12000], perfil=["recien"], exp="Sin años mínimos", chips=["Dos turnos"])
add(id="linea-sigma-penjamo", cat="empleo", sector="Calidad e inocuidad", desde="2026-11",
    titulo="Inspector de línea · producción de cárnicos", org="Sigma",
    lugar="Pénjamo, Gto.", muni="Pénjamo",
    url=CT+"inspector-de-linea-produccion-giro-carnico-en-penjamo-0C7B2553BA095EB561373E686DCF3405",
    linea="Revisas buenas prácticas al arranque y al cierre, tomas muestras de producto terminado y reportas anomalías.",
    perfil=["recien"], exp="Tus prácticas cuentan como experiencia", contrato="Prestaciones de ley", chips=["Rola turnos"])
add(id="areas-verdes-tultitlan", cat="empleo", sector="Manejo ambiental", desde="2026-11", familia="produccion",
    titulo="Biólogo o agrónomo · supervisor de áreas verdes", org="Arquitectura, Vegetación y Paisaje",
    lugar="Tultitlán, Méx.", muni="Tultitlán",
    url=CT+"biologo-o-agronomo-supervisor-de-areas-verdes-con-experiencia-en-tultitlan-DFD9D5B8E4BC6C7761373E686DCF3405",
    linea="Supervisas el mantenimiento de las áreas verdes de una planta industrial: personal, programa, inventarios.",
    sueldo=[15000, 15000], perfil=["recien"], exp="Pide 1 año")
# ── Empleos que siguen de octubre ──
add(id="agronomo-apaseo", cat="empleo", sector="Producción agrícola", desde="2026-10",
    titulo="Ingeniero agrónomo · plántula de hortalizas en invernadero", org="AGROGUANAJUATO",
    lugar="Apaseo el Grande, Gto.", muni="Apaseo el Grande",
    url=CT+"ingeniero-agronomo-en-apaseo-el-grande-F8849C59FECDFC7561373E686DCF3405",
    linea="Producción de plántula en invernadero. La empresa actualizó la vacante esta semana.",
    perfil=["recien"], exp="Pide 1 año", contrato="Vales de despensa y bonos")
add(id="granjas-bachoco-celaya", cat="empleo", sector="Producción pecuaria", desde="2026-10", familia="pecuario",
    titulo="Supervisor de limpieza y sanitización de granjas", org="Grupo Bachoco",
    lugar="Celaya, Gto.", muni="Celaya",
    url=CT+"supervisor-de-limpieza-granjas-en-celaya-8F81D29BD44FADA561373E686DCF3405",
    linea="Mantienes el estándar de limpieza de las granjas: cuadrillas, presupuestos, proveedores y transporte.",
    sueldo=[19199, 19199], perfil=["experiencia"], exp="Pide 2 años y licencia")
add(id="agronomo-educativo-corregidora", cat="empleo", sector="Extensión rural", desde="2026-10",
    titulo="Ingeniero agrónomo con vocación educativa", org="Corporativo JM",
    lugar="Corregidora, Qro.", muni="Corregidora",
    url=CT+"ingeniero-agronomo-titulado-en-corregidora-ADE7B8C6FEBE2DE161373E686DCF3405",
    linea="Desarrollas proyectos educativos de agronomía y agricultura sostenible con aprendizaje práctico.",
    perfil=["recien"], exp="Pide menos de 1 año y título")
add(id="inocuidad-sunnyfields-colon", cat="empleo", sector="Calidad e inocuidad", desde="2026-10",
    titulo="Coordinador de calidad e inocuidad · invernadero", org="Sunny Fields",
    lugar="Colón, Qro.", muni="Colón",
    url=CT+"coordinador-de-calidad-e-inocuidad-en-colon-39B07BEE8F5DADD661373E686DCF3405",
    linea="Mantienes el sistema de gestión: documentación, auditorías internas, capacitación e indicadores.",
    perfil=["recien"], exp="Sin años mínimos", chips=["Pide cambio de residencia"])

# ── Becas y primer empleo ──
add(id="beca-secihti", cat="beca", sector="Beca de posgrado", desde="2026-08",
    titulo="Beca Nacional para Estudios de Posgrado 2026", org="SECIHTI", lugar="nacional",
    url="https://secihti.mx/convocatoria/becas-nacionales/convocatoria-de-becas-nacionales-para-estudios-de-posgrado-2026/",
    linea="La beca mensual que te sostiene mientras estudias una maestría o doctorado de tiempo completo en México.",
    monto="$16,048", monto_nota="al mes en maestría · $21,397 en doctorado", perfil=["recien"], cierre="2026-11-28")
add(id="maestria-ecosur", cat="beca", sector="Posgrado con beca", desde="2026-10",
    titulo="Maestría en Recursos Naturales y Desarrollo Rural · 2027", org="El Colegio de la Frontera Sur",
    lugar="Chiapas, Tabasco, Campeche y Quintana Roo",
    url="https://www.ecosur.mx/posgrado/convocatoria-de-admision-al-programa-de-maestria-en-ciencias-en-recursos-naturales-y-desarrollo-rural-generacion-2027-2029/",
    linea="Dos años en un centro público de investigación. El registro en línea abrió el 13 de noviembre.",
    monto="$16,048", monto_nota="al mes con la beca SECIHTI, si te admiten", perfil=["recien"], cierre="2027-02-18")
add(id="fulbright", cat="beca", sector="Posgrado en el extranjero", desde="2026-11",
    titulo="Beca Fulbright-García Robles · maestría o doctorado en Estados Unidos", org="COMEXUS", lugar="para iniciar en agosto de 2028",
    url="https://www.comexus.org.mx/becas_para_mexicanos/fulbright_garcia_robles",
    linea="Se planea con un año de anticipación: pide inglés certificado (TOEFL 80, IELTS 6.5 o Duolingo 120) y examen GRE.",
    perfil=["recien"], cierre="2027-01-15")
add(id="practicante-munsa-slp", cat="beca", sector="Práctica pagada", desde="2026-11",
    titulo="Practicante de calidad · laboratorio de un molino", org="Munsa Molinos",
    lugar="San Luis Potosí, S.L.P.", muni="San Luis Potosí",
    url=CT+"practicante-de-calidad-alimenticio-en-san-luis-potosi-6B5E633D5D5516E761373E686DCF3405",
    linea="Análisis de laboratorio y control documental, de 10:00 a 15:00. Pide seguro facultativo vigente.",
    monto="$6,000", monto_nota="al mes de beca", perfil=["estudiante"])
add(id="becario-agronegocios", cat="beca", sector="Práctica pagada", desde="2026-11",
    titulo="Becario de agronegocios · crédito al campo en un banco", org="INROADS con Santander",
    lugar="Guadalajara, Jal.",
    url="https://vacantes.inroads.org.mx/job/becario-de-agronegocios-2/",
    linea="Medio tiempo, de lunes a viernes de 9:00 a 14:00. Antes hay que registrarse en el programa INROADS.",
    monto="$10,000", monto_nota="brutos al mes, medio tiempo", perfil=["estudiante", "recien"])

# ── Apoyos ──
add(id="apoyo-sedea-penamiller", cat="apoyo", sector="Apoyo para tu parcela", desde="2026-11",
    titulo="Apoyo al Campo Queretano · proyectos en Peñamiller", org="SEDEA Querétaro y Municipio de Peñamiller",
    lugar="Peñamiller, Qro.", muni="Peñamiller",
    url="https://queretaro.gob.mx/documents/828910/1649708/CONVO-PET-PENAMILLER_2026.pdf/20a9ff6e-ae13-7e92-5d03-83daa34704d1?t=1794510863549",
    linea="Subsidio para comprar equipo, implementos, animales o plantas. Ventanilla en la Dirección de Desarrollo Agropecuario del municipio.",
    monto="Hasta 66 %", monto_nota="del costo · topes de $25,000 a $125,000", perfil=["recien", "estudiante"],
    chips=["O hasta agotar el recurso"], cierre="2026-11-23")
add(id="agentes-cambio-gto", cat="apoyo", sector="Extensión rural", desde="2026-10",
    titulo="Agentes de cambio en comercialización agroalimentaria", org="Secretaría del Campo de Guanajuato", lugar="Guanajuato",
    url="https://secam.guanajuato.gob.mx/contenido/adjuntos/convocatorias/2026/Convocatoria_Agentes_de_Cambio_2026_0001.pdf",
    linea="Acompañas a un grupo de productores en lo organizativo, fiscal y comercial. La organización te propone y recibe el apoyo.",
    monto="$20,000 a $25,000", monto_nota="al mes por agente", perfil=["recien"],
    chips=["Con título o carta pasante", "Sin fecha de cierre: pregunta si queda cupo"])
add(id="cosechando-soberania", cat="apoyo", sector="Financiamiento", desde="2026-08",
    titulo="Cosechando Soberanía · crédito con acompañamiento", org="SADER y FIRA", lugar="nacional",
    url="https://www.fira.gob.mx/Nd/pagCosechandoSoberania.jsp",
    linea="Crédito de tasa baja con seguro y asistencia técnica para pequeños y medianos productores de alimentos básicos.",
    perfil=[], permanente=True)

# ── Capacitaciones ──
add(id="taller-suelo-uaq", cat="curso", sector="Taller presencial", desde="2026-11",
    titulo="Taller de indicadores de calidad del suelo · carbono, agua y biodiversidad", org="UAQ, Facultad de Ciencias Naturales, con UNAM Juriquilla",
    lugar="Juriquilla, Qro.", muni="Querétaro",
    url="https://fcn.uaq.mx/index.php/convocatorias/proxima/2498-taller-indicadores-calidad-suelo",
    linea="Cuatro días midiendo la salud del suelo en campo y laboratorio, del 25 al 28 de noviembre.",
    monto="Cuesta $2,500", monto_nota="para estudiantes", perfil=["estudiante", "recien"], evento="2026-11-25", evento_txt="Empieza el 25 de noviembre")
add(id="fira-extensionismo", cat="curso", sector="Curso en línea", desde="2026-09",
    titulo="Modelo de extensionismo de productor a productor", org="FIRA", lugar="virtual",
    url="https://www.fira.gob.mx/CursosSeminariosXML/DetalleCurso.jsp?op=1733",
    linea="Cómo organizar el intercambio de técnicas entre productores, con la metodología campesino a campesino.",
    monto="Gratuito", perfil=["estudiante", "recien"], evento="2026-11-27")
add(id="habilidad-qgis", cat="curso", sector="Habilidad del mes", desde="2026-11",
    titulo="Aprende a hacer mapas con QGIS", org="Proyecto QGIS", lugar="manual oficial en español",
    url="https://docs.qgis.org/latest/es/docs/training_manual/index.html",
    linea="Curso paso a paso, a tu ritmo. Termínalo con un mapa de tu parcela o tu comunidad y ponlo en tu CV.",
    monto="Gratuito", perfil=["estudiante", "recien"], permanente=True)
add(id="kobotoolbox", cat="curso", sector="Herramienta de campo", desde="2026-11",
    titulo="Levanta datos en campo con el celular, sin señal", org="KoboToolbox", lugar="guías oficiales en español",
    url="https://support.kobotoolbox.org/es/",
    linea="Diseñas tu encuesta, la llenas en la parcela sin internet y los datos suben solos cuando hay señal.",
    monto="Gratuito", perfil=["estudiante", "recien"], permanente=True)
add(id="sinavef", cat="curso", sector="Cursos en línea", desde="2026-09",
    titulo="Cursos de vigilancia fitosanitaria con constancia", org="SENASICA y SINAVEF", lugar="en línea",
    url="https://sinavef.senasica.gob.mx/pvefeduc/",
    linea="Plagas, muestreo y trampeo: los temas del examen técnico que aplican los comités de sanidad.",
    monto="Gratuito", perfil=["estudiante", "recien"], permanente=True)
add(id="fao-elearning", cat="curso", sector="Cursos en línea", desde="2026-08",
    titulo="FAO elearning Academy", org="FAO", lugar="en línea, en español",
    url="https://elearning.fao.org/?lang=es",
    linea="Agroecología, suelos, agua, clima e inocuidad, con insignia digital al terminar.",
    monto="Gratuito", perfil=["estudiante", "recien"], permanente=True)

# ── Convocatorias y registros ──
add(id="vigila-cesaveq", cat="registro", sector="Vigila esta página", desde="2026-11",
    titulo="Convocatorias del Comité de Sanidad Vegetal de Querétaro", org="CESAVEQ", lugar="Querétaro",
    url="https://cesaveq.org.mx/convocatorias",
    linea="Aquí salen las plazas de auxiliar de campo y profesional de proyecto. Duran una semana: revísala cada lunes.",
    perfil=["recien", "estudiante"], chips=["Hoy sin plazas abiertas"])
add(id="vigila-cesaveg", cat="registro", sector="Vigila esta página", desde="2026-11",
    titulo="Convocatorias del Comité de Sanidad Vegetal de Guanajuato", org="CESAVEG", lugar="Irapuato, Gto.",
    url="https://www.cesaveg.org.mx/convocatorias.php",
    linea="El comité que más publicó este otoño: auxiliar de inocuidad ($15,000) y profesional de frutillas ($21,000).",
    perfil=["recien", "estudiante"], chips=["La última cerró el 13 de noviembre"])
add(id="vigila-cesaveslp", cat="registro", sector="Vigila esta página", desde="2026-11",
    titulo="Convocatorias del Comité de Sanidad Vegetal de San Luis Potosí", org="CESAVE S.L.P.", lugar="Zona Media y Huasteca",
    url="http://www.cesaveslp.org.mx/Conv_2026.html",
    linea="En octubre contrató auxiliar de campo en Lagunillas, vecino de Arroyo Seco: $15,500 con bachillerato y 6 meses.",
    perfil=["recien", "estudiante"], chips=["Hoy sin plazas abiertas"])
add(id="vigila-conanp", cat="registro", sector="Vigila esta página", desde="2026-11",
    titulo="Plazas de la CONANP · Servicio Profesional de Carrera", org="Comisión Nacional de Áreas Naturales Protegidas", lugar="nacional",
    url="https://spc.conanp.gob.mx/ingreso.php",
    linea="En octubre abrió técnico operativo con sede en Querétaro: $16,701 brutos, acepta pasantes y pide 2 años.",
    perfil=["experiencia"], chips=["Se postula por trabajaen.gob.mx"])
add(id="bolsa-uaq", cat="registro", sector="Registro", desde="2026-08",
    titulo="Bolsa de Trabajo UAQ · regístrate como egresado", org="Universidad Autónoma de Querétaro", lugar="",
    url="https://www.uaq.mx/informatica/BolsaDeTrabajoUAQ/",
    linea="Vacantes de las empresas registradas ante la universidad.", perfil=["recien", "estudiante"], permanente=True)
add(id="guardianes-bosques", cat="registro", sector="Voluntariado", desde="2026-09",
    titulo="Guardianes de los Bosques Mexiquenses", org="PROBOSQUE", lugar="Estado de México",
    url="https://probosque.edomex.gob.mx/sites/probosque.edomex.gob.mx/files/files/convocatorias/2026/ConvocatoriaGuardianesBosqMexiq/convocaGuardianesBosquesMexiqPbq202601.pdf",
    linea="Voluntariado sin pago en reforestaciones y eventos forestales, con capacitación.",
    perfil=["estudiante"], cierre="2026-11-30")

H = lambda fam, lo, hi, t, o, mes: dict(familia=fam, sueldo=[lo, hi], titulo=t, org=o, mes=mes)
HIST = [
 # comités y sector público
 H("publico", 15000, 15000, "Auxiliar de campo de inocuidad", "CESAVEG, Irapuato", "noviembre (ya cerró)"),
 H("publico", 21000, 21000, "Profesional de proyecto, frutillas", "CESAVEG, Irapuato", "noviembre (ya cerró)"),
 H("publico", 18000, 18000, "Técnico de capacitación y divulgación", "CESAVEG, Irapuato", "noviembre (ya cerró)"),
 H("publico", 15000, 15000, "Auxiliar de campo de inocuidad", "CESAVEH, Hidalgo", "noviembre (ya cerró)"),
 H("publico", 20500, 20500, "Profesional de proyecto de inocuidad", "CESAVEH, Hidalgo", "noviembre (ya cerró)"),
 H("publico", 14000, 14000, "Auxiliar de campo, movilización pecuaria", "Comité pecuario de Hidalgo", "octubre"),
 H("publico", 15500, 15500, "Auxiliar de campo, moscas de la fruta", "CESAVE S.L.P., Lagunillas", "octubre"),
 H("publico", 15000, 15000, "Auxiliar de campo, aguacate", "CESAVEM, Coatepec Harinas", "octubre"),
 H("publico", 16701, 16701, "Técnico operativo de área natural protegida", "CONANP, Querétaro", "octubre"),
 H("publico", 19500, 19500, "Profesional de proyecto, brucelosis (pide MVZ)", "Comité pecuario de Querétaro", "octubre"),
 H("publico", 13500, 13500, "Auxiliar técnico de centro de acopio", "CESAVEQ, El Marqués", "septiembre"),
 H("publico", 19000, 19000, "Profesional de proyecto, plagas de los cítricos", "CESAVE S.L.P.", "septiembre"),
 H("publico", 15500, 15500, "Auxiliar de campo, plagas de los cítricos", "CESAVE S.L.P., Tamazunchale", "septiembre"),
 # calidad e inocuidad
 H("calidad", 14500, 14500, "Inspector de calidad de perecederos", "Walmart, El Marqués", "septiembre"),
 H("calidad", 17000, 23000, "Encargado de inocuidad", "Agricultores El Fuerte, Pedro Escobedo", "agosto"),
 H("calidad", 13322, 13322, "Inspector de calidad", "Irapuato", "noviembre (no entró a la bolsa)"),
 H("calidad", 14000, 14000, "Analista de aseguramiento de calidad", "Viren, Querétaro", "noviembre (no entró a la bolsa)"),
 H("calidad", 12000, 12000, "Analista de laboratorio", "Irapuato", "noviembre (no entró a la bolsa)"),
 H("calidad", 13244, 13244, "Auditor de calidad, planta de alimentos", "Chalco, Méx.", "noviembre (no entró a la bolsa)"),
 H("calidad", 16000, 16000, "Jefe de sistema de gestión de calidad", "Plantecnia, León", "noviembre (no entró a la bolsa)"),
 H("calidad", 24720, 24720, "Supervisor de calidad (pide 2 años)", "El Marqués, Qro.", "noviembre (no entró a la bolsa)"),
 H("calidad", 25000, 25000, "Gerente de calidad e inocuidad (pide 5 años)", "Irapuato", "noviembre (no entró a la bolsa)"),
 # producción
 H("produccion", 13000, 13000, "Supervisor de producción de champiñón", "El Encinal, Santa María Rayón", "agosto"),
 H("produccion", 8000, 12000, "Supervisor de producción", "La Campiña, Santa Elena, Gto.", "agosto"),
 H("produccion", 10200, 10200, "Auxiliar para rancho, recién egresados", "Poliservicios, San Luis Potosí", "septiembre"),
 H("produccion", 15000, 15000, "Inspector de ciclo de cultivo", "PORTIKA, Huimilpan", "septiembre"),
 H("produccion", 17200, 17200, "Técnico de investigación y desarrollo", "FEMSSA, El Marqués", "septiembre"),
 H("produccion", 40000, 43000, "Gerente Jr. de aplicaciones foliares", "Wonderful Citrus, Ciudad Valles", "agosto"),
 # pecuario
 H("pecuario", 17000, 17000, "Analista de embriología, planta incubadora", "Pilgrim's, El Marqués", "octubre"),
 H("pecuario", 19000, 19000, "Supervisor de limpieza, granja de cerdos (pide 3 años)", "Bachoco, Celaya", "noviembre (no entró a la bolsa)"),
 H("pecuario", 22000, 22000, "Supervisor de producción, planta de alimentos (pide 3 años)", "Avigrupo, Tizayuca", "noviembre (no entró a la bolsa)"),
 # asesoría y ventas técnicas
 H("asesoria", 16000, 18000, "Generador de demanda en nutrición vegetal", "MAS Agroquímicos, Celaya", "septiembre"),
 H("asesoria", 20000, 25000, "Agente de cambio en comercialización", "Secretaría del Campo de Guanajuato", "octubre"),
 H("asesoria", 35000, 35000, "Representante técnico comercial de agroinsumos", "Agricam, Toluca", "agosto"),
 H("asesoria", 16500, 16500, "Ejecutivo de ventas de alimento balanceado", "Bachoco, Ezequiel Montes", "noviembre (no entró a la bolsa)"),
 H("asesoria", 19000, 19000, "Ejecutivo de ventas (pide 1 año)", "Bachoco, San Miguel de Allende", "noviembre (no entró a la bolsa)"),
 H("asesoria", 25000, 25000, "Ingeniero agrónomo, gerente de ventas (pide 5 años)", "Villa de Arista, S.L.P.", "noviembre (no entró a la bolsa)"),
]

D = dict(
 mes="2026-11", edicion=4, actualizado="2026-11-13", items=I,
 gancho_html="¿Cuánto paga el campo a quien acaba de egresar? Este mes, entre <b>$11,550</b> y <b>$15,000</b>.",
 bajada_html="Leímos una por una más de cien vacantes y convocatorias. Aquí está lo que sirve a un perfil PAS, con su sueldo, qué tan lejos queda de Concá y cuándo cierra.",
 cifra_media=dict(valor=19199, pre="$", texto_html="el sueldo más alto publicado este mes", href="#sueldos"),
 notas_categoria=dict(
  empleo="Querétaro, Guanajuato, San Luis Potosí y Estado de México. Este mes no encontramos empleo del sector dentro de la Sierra Gorda: lo más cercano está en San Luis de la Paz.",
  beca="Posgrados con beca y prácticas pagadas para quien estudia o apenas egresa.",
  apoyo="Dinero y asesoría pagada para echar a andar o fortalecer un proyecto productivo, propio o de tu familia.",
  curso="Casi todo en línea y sin costo. Cada uno deja algo que puedes poner en tu CV.",
  registro="Páginas donde las plazas aparecen y desaparecen en días. Guárdalas y revísalas cada semana."),
 destacadas=[
  dict(id="calidad-pimientos-slpaz", lema="El empleo más cerca de casa", grande_html="{km} <small>km de Concá</small>"),
  dict(id="areas-verdes-tultitlan", lema="La mejor pagada pidiendo un año o menos", grande_html="$15,000 <small>al mes</small>"),
  dict(id="apoyo-sedea-penamiller", lema="Cierra primero, y es en la Sierra", grande_html="23 <small>de noviembre</small>"),
 ],
 intro_lista_html="Cada tarjeta dice para quién es, cuánto paga, qué tan lejos queda y cuándo cierra. Guarda las que te interesen o mándaselas a alguien.",
 familias=[["publico", "Comités de sanidad y sector público"], ["calidad", "Calidad, inocuidad y agroindustria"],
           ["produccion", "Producción en campo e invernadero"], ["pecuario", "Producción pecuaria"],
           ["asesoria", "Asesoría técnica y ventas a productores"]],
 historico_sueldos=HIST,
 referencias_sueldo=[
  dict(valor=9582, texto_html="Salario mínimo<br>$9,582", alto=0, color="#4A5A53"),
  dict(valor=16048, texto_html="Beca de maestría<br>$16,048", alto=0, color="#1D4D77")],
 sueldos_titular_html="De {n} sueldos publicados que hemos leído desde agosto, <b>la mitad cae entre {q1} y {q3}</b> al mes.",
 sueldos_nota_html="Son los sueldos mensuales tal como los publicó cada empleador en {n} vacantes de Querétaro, Guanajuato, San Luis Potosí, Hidalgo y Estado de México, de agosto a noviembre de 2026. Los comités de sanidad publican sueldo bruto; los portales de empleo casi nunca dicen si es bruto o neto. La mayoría de las vacantes no publica sueldo, así que esto es una referencia y no un promedio del sector. Dos vacantes de más de $26,000 quedan fuera del eje, marcadas con una flecha.",
 piden=dict(n=94,
  intro_html="Este mes leímos 94 vacantes agroalimentarias de la región. Cada punto es una vacante; los verdes son las que lo piden.",
  nota_html="Conteo sobre 94 fichas de Computrabajo leídas del 13 de noviembre de 2026. En 83 de ellas los requisitos se detectaron por palabras clave en el texto de la ficha, así que las cifras son aproximadas.",
  lista=[
   dict(k=28, titulo="Un año o menos de experiencia", como_html="Otras 23 no fijan años. Sigma y el comité de sanidad del Estado de México cuentan las prácticas profesionales como experiencia: ponlas en tu CV con fechas y funciones."),
   dict(k=42, titulo="Inocuidad: buenas prácticas, HACCP o certificaciones", como_html="Es lo más pedido. Empieza con los cursos gratuitos de <a href=\"#v-sinavef\">SINAVEF</a> y de la <a href=\"#v-fao-elearning\">FAO</a>, que dan constancia."),
   dict(k=35, titulo="Excel y paquetería de oficina", como_html="Te lo van a probar con registros de producción e inventarios. Practica tablas dinámicas y fórmulas con tus propios datos de prácticas."),
   dict(k=35, titulo="Manejo de personal", como_html="¿Coordinaste una brigada, un equipo de servicio social o una cuadrilla en prácticas? Eso cuenta: dilo con número de personas."),
   dict(k=31, titulo="Licencia de conducir", como_html="Una de cada tres la pide y varias suman vehículo propio. Tramítala antes de egresar: sin ella muchas puertas de campo no se abren."),
   dict(k=10, titulo="Inglés", como_html="Solo una de cada nueve lo pide, pero es requisito para becas como <a href=\"#v-fulbright\">Fulbright</a>."),
  ]),
 radar=dict(nota="Lo que nos dejó el escaneo de noviembre de 2026.", columnas=[
  dict(titulo="A quién seguir", puntos_html=[
   "<strong>Los comités de sanidad.</strong> Contratan auxiliares de campo desde pasante por $14,000 a $15,500 brutos, y profesionales de proyecto por $19,500 a $21,000. Sus convocatorias duran una semana: hay que vigilarlas.",
   "<strong>Agrícola Los Pimientos (AGRIZAR).</strong> Es el empleador agrícola con vacantes más cercano a la Sierra: tres puestos este mes entre San Luis de la Paz y Silao.",
   "<strong>CIMMYT.</strong> Publicó en noviembre dos plazas técnicas de reclutamiento local: <a href=\"https://www.cgiar.org/careers/m26363-ayudante-de-invernaderos-reclutada-localmente\" target=\"_blank\" rel=\"noopener\">ayudante de invernaderos</a> y <a href=\"https://www.cgiar.org/careers/m26366-asistente-principal-de-laboratorio-localmente-reclutado\" target=\"_blank\" rel=\"noopener\">asistente de laboratorio</a>. No dicen sede ni sueldo: pregúntalo al postular."]),
  dict(titulo="Se mueve en el sector", puntos_html=[
   "<strong>La puerta de entrada es la calidad.</strong> De las vacantes de este mes que aceptan a recién egresados, la mayoría son de inspección, calidad e inocuidad en empaques y plantas de alimentos.",
   "<strong>Dentro de la Sierra Gorda, los portales no traen empleo del sector.</strong> En Jalpan, Pinal, Cadereyta, Rioverde y Xilitla solo aparecen ventas, banca y telefonía. Lo que sí hay son apoyos, como el de SEDEA en Peñamiller.",
   "<strong>Jóvenes Construyendo el Futuro sigue sin fecha.</strong> La plataforma oficial dice «próximo inicio de postulaciones: por anunciar»."]),
  dict(titulo="Fortalece tu CV", puntos_html=[
   "<strong>Un curso de inocuidad con constancia</strong>, porque lo piden 42 de 94 vacantes.",
   "<strong>Tus prácticas, contadas como experiencia</strong>: empresa, meses, funciones y a cuántas personas coordinaste.",
   "<strong>Un mapa hecho por ti en QGIS</strong>, la habilidad del mes: pocas vacantes lo piden todavía, y por eso distingue."]),
 ]),
)
dst = os.path.join(os.path.dirname(os.path.abspath(__file__)), "2026-11.json")
json.dump(D, open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(dst, len(I), "oportunidades")
