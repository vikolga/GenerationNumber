from tkinter import *
from random import sample

window = Tk()
img = PhotoImage(file = 'logo.gif')
small_img = PhotoImage.subsample(img, x = 4, y = 4)

# создаем виджеты
imgLbl = Label(window, image = small_img)
label_1 = Label(window, relief = 'groove', width = 2)
label_2 = Label(window, relief = 'groove', width = 2)
label_3 = Label(window, relief = 'groove', width = 2)
label_4 = Label(window, relief = 'groove', width = 2)
label_5 = Label(window, relief = 'groove', width = 2)
label_6 = Label(window, relief = 'groove', width = 2)
getBtn = Button(window)
resBtn = Button(window)


# добавляем виджеты на экран
imgLbl.grid(row = 1, column = 1, rowspan = 2)
label_1.grid(row = 1, column = 2, padx = 10)
label_2.grid(row = 1, column = 3, padx = 10)
label_3.grid(row = 1, column = 4, padx = 10)
label_4.grid(row = 1, column = 5, padx = 10)
label_5.grid(row = 1, column = 6, padx = 10)
label_6.grid(row = 1, column = 7, padx = 10)
getBtn.grid(row = 2, column = 2, columnspan = 4)
resBtn.grid(row = 2, column = 5, columnspan = 4)

# Инициирование переменных
label_1.configure(text = '...')
label_2.configure(text = '...')
label_3.configure(text = '...')
label_4.configure(text = '...')
label_5.configure(text = '...')
label_6.configure(text = '...')
resBtn.configure(state = DISABLED)

# Постоянные переменные
window.title('Генератор случайных чисел')
window.resizable(0, 0)
getBtn.configure(text = 'Получить числа')
resBtn.configure(text = 'Сбросить')

def pick():
    nums = sample(range(1, 49), 6)
    label_1.configure(text = nums[0])
    label_2.configure(text = nums[1])
    label_3.configure(text = nums[2])
    label_4.configure(text = nums[3])
    label_5.configure(text = nums[4])
    label_6.configure(text = nums[5])
    getBtn.configure(state = DISABLED)
    resBtn.configure(state = NORMAL)

def reset():
    label_1.configure(text = '...')
    label_2.configure(text = '...')
    label_3.configure(text = '...')
    label_4.configure(text = '...')
    label_5.configure(text = '...')
    label_6.configure(text = '...')
    getBtn.configure(state = NORMAL)
    resBtn.configure(state = DISABLED)

getBtn.configure(command = pick)
resBtn.configure(command = reset)

window.mainloop()
