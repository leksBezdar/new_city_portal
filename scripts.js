const iconMenu = document.querySelector('.burger-menu')
if (iconMenu) {
    const menuBody = document.querySelector('.menu-body')
    iconMenu.addEventListener('click', function (e) {
        iconMenu.classList.toggle('_active')
        menuBody.classList.toggle('_active')
    })
}