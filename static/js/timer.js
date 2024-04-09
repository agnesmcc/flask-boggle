let gameSeconds = 60
let gameExpired = false;

updateTimeLeft(gameSeconds);

function updateTimeLeft(seconds) {
    $("#countdown").text(`${seconds} seconds remaining`);
}

let timer = setInterval(countdown, 1000);

function countdown() {
    if (gameSeconds > 0) {
        // console.log(`${gameSeconds} seconds remaining`);
        updateTimeLeft(gameSeconds);
        gameSeconds--;
    } else {
        clearInterval(timer);
        // console.log("Time's up!");
        $("#countdown").text("Time's up!");
        gameExpired = true;
    }
}
