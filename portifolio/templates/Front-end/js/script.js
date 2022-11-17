let menu = document.querySelector('#menu-btn');
let header = document.querySelector('.header');
let btniconedit = document.querySelector('.btn-icon-edit');
let btnicondelete = document.querySelector('.btn-icon-delete');

menu.onclick = () =>{
    menu.classList.toggle('fa-times');
    header.classList.toggle('active');
    
}

window.onscroll = () =>{
    menu.classList.remove('fa-times');
    header.classList.remove('active');
}

let themeToggler = document.querySelector('#theme-toggler');
let getMode = localStorage.getItem('mode');
if(getMode && getMode ==='dark'){
  document.body.classList.add('active');
  btniconedit.classList.toggle('active');        
  btnicondelete.classList.toggle('active');
}

themeToggler.onclick = () =>{
    themeToggler.classList.toggle('fa-sun');
    if(themeToggler.classList.contains('fa-sun')){
        document.body.classList.add('active');
        btniconedit.classList.toggle('active');        
        btnicondelete.classList.toggle('active');        
              
        return localStorage.setItem('mode','dark')
    }else{
        document.body.classList.remove('active');
        btniconedit.classList.remove('active');
        btnicondelete.classList.remove('active');
        
        return localStorage.setItem('mode','ligth')
    }
}

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }