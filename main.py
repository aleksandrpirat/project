meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            'РОФЛ': 'шутка',
            'ЩИЩ': 'одобрение или восторг',
            'КРИПОВЫЙ':  'страшный, пугающий',
            'АГРИТЬСЯ': 'злиться'
            }
            
print("Здравствуйте, дорогие пользователи бота! Этот бот является словарем сленговых слов и поможет вам с ними разобраться.")
word = input("Введите непонятное слово: ").upper()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Упс! Такого слова нет в словаре. Напишите в техподдержку и мы добавим значение неизвестного вам слова в наш словарь.")
