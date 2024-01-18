#program1BaronRoksana.py

import PySimpleGUI as sg

layout = [[sg.Text("Baron Roksana")],
          [sg.Button("OK")],
          [sg.Image(key="-IMAGE-")],]

window = sg.Window("Program1",layout, resizable=True,
                   size=(800,600), finalize=True)
window["-IMAGE-"].update("image.png")

while True:
    event,values = window.read()
    if event=="OK" or event==sg.WIN_CLOSED:
        break

window.close()

