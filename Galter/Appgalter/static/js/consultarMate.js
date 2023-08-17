function consultarMate(){
    fetch("http://127.0.0.1:8000/Material",{
        method:"GET",
        headers:{
            "consultar-tipe":"Appgalter/json"
        }
    })
    .then(res => res.json())
    .then(datos => {
        console.log(datos)
        let tabla=document.getElementById("ConsultaMaterial");
        tabla.innerHTML="";
        if(datos==0){
            tabla.innerHTML+=`<tr> <td> No hay datos </td></tr>`
        
        }
        else{
            for(let dat of datos){
                tabla.innerHTML+=`
                <tr>
                <td>${dat.codi_mate}</td>
                <td>${dat.nomb_mate}</td>
                <td>${dat.cant_mate}</td>
                <td>${dat.proveedor_mate}</td>
                </tr>`
            }
        }
    })
}