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
    
    var getMatch = function(id, succ, err) {
      $.ajax({
            type: "GET",
            url: URL + '/match/'+id,
            error: err,
            success: succ,
            dataType: 'html'
        }); 
    };
    
    var deleteUser = function(id, succ, err) {
      $.ajax({
            type: "DELETE",
            url: URL + '/user/'+id,
            error: err,
            success: succ,
            dataType: 'html'
        }); 
    };
    
    return {
        postUser: postUser,
        getMatch: getMatch,
        deleteUser: deleteUser
    };
    
}(jQuery));
