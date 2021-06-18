import subprocess
from PIL import Image, ImageDraw, ImageFont

''' Adiciona uma margem à imagem'''
def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

''' Gera um screenshot do site'''
def create_screenshot(website, output_path, file_name, counter):
	attempt_counter = 1
	number_of_attempts = 5
	while attempt_counter < number_of_attempts + 1:
		print('Gerando screenshot do site ' + str(counter) + '. Tentativa ' + str(attempt_counter) + ' de ' + str(number_of_attempts))
		subprocess.call('"C:/Program Files/Google/Chrome/Application/chrome.exe" --headless --screenshot="' + output_path + file_name + '" --hide-scrollbars --window-size=1366,2000 "' + website + '"')
		attempt_counter += 1
		try:
			with Image.open(output_path + file_name) as im:
				print('Finalizado screenshot do site ' + str(counter))
				break
		except:
			pass

''' Insere data e hora nos screenshots''' 
def create_header(website, output_path, file_name, counter, text_font):
	try:
		with Image.open(output_path + file_name) as im:
			print('Gerando cabeçalho do screenshot ' + str(counter))
			new_name = 'edit_' + file_name
			im_new = add_margin(im, 100, 0, 0, 0, (200, 200, 200))
			im_new.save(output_path + new_name, quality=95)
			print('Finalizado cabeçalho do screenshot ' + str(counter))
	except:
		print('Falha ao gerar o screenshot do site ' + str(counter))
		print('Adicionando site ' + str(counter) + ' à lista de falhas (falhas.txt)')
		with open (output_path + 'falhas.txt', 'a') as failures:
			failures.write(website)
		print('Site ' + str(counter) + ' adicionado à lista de falhas. Passando para o próximo site')
		pass

''' Ler o arquivo txt com a lista de sites e chamar as funções'''
def loop_websites(websites_list):
	counter = 1
	zeroes = ''
	for website in websites_list:
		if counter < 10:
			zeroes = '000'
		elif counter < 100:
			zeroes = '00'
		elif counter < 1000:
			zeroes = '0'
		else:
			zeroes = ''
		file_name = 'screenshot_' + zeroes + str(counter) + '.png'
		create_screenshot(website, output_path, file_name, counter)
		create_header(website, output_path, file_name, counter, text_font)
		counter += 1

output_path = 'C:/Users/rodol/Downloads/'
input_file = input('Arquivo TXT com a lista de websites (deve ser incluído o caminho completo e a extensão):')
try:
	text_font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 10)
except:
	print('Problema ao carregar a fonte')
websites = []
with open(input_file) as websites_file:
	for line in websites_file:
		websites.append(line)
loop_websites(websites)