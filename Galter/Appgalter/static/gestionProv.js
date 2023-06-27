document.addEventListener("DOMContentLoaded", function(){
    document.getElementById("frmProveedor").addEventListener("submit", function(event){
        event.preventDefault();
        var data={
            nombre_proveedor:document.getElementById("nombre").value,
            telefono_proveedor:document.getElementById("telefono").value,
        }
        var jsonData=JSON.stringify(data);
        fetch("http://127.0.0.1:8000/insertarProv/",{
            method:'POST',
            body:jsonData,
            headers:{
                "Content-Type":"Appgalter/json"
            }
        })
        .then(res => res.json())
        .then(datos =>{
            console.log(datos)
            consultarProv();
        })
        .catch(console.error)
    })
})