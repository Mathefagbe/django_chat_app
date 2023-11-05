$(".nav").each(function (index, element) {
    $(element).on("click", function (e) {
        e.preventDefault()
        if(index==0){
           return window.location=`https://${window.location.host}/chats/`
        }else if(index==1){
           return  window.location=`https://${window.location.host}/following/`
        }else{
          return window.location=`https://${window.location.host}/people/`
        }
        
    });  
});

