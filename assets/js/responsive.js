
/***************************Responsive Top Navigation*******************************/
function headMenu() {
    var x = document.getElementById("responsive-head");

    if (x.className === "hide") {
        x.className = "show";
    } else {
        x.className = "hide";
    }
}

/*****************************Responsive Footer Navigation*****************************/
function footerMenu() {
    var x = document.getElementById("responsive-footer");

    if (x.className === "hide2") {
        x.className = "show2";
    } else {
        x.className = "hide2";
    }
}

/*****************************Fade In on Scroll Down, Fade Out on Scroll Up*****************************/
//reference: http://stackoverflow.com/questions/26694385/fade-in-on-scroll-down-fade-out-on-scroll-up-based-on-element-position-in-win

$(window).on("load",function() {
  $(".card-block:nth-of-type(2), .card-block:nth-of-type(3)").addClass("load");
  $(".card-block:nth-of-type(n+4)").addClass("load1");
  $(window).scroll(function() {
    var windowBottom = $(this).scrollTop() + $(this).innerHeight();
    $(".card-block").each(function() {
      /* Check the location of each desired element */
      var objectBottom = $(this).offset().top + $(this).outerHeight();
      
      /* If the element is completely within bounds of the window, fade it in */
      if (objectBottom < windowBottom) { //object comes into view (scrolling down)
        if ($(this).css("opacity")==0.3) {$(this).fadeTo(0,1);}
      } else { //object goes out of view (scrolling up)
        if ($(this).css("opacity")==1) {$(this).fadeTo(0,0.3);}
      }
    });
  }).scroll(); //invoke scroll-handler on page-load
});



