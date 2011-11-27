function box_rotation(id){
    var container_id = 'container-'+id;

    var drag_elem = $("#"+container_id+" .bt_drag");
    var center_elem = $("#"+container_id+" .bt_center");
    var box_elem = $("#"+container_id+" .box");

    //box_elem.css("width", (parseInt($("#content-"+id).attr('width')))+"px");

    drag_elem.draggable({containment: "#"+container_id});

    var bPos = box_elem.position();
    var bWidth = box_elem.width();
    var bHeight = box_elem.height();

    var center_top = bHeight/2 + bPos.top - 16;
    var center_left = bWidth/2 + bPos.left - 16;

    drag_elem.show();
    center_elem.show();

    drag_elem.css("top", center_top);
    drag_elem.css("left", center_left);

    center_elem.css("top", center_top);
    center_elem.css("left", center_left);

    $(document).mousemove(function(e){
        window.mouseXPos = e.pageX;
        window.mouseYPos = e.pageY;
    });

    drag_elem.mousedown(function(e) {
        var bPos = box_elem.offset();
        var bWidth = box_elem.width();
        var bHeight = box_elem.height();

        var center_top = bHeight/2 + bPos.top;
        var center_left = bWidth/2 + bPos.left;

        intervalId = setInterval(function() {
            y = center_top - window.mouseYPos + 32;
            x = window.mouseXPos - center_left - 32;

            rad = 360 - (180/Math.PI) * Math.atan2(y,x);

            box_elem.css("transform","rotate(" + rad + "deg)");
            box_elem.css("-moz-transform","rotate(" + rad + "deg)");
            box_elem.css("-webkit-transform","rotate(" + rad + "deg)");
            box_elem.css("-o-transform","rotate(" + rad + "deg)");

            drag_elem.css("transform","rotate(" + rad + "deg)");
            drag_elem.css("-moz-transform","rotate(" + rad + "deg)");
            drag_elem.css("-webkit-transform","rotate(" + rad + "deg)");
            drag_elem.css("-o-transform","rotate(" + rad + "deg)");

            center_elem.css("transform","rotate(" + rad + "deg)");
            center_elem.css("-moz-transform","rotate(" + rad + "deg)");
            center_elem.css("-webkit-transform","rotate(" + rad + "deg)");
            center_elem.css("-o-transform","rotate(" + rad + "deg)");
        }, 100);
    }).mouseup(function() {
        clearInterval(intervalId);
        var currentPos = center_elem.position();
        drag_elem.animate({
            top: currentPos.top,
            left: currentPos.left
            }, "slow", function() {
        });
    });
}
