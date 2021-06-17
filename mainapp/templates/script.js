const url = 'http://127.0.0.1:8000/api/'

function sendRequest(method, requestURL, data=null){
    return new Promise((resolve, reject) => {
       const xhr = new XMLHttpRequest()
       xhr.open(method, requestURL) 

       xhr.responseType = 'json'

       xhr.onload = () => {
           if(xhr.status >= 400){
               reject(xhr.response)
           }else{
               resolve(xhr.response)
           }
       }

       xhr.onerror = () => {
           reject(xhr.response)
       }
       xhr.send(data)
    })
}


function SwitchScene(scene_name){
    console.log(scene_name)
    $.ajax({
        type: "POST",
        url: 'http://127.0.0.1:8000/api/',
        data:{'name': scene_name},
        async:true,
        dataType : 'jsonp', 
        crossDomain:true,
        success: function(data, status, xhr) {
            alert(xhr.getResponseHeader('Location'));
        }
    });
}