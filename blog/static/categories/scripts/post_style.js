let field = document.querySelector("main .container .post-box form .user-box:nth-child(4)");
let toBeremoved = []

field.childNodes.forEach((node)=> {
    if (node.tagName != "INPUT" && node.tagName != "A" && node.tagName != "LABEL"){
        toBeremoved.push(node);
    }
});

for (node in toBeremoved)
    field.removeChild(toBeremoved[node]);