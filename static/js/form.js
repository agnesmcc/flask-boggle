$("#guess-input").focus();

async function submit_guess(guess){
    console.debug('guess submitted!');
    console.debug(guess);
    resp = await axios.post(`/submit?guess=${guess}`)
    let {result, score} = resp.data
    console.debug('RESULT:', result)

    if (result == 'ok') {
        result = `${guess} is on the board!`
    } else if (result == 'not-on-board') {
        result = `${guess} is not on the board!`
    } else if (result == 'not-word') {
        result = `${guess} is not a word!`
    }

    $('#result').text(result)
    $("#player-score").text(score);
    return null;
}

$('#guess-form').on('submit', function(evt){
    evt.preventDefault();
    if (!gameExpired) {
        let guess = $('#guess-input').val()
        submit_guess(guess);
    }
})

