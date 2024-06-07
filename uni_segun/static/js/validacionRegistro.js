$(document).ready(function () {
    $("#btnEnviar").click(function (event) { 
        event.preventDefault();
        var run = $("#validationCustom03").val();//validar numeros
        var numTelefono = $("#validationCustom04").val();//validar numeros
        
        var nombre = $("#validationCustom01").val(); //validar vacio
        var apellido = $("#validationCustom02").val();//validar vacio
        var academi = $("#validationCustom07").val(); //validar vacio
        var email = $("#validationCustom06").val();//validar vacio
        var contra = $("#validationCustom05").val();//validar vacio

                //validar run
                if(isNaN(run)){

                    $("#errorRun").css("visibility", "visible").css("color", "red").text("Sólo se aceptan numeros");

                }else if(run == '' ){
                    $("#errorRun").css("visibility", "visible").css("color", "red").text("Tienes rellenar este campo");
                }
                else{
                    $("#errorRun").css("visibility", "visible").css("color", "green").text("Está correcto");
                    var flag = true;

                }

                //validar numero telefono
                if(isNaN(numTelefono)){

                    $("#errorTelefono").css("visibility", "visible").css("color", "red").text("Sólo se aceptan numeros");

                }else if(numTelefono == '' ){
                    $("#errorTelefono").css("visibility", "visible").css("color", "red").text("Tienes rellenar este campo");
                }
                else{
                    $("#errorTelefono").css("visibility", "visible").css("color", "green").text("Es un numero");
                    var flag1 = true;
                }
                


                if(nombre && numTelefono && nombre && apellido && academi && email && contra && flag && flag1) { // comparo que esten llenos (true or false)
                    window.location.href = 'inicioUsuario.html'; //mando al ususario al link
                  }
    });
});