
// Functions

function initialize () {
    
    $(".loading").removeClass("loading");
}

// Events

$('#contact').on('show.bs.modal', function () {
    
    $("body").addClass('loading');
})

$('#contact').on('hide.bs.modal', function () {
    
    $("body").removeClass('loading');
})