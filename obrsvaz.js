document.getElementById('feedbackForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const formData = {
        name: this.name.value,
        email: this.email.value,
        subject: this.subject.value,
        message: this.message.value
    };

    try {
        const response = await fetch('/feedback', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });
        const result = await response.json();

        if(result.status === 'success') {
            alert('Сообщение отправлено!');
            this.reset();
        } else {
            alert('Ошибка при отправке: ' + (result.message || 'Неизвестная ошибка'));
        }
    } catch (error) {
        alert('Ошибка соединения с сервером: ' + error.message);
    }
});