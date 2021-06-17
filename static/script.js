$('button').click(function(e){
    var btns = document.querySelectorAll('button')

    for (let index = 0; index < btns.length; index++) {
        if(btns[index] == e.target){
            btns[index].setAttribute('class', "btn btn-outline-primary")
        }else {
            btns[index].setAttribute('class', "btn btn-outline-secondary")
        }
    }

    var name_scene = e.target.innerText
    var data = {'name': name_scene}
    $.ajax({
        url: "http://localhost:8000/api/",
        dataType: "json",
        method: 'post',
        data: data,
        success: function(resp){
        }
    });
});