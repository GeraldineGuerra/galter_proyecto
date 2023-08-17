function consultarPedi(){
    fetch("http://127.0.0.1:8000/Pedido",{
        method:"GET",
        headers:{
            "consultar-tipe":"Appgalter/json"
        }
    })
    .then(res => res.json())
    .then(datos => {
        console.log(datos)
        let tabla=document.getElementById("ConsultaPedido");
        tabla.innerHTML="";
        if(datos==0){
            tabla.innerHTML+=`<tr> <td> No hay datos </td></tr>`
        
        }
        else{
            for(let dat of datos){
                tabla.innerHTML+=`
                <tr>
                <td>${dat.id_pedido}</td>
                <td>${dat.cliente_pedido}</td>
                <td>${dat.producto_pedido}</td>
                <td>${dat.usuario_pedido}</td>
                <td>${dat.tiempo_pedido}</td>
                <td>${dat.fecha_encargo}</td>
                <td>${dat.fecha_entrega}</td>
                </tr>`
            }
        }
    })
}