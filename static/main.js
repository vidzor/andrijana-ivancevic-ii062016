
$(document).ready(function(){

    list_all_users();

    $('.addUserDiv #add-user-btn').click(function(){
        var name = $('.addUserDiv #add-user-name').val().trim();
        var age = $('.addUserDiv #add-user-age').val().trim();
        var height = $('.addUserDiv #add-user-height').val().trim();

        if (name=='' || age=='' || height==''){
            alert(' Invalid input: Fill out all the fields. ');
            return;
        }

        var new_user = {
            'id':0, 'name':name, 'age':age, 'height':height,
            'datetime_format': '', 'creation_datetime': ''
        };
        add_user( new_user );
    });

    $('#search-users_input').on('keyup paste',function(){
        search_term = $(this).val().trim();
        if (search_term == ''){
            list_all_users();
            return;
        }
        $.ajax({
            method: "GET",
            contentType: "application/json",
            url: "/users/search/"+search_term,
            data: {}
        })
        .done(function( response ){
            $('.listUsersDiv').html( response );
            define_events();
        })
        .fail(function( xhr, textStatus, errorThrown ){
            alert(' Error ')
        });
    });

})
function define_events(){
    $('.listUsersTable').find('.td-with-xbtn').on('click','.remove-user-btn', function(){
        user_id2remove = $(this).attr('user-id');
        remove_user( user_id2remove );
    });
}

function add_user( new_user ){
    $.ajax({
        method: "POST",
        contentType: "application/json",
        url: "/users/add",
        data: JSON.stringify( new_user )
    })
    .done(function( response ){
        if (response == 'DONE'){
            list_all_users();
        }
    })
    .fail(function( xhr, textStatus, errorThrown ){
        alert(' Error ')
    });
}

function remove_user( user_id ){
    $.ajax({
        method: "DELETE",
        contentType: "application/json",
        url: "/users/remove/"+user_id,
        data: {}
    })
    .done(function( response ){
        if (response == 'DONE'){
            list_all_users();
        }
    })
    .fail(function( xhr, textStatus, errorThrown ){
        alert(' Error ')
    });
}

function list_all_users(){
    $.ajax({
        method: "GET",
        contentType: "application/json",
        url: "/users/getall",
        data: {}
    })
    .done(function( response ){
        $('.listUsersDiv').html( response )
        define_events();
    })
    .fail(function( xhr, textStatus, errorThrown ){
        alert(' Error ')
    })
    .always(function( msg ){
        // nothing
    });
}