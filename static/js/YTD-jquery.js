/**
 * Created by loctrinh on 1/3/16.
 */
$(document).ready(function(){
    $(".video_link").click(function(){
        var url = $(this).attr("data-url");
        $.get("/frame/", {"url": url}, function(data){
            $("#player").html(data);
        });
    });
});