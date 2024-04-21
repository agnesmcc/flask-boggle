async function updateScore(){
    console.debug('updating high score');
    let score = $("#player-score").text();
    resp = await axios.post('/score', {score: score})
}