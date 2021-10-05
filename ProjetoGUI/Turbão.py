
from guizero import App, PushButton, Text, Box, Picture
import sys


def exitapp():
    sys.exit()

app = App(title="Mecmaq")
app.tk.attributes("-fullscreen", True)
#app.image("icone")
#picture = Picture(app, image="/home/pi/Pictures/TELA AUTOMAÇÃO FUNDO.png")

intro_Box = Box(app, width="fill", align="top", border=True )
intro = Text(intro_Box, text = "Selecione a cultura a ser tratada:")
intro.text_size = 18


app.display()