
var targ = document.getElementsByClassName("targ");
var previousTarg;

for (var i = 0; i < targ.length; i++) {
    targ[i].addEventListener("click", displayProject);
}


function displayProject(a) {
    var toShow = document.getElementsByClassName("content");
    var viewTarget = document.getElementsByClassName("base-content");


    var i = Array.prototype.indexOf.call(targ, a.target);
    var display = toShow[i].style.display;

    if (previousTarg != undefined && previousTarg != i) {
        toShow[previousTarg].style.display = "none";
    }
    if (display == "none" || display == "") {
        toShow[i].style.display = "inline-block";
        previousTarg = i;
    }
    else {
        toShow[i].style.display = "none";
    }

    viewTarget[i].scrollIntoView();
}



function closeAll() {
    var toShow = document.getElementsByClassName("content");

    for (var a = 0; a < targ.length; a++) {
        toShow[a].style.display = "none";
    }
}

function openAll() {
    var toShow = document.getElementsByClassName("content");

    for (var a = 0; a < targ.length; a++) {
        toShow[a].style.display = "inline-block";
    }
}
