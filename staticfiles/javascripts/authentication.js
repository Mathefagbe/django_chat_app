$('#login').on("click",(e)=>{
    var protocol=location.protocol.split(":")[0]
    var token =  $('input[name="csrfmiddlewaretoken"]').attr("value"); 
    var username=$("#login-username").val()
    var password=$("#password").val()
    e.preventDefault()
    $("#spinner").show();
    $.ajax({
        type: "POST",
        url: `${protocol}://${window.location.host}/login/`,
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
                window.location=`${protocol}://${window.location.host}/chats/`
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
        url: `${window.location.protocol}://${window.location.host}/logout/`,
        headers: {
            'X-CSRFToken': token
       },
        dataType: "json",
        success: function (res) {
            if (res.status===200){
                window.location=`${window.location.protocol}://${window.location.host}/login/`
            } 
        },
        error:function(error){
            alert(error)
        }
        
    });
    
});