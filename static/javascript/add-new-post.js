const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-inputt');
const resultBox = document.getElementById('result-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
const selectedSkill = document.getElementById('selected-skills')

const sendSearchData=(skill) => {
    $.ajax({
        type: 'POST',
        url:"search/",
        data:{
            'csrfmiddlewaretoken':csrf,
            'skill':skill
        },
        success: (res) => {
            const data =res.data
            if(Array.isArray(data)){

                resultBox.innerHTML=" "
                data.forEach((item=> {
                    resultBox.innerHTML += `
                        <div class="py-3">
                                <input class="form-check-input me-1 item-search" name="tag_skill" type="checkbox" id="${item.pk}" value="${item.name}" aria-label="...">
                                ${item.name}
                                </div>
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
const sendSkillData=(name,id)=>{
    $.ajax({
        type: 'POST',
        url:"add-skill/",
        data:{
            'csrfmiddlewaretoken':csrf,
            'id':id,
            'name':name
        },
        success: (res) => {
            const data =res.data
            selectedSkill.innerHTML += `<span class="px-3 py-1 me-2 id=${data[0].id}">${data[0].name}</span>`

        },
        error: (err) => {
            
        }
    })

}
$(document).on('change','.item-search',function(){
    if (this.checked === true){
            sendSkillData(this.value, this.id)
        }
})

searchInput.addEventListener('keyup', e=>{
    console.log(e.target.value);
    if(resultBox.classList.contains('not-visible')){
        resultBox.classList.remove('not-visible')
    }
    sendSearchData(e.target.value)
})