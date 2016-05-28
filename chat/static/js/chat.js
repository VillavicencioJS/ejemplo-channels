$(function() {

    var chatsocket = new WebSocket('ws://' + window.location.host + "/chat" + window.location.pathname);

    chatsocket.onmessage = function(message) {
        var data = JSON.parse(message.data);
        var chat = $("#chat");
        var element = $('<tr></tr>');

        element.append(
            $("<td></td>").text(data.timestamp)
        );
        element.append(
            $("<td></td>").text(data.handle)
        );
        element.append(
            $("<td></td>").text(data.message)
        );

        chat.prepend(element);
    };

    $("#chatform").on("submit", function(event) {
        var message = {
            handle: $('#handle').val(),
            message: $('#message').val(),
        }
        chatsocket.send(JSON.stringify(message));
        $("#message").val('').focus();
        return false;
    });
});
