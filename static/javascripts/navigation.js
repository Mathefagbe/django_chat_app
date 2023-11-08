$(".nav").each(function (index, element) {
  var protocol=location.protocol.split(":")[0]
    $(element).on("click", function (e) {
        e.preventDefault()
        if(index==0){
           return window.location=`${protocol}://${window.location.host}/chats/`
        }else if(index==1){
           return  window.location=`${protocol}://${window.location.host}/following/`
        }else{
          return window.location=`${protocol}://${window.location.host}/people/`
        }
        
    });  
});

