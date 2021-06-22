var nombre = document.getElementById('nombre');
var telefono = document.getElementById('telefono');
var error = document.getElementById('error');
error.style.color = 'red';

//function enviarFormulario(){
//	console.log('Enviando Formulario...');

//	var mensajesError =[]
//	if (nombre.value ===  null || nombre.value=== ''){
//		mensajesError.push('Ingresa tu nombre');
//	}

//	if (telefono.value ===  null || telefono.value=== ''){
//		mensajesError.push('Ingresa tu telefono');
//	}
//	if (email.value ===  null || email.value=== ''){
//		mensajesError.push('Ingresa tu Correo Electronico');
//	}
//		error.innerHTML =mensajesError.join(', ');

//	return false;
// }

var form = document.getElementById('formulario')
	form = addEventListener('submit', function(evt){
		evt.preventDefault();
		var mensajesError =[]

	if (nombre.value ===  null || nombre.value=== ''){
		mensajesError.push('Ingresa tu nombre');
	}

	if (telefono.value ===  null || telefono.value=== ''){
		mensajesError.push('Ingresa tu telefono');
	}

	if (email.value ===  null || email.value=== ''){
		mensajesError.push('Ingresa tu Correo Electronico');
	}
		error.innerHTML =mensajesError.join(', ');

	});


	