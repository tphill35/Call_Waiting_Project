var typed = new Typed('.element', {
  strings: ["First sentence.", "Second sentence."],
  typeSpeed: 30
});

$(document).ready(function(){
    $("#AddFormButton").click(function(){
        $("#AddForm").toggle();
    });
	$("#RemoveFormButton").click(function(){
        $("#RemoveForm").toggle();
    });
});

