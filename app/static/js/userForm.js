var userForm = (function($, userList) {
    
    var addButton;
    var nameField;
    var emailField;
    var usersList;
    
    var init = function() {
        addButton = $('.btn-add-user');
        nameField = $('input.user-name');
        emailField = $('input.user-email');
        usersList = $('.userlist');
        addButton.click(onAddClicked);
    };
    
    var onAddClicked = function(e) {
        var userName = nameField.val();
        var userEmail = emailField.val();
        if (isValidName(userName) && isValidEmail(userEmail)) {
            RequestHandler.postUser({'name':userName, 'email':userEmail}, onAddSuccess, onAddFailed);
        }
    };
    
    var isValidName = function(name) {
        return name.length > 2;
    };
    
    var isValidEmail = function(email) {
        return email.length > 3 && email.indexOf('@') > -1;
    };
    
    var onAddSuccess = function(data, textStatus, jqXHR) {
        usersList.html(data);
        nameField.val('');
        emailField.val('');
        // we need to init here as the DOM has changed
        userList.init();
    };
    
    var onAddFailed = function(jqXHR, textStatus, errorThrown) {
        console.error(jqXHR);
    };
    
    return {
        init: init
    };
    
}(jQuery, userList));
