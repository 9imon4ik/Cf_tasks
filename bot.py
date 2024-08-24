import telebot
import main
import os

bot = telebot.TeleBot(os.environ['TOKEN'])


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     "Привет! Отправь мне ссылку на задачу на codeforces.com и я отправлю тебе похожие.")


@bot.message_handler(content_types=['text'])
def tasks(message):
    s = message.text
    if s[-1] == '/':
        s = s[:-1]
    url = s.split('/')
    if len(url) != 7:
        bot.send_message(message.chat.id, "Пожалуйста отправь корректную ссылку на задачу из архива codeforces.com.")
        return
    # bot.send_message(message.chat.id, ", ".join(url))
    if url[0] != 'https:' or url[1] != '' or url[2] != 'codeforces.com':
        bot.send_message(message.chat.id, "Пожалуйста отправь корректную ссылку на задачу из архива codeforces.com.")
        return
    contest_id = url[-2]
    index = url[-1]
    if url[3] == 'contest':
        if url[5] != 'problem':
            bot.send_message(message.chat.id,
                             "Пожалуйста отправь корректную ссылку на задачу из архива codeforces.com.")
            return
        contest_id = url[4]
    elif url[3] != 'problemset' or url[4] != 'problem':
        bot.send_message(message.chat.id, "Пожалуйста отправь корректную ссылку на задачу из архива codeforces.com.")
        return
    # bot.send_message(message.chat.id, contest_id + '/' + index)

    try:
        contest_id = int(contest_id)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста отправь корректную ссылку на задачу из архива codeforces.com.")
        return

    task = main.find_problem(contest_id, index)
    if task == -1:
        bot.send_message(message.chat.id, "Пожалуйста отправь корректную ссылку на задачу из архива codeforces.com.")
        return

    l = main.find_similar(main.tasks_parsed[task])[1:]
    s = ''
    for x in l:
        s += x['name'] + ', ' + 'https://codeforces.com/problemset/problem/' + str(x['contest_id']) + '/' + str(
            x['index']) + '\n'
    bot.send_message(message.chat.id, s)


bot.infinity_polling()
