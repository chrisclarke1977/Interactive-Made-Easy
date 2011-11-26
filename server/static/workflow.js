$(document).ready(function(){
    $(".slide_list").sortable({
        axis        : 'y',              // Only vertical movements allowed
        containment : 'window',         // Constrained by the window
        update      : function(){       // The function is called after the todos are rearranged

            // The toArray method returns an array with the ids of the todos
            var arr = $(".slide_list").sortable('toArray');

            // Striping the slide- prefix of the ids:
            arr = $.map(arr,function(val,key){
                return val.replace('slide-', '');
            });

            $.get("/workflow/", {action: 'rearrange', positions: arr});
        },

        /* Opera fix: */
        stop: function(e, ui) {
            ui.item.css({'top':'0', 'left':'0'});
        }
    });

    var currentTODO;

    // If any link in the todo is clicked, assign
    // the todo item to the currentTODO variable for later use.

    $('.slide_list a').live('click', function(e){
        currentTODO = $(this).closest('.slide_class');
        console.log("1", currentTODO.attr('id'));
        currentTODO.data('id', currentTODO.attr('id').replace('slide-',''));

        e.preventDefault();
    });

    // Configuring the delete confirmation dialog
    $("#dialog-confirm").dialog({
        resizable: false,
        height:200,
        modal: true,
        autoOpen:false,
        buttons: {
            'Delete item': function() {
                $.get("/workflow/",{"action": "delete", "id": currentTODO.data('id')}, function(msg){
                    currentTODO.remove();
                })

                $(this).dialog('close');
            },
            Cancel: function() {
                $(this).dialog('close');
            }
        }
    });

    $("#create-workflow").dialog({
        resizable: false,
        height:200,
        modal: true,
        autoOpen:false,
        buttons: {
            'Create list': function() {
                $.get("/workflow/", {"action": "create_workflow", "name": $("#workflow_name").val()}, function(msg){
                    $("#workflow_name").val('');
                });
                $(this).dialog('close');
            },
            Cancel: function() {
                $(this).dialog('close');
            }
        }
    });

    $('.slide_list a.delete').live('click',function(){
        $("#dialog-confirm").dialog('open');
    });
});
