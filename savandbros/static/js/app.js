/**
 * By Kloud51.com
 * Copyright 2017, all rights reserved.
 */

function showDebugElements() {
  // Check if in debug mode
  if (localStorage.getItem("debug") !== "true") {
    return;
  }
  // Show hidden elements
  $("[hidden]").removeAttr("hidden");
}

function animateScroll(selector) {
  // Get scroll top position
  var scroll = $(selector).position().top;
  // Scroll
  $("html, body").animate({ scrollTop: scroll }, 1000);
}

function showHostings() {
  $("#Hosting").trigger("click");
}

$(function () {
  $(".dropdown-toggle").dropdown();
  $("[tooltip]").tooltip();
  showDebugElements();
  grid(".grid");
  grid(".grid-2");
  grid(".grid-3");
});
