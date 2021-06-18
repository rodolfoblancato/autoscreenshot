import subprocess
from PIL import Image, ImageDraw

''' Passo 1 - Ler o arquivo txt com a lista de sites'''

''' Passo 2 - Gerar os screenshots'''

website = '"https://www.folha.uol.com.br/"'
output_file = '"C:/Users/rodol/Downloads/print_01.png"'
subprocess.call('"C:/Program Files/Google/Chrome/Application/chrome.exe" --headless --screenshot=' + output_file + ' --hide-scrollbars --window-size=1366,2000 ' + website)

''' Passo 3 - Inserir data e hora nos screenshots''' 
with Image.open("C:/Users/rodol/Downloads/print_01.png") as img1:
    img2 = img1.crop( (0,-34,1366,2000) )  
    draw = ImageDraw.Draw(img2)
    draw.rectangle( (0,0,1366,34), fill="white" )
    draw.rectangle( (0,2000,1366,1366), fill="white" )
    del draw
    img2.save("C:/Users/rodol/Downloads/img2.png", "PNG", quality=75)