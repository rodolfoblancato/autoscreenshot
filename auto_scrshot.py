import subprocess
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

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
	number_of_attempts = 20
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

''' Cria um cabeçalho e insere data e hora nos screenshots''' 
def create_header(website, output_path, file_name, counter):
	try:
		with Image.open(output_path + file_name) as im:
			print('Gerando cabeçalho do screenshot ' + str(counter))
			new_name = 'edit_' + file_name
			im_with_header = add_margin(im, 80, 0, 0, 0, (220, 220, 220))
			im_edit = ImageDraw.Draw(im_with_header)
			date_now = datetime.now()
			date_text = date_now.strftime('%d/%m/%Y %H:%M')
			header_text = 'Website: ' + website + '\nData e hora do acesso: ' + date_text
			font = ImageFont.truetype('arial.ttf', 16)
			im_edit.multiline_text((10,10), header_text, (0, 0, 0), font=font)
			im_with_header.save(output_path + new_name, quality=95)
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
		create_header(website, output_path, file_name, counter)
		counter += 1

output_path = input('Pasta em que serão salvos os screenshots:')
input_file = input('Arquivo TXT com a lista de websites (deve ser incluído o caminho completo e a extensão):')
if output_path.startswith('"'):
	output_path = output_path[1:len(output_path)-1]
if input_file.startswith('"'):
	input_file = input_file[1:len(input_file)-1]
websites = []
with open(input_file) as websites_file:
	for line in websites_file:
		websites.append(line)
loop_websites(websites)