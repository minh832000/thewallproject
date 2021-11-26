jQuery(document).ready(function($){
 // Slide review
    $('#previous').on('click', function(){
    // Change to the previous Card
        $('#card_' + currentCard).stop().fadeOut(1);
        decreaseCard();
        $('#card_' + currentCard).stop().fadeIn(1);
        });
        $('#next').on('click', function(){
        // Change to the next Card
        $('#card_' + currentCard).stop().fadeOut(1);
        increaseCard();
        $('#card_' + currentCard).stop().fadeIn(1);
    });
    var currentCard = 1;
    var totalCards = 3;
    function increaseCard() {
        ++currentCard;
        if(currentCard > totalCards) {
            currentCard = 1;
        }
    }
    function decreaseCard() {

        --currentCard;
        if(currentCard < 1) {
            currentCard = totalCards;
        }
    }
    window.setInterval(function() {
        $('#previous').click();
    }, 5000);


// Sự kiện thay đổi thông tin giới thiệu công việc
//Set cho mấy cái kia ẩn hết nè
$('#finance-introduce').hide();
//xử lý bấm từng cái chứ sao giờ
$(document).on('click', "#job-1", function() {
    $('#finance-introduce').hide(400);
    $('#design-introduce').show(400);
})
$(document).on('click', "#job-2", function() {
    $('#design-introduce').hide(400);
    $('#finance-introduce').show(400);
})



// slideshow swiper
    function toggleNavbar(collapseID) {
        document.getElementById(collapseID).classList.toggle("hidden");
        document.getElementById(collapseID).classList.toggle("block");
    }
    var swiper = new Swiper(".mySwiper-slide", {
        effect: "coverflow",
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: "auto",
        loop:"true",
        spaceBetween:32,
        coverflowEffect: {
            rotate: 0,
        },
    });


// Slide review người dùng The Wall
$('#previous-rv').on('click', function(){
    // Change to the previous Review
        $('#rv-' + currentReview).hide();
        decreaseReview();
        $('#rv-' + currentReview).show();
        });
        $('#next-rv').on('click', function(){
        // Change to the next Review
        $('#rv-' + currentReview).hide();
        increaseReview();
        $('#rv-' + currentReview).show();
    });
    var currentReview = 1;
    var totalReviews = 3;
    function increaseReview() {
        ++currentReview;
        if(currentReview > totalReviews) {
            currentReview = 1;
        }
    }
    function decreaseReview() {

        --currentReview;
        if(currentReview < 1) {
            currentReview = totalReviews;
        }
    }
    window.setInterval(function() {
        $('#previous-rv').click();
    }, 5000);
})

