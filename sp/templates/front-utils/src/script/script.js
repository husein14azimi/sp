// display modal of login 
const loginBtn = document.getElementById('loginBtn')
const closeBtn = document.getElementById('closeModal')
const modal = document.getElementById('loginModal'); 
loginBtn.addEventListener('click' , ()=> { 
    modal.style.display = "flex"
    closeBtn.addEventListener('click', ()=> {
        modal.style.display ="none"
    })
})
window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
}

