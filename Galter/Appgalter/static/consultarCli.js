function consultarCli(){
    fetch("http://127.0.0.1:8000/Cliente",{
        method:"GET",
        headers:{
            "consultar-tipe":"Appgalter/json"
        }
    })
    .then(res => res.json())
    .then(datos => {
        console.log(datos)
        let tabla=document.getElementById("ConsultaCliente");
        tabla.innerHTML="";
        if(datos==0){
            tabla.innerHTML+=`<tr> <td> No hay datos </td></tr>`
        
        }
        else{
            for(let dat of datos){
                tabla.innerHTML+=`
                <tr>
                <td>${dat.id_cliente}</td>
                <td>${dat.nombre_cliente}</td>
                <td>${dat.telefono_cliente}</td>
                <td>${dat.representante_cliente}</td>
                <td>${dat.direccion}</td>
                </tr>`
            }
        }
    })
}