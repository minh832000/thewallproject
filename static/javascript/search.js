const url = window.location.href
const searchFormNav = document.getElementById('search-form-nav')
const searchPost = document.getElementById('search-post');
const searchLocation = document.getElementById('search-location');
const resultSearch = document.getElementById('result-search')
const resultLocation = document.getElementById('result-location')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
const sendSearchPost=(post) => {
    $.ajax({
        type: 'POST',
        url:"search-post/",
        data:{
            'csrfmiddlewaretoken':csrf,
            'post':post
        },
        success: (res) => {
            const data =res.data
            if(Array.isArray(data)){

                resultSearch.innerHTML=" "
                data.forEach((item=> {
                    resultSearch.innerHTML += `
                        <div class="item-search">${item.name}</div>
                    `
                    }))
            } else {
                if(searchPost.value.length > 0){
                    resultSearch.innerHTML = `<b> ${data}</b>`
                }
                else {
                    resultSearch.classList.add('not-visible')
                }
            }
        },
        error: (err) => {
            
        }
    })
}
searchPost.addEventListener('keyup', e=>{
    
    if(resultSearch.classList.contains('not-visible')){
        resultSearch.classList.remove('not-visible')
    }
    sendSearchPost(e.target.value)
})
$('html').click(function (e) {
    if(!(resultSearch.classList.contains('not-visible'))){
        if (e.target.id == 'result-search' ) {
            //do something

        } else {
            resultSearch.classList.add('not-visible')
        }
    }
});
$('html').click(function(e){
    if($(e.target).attr('class')==="item-search"){
        $('#search-post').val($(e.target).text())
    }
})
//--------------------------------------------------------------------------------------------
const sendSearchLocation=(loc) => {
    $.ajax({
        type: 'POST',
        url:"search-location/",
        data:{
            'csrfmiddlewaretoken':csrf,
            'loc':loc
        },
        success: (res) => {
            const data =res.data
            if(Array.isArray(data)){

                resultLocation.innerHTML=" "
                data.forEach((item=> {
                    resultLocation.innerHTML += `
                        <div class="item-search-loc">${item.location}</div>
                    `
                    }))
            } else {
                if(searchLocation.value.length > 0){
                    resultLocation.innerHTML = `<b> ${data}</b>`
                }
                else {
                    resultLocation.classList.add('not-visible')
                }
            }
        },
        error: (err) => {
            
        }
    })
}
searchLocation.addEventListener('keyup', e=>{
    
    if(resultLocation.classList.contains('not-visible')){
        resultLocation.classList.remove('not-visible')
    }
    sendSearchLocation(e.target.value)
})
$('html').click(function (e) {
    if(!(resultLocation.classList.contains('not-visible'))){
        if (e.target.id == 'result-location' ) {
            //do something

        } else {
            resultLocation.classList.add('not-visible')
        }
    }
});
$('html').click(function(e){
    if($(e.target).attr('class')==="item-search-loc"){
        $('#search-location').val($(e.target).text())
    }
})
