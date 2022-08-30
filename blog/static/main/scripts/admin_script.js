let cards = document.querySelectorAll("main .container .card-list .info-wrapper .info");
let currentCard = document.querySelector("main .container .card-list .info-wrapper .info.current");
let leftButton = document.querySelector("main .container .card-list .icon.left span");
let rightButton = document.querySelector("main .container .card-list .icon.right span");

let users = document.querySelector(".users");
let posts = document.querySelector(".posts");
let categories = document.querySelector(".categories");
let forbidden_words = document.querySelector(".forbidden-words");

let shown = [users, posts, categories, forbidden_words];

leftButton.addEventListener("click", ()=> {
    for (let i = 0; i < cards.length; i++) {
        if (cards[i] === currentCard) {
            shown[i].classList.remove("current");
            if (i === 0) {
                i = cards.length;
            }
            i--;
            currentCard.classList.remove("current");
            cards[i].classList.add("current");
            shown[i].classList.add("current");
            currentCard = cards[i];
            break;
        }
    }
});

rightButton.addEventListener("click", ()=> {
    for (let i = 0; i < cards.length; i++) {
        if (cards[i] === currentCard) {
            shown[i].classList.remove("current");
            if (i === cards.length - 1) {
                i = -1;
            }
            i++;
            currentCard.classList.remove("current")
            cards[i].classList.add("current");
            shown[i].classList.add("current");
            currentCard = cards[i];
            break;
        }
    }
});