$('#horizontal').click(function(event){
    $('#bird').addClass('horz')
    $('#bird').removeClass('vert')
})

$('#vertical').click(function(event){
    $('#bird').removeClass('horz')
    $('#bird').addClass('vert')
})



$('#play-btn').click(function(event){
    $('#bird').addClass('play');
    $('#bird').removeClass('pause')
})

$('#pause-btn').click(function(event){
    $('#bird').removeClass('play')
    $('#bird').addClass('pause')
})

