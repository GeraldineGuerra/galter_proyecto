function consultarProd(){
    fetch("http://127.0.0.1:8000/Producto",{
        method:"GET",
        headers:{
            "consultar-tipe":"Appgalter/json"
        }
    })
    .then(res => res.json())
    .then(datos => {
        console.log(datos)
        let tabla=document.getElementById("ConsultaProducto");
        tabla.innerHTML="";
        if(datos==0){
            tabla.innerHTML+=`<tr> <td> No hay datos </td></tr>`
        
        }
        else{
            for(let dat of datos){
                tabla.innerHTML+=`
                <tr>
                <td>${dat.codi_prod}</td>
                <td>${dat.nomb_prod}</td>
                <td>${dat.tiempo_prod}</td>
                <td>${dat.long_prod}</td>
                <td>${dat.material_prod}</td>
                <td>${dat.prec_prod}</td>
                </tr>`
            }
        }
    })
}