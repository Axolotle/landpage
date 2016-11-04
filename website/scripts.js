
var targ = document.getElementsByClassName("targ");
var toShow = document.getElementsByClassName("content");
var viewTarget = document.getElementsByClassName("base-content");

//openAll()

function resetContent(a) {
    for (var a = 0; a < targ.length; a++) {
        toShow[a].style.display = "none";
    }
}

function showContent(a) {
    var i = Array.prototype.indexOf.call(targ, a.target);
    var dis = toShow[i].style.display;

    if (dis == "none") {
        resetContent(i);
        toShow[i].style.display = "inline-block";
        viewTarget[i].scrollIntoView();
    }
    else {
        resetContent(i);
    }
}

for (var i = 0; i < targ.length; i++) {
    targ[i].addEventListener("click", showContent);
}


function openAll() {
    for (var a = 0; a < targ.length; a++) {
        toShow[a].style.display = "inline-block";
    }
}
