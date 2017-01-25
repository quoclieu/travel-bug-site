function headMenu() {
    var x = document.getElementById("responsive-head");

    if (x.className === "hide") {
        x.className = "show";
    } else {
        x.className = "hide";
    }
}
function footerMenu() {
    var x = document.getElementById("responsive-footer");

    if (x.className === "hide2") {
        x.className = "show2";
    } else {
        x.className = "hide2";
    }
}