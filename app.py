import os
from flask import Flask, request, jsonify, render_template, send_from_directory
from telegram import Bot
from telegram.error import TelegramError
import re

app = Flask(__name__)

app.template_folder = os.path.join(os.path.dirname(__file__), 'templates')
app.static_folder = os.path.join(os.path.dirname(__file__), 'static')

BOT_TOKEN = '7916793584:AAGGsNaSo4gAzfUsJ9HhwKg3jDaw-z43WHw'
CHAT_ID = 798039063


bot = Bot(token=BOT_TOKEN)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/Price')
def price():
    return render_template('Price.html')

@app.route('/price1')
def price1():
    return render_template('price1.html')

@app.route('/price2')
def price2():
    return render_template('price2.html')

@app.route('/price3')
def price3():
    return render_template('price3.html')


@app.route('/obrsvaz')
def obrsvaz():
    return render_template('obrsvaz.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/feedback', methods=['POST'])
def handle_feedback():
    try:
        data = request.json

        phone = data.get('telephone', '')
        if not re.match(r'^(\+7|8)\d{10}$', phone):
            return jsonify({'status': 'error', 'message': 'Неверный формат телефона. Используйте +7 или 8 и 10 цифр'}), 400
        
        message = (
            f"📩 Новое сообщение\n"
            f"👤 Имя: {data.get('name', 'Не указано')}\n"
            f"Телефон: {data.get('telephone', 'Не указано')}\n"
            f"📧 Email: {data.get('email', 'Не указано')}\n"
            f"📌 Тема: {data.get('subject', 'Без темы')}\n"
            f"✉️ Сообщение:\n{data.get('message', 'Пустое сообщение')}"
        )

        print(f"Отправка сообщения в чат {CHAT_ID}...")  # Логирование
        bot.send_message(chat_id=CHAT_ID, text=message)
        print("Сообщение отправлено успешно!")

        return jsonify({'status': 'success'}), 200
    
    except TelegramError as e:
        print(f"Ошибка Telegram: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500
    except Exception as e:
        print(f"Общая ошибка: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
