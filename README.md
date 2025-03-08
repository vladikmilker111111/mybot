# mybot
import telebot
from telebot import types
import datetime


BOT_TOKEN = '8170044011:AAFJ11Jng4xC3GTiDNRmBHns-z9f10iZZUA'  
bot = telebot.TeleBot("8170044011:AAFJ11Jng4xC3GTiDNRmBHns-z9f10iZZUA")


schedule_data = {
    "понедельник": [
        {"time": "10:00", "subject": "Математика (алгебра)", "teacher": "Иванов И.И."},
        {"time": "11:30", "subject": "Русский язык", "teacher": "Петрова А.С."},
        {"time": "13:00", "subject": "История", "teacher": "Сидоров В.К."}
    ],
    "вторник": [
        {"time": "10:00", "subject": "Литература", "teacher": "Петрова А.С."},
        {"time": "11:30", "subject": "Физика", "teacher": "Кузнецов П.Л."},
        {"time": "13:00", "subject": "Английский язык", "teacher": "Смирнова Е.Г."}
    ],
    "среда": [
        {"time": "10:00", "subject": "Химия", "teacher": "Кузнецов П.Л."},
        {"time": "11:30", "subject": "География", "teacher": "Сидоров В.К."},
        {"time": "13:00", "subject": "Математика (геометрия)", "teacher": "Иванов И.И."}
    ],
    "четверг": [
        {"time": "10:00", "subject": "Информатика", "teacher": "Смирнова Е.Г."},
        {"time": "11:30", "subject": "Обществознание", "teacher": "Сидоров В.К."},
        {"time": "13:00", "subject": "Русский язык", "teacher": "Петрова А.С."}
    ],
    "пятница": [
        {"time": "10:00", "subject": "Физкультура", "teacher": "Васильев Н.М."},
        {"time": "11:30", "subject": "Литература", "teacher": "Петрова А.С."}
    ]
}


# Функция для форматирования расписания в строку
def format_schedule(schedule):
    if not schedule:
        return "На этот день расписание не найдено.  Может, сегодня выходной? 😉"
    formatted_schedule = ""
    for lesson in schedule:
        formatted_schedule += f"🕒 {lesson['time']}: {lesson['subject']} ({lesson['teacher']})\n"
    return formatted_schedule


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("📚 Расписание на сегодня")
    item2 = types.KeyboardButton("🗓️ Расписание на всю неделю")
    markup.add(item1, item2)

    # Приветственное сообщение
    bot.send_message(message.chat.id,
                     "Привет, студент! 👋 Я бот онлайн-школы и помогу тебе узнать расписание занятий.  Выбери, что ты хочешь увидеть:",
                     reply_markup=markup)


# Обработчик текстовых сообщений (для кнопок)
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "📚 Расписание на сегодня":
        today = datetime.datetime.now().strftime("%A").lower()
        schedule = schedule_data.get(today, [])
        formatted_schedule = format_schedule(schedule)
        bot.send_message(message.chat.id, f"✨ Твое расписание на сегодня ({today}):\n{formatted_schedule}")

    elif message.text == "🗓️ Расписание на всю неделю":
        schedule_text = "📅 Расписание на всю неделю:\n\n"
        for day, schedule in schedule_data.items():
            schedule_text += f"*{day.capitalize()}*\n"  # Делаем дни недели жирным
            formatted_schedule = format_schedule(schedule)
            schedule_text += formatted_schedule + "\n"
        bot.send_message(message.chat.id, schedule_text, parse_mode="Markdown")

    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю 😕.  Воспользуйся кнопками!")


# Запуск бота
if __name__ == '__main__':
    print("Бот запущен!")
    bot.polling(none_stop=True)


