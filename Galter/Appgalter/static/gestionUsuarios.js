document.addEventListener("DOMContentLoaded", function(){
    document.getElementById("frmInsertar").addEventListener("submit", function(event){
        event.preventDefault();
        var data={
            codi_usuario:document.getElementById("codigo").value,
            nombre_usuario:document.getElementById("nombre").value,
            apellido_usuario:document.getElementById("apellido").value,
            correo_usuario:document.getElementById("correo"). value,
        };
        var jsonData=JSON.stringify(data);
        fetch("http://127.0.0.1:8000/insertarUsu/",{
            method:'POST',
            body:jsonData,
            headers:{
                "Content-Type":"Appgalter/json"
            }
        })

        .then(res => res.json())
        .then(datos=>{
            console.log(datos)
            consultar();
        })
        .catch(console.error)
    });
});