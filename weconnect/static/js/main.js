
const myNav = document.querySelector("#my-nav")
const burger = document.querySelector("#burger")
burger.addEventListener('click', ()=> {
    myNav.classList.toggle("is-active")
    burger.classList.toggle("is-active")
})

function toggleDropdown() {
    const myNav = document.querySelector("#my-nav")
    const burger = document.querySelector("#burger")
    myNav.classList.toggle("is-active")
    burger.classList.toggle("is-active")
}
