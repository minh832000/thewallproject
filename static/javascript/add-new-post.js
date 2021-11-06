const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-inputt');
const resultBox = document.getElementById('result-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

const sendSearchData=(skill) => {
    $.ajax({
        type: 'POST',
        url:"search/",
        data:{
            'csrfmiddlewaretoken':csrf,
            'skill':skill
        },
        success: (res) => {
            console.log(res)
            const data =res.data
            if(Array.isArray(data)){
                resultBox.innerHTML=" "
                data.forEach((item=> {
                    resultBox.innerHTML += `
                        <div class="item-search" id= ${item.pk}> ${item.name} </div>
                    `
                }))
            } else {
                if(searchInput.value.length > 0){
                    resultBox.innerHTML = `<b> ${data}</b>`
                }
                else {
                    resultBox.classList.add('not-visible')
                }
            }
        },
        error: (err) => {
            
        }
    })
}
const sendSkillData=(id)=>{
    $.ajax({
        type: 'POST',
        url:"add-skill/",
        data:{
            id: id
            
        },
        success: (res) => {
            console.log(res)
        }
    })
}
$(document).on('click','.item-search',function(){
    console.log(this.id)
    sendSkillData(this.id)
})
searchInput.addEventListener('keyup', e=>{
    console.log(e.target.value);
    if(resultBox.classList.contains('not-visible')){
        resultBox.classList.remove('not-visible')
    }
    sendSearchData(e.target.value)
})