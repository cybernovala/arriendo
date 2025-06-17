const backendURL = "https://arriendo-2wag.onrender.com/generar_pdf";

function mostrarVistaPrevia() {
  const data = obtenerDatosFormulario();
  const texto = generarTextoVistaPrevia(data);
  document.getElementById("vistaPreviaTexto").textContent = texto;
  document.getElementById("formulario").style.display = "none";
  document.getElementById("vistaPreviaContainer").style.display = "block";
}

function ocultarVistaPrevia() {
  document.getElementById("formulario").style.display = "block";
  document.getElementById("vistaPreviaContainer").style.display = "none";
}

function obtenerDatosFormulario() {
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
    direccion_inmueble: document.getElementById("direccion_inmueble").value,
    uso_inmueble: document.getElementById("uso_inmueble").value,
    inicio_vigencia: document.getElementById("inicio_vigencia").value,
    termino_vigencia: document.getElementById("termino_vigencia").value,
    renta: document.getElementById("renta").value,
    cuenta: document.getElementById("cuenta").value,
    banco: document.getElementById("banco").value,
    garantia: document.getElementById("garantia").value
  };
}

function generarTextoVistaPrevia(data) {
  return `Contrato de Arriendo entre ${data.arrendador} y ${data.arrendatario}, por la propiedad en ${data.direccion_inmueble}. Renta mensual de ${data.renta}, inicio ${data.inicio_vigencia}, término ${data.termino_vigencia}.`;
}

document.getElementById("formulario").addEventListener("submit", async function(e) {
  e.preventDefault();
  const data = obtenerDatosFormulario();

  try {
    const response = await fetch(backendURL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    if (!response.ok) throw new Error("Error al generar PDF");

    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "arriendo_cybernova.pdf";
    a.click();
    window.URL.revokeObjectURL(url);
  } catch (err) {
    alert("Error al generar el PDF.");
  }
});
