$('#login').on("click",(e)=>{
    var token =  $('input[name="csrfmiddlewaretoken"]').attr("value"); 
    var username=$("#login-username").val()
    var password=$("#password").val()
    e.preventDefault()
    $("#spinner").show();
    $.ajax({
        type: "POST",
        url: `https://${window.location.host}/login/`,
        headers: {
            'X-CSRFToken': token
       },
        data: JSON.stringify(
            {username:username,
            password:password,}
        ),
        dataType: "json",
        success: function (res) {
            if (res.status===200){
                window.location=`https://${window.location.host}/chats/`
                $("#spinner").hide();
            }else{
                alert(message=res.error)
                $("#spinner").hide();
            }  
        },
        error:function(error){
            alert(error)
            $("#spinner").hide();
        }
        
    });
    
})



$("#logout").on("click", function (e) {
    e.preventDefault()
    var token =  $('input[name="csrfmiddlewaretoken"]').attr("value"); 
    $.ajax({
        type: "POST",
        url: `https://${window.location.host}/logout/`,
        headers: {
            'X-CSRFToken': token
       },
        dataType: "json",
        success: function (res) {
            if (res.status===200){
                window.location=`https://${window.location.host}/login/`
            } 
        },
        error:function(error){
            alert(error)
        }
        
    });
    
});