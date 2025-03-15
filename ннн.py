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



def format_schedule(schedule):
    if not schedule:
        return "На этот день расписание не найдено.  Может, сегодня выходной? 😉"
    formatted_schedule = ""
    for lesson in schedule:
        formatted_schedule += f"🕒 {lesson['time']}: {lesson['subject']} ({lesson['teacher']})\n"
    return formatted_schedule


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("📚 Расписание на сегодня")
    item2 = types.KeyboardButton("🗓️ Расписание на всю неделю")
    item3 = types.KeyboardButton("🦾 Информация о боте")
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Привет, студент! 👋 Я бот онлайн-школы и помогу тебе узнать расписание занятий.  Выбери, что ты хочешь увидеть:",
                     reply_markup=markup)


info_text = """
🎓 Привет, дорогой пользователь. Данная функция позволит тебе узнать все возможные команды нашего бота, а также этот бот поможет тебе узнать расписание занятий онлайн-школы.
Доступные команды:
    /start - Начать работу с ботом.
    /info - Получить информацию о боте.
    
Кнопки:
    📚 Расписание на сегодня - Показать расписание на текущий день.
    🗓️ Расписание на всю неделю - Показать расписание на все дни недели.
    """



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
            schedule_text += f"*{day.capitalize()}*\n"  
            formatted_schedule = format_schedule(schedule)
            schedule_text += formatted_schedule + "\n"
        bot.send_message(message.chat.id, schedule_text, parse_mode="Markdown")
    elif message.text == "🦾 Информация о боте":
        bot.send_message(message.chat.id, info_text)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю 😕.  Воспользуйся кнопками!")



# Запуск бота
if __name__ == '__main__':
    print("Бот запущен!")
    bot.polling(none_stop=True)