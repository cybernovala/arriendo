function vistaPrevia() {
  const datos = obtenerDatos();
  const preview = `
CONTRATO DE ARRENDAMIENTO

En ${datos.ciudad} de Chile, a ${datos.fecha}, entre: don(ña) ${datos.arrendador}, nacionalidad ${datos.nacionalidad_arrendador}, cédula de identidad N° ${datos.rut_arrendador}, con domicilio en ${datos.domicilio_arrendador} (en adelante, el “Arrendador”); y don(ña) ${datos.arrendatario}, nacionalidad ${datos.nacionalidad_arrendatario}, cédula de identidad N° ${datos.rut_arrendatario}, con domicilio en ${datos.domicilio_arrendatario} (en adelante, el “Arrendatario”), exponen que han convenido el siguiente Contrato...

[Texto completo en el backend]
  `;

  document.getElementById("preview").innerText = preview;
  document.getElementById("preview").style.display = "block";
  document.getElementById("btn-generar").style.display = "block";
}

function obtenerDatos() {
  return {
    ciudad: document.getElementById("ciudad").value,
    fecha: document.getElementById("fecha").value,
    arrendador: document.getElementById("arrendador").value,
    nacionalidad_arrendador: document.getElementById("nacionalidad_arrendador").value,
    rut_arrendador: document.getElementById("rut_arrendador").value,
    domicilio_arrendador: document.getElementById("domicilio_arrendador").value,
    arrendatario: document.getElementById("arrendatario").value,
    nacionalidad_arrendatario: document.getElementById("nacionalidad_arrendatario").value,
    rut_arrendatario: document.getElementById("rut_arrendatario").value,
    domicilio_arrendatario: document.getElementById("domicilio_arrendatario").value,
    direccion_inmueble: document.getElementById("direccion_inmueble").value,
    uso: document.getElementById("uso").value,
    inicio: document.getElementById("inicio").value,
    termino: document.getElementById("termino").value,
    renta: document.getElementById("renta").value,
    cuenta: document.getElementById("cuenta").value,
    banco: document.getElementById("banco").value,
    garantia: document.getElementById("garantia").value
  };
}

async function generarPDF() {
  const datos = obtenerDatos();

  const response = await fetch("https://arriendo-2wag.onrender.com/generar_pdf", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(datos),
  });

  const blob = await response.blob();
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = "arriendo_cybernova.pdf";
  document.body.appendChild(link);
  link.click();
  link.remove();
}
