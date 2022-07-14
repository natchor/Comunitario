function validacion() {

    mail = document.getElementById('correo').value;
    user = document.getElementById('usuario').value;
    pass = document.getElementById('clave').value;
    pass2 = document.getElementById('clave2').value;
    nac = document.getElementById('fechanac').value;

    if( !(/\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)/.test(mail)) ) {
        alert('Debe ingresar un correo electrónico válido');
        document.getElementById('correo').value="";
        document.datos.mail.focus();
        return false;
    }

    if(user == null || user.length==0 || /^\s+$/.test(user)) {
        alert('Debe ingresar un nombre de usuario');
        document.getElementById('usuario').value="";
        document.datos.user.focus();
        return false;
    }


    return true;





}