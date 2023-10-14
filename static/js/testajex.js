function Like(slug, Pk){
    var element = document.getElementById('liked')
    var count = document.getElementById('count')
    $.get(`/blogs/detail/${slug}/like/${Pk}`).then(response =>{
        if(response['response'] === "liked") {
            element.className = "fa fa-heart"
            count.innerText = Number(count.innerText) + 1
        }else{
            element.className = "fa fa-heart-o"
            count.innerText = Number(count.innerText) - 1

        }
    })
}

