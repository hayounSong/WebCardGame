var loader;

function loading() {
  loader = setTimeout(showPage, 1500);
}

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("loader__container").style.display = "none";
  document.getElementById("wrapper").style.display = "flex";
}