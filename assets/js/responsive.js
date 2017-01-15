function headMenu() {
    var x = document.getElementById("rightnav");
    var y = document.getElementById("top-nav-line");
    if (x.className === "") {
        x.className = "responsive";
        y.className="";
    } else {
        x.className = "";
        y.className="vertical-line";
    }
}


function footMenu() {
    var x = document.getElementById("links");
    if (x.className === "") {
        x.className = "responsive";
    } else {
        x.className = "";
    }
}
