//hide and show btn
function toggleHideAndShow() {
  var x = document.getElementById("show-hide");
  if (x.style.display === "none") {
    x.style.display = "flex";
    x.style.flexDirection = "column";
    x.style.alignItems = "center";
  } else {
    x.style.display = "none";
  }
}