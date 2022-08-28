let icon = document.querySelector("main aside .content-side .icon")
let categories = document.querySelector("main aside .content-side .categories")

icon.addEventListener("click", ()=> {
    let style = getComputedStyle(categories);
    if(style["display"] === "none")
        categories.style.display = "block"
    else
        categories.style.display = "none"
});