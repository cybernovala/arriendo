const backendUrl = "https://arriendo-2wag.onrender.com/generar_pdf";

const form = document.getElementById("formulario");
const btnVistaPrevia = document.getElementById("vista-previa");
const btnModificar = document.getElementById("modificar");
const btnGenerar = document.getElementById("generar");

btnVistaPrevia.addEventListener("click", () => {
  const inputs = form.querySelectorAll("input");
  inputs.forEach(input => input.setAttribute("readonly", true));
  btnVistaPrevia.style.display = "none";
  btnModificar.style.display = "block";
  btnGenerar.style.display = "block";
});

btnModificar.addEventListener("click", () => {
  const inputs = form.querySelectorAll("input");
  inputs.forEach(input => input.removeAttribute("readonly"));
  btnVistaPrevia.style.display = "block";
  btnModificar.style.display = "none";
  btnGenerar.style.display = "none";
});

form.addEventListener("submit", async function (e) {
  e.preventDefault();

  const datos = {
    ciudad: document.getElementById("ciudad").value,
    fecha: document.getElementById("fecha").value,
    arrendador: document.getElementById("arrendador").value,
    nacionalidad_arrendador: document.getElementById("nacionalidad_arrendador").value,
    cedula_arrendador: document.getElementById("cedula_arrendador").value,
    domicilio_arrendador: document.getElementById("domicilio_arrendador").value,
    arrendatario: document.getElementById("arrendatario").value,
    nacionalidad_arrendatario: document.getElementById("nacionalidad_arrendatario").value,
    cedula_arrendatario: document.getElementById("cedula_arrendatario").value,
    direccion_inmueble: document.getElementById("direccion_inmueble").value,
    uso: document.getElementById("uso").value,
    inicio: document.getElementById("inicio").value,
    termino: document.getElementById("termino").value,
    renta: document.getElementById("renta").value,
    cuenta: document.getElementById("cuenta").value,
    banco: document.getElementById("banco").value,
    garantia: document.getElementById("garantia").value
  };

  try {
    const response = await fetch(backendUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(datos)
    });

    if (!response.ok) throw new Error("Error al generar PDF");

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "arriendo_cybernova.pdf";
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
  } catch (error) {
    alert("Error al generar el PDF. Intenta de nuevo.");
    console.error("Error:", error);
  }
});
