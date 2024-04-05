function submit_guess(guess){
    console.debug('guess submitted!');
    console.debug(guess);
    return null;
}

$('#guess-form').on('submit', function(evt){
    evt.preventDefault();
    let guess = $('#guess-input').val()
    submit_guess(guess);
})

