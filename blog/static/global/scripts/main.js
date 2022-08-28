let colors = document.querySelectorAll('nav span');
let r = document.querySelector(':root');
let c = localStorage.getItem("color");

function dark() {
    r.style.setProperty('--main-color', '#03e9f4');
    r.style.setProperty('--back-color-1', '#141e30');
    r.style.setProperty('--back-color-2', '#243b55');
    r.style.setProperty('--text-color', '#fff');
    r.style.setProperty('--box-color', 'rgba(0, 0, 0, 0.5)');
}

function light() {
    r.style.setProperty('--main-color', '#bfc3dc');
    r.style.setProperty('--back-color-1', '#e7e7e7');
    r.style.setProperty('--back-color-2', '#fff');
    r.style.setProperty('--text-color', '#fff');
    r.style.setProperty('--box-color', 'rgb(52, 51, 51)');
}

if (c) {
    if (c === "dark")
        dark();
    else if (c === "light")
        light();
        
    colors.forEach((color) => {
        color.classList.remove('active')
        if(c === color.dataset.color) {
            color.classList.add('active')
        }
    });
}

colors.forEach((color) => {
    color.addEventListener("click", (e)=> {
        colors.forEach((color) => {
            color.classList.remove('active')
        })
        e.currentTarget.classList.add('active')
        localStorage.setItem("color", e.currentTarget.dataset.color)
        if (e.currentTarget.dataset.color === "dark")
            dark();
        else if (e.currentTarget.dataset.color === "light")
            light();
    });
});

function dark() {
    r.style.setProperty('--main-color', '#03e9f4');
    r.style.setProperty('--back-color-1', '#141e30');
    r.style.setProperty('--back-color-2', '#243b55');
    r.style.setProperty('--text-color', '#fff');
    r.style.setProperty('--box-color', 'rgba(0, 0, 0, 0.5)');
}

function light() {
    r.style.setProperty('--main-color', '#333');
    r.style.setProperty('--back-color-1', '#e7e7e7');
    r.style.setProperty('--back-color-2', '#d1d1d1');
    r.style.setProperty('--text-color', '#138086');
    // r.style.setProperty('--box-color', '#138086');
    r.style.setProperty('--box-color', '#ffffff47');
}