pole_dlya_igri_size = 3

#игровое поле
pole = ["1","2","3","4","5","6","7","8","9"]


def pole_vivel():
	
	print("-" * 4 * pole_dlya_igri_size)
	for i in range(pole_dlya_igri_size):
		print((" " * 3 + "|" )* 3)
		print("", pole[i*3], "|", pole[1 + i*3], "|", pole[2 + i*3], "|")
		print(("_" * 3 + "|")*3)

def igryshka_topchik(hodim, char):
	
	if	(hodim > 9 or hodim < 1 or pole[hodim-1] in ("X", "O")):
		return False
		
	pole[hodim-1] = char
	return True

def pobeda():
	return False

def change_pole(hodim, tekushij_igrok):
	index = pole.index(hodim)
	pole[index] = tekushij_igrok

def pognali():
	
	tekushij_igrok = "X"

	step = 1

	pole_vivel()
	
	while (step<10):
		hodim = input("Ходит игрок " + tekushij_igrok + ". Введите номер поля (0 - выход):")
		# добавить проверку на идентичность чисел
		print("Наше число:", hodim)
		if (hodim == "0"):
			break
		change_pole(hodim, tekushij_igrok)
		pole_vivel()
		if pobeda():
			Print(tekushij_igrok)

		step += 1
		if step % 2 == 0:
			tekushij_igrok = "O"
		else:
			tekushij_igrok = "X"

print("каждая победа +10 к iq")
pognali()
input()

