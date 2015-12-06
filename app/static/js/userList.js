var userList = (function($, RequestHandler) {
    
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
        // ensure click only fires if we're clicking the item
        if (!$(e.target).is('.btn-delete')) {
            var userId = e.currentTarget.classList[1].split('-')[2];
            RequestHandler.getMatch(userId, onGetMatchSuccess, onGetMatchFailed);
        }
    };
    
    var onDeleteClicked = function(e) {
        var userId = e.currentTarget.classList[3].split('-')[2];
        RequestHandler.deleteUser(userId, onDeleteSuccess, onDeleteError);
    };
    
    var onDeleteSuccess = function(data, textStatus, jqXHR) {
        usersList.html(data);
        // refresh to catch DOM update
        init();
    };
    
    var onDeleteError = function(jqXHR, textStatus, error) {
        console.error('Error: ' + jqXHR.status + ' ' + jqXHR.statusText);
    };
    
    var onGetMatchSuccess = function(data, textStatus, jqXHR) {
        alert('your match is: ' + data.name + ' ' + data.email);
    };
    
    var onGetMatchFailed = function(jqXHR, textStatus, error) {
        console.error('Error: ' + jqXHR.status + ' ' + jqXHR.statusText);
    };
    
    return {
        init: init
    };
    
}(jQuery, RequestHandler));
