#подключаем бота
import cleverbot_io

def give_name():
	#даем имя боту
	name = ''
	name = str(input('Введите имя бота: '))
	return(name)
	
def choose_action():
	action = 9
	while action not in (1,0):	
		print ('Введите следующие цифры для действий: 0 = Выйти 1 = Поболтать')
		action = int(input())
	return(action)
	
def talk(name):
	print('А как тебя зовут, представься')
	my_name = str(input())
	print('Ну давай поговорим, предлагай тему, только скажи когда тебе пора уходить')
	text = ''
	while text not in ('Пока', 'пока', 'До свидания', 'до свидания', 'Мне пора' 'мне пора'):
		text = str(input(my_name + ':'))
		print(name + ':' + bot.ask(text))
	
#def starving():
#функция голода, пока сложновато

#def feeding():
#тоже потом

name = give_name()
#прописываем боту настройки
bot = cleverbot_io.set(user='31DoSUX6zhav4sqj', key='PG1LHunpXtrxPKOl7UalSqyoWnUdJ6j0', nick=name)
while True:
	var = choose_action()
	if var == 0:
		break
	elif var == 1:
		talk(name)
	else:
		pass

	
			
