import subprocess
from PIL import Image, ImageDraw

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
	print('Fazendo screenshot do site ' + str(counter))
	subprocess.call('"C:/Program Files/Google/Chrome/Application/chrome.exe" --headless --screenshot="' + output_path + file_name + '" --hide-scrollbars --window-size=1366,2000 "' + website + '"')
	print('Criado screenshot do site ' + str(counter))


''' Insere data e hora nos screenshots''' 
def create_header(output_path, file_name, counter):
	with Image.open(output_path + file_name) as im:
		print('Gerando cabeçalho do screenshot ' + str(counter))
		new_name = 'edit_' + file_name
		im_new = add_margin(im, 100, 0, 0, 0, (100, 100, 100))
		im_new.save(output_path + new_name, quality=95)
		print('Finalizado cabeçalho do screenshot ' + str(counter))

''' Ler o arquivo txt com a lista de sites e chamar as funções'''
def loop_websites(websites_list):
	counter = 1
	for website in websites_list:
		file_name = 'screenshot_' + str(counter) + '.png'
		create_screenshot(website, output_path, file_name, counter)
		create_header(output_path, file_name, counter)
		counter += 1

output_path = 'C:/Users/rodol/Downloads/'
input_file = input('Arquivo TXT com a lista de websites (deve ser incluído o caminho completo e a extensão):')
websites = []
with open(input_file) as websites_file:
	for line in websites_file:
		websites.append(line)
loop_websites(websites)
