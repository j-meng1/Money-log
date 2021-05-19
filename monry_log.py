import csv
from datetime import datetime
import os
import pathlib
import pandas
import PySimpleGUI as sg

file = pathlib.Path("money_log.csv")

filename = "money_log.csv"

field = ['Date', 'Received from', 'Comapany', 'Amount']

# create a new file if file does not exist
if (not file.exists()):
    with open (filename, 'w') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=field)
        csvwriter.writeheader()

# insert input
def write_input(filename = filename): 
    with open (filename, 'a') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=field, quoting=csv.QUOTE_NONNUMERIC)
        row = {'Date':datetime.today().strftime('%Y-%m-%d'), 'Received from':values[0],'Company':values[1], 'Amount':values[2]}
        csvwriter.writerow(row)

# create a simple GUI
layout = [
    [sg.Text('Received from', size=(17, 1)), sg.InputText()],
    [sg.Text('Company', size=(17, 1)), sg.InputText()],
    [sg.Text('Amount', size=(17, 1)), sg.InputText()],
    [sg.Button('Submit'), sg.Button('Open File'), sg.Button('Exit') ]
]

window = sg.Window('money log', layout)

while (1):
    event, values = window.read()
    if event == 'Exit':
        break
    elif event == 'Submit':
        write_input()
    elif event == 'Open File':
        os.system('open money_log.csv')

window.close()
