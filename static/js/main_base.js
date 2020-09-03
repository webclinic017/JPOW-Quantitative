//close modal on outside click
$(function() {
  $("body").click(function(e) {
    if (e.target.id == "login" || e.target.id == "signup" || $(e.target).parents("#signup").length || $(e.target).parents("#login").length) {
      //do nothing
    } else {
      $(".modal").modal("hide");
    }
  });
})
