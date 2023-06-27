document.addEventListener("DOMContentLoaded", function(){
    document.getElementById("frmInsertar").addEventListener("submit", function(event){
        event.preventDefault();
        var data={
            codi_usuario:document.getElementById("codigo").value,
            nombre_usuario:document.getElementById("nombre").value,
            correo_usuario:document.getElementById("correo"). value,
            pass_usuario:document.getElementById("password").value,
            tipo_usuario:document.getElementById("tipo").value
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