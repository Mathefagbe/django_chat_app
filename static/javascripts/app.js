const inputs = document.createElement('input');

$(".followbtn").each(function (index, element) {
    var protocol=location.protocol.split(":")[0]
        $(element).on("click", function (e) {
            e.preventDefault()
            var token =  $('input[name="csrfmiddlewaretoken"]').attr("value"); 
            var btnElement=$(this)
            var parentElement=btnElement.parent()
            var userElement=parentElement.find(".user")
            var textContent=userElement.text()
        $.ajax({
            type: "POST",
            url:`${protocol}://${window.location.host}/follow/`,
            headers: {
                'X-CSRFToken': token
           },
            data: JSON.stringify({
                user:textContent
            }),
            dataType: "json",
            success: function (response) {
                if(response.status===200){
                    btnElement.text(response.data)
                }else{
                    alert(response.error)
                }
            },
            error:function(error){
                alert(error)
            }
        });
});
});


$("#avatar").on("click", function (e) {
    e.preventDefault()
    if ($("#userDropdown").css("display")==="block"){
        $("#userDropdown").hide();

    }else{
        $("#userDropdown").show();
    }
});

$("#profile_btn").on("click", function (e) {
    e.preventDefault()
    inputs.type = "file";
    inputs.setAttribute('accept','image/*')
    inputs.onchange=displays
    inputs.click();
    
});

function displays() {
    const file=inputs.files[0]
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.getElementById("profile-img")
            const avartar_img=document.getElementById("avatar")
            img.src = e.target.result;
            avartar_img.src=e.target.result
            uploadFile(file)
        };
        reader.readAsDataURL(file);
        
    }
}

function uploadFile(uploads) {
    var protocol=window.location.protocol
    var token =  $('input[name="csrfmiddlewaretoken"]').attr("value"); 
    const formdata=new FormData()
    formdata.append('profile',uploads)
    $.ajax({
        type: "POST",
        url: `${protocol}://${window.location.host}/upload/`,
        data: formdata,
        headers: {
            'X-CSRFToken': token
       },
        processData: false,
        contentType: false,
        success: function (response) {
            alert(response.data)
        },
        error:{

        }
    });
    
}