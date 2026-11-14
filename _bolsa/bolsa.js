(function(){
  "use strict";
  var $=function(s,c){return (c||document).querySelector(s)};
  var $$=function(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s))};
  var MESES=["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"];
  var MESES_L=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"];
  var hoy=new Date(); hoy.setHours(0,0,0,0);
  function fecha(s){var p=s.split("-");return new Date(+p[0],+p[1]-1,+p[2])}
  function dias(s){return Math.round((fecha(s)-hoy)/864e5)}
  function larga(s){var d=fecha(s);return d.getDate()+" de "+MESES_L[d.getMonth()]}
  function faltan(n){return n<0?"ya pasó":n===0?"es hoy":n===1?"es mañana":"faltan "+n+" días"}

  /* 1 · Cuenta regresiva de cierres: la página se mantiene al día sola */
  var tarjetas=$$(".vacante");
  tarjetas.forEach(function(t){
    var c=t.getAttribute("data-cierre"), chip=$(".c-cierre",t);
    if(!c||!chip) return;
    var n=dias(c), verbo=chip.getAttribute("data-verbo")||"Cierra";
    if(n<0){
      t.classList.add("cerrada");
      chip.textContent=(verbo==="Es"?"Fue el ":"Cerró el ")+larga(c);
    }else if(n<=14){
      chip.classList.add("pronto");
      chip.textContent=n===0?verbo+" hoy":n===1?verbo+" mañana":verbo+" en "+n+" días";
      chip.title=larga(c);
    }
  });
  $$(".fecha").forEach(function(f){
    var c=f.getAttribute("data-fecha"), e=$(".faltan",f); if(!c) return;
    var n=dias(c);
    if(e) e.textContent=faltan(n);
    if(n<0) f.classList.add("paso"); else if(n<=14) f.classList.add("pronto");
  });
  // lo ya pasado se va al final de la lista de fechas
  $$(".fechas").forEach(function(l){$$(".fecha.paso",l).forEach(function(f){l.appendChild(f.parentNode===l?f:f.parentNode)})});

  /* 2 · Cifras de la portada, contadas en vivo */
  var vivas=tarjetas.filter(function(t){return !t.classList.contains("cerrada")});
  var porCerrar=vivas.filter(function(t){var c=t.getAttribute("data-cierre");return c&&dias(c)<=21}).length;
  var cTot=$("#cifra-total"), cCie=$("#cifra-cierran");
  if(cTot) cTot.setAttribute("data-a",vivas.length);
  if(cCie) cCie.setAttribute("data-a",porCerrar);
  function contar(el){
    var fin=+el.getAttribute("data-a"), pre=el.getAttribute("data-pre")||"", t0=null, dur=1100;
    if(window.matchMedia&&matchMedia("(prefers-reduced-motion:reduce)").matches){el.textContent=pre+fin.toLocaleString("es-MX");return}
    function paso(t){
      if(!t0) t0=t; var p=Math.min(1,(t-t0)/dur); p=1-Math.pow(1-p,3);
      el.textContent=pre+Math.round(fin*p).toLocaleString("es-MX");
      if(p<1) requestAnimationFrame(paso);
    }
    requestAnimationFrame(paso);
  }
  $$("[data-a]").forEach(contar);

  /* 3 · Aparecer al hacer scroll */
  if("IntersectionObserver" in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("visto");io.unobserve(e.target)}})},{rootMargin:"0px 0px -8% 0px"});
    $$(".aparece,.pide").forEach(function(e){io.observe(e)});
  }else{$$(".aparece,.pide").forEach(function(e){e.classList.add("visto")})}
  $$(".pide").forEach(function(p){$$(".puntos i.si",p).forEach(function(i,k){i.style.transitionDelay=(k*35)+"ms"})});

  /* 4 · Guardadas (solo en este teléfono) */
  var CLAVE="bolsa-pas-guardadas", guardadas=[];
  try{guardadas=JSON.parse(localStorage.getItem(CLAVE)||"[]")}catch(e){}
  function persistir(){try{localStorage.setItem(CLAVE,JSON.stringify(guardadas))}catch(e){}}
  function pintaGuardadas(){
    tarjetas.forEach(function(t){var b=$(".v-guardar",t); if(b){var s=guardadas.indexOf(t.id)>-1; b.setAttribute("aria-pressed",s); b.setAttribute("aria-label",s?"Quitar de guardadas":"Guardar para después")}});
    var n=tarjetas.filter(function(t){return guardadas.indexOf(t.id)>-1}).length, e=$("#f-guardadas .n");
    if(e) e.textContent=n?n:"";
  }

  /* 5 · Filtros */
  var activos={};
  var PRUEBAS={
    recien:function(t){return (t.getAttribute("data-perfil")||"").indexOf("recien")>-1},
    estudiante:function(t){return (t.getAttribute("data-perfil")||"").indexOf("estudiante")>-1},
    cerca:function(t){var k=t.getAttribute("data-km");return k!==null&&k!==""&&+k<=130},
    sueldo:function(t){return !!t.getAttribute("data-sueldo")},
    pronto:function(t){var c=t.getAttribute("data-cierre");if(!c)return false;var n=dias(c);return n>=0&&n<=21},
    nuevas:function(t){return t.hasAttribute("data-nueva")},
    guardadas:function(t){return guardadas.indexOf(t.id)>-1}
  };
  function aplicar(){
    var claves=Object.keys(activos).filter(function(k){return activos[k]}), visibles=0;
    tarjetas.forEach(function(t){
      var ok=claves.every(function(k){return PRUEBAS[k](t)});
      t.classList.toggle("fuera",!ok); if(ok) visibles++;
    });
    $$(".categoria").forEach(function(c){
      var n=$$(".vacante:not(.fuera)",c).length;
      c.classList.toggle("vacia",n===0);
      var e=$(".cat-n",c); if(e) e.textContent=n;
      var nav=$('.nav-bolsa a[href="#'+c.id+'"] .n'); if(nav) nav.textContent=n;
    });
    var est=$("#f-estado");
    if(est){
      if(!claves.length) est.innerHTML="";
      else if(!visibles) est.innerHTML="Nada coincide con esa combinación. <button type=\"button\" id=\"f-limpiar\">Quitar filtros</button>";
      else est.innerHTML="Mostrando <strong>"+visibles+"</strong> de "+tarjetas.length+". <button type=\"button\" id=\"f-limpiar\">Ver todo</button>";
      var l=$("#f-limpiar"); if(l) l.onclick=function(){activos={};$$(".f").forEach(function(b){b.setAttribute("aria-pressed","false")});aplicar()};
    }
  }
  $$(".f").forEach(function(b){
    var k=b.getAttribute("data-f"), cuenta=$(".n",b);
    if(cuenta&&k!=="guardadas") cuenta.textContent=tarjetas.filter(function(t){return !t.classList.contains("cerrada")&&PRUEBAS[k](t)}).length;
    b.addEventListener("click",function(){
      activos[k]=!activos[k]; b.setAttribute("aria-pressed",!!activos[k]); aplicar();
    });
  });
  document.addEventListener("click",function(ev){
    var g=ev.target.closest&&ev.target.closest(".v-guardar");
    if(g){
      var id=g.closest(".vacante").id, i=guardadas.indexOf(id);
      if(i>-1) guardadas.splice(i,1); else guardadas.push(id);
      persistir(); pintaGuardadas(); if(activos.guardadas) aplicar(); return;
    }
    var c=ev.target.closest&&ev.target.closest(".v-compartir");
    if(c){
      var t=c.closest(".vacante"), titulo=$("h4",t).textContent.trim(), org=$(".v-org",t).textContent.trim();
      var liga=location.origin+location.pathname+"#"+t.id;
      var texto="Mira esta oportunidad de la Bolsa PAS: "+titulo+" · "+org;
      if(navigator.share){navigator.share({title:titulo,text:texto,url:liga}).catch(function(){})}
      else{window.open("https://wa.me/?text="+encodeURIComponent(texto+" "+liga),"_blank","noopener")}
    }
  });
  pintaGuardadas();

  /* 6 · Llegar a una tarjeta por enlace (#v-…) y señalarla */
  function senalar(){
    var h=location.hash; if(!h||h.indexOf("#v-")!==0) return;
    var t=document.getElementById(h.slice(1)); if(!t) return;
    if(t.classList.contains("fuera")){activos={};$$(".f").forEach(function(b){b.setAttribute("aria-pressed","false")});aplicar()}
    t.scrollIntoView({block:"center"});
    t.classList.remove("senalada"); void t.offsetWidth; t.classList.add("senalada");
  }
  window.addEventListener("hashchange",senalar);
  setTimeout(senalar,350);

  /* 7 · Mapa: tocar un punto abre su lugar en la lista */
  var puntos=$$(".mapa-svg .pt");
  function elegir(clave,desdeMapa){
    puntos.forEach(function(p){p.classList.toggle("sel",p.getAttribute("data-l")===clave)});
    $$(".lugar").forEach(function(d){
      var es=d.getAttribute("data-l")===clave;
      if(desdeMapa) d.open=es;
      if(es&&desdeMapa){var caja=d.closest(".lugares"); if(caja) caja.scrollTop=d.offsetTop-caja.offsetTop-6}
    });
  }
  puntos.forEach(function(p){
    function ir(){elegir(p.getAttribute("data-l"),true)}
    p.addEventListener("click",ir);
    p.addEventListener("keydown",function(e){if(e.key==="Enter"||e.key===" "){e.preventDefault();ir()}});
  });
  $$(".lugar").forEach(function(d){d.addEventListener("toggle",function(){if(d.open){elegir(d.getAttribute("data-l"),false);$$(".lugar").forEach(function(o){if(o!==d)o.open=false})}})});

  /* 8 · Globo de la gráfica de sueldos */
  var globo=$(".sl-globo"), sl=$(".sl");
  if(globo&&sl){
    var ver=function(p){
      globo.innerHTML="<b>"+p.getAttribute("data-s")+"</b>"+p.getAttribute("data-t");
      var r=p.getBoundingClientRect(), b=sl.getBoundingClientRect();
      globo.classList.add("ver");
      var x=r.left-b.left+r.width/2-globo.offsetWidth/2;
      x=Math.max(0,Math.min(x,b.width-globo.offsetWidth));
      globo.style.left=x+"px"; globo.style.top=(r.top-b.top-globo.offsetHeight-8)+"px";
    };
    $$(".sl-p").forEach(function(p){
      p.addEventListener("mouseenter",function(){ver(p)});
      p.addEventListener("focus",function(){ver(p)});
      p.addEventListener("mouseleave",function(){globo.classList.remove("ver")});
      p.addEventListener("blur",function(){globo.classList.remove("ver")});
      p.addEventListener("click",function(e){if(!p.getAttribute("href")){e.stopPropagation();ver(p)}});
    });
    document.addEventListener("click",function(e){if(!(e.target.closest&&e.target.closest(".sl-p")))globo.classList.remove("ver")});
  }

  /* 9 · Barra de secciones: marca dónde vas */
  var enlaces=$$(".nav-bolsa a"), blancos=enlaces.map(function(a){return document.getElementById(a.getAttribute("href").slice(1))});
  var marcando=false;
  function marcar(){
    marcando=false;
    var y=window.scrollY+90, act=-1;
    blancos.forEach(function(b,i){if(b&&!b.classList.contains("vacia")&&b.offsetParent!==null&&b.getBoundingClientRect().top+window.scrollY<=y) act=i});
    enlaces.forEach(function(a,i){
      var es=i===act; if(a.classList.contains("activa")!==es){a.classList.toggle("activa",es); if(es&&a.scrollIntoView){var u=a.closest("ul"); u.scrollLeft=a.offsetLeft-u.clientWidth/2+a.clientWidth/2}}
    });
  }
  window.addEventListener("scroll",function(){if(!marcando){marcando=true;requestAnimationFrame(marcar)}},{passive:true});
  marcar();
})();
