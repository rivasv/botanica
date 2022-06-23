function cambio() {
    console.log(document.getElementById('oculto').value)
    if (document.getElementById('oculto').value == 1) {
        document.getElementById('titulo').style.color = 'white'
        document.getElementById('oculto').value = 2
    }else{
        document.getElementById('titulo').style.color = 'black'
        document.getElementById('oculto').value = 1
    }
}

function aumento() {
    var aumento = document.getElementById('letra').value
    aumento = parseInt(aumento) + 2
    document.getElementById("letra").value = aumento
    var a=String("font-size:"+ aumento )+'px'
    console.log(a)

    //document.getElementById("parrafo").align="center"
    document.getElementById("parrafo").style=a
}

function menos() {
    var aumento = document.getElementById('letra').value
    aumento = parseInt(aumento) - 2
    document.getElementById("letra").value = aumento
    var a=String("font-size:"+ aumento )+'px'
    console.log(a)

    document.getElementById("parrafo").style=a
}

// $.each(data.data.memes, function(i, item) {
$(document).ready(function() {
//  alert("trata de usar API")
    $.get("http://127.0.0.1:8000/api/suscripcion/",function(data){
        $.each(data, function(i, item) {
            $("#tabla").append("<tr><td>" 
            + item.id + "</td><td>" 
            + item.rut + "</td><td>" 
            + item.estado + "</td></tr>" );
        })
    })
});


$(document).ready(function () {
 $("#busqueda").click(function(){
    $("#resultado").val("");
    $("#estado").val("");


   var n1=parseInt($("#rutbuscar").val());
   var sum = n1
   alert("buscando via api rut :" + n1);

  // $("#resultado").val(sum);

   $.get("http://127.0.0.1:8000/api/suscripcion/?rut="+String(n1),function(data){
    $.each(data, function(i, item) {
        //$("#tabla").append("<tr><td>" 
        //+ item.id + "</td><td>" 
        //+ item.rut + "</td><td>" 
        //+ item.estado + "</td></tr>" );
        
        //var a=String(item.rut + " | " + item.estado)
        $("#resultado").val(item.rut);
        $("#estado").val(item.estado);
    })
})


});
})
