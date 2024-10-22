var swiper = new Swiper(".swiper", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    coverflowEffect: {
        rotate: 0,
        stretch: 0,
        depth: 100,
        modifier: 2,
        slideShadows: true
    },
    keyboard: {
        enabled: true
    },
    mousewheel: {
        thresholdDelta: 70
    },
    spaceBetween: 60,
    loop: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true
    }
});

document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting normally
  
    // Get the form data
    var formData = new FormData(event.target);
    var name = formData.get('name');
    var email = formData.get('email');
    var message = formData.get('message');
  
    console.log('Email:', email);
    console.log('Message:', message);
  });