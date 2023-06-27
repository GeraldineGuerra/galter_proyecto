document.addEventListener("DOMContentLoaded", function(){
    document.getElementById("frmProducto").addEventListener("submit", function(event){
        event.preventDefault();
        var data={
            codi_prod:document.getElementById("codigo").value,
            nomb_prod:document.getElementById("nombre").value,
            tiempo_prod:document.getElementById("tiempo"). value,
            long_prod:document.getElementById("longitud").value,
            material_prod:document.getElementById("material").value,
            prec_prod:document.getElementById("precio").value
            
        };
        
        var jsonData=JSON.stringify(data);
        fetch("http://127.0.0.1:8000/insertarProd/",{
            method:'POST',
            body:jsonData,
            headers:{
                "Content-Type":"Appgalter/json"
            }
        })

        .then(res => res.json())
        .then(datos=>{
            console.log(datos)
            consultarProd();
        })
        .catch(console.error)
    });
});