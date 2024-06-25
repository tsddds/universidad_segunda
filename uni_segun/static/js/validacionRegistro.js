$(document).ready(function () {
    $("#btnEnviar").click(function (event) { 
        event.preventDefault();
        var run = $("#validationCustom03").val(); //validar numeros
        var numTelefono = $("#validationCustom04").val(); //validar numeros
        
        var nombre = $("#validationCustom01").val(); //validar vacio
        var apellido = $("#validationCustom02").val(); //validar vacio
        var academi = $("#validationCustom07").val(); //validar vacio
        var email = $("#validationCustom06").val(); //validar vacio
        var contra = $("#validationCustom05").val(); //validar vacio

                //validar Nombre
                if(nombre == '' ){
                    $("#errorNombre").css("visibility", "visible").css("color", "red").text("Tienes rellenar este campo");
                }
                else{
                    $("#errorNombre").css("visibility", "visible").css("color", "green").text("Está correcto");
                    var flag = true;
                }

                //validar Apellido
                if (apellido == '' ){
                    $("#errorApellido").css("visibility", "visible").css("color", "red").text("Tienes rellenar este campo");
                }
                else{
                    $("#errorApellido").css("visibility", "visible").css("color", "green").text("Está correcto");
                    var flag1 = true;
                }

                //validar run
                if(run == '' ){
                    $("#errorRun").css("visibility", "visible").css("color", "red").text("Tienes rellenar este campo");
                }
                else{
                    $("#errorRun").css("visibility", "visible").css("color", "green").text("Está correcto");
                    var flag2 = true;

                }

                //validar Institucion academica
                if(academi == '' ){
                    $("#errorInstitucionAcademica").css("visibility", "visible").css("color", "red").text("Tienes rellenar este campo");
                }
                else{
                    $("#errorInstitucionAcademica").css("visibility", "visible").css("color", "green").text("Está correcto");
                    var flag3 = true;
                }                

                //validar email
                if(email == '' ){
                    $("#errorEmail").css("visibility", "visible").css("color", "red").text("Tienes rellenar este campo");
                }
                else{
                    $("#errorEmail").css("visibility", "visible").css("color", "green").text("Está correcto");
                    var flag4 = true;
                }    

                //validar contraseña
                if(contra == '' ){
                    $("#errorContraseña").css("visibility", "visible").css("color", "red").text("Tienes rellenar este campo");
                }
                else{
                    $("#errorContraseña").css("visibility", "visible").css("color", "green").text("Está correcto");
                    var flag5 = true;
                } 

                //validar numero telefono
                if(isNaN(numTelefono)){

                    $("#errorTelefono").css("visibility", "visible").css("color", "red").text("Sólo se aceptan numeros");

                }else if(numTelefono == '' ){
                    $("#errorTelefono").css("visibility", "visible").css("color", "red").text("Tienes rellenar este campo");
                }
                else{
                    $("#errorTelefono").css("visibility", "visible").css("color", "green").text("Es un numero");
                    var flag6 = true;
                }



                if(flag && flag1 && flag2 && flag3 && flag4 && flag5 && flag6 ) { // comparo que esten llenos (true or false)
                    window.location.href = 'index.html'; //mando al ususario al link
                  }
    });
});