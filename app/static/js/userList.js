var userList = (function($) {
    
    var usersList;
    var userListItems;
    var deleteButton;
    
    var init = function() {
        usersList = $('.userlist');
        userListItems = $('li.list-group-item');
        deleteButton = $('.btn-delete');
        userListItems.click(onListItemClicked);
        deleteButton.click(onDeleteClicked);
    };
    
    var onListItemClicked = function(e) {
        var userId = e.currentTarget.classList[1].split('-')[2];
    };
    
    var onDeleteClicked = function(e) {
        var userId = e.currentTarget.classList[3].split('-')[2];
    };
    
    return {
        init: init
    };
    
}(jQuery));
