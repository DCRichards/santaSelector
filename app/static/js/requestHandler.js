var RequestHandler = (function($) {
    
    // TODO: place this in a config
    var URL = 'http://127.0.0.1:5000';
    
    var postUser = function(user, succ, err) {
      $.ajax({
            type: "POST",
            url: URL + '/user',
            error: err,
            success: succ,
            data: JSON.stringify(user),
            dataType: 'html',
            contentType: 'application/json'
        }); 
    };
    
    return {
        postUser: postUser
    };
    
}(jQuery));
