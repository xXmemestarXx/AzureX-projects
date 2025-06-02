//Opinion handling
function opinion(){
    var input = document.getElementById('opinion').value;
    if(input.length > 6){
        alert("This has been saved: " + input);
    } else if(input.length < 20){
        alert("That is not over 20 characters");
    }
}
//Clock
function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('txt').innerHTML =
        h + ":" + m + ":" + s;
    var t = setTimeout(startTime, 500);
}

function checkTime(i) {
    if (i < 10) {
        i = "0" + i
    }; // add zero in front of numbers < 10
    return i;
}