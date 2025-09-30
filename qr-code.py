import pyautogui
import qrcode


img = qrcode.make('Seja bem vindo!!!')

type(img)
img.save("saudacao.png")