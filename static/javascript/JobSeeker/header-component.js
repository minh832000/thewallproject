// Array contain the latest and have not seen notifications
const array_of_notifications = [];

// Getting the user's list of notifications when loading page 
const notifications = document.querySelectorAll('.numbers_of_notifications');
const menuNotifications = document.querySelectorAll('.dropdown_menu_notifications');
console.log(menuNotifications.length);

window.addEventListener('load', async function() {
    let url = 'http://127.0.0.1:8000/notifications/';
    const res = await this.fetch(url);
    if(!res.ok){
        let message = `An error has occured: ${res.status}`;
        throw new Error(message);
    }
    const data = await res.json();
    
    // Displaying the numbers of notifications 
    for(let i = 0; i < notifications.length; i++){
        notifications[i].classList.add('text-light');
        notifications[i].textContent = data['numbers_of_notifications'];
    }

    // Store list of notifications to array
    data['list_of_notifications'].forEach(i => {
        array_of_notifications.push(i);
    })
  
    array_of_notifications.forEach(i => {
        let node = document.createElement('LI');
        node.classList.add('dropdown-item');
        node.classList.add('font-WorkSans-Regular');
        node.classList.add('py-3');
        let textNode;
        // Format datetime
        let d = new Date(i['created_at']);
        let t = d.toLocaleString();
        if(i['type_of_notification'] == 1){
            node.id = i['id'];
            textNode = document.createTextNode(`Bạn vừa tạo tài khoản vào lúc ${t}`);
            node.appendChild(textNode);
            for(let i = 0; i < menuNotifications.length; i++){
                menuNotifications[i].appendChild(node);
            }
        }
        if(i['type_of_notification'] == 2){
            node.id = i['id'];
            textNode = document.createTextNode(`Bạn vừa cập nhật hồ sơ vào lúc ${t}`);
            node.appendChild(textNode);
            for(let i = 0; i < menuNotifications.length; i++){
                menuNotifications[i].appendChild(node);
            }
        }
        if(i['type_of_notifications'] == 3){

        }
    })
})

jQuery(document).ready(function($){
    //xử lý đóng mở menu
    $(document).on('click', ".icon_close_menu, .over", function() {
        $('.over, .nav, .header-nav').fadeOut(300 , function() {
                $('.over').remove();
        });
        $('.nav').hide();
        $('.header-nav').hide();
        $('.icon_show_menu').show(100)
        return false;
    });
    // Xử lý mở menu
    $('.icon_show_menu').click(function(){
        $('.nav').show();
        $('.header-nav').show();
        $('body').append('<div class="over">');
        $('.over').fadeIn();
    })

    // Repeating the ajax call to get the user's list of notifications 
    const getNotifications = async () => {
        let url = 'http://127.0.0.1:8000/notifications/';
        // Fetching the list of notifications from server
        const res = await fetch(url);
        // Checking response
        if(!res.ok){
            let message = `An error has occured: ${res.status}`;
            throw new Error(message);
        }
        // Convert response to json
        const data = await res.json();
        
        // Change the number of notifications
        for(let i = 0; i < notifications.length; i++){
            notifications[i].textContent = data['numbers_of_notifications'];
        }

        data['list_of_notifications'].forEach(i => {
            const checkId = array_of_notifications.every(k => {
                return i['id'] != k['id'];
            })
        
            if(checkId){
                array_of_notifications.unshift(i);
                //Add the latest and have not seen notification
                let node = document.createElement('LI');
                node.classList.add('dropdown-item');
                node.classList.add('font-WorkSans-Regular');
                node.classList.add('py-3');
                let textNode;
                // Format datetime
                let d = new Date(i['created_at']);
                let t = d.toLocaleString();
                if(i['type_of_notification'] == 1){
                    node.id = i['id'];
                    textNode = document.createTextNode(`Bạn vừa tạo tài khoản vào lúc ${t}`);
                    node.appendChild(textNode);
                    for(let i = 0; i < menuNotifications.length; i++){
                        menuNotifications[i].appendChild(node);
                    }
                }
                if(i['type_of_notification'] == 2){
                    node.id = i['id'];
                    textNode = document.createTextNode(`Bạn vừa cập nhật hồ sơ vào lúc ${t}`);
                    node.appendChild(textNode);
                    for(let i = 0; i < menuNotifications.length; i++){
                        menuNotifications[i].insertBefore(node, menuNotifications[i].firstChild)
                    }
                }
                if(i['type_of_notifications'] == 3){
        
                }                
            }
        })
    };
    setInterval(getNotifications, 3000);
})