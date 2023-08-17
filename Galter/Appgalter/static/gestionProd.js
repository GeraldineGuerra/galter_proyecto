document.addEventListener("DOMContentLoaded", function(){
    document.getElementById("frmProducto").addEventListener("submit", function(event){
        event.preventDefault();

        var codigo = document.getElementById("codigo").value;
        var nombre = document.getElementById("nombre").value;
        var tiempo = document.getElementById("tiempo").value;
        var longitud = document.getElementById("longitud").value;
        var material = document.getElementById("material").value;
        var precio = document.getElementById("precio").value;

        if (!codigo || !nombre || !tiempo || !longitud || !material || !precio) {
            Swal.fire({
                title: '',
                text: 'Por favor, complete todos los campos del formulario',
                icon: 'error',
                confirmButtonText: 'Aceptar'
            });
            return; 
        }

      
        var data = {
            codi_prod: codigo,
            nomb_prod: nombre,
            tiempo_prod: tiempo,
            long_prod: longitud,
            material_prod: material,
            prec_prod: precio
        };

        var jsonData = JSON.stringify(data);
        fetch("http://127.0.0.1:8000/insertarProd/", {
            method: 'POST',
            body: jsonData,
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(res => res.json())
        .then(datos => {
            console.log(datos);
            if (datos.mensaje === 'datos guardados') {
                Swal.fire({
                    title: '',
                    text: 'Datos guardados correctamente',
                    icon: 'success',
                    confirmButtonText: 'Aceptar'
                });
            }
        })
        .catch(console.error);
    });
});


