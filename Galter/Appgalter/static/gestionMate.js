document.addEventListener("DOMContentLoaded", function(){
    document.getElementById("frmMaterial").addEventListener("submit", function(event){
        event.preventDefault();
        var data={
            codi_mate:document.getElementById("codigo").value,
            nomb_mate:document.getElementById("nombre").value,
            cant_mate:document.getElementById("cantidad").value,
            proveedor_mate:document.getElementById("proveedor").value,
        }
        var jsonData=JSON.stringify(data);
        fetch("http://127.0.0.1:8000/insertarMate/",{
            method:'POST',
            body:jsonData,
            headers:{
                "Content-Type":"Appgalter/json"
            }
        })
        .then(res => res.json())
        .then(datos =>{
            console.log(datos)
            consultarMate();
        })
        .catch(console.error)
    })
})