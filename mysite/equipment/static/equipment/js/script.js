/* Проходим по всем кнопкам активации выпадающего подменю, чтобы переключить скрытое/показанное состояние их контейнеров. Это позволяет пользователю иметь несколько выпадающих подменю без конфликтов */
var dropdown = document.getElementsByClassName("dropdown-btn");
var i;
    
for (i = 0; i < dropdown.length; i++) {
    dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
        dropdownContent.style.display = "none";
    } else {
        dropdownContent.style.display = "block";
    }
    });
}
