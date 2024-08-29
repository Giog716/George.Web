// script.js

// Funcție pentru scroll smooth
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Funcție pentru validarea formularului de contact
document.querySelector('form').addEventListener('submit', function(e) {
    const name = document.getElementById('nume').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('mesaj').value;

    if (name === '' || email === '' || message === '') {
        alert('Toate câmpurile sunt obligatorii!');
        e.preventDefault();
    } else {
        alert('Mesajul a fost trimis cu succes!');
    }
});
