function initialize() {
  $(".loading:not(.h)").removeClass("loading");

  setTimeout(function () {
    $(".loading").removeClass("loading hidden");
  }, 2000);
}

$('#contact').on('show.bs.modal', function () {
  $("body").addClass('loading');
})

$('#contact').on('hide.bs.modal', function () {
  $("body").removeClass('loading');
})
