import pyautogui
import pyperclip
import time


pyautogui.PAUSE = 1
    #a cada comando ele espera um segundo

#aperta windows (comand + barra de espaço)
pyautogui.press("win")
#digita o nome do programa
pyautogui.write("notepad")
time.sleep(3)


# Move the mouse to the start of the text you want to select
pyautogui.moveTo(x=543, y=228)

# Click and hold the mouse button
pyautogui.doubleClick()

# Copy the selected text to the clipboard
pyautogui.hotkey('ctrl', 'c')

# Save the selected text as a variable
selected_text = pyperclip.paste()
print(selected_text)