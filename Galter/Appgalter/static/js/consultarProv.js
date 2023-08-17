function consultarProv(){
    fetch("http://127.0.0.1:8000/Proveedor",{
        method:"GET",
        headers:{
            "consultar-tipe":"Appgalter/json"
        }
    })
    .then(res => res.json())
    .then(datos => {
        console.log(datos)
        let tabla=document.getElementById("ConsultaProveedor");
        tabla.innerHTML="";
        if(datos==0){
            tabla.innerHTML+=`<tr> <td> No hay datos </td></tr>`
        
        }
        else{
            for(let dat of datos){
                tabla.innerHTML+=`
                <tr>
                <td>${dat.nombre_proveedor}</td>
                <td>${dat.telefono_proveedor}</td>
                </tr>`
            }
        }
    })
}