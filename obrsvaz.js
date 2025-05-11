document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('feedbackForm');
    const errorElement = document.createElement('div');
    errorElement.className = 'error-message';
    errorElement.style.display = 'none';
    form.prepend(errorElement);

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        errorElement.style.display = 'none';

        // Валидация формы перед отправкой
        const telephone = form.telephone.value.trim();
        if (!/^(\+7|8)\d{10}$/.test(telephone)) {
            showError('Пожалуйста, введите корректный номер телефона (+7XXX или 8XXX)');
            form.telephone.focus();
            return;
        }

        // Подготовка данных формы
        const formData = {
            name: form.name.value.trim(),
            telephone: telephone,
            email: form.email.value.trim(),
            subject: form.subject.value.trim(),
            message: form.message.value.trim()
        };

        // Валидация обязательных полей
        if (!formData.name || !formData.email || !formData.subject || !formData.message) {
            showError('Пожалуйста, заполните все обязательные поля');
            return;
        }

        try {
            // Показываем индикатор загрузки
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn.textContent;
            submitBtn.disabled = true;
            submitBtn.textContent = 'Отправка...';

            const response = await fetch('/feedback', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();

            if (!response.ok) {
                throw new Error(result.message || 'Произошла ошибка при отправке');
            }

            // Успешная отправка
            form.reset();
            showSuccess('Сообщение успешно отправлено!');
        } catch (error) {
            console.error('Ошибка:', error);
            showError(error.message || 'Ошибка соединения с сервером');
        } finally {
            // Восстанавливаем кнопку
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = false;
                submitBtn.textContent = originalBtnText;
            }
        }
    });

    // Функция показа ошибки
    function showError(message) {
        errorElement.textContent = message;
        errorElement.style.display = 'block';
        errorElement.style.color = '#d32f2f';
        errorElement.style.backgroundColor = '#ffebee';
        errorElement.style.padding = '10px';
        errorElement.style.marginBottom = '15px';
        errorElement.style.borderRadius = '4px';
    }

    // Функция показа успешного сообщения
    function showSuccess(message) {
        errorElement.textContent = message;
        errorElement.style.display = 'block';
        errorElement.style.color = '#388e3c';
        errorElement.style.backgroundColor = '#e8f5e9';
    }

    // Маска для телефона (опционально)
    const phoneInput = form.telephone;
    if (phoneInput) {
        phoneInput.addEventListener('input', function(e) {
            let value = this.value.replace(/\D/g, '');
            if (value.startsWith('7') && !value.startsWith('+7')) {
                value = '+7' + value.substring(1);
            } else if (value.startsWith('8')) {
                value = '+7' + value.substring(1);
            }
            this.value = value.substring(0, 12);
        });
    }
});