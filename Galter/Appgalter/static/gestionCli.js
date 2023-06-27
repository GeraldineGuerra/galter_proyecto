document.addEventListener("DOMContentLoaded", function(){
    document.getElementById("frmClientes").addEventListener("submit", function(event){
        event.preventDefault();
        var data={
            id_cliente:document.getElementById("id").value,
            nombre_cliente:document.getElementById("nombre").value,
            telefono_cliente:document.getElementById("telefono").value,
            representante_cliente:document.getElementById("representante").value,
            direccion:document.getElementById("direccion").value
        }
        var jsonData=JSON.stringify(data);
        fetch("http://127.0.0.1:8000/insertarCli/",{
            method:'POST',
            body:jsonData,
            headers:{
                "Content-Type":"Appgalter/json"
            }
        })
        .then(res => res.json())
        .then(datos =>{
            console.log(datos)
            consultarCli();
        })
        .catch(console.error)
    })
})