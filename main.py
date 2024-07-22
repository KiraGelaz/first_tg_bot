from telebot import TeleBot, types
from text_to_speech import text_to_speech
import os

os.environ["SUNO_OFFLOAD_CPU"] = "True"
os.environ["SUNO_USE_SMALL_MODELS"] = "True"

TOKEN = '6831186333:AAE9l-GIpW77BH0PauqbpylnvqyHU0UORuQ'
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    answer = f'<b>Привет!</b> <u>{message.from_user.first_name}</u> <u>{message.from_user.last_name}</u>'
    bot.send_message(message.chat.id, text=answer, parse_mode='html')

@bot.message_handler(commands=['speech'])
def duck(message):
    text = ' '.join(message.text.split(' ')[1:])
    text_to_speech(text)
    with open('bark_generation.wav', 'rb') as f:
        bot.send_audio(message.chat.id, f)

if __name__ == '__main__':
    bot.polling(non_stop=True)