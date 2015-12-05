var userForm = (function($, userList) {
    
    var addButton;
    var nameField;
    var emailField;
    var usersList;
    var errorMessage;
    var errorText;
    
    var init = function() {
        addButton = $('.btn-add-user');
        nameField = $('input.user-name');
        emailField = $('input.user-email');
        usersList = $('.userlist');
        errorMessage = $('.error-popup');
        errorText = $('.error-popup .error-text')
        addButton.click(onAddClicked);
    };
    
    var onAddClicked = function(e) {
        errorMessage.hide();
        var userName = nameField.val();
        var userEmail = emailField.val();
        if (!isValidName(userName)) {
            showError('Sorry, that name is too short!');
        } else if (!isValidEmail(userEmail)) {
            showError('Sorry, that\'s not a valid email! If you don\'t want to add one, you can leave it blank');
        } else {
            RequestHandler.postUser({'name':userName, 'email':userEmail}, onAddSuccess, onAddFailed);
        }
    };
    
    var isValidName = function(name) {
        return name.length > 2;
    };
    
    var isValidEmail = function(email) {
        return (email === '' || (email.length > 3 && email.indexOf('@') > -1));
    };
    
    var onAddSuccess = function(data, textStatus, jqXHR) {
        usersList.html(data);
        nameField.val('');
        emailField.val('');
        // we need to init here as the DOM has changed
        userList.init();
    };
    
    var onAddFailed = function(jqXHR, textStatus, error) {
        console.error(jqXHR);
    };
    
    var showError = function(message) {
        errorText.text(message);
        errorMessage.show();
    };
    
    return {
        init: init
    };
    
}(jQuery, userList));
