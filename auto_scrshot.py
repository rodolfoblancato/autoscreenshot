import subprocess
from PIL import Image, ImageDraw

'''Funções '''
def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

''' Passo 1 - Ler o arquivo txt com a lista de sites'''

''' Passo 2 - Gerar os screenshots'''

website = '"https://www.folha.uol.com.br/"'
output_file = '"C:/Users/rodol/Downloads/print_01.png"'
subprocess.call('"C:/Program Files/Google/Chrome/Application/chrome.exe" --headless --screenshot=' + output_file + ' --hide-scrollbars --window-size=1366,2000 ' + website)

''' Passo 3 - Inserir data e hora nos screenshots''' 

with Image.open("C:/Users/rodol/Downloads/print_01.png") as im:
	im_new = add_margin(im, 0, 0, 100, 0, (0, 0, 0))
	im_new.save('C:/Users/rodol/Downloads/print_rodape_01.png', quality=95)