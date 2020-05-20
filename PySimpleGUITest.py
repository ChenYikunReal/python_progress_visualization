import PySimpleGUI as sg
import time

items = range(10)
for i, item in enumerate(items):
    sg.one_line_progress_meter('Progress Meter', i+1, len(items), '-key-')
    time.sleep(1)
