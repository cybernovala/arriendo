document.getElementById("formulario").addEventListener("submit", async function (e) {
  e.preventDefault();

  const datos = {
    ciudad: document.getElementById("ciudad").value.toUpperCase(),
    dia: document.getElementById("dia").value,
    mes: document.getElementById("mes").value.toUpperCase(),
    anio: document.getElementById("anio").value,
    arrendador: document.getElementById("arrendador").value.toUpperCase(),
    nacionalidad_arrendador: document.getElementById("nacionalidad_arrendador").value.toUpperCase(),
    rut_arrendador: document.getElementById("rut_arrendador").value,
    direccion_arrendador: document.getElementById("direccion_arrendador").value.toUpperCase(),
    comuna_arrendador: document.getElementById("comuna_arrendador").value.toUpperCase(),
    arrendatario: document.getElementById("arrendatario").value.toUpperCase(),
    nacionalidad_arrendatario: document.getElementById("nacionalidad_arrendatario").value.toUpperCase(),
    rut_arrendatario: document.getElementById("rut_arrendatario").value,
    direccion_arrendatario: document.getElementById("direccion_arrendatario").value.toUpperCase()
  };

  try {
    const response = await fetch("https://arriendo-2wag.onrender.com/generar_pdf", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(datos)
    });

    if (!response.ok) throw new Error("Error al generar PDF");

    const blob = await response.blob();
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "arriendo_cybernova.pdf";
    link.click();
  } catch (error) {
    alert("Hubo un error al generar el PDF.");
    console.error("Error:", error);
  }
});
