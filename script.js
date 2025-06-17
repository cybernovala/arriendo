function obtenerDatosFormulario() {
  return {
    ciudad: document.getElementById("ciudad").value,
    fecha: document.getElementById("fecha").value,
    arrendador: document.getElementById("arrendador").value,
    nacionalidad_arrendador: document.getElementById("nacionalidad_arrendador").value,
    ci_arrendador: document.getElementById("ci_arrendador").value,
    domicilio_arrendador: document.getElementById("domicilio_arrendador").value,
    arrendatario: document.getElementById("arrendatario").value,
    nacionalidad_arrendatario: document.getElementById("nacionalidad_arrendatario").value,
    ci_arrendatario: document.getElementById("ci_arrendatario").value,
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

function mostrarVistaPrevia() {
  const datos = obtenerDatosFormulario();
  const vista = `
CONTRATO DE ARRENDAMIENTO

En ${datos.ciudad.toUpperCase()} DE CHILE, A ${datos.fecha.toUpperCase()} ENTRE: DON(ÑA) ${datos.arrendador.toUpperCase()}, NACIONALIDAD ${datos.nacionalidad_arrendador.toUpperCase()}, CI ${datos.ci_arrendador}, DOMICILIO ${datos.domicilio_arrendador.toUpperCase()} (ARRENDADOR); Y DON(ÑA) ${datos.arrendatario.toUpperCase()}, NACIONALIDAD ${datos.nacionalidad_arrendatario.toUpperCase()}, CI ${datos.ci_arrendatario} (ARRENDATARIO). LAS PARTES CONVIENEN EL SIGUIENTE CONTRATO...
`.trim();
  document.getElementById("vistaPrevia").textContent = vista;
  document.getElementById("vistaPreviaContainer").style.display = "block";
}

function editarFormulario() {
  document.getElementById("vistaPreviaContainer").style.display = "none";
}

document.getElementById("formulario").addEventListener("submit", async function (e) {
  e.preventDefault();
  const datos = obtenerDatosFormulario();
  try {
    const response = await fetch("https://arriendo-cybernova.onrender.com/generar_pdf", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(datos)
    });

    if (!response.ok) throw new Error("Error al generar el PDF");

    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "arriendo_cybernova.pdf";
    a.click();
    window.URL.revokeObjectURL(url);
  } catch (error) {
    alert("Hubo un problema al generar el PDF");
  }
});
