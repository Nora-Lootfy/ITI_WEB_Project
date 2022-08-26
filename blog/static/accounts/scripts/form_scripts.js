let page_specify = document.querySelectorAll('.login-box .login-action h2')
let pages = document.querySelectorAll('.login-box form .form')

page_specify.forEach((p) => {
    p.addEventListener("click", (e)=> {
        page_specify.forEach((p) => {
            p.removeAttribute("active");
        })
        e.currentTarget.setAttributeNode(document.createAttribute("active"));
        if (e.currentTarget.classList[0] === "login"){
            pages[0].setAttributeNode(document.createAttribute("active-form"));
            pages[1].removeAttribute("active-form");
        } else if (e.currentTarget.classList[0] === "register") {
            pages[0].removeAttribute("active-form");
            pages[1].setAttributeNode(document.createAttribute("active-form"));
        }
    });
});