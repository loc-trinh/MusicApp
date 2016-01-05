/**
 * Created by loctrinh on 1/3/16.
 */
$(document).ready(function(){
    $(".video_link").click(function(){
        var url = $(this).attr("data-url");
        $.get("/frame/", {"url": url}, function(data){
            $("#player").html(data);
            $("#download").attr( "data-url", url ).css("display", "block");
        });
    });

    $("#download").on("submit", function(e){
        e.preventDefault();
        var video_id = $(this).attr("data-url");
        var playlist = $("#playlist_select").val();
        $.get("/add_to_download/", {"video_id": video_id, "playlist": playlist}, function(){
            $("#download").css("display", "none");
        });
    });

    $(".download_link").click(function(){
        var url = $(this).attr("data-url");
        var playlist = $(this).attr("data-playlist");
        var song_name = $(this).attr("data-name");
        $(this).hide();
        $("#loading").slideToggle()
        $('button').prop('disabled', true);
        $.get("/download_video/", {"url": url, "playlist": playlist, "song_name": song_name}, function(){
            $('button').prop('disabled', false);
             $("#loading").slideToggle()
        });
    });
});