$(function() {
    $("#scheduleBtnSlide").click(function() {
        $("#scheduledPanel").slideToggle(1000);
    });
    $("#scheduleBtnSlide2").click(function() {
        $("#SDVscheduledPanel").slideToggle(1000);
    });
    $("#requestBtnSlide").click(function() {
        $("#requestPanel").slideToggle(1000);
    });
});

$(document).ready(function(){
    $("#viewToggle").click(function(){

        var x = document.getElementById("singleDayView");
        var y = document.getElementById("weekView");

        if($("#singleDayView").toggle()) {
            y.style.display = "none";
            x.style.display = "block";
        }
    });

});
