import subprocess
from PIL import Image, ImageDraw

''' Adiciona uma margem à imagem '''
def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

''' Gera um screenshot do site'''
def create_screenshot(website, output_file):
	print('Fazendo screenshot do site 1')
	subprocess.call('"C:/Program Files/Google/Chrome/Application/chrome.exe" --headless --screenshot="' + output_file + '" --hide-scrollbars --window-size=1366,2000 "' + website + '"')
	print('Criado screenshot do site 1')


''' Insere data e hora nos screenshots''' 
def create_header(screenshot_file):
	with Image.open(screenshot_file) as im:
		print('Gerando cabeçalho do screenshot 1')
		im_new = add_margin(im, 100, 0, 0, 0, (255, 255, 255))
		im_new.save('C:/Users/rodol/Downloads/print_edit_01.png', quality=95)
		print('Finalizado cabeçalho do screenshot 1')

''' Ler o arquivo txt com a lista de sites e chamar as funções'''
website = 'https://www.folha.uol.com.br/'
file_path = 'C:/Users/rodol/Downloads/print_01.png'
create_screenshot(website, file_path)
create_header(file_path)