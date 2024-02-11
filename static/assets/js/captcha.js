document.getElementById('refresh-captcha').addEventListener('click', function () {
    fetch("/captcha/refresh/", {
        method: "GET",
        headers: {"X-Requested-With": "XMLHttpRequest"},
        credentials: "same-origin"
    })
    .then(response => response.json())
    .then(data => {
        document.querySelector('.captcha').src = data['image_url'];
        document.getElementById('id_captcha_0').value = data['key']
    });
});