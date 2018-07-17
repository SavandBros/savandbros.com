/**
 * Open mail client with subject and message of form
 */
var contactUs = function (form) {

  // Prevent default behavior of form
  event.preventDefault();

  // Savand Bros email
  var email = "hello@savandbros.com";

  // Get subject and message of form
  var subject = $("#subject").val();
  var message = $("#message").val();

  // Setup mailto link
  var mailto = "mailto:" + email + "?subject=" + subject + "&body=" + message;

  // Open mail client
  window.open(mailto, "emailWindow");
};
