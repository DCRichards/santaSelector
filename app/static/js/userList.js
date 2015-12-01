var userList = (function($) {
    
    var usersList;
    var userListItems;
    
    var init = function() {
        usersList = $('.userlist');
        userListItems = $('li.list-group-item');
        userListItems.click(onListItemClicked);
    };
    
    var onListItemClicked = function(e) {
        var userId = e.currentTarget.classList[1].split('-')[2];
    };
    
    var onMatchSuccess = function(data, textStatus, jqXHR) {
        
    };
    
    var onMatchFailed = function(jqXHR, textStatus, errorThrown) {
        console.error(jqXHR);
    };
    
    return {
        init: init
    };
    
}(jQuery));
