$(document).ready(function(){
    $('#loginForm').submit(function(event) {
      
      event.preventDefault(); // Evita que el coso del formualrio se envíe por defecto (que no se recargue la pagina)
      
      var email = $('#txtCorreo').val(); // capturo ambos campos de txt
      var password = $('#inputPassword').val();
      
      if(email && password) { // comparo que esten llenos (true or false)
        window.location.href = 'inicioUsuario.html'; //mando al ususario al link
      }
    });
  });