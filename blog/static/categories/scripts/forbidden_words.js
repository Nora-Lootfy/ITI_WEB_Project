let forbiddenWords = document.querySelectorAll(".hidden .word");
let comments = document.querySelectorAll(".comments-section ul li div p");
let words = [];

for (let i = 0; i < forbiddenWords.length; i++) {
    words.push(forbiddenWords[i].innerHTML);
}

comments.forEach((comment)=>{
    let com = comment.innerHTML;
    for (word in words){
        let c = com.toLowerCase().indexOf(words[word].toLowerCase());
        if (c != -1) {
            let stars = "*".repeat(words[word].length);
            comment.innerHTML = comment.innerHTML.replace(words[word], stars); 
        }
    }
});




