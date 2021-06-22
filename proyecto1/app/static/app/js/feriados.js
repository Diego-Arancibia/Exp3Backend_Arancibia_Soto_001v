

// API con todos los feriados

let url="https://apis.digital.gob.cl/fl/feriados"
$.get(url,function(respuesta)
{
    /*
    respuesta.forEach(function(item)
    {
        console.log(item);    
    })*/ //muestra cada item de feriados
    
    let feriado=respuesta[respuesta.length-1];
    let feriado2=respuesta[0];
    $("#feriado").text(feriado.nombre + "-" + feriado.fecha);
    $("#feriado2").text(feriado2.nombre + "-" + feriado2.fecha);
    



}, "json")

