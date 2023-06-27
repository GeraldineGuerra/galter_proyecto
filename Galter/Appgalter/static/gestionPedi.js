document.addEventListener("DOMContentLoaded", function(){
    document.getElementById("frmPedido").addEventListener("submit", function(event){
        event.preventDefault();
        var data={
            id_pedido:document.getElementById("codigo").value,
            cliente_pedido:document.getElementById("cliente").value,
            producto_pedido:document.getElementById("producto").value,
            usuario_pedido:document.getElementById("usuario").value,
            tiempo_pedido:document.getElementById("tiempo").value,
            fecha_encargo:document.getElementById("encargo").value,
            fecha_entrega:document.getElementById("entrega").value
        }
        var jsonData=JSON.stringify(data);
        fetch("http://127.0.0.1:8000/insertarPedi/",{
            method:'POST',
            body:jsonData,
            headers:{
                "Content-Type":"Appgalter/json"
            }
        })
        .then(res => res.json())
        .then(datos =>{
            console.log(datos) 
            consultarPedi(); 
        })
        .catch(console.error)
    })
})