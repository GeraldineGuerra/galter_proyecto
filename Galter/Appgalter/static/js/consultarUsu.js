function consultar(){
    
    fetch("http://127.0.0.1:8000/Usuario",{
        method:"GET",
        headers:{
            "consultar-tipe":"Appgalter/json"
        }
    })
    .then(response => response.json())
    .then(datos =>{
        console.log(datos)
        let tabla=document.getElementById("ConsultaUsuarios");
        tabla.innerHTML="";
        if(datos==0){
            tabla.innerHTML+=`<tr> <td> No hay datos </td></tr>`
        }
        else{
            for(let dat of datos){
                tabla.innerHTML+=`
                <tr>
                <td>${dat.codi_usuario}</td>
                <td>${dat.nombre_usuario}</td>
                <td>${dat.apellido_usuario}</td>
                <td>${dat.correo_usuario}</td>
                </tr>`
            }
        }
    })
}