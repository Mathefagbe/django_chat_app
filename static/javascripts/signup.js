$('#sign-up').on("click",(e)=>{
    var token =  $('input[name="csrfmiddlewaretoken"]').attr("value"); 
    var username = $("#username").val()
    var  fullName = $("#full-name").val()
    var password = $("#password").val()
    var confirm_password = $("#confirm-password").val()
    var email = $("#email").val()
    e.preventDefault()
    $("#spinner").show();
    if(password==confirm_password){
    $.ajax({
        type: "POST",
        url: `https://${window.location.host}/sign-up/`,
        headers: {
            'X-CSRFToken': token
       },
        data: JSON.stringify(
            {username:username,
            password:password,
            email:email,
            full_name:fullName,
        }
        ),
        dataType: "json",
        success: function (res) {
            if (res.status===201){
                $("#spinner").hide();
                window.location=`https://${window.location.host}/login/`
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
}else{
    alert("password does not match")
    $("#spinner").hide();
}
    
})
