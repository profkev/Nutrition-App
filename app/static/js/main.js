// Example JavaScript function to alert users when a form is submitted
document.addEventListener('DOMContentLoaded', function () {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function (event) {
            alert('Form submitted!');
        });
    });
});
