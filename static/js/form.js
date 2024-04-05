function submit_guess(){
    console.debug('guess submitted!');
    return null;
}

$('#guess-form').on('submit', function(evt){
    evt.preventDefault();
    submit_guess();
})

