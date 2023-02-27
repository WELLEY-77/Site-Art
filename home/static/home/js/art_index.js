function meuPopup(number) {
    var class_popup = ".popup__texto"+number;
    var popup = document.querySelector(class_popup);
    var class_show = "show"+number;
    popup.classList.toggle(class_show);
}