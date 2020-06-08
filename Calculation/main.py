import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('my window')
window.geometry('400x200')

title = tk.Label(window,
                 text='简易计算器',
                 bg='#cccccc',
                 font=('Microsoft YaHei', 16),
                 width=30,
                 height=2,
                 )
title.place(x=0, y=0)

body = tk.Label(window,
                text='',
                bg='#8fbc8f',
                font=('Microsoft YaHei', 16),
                width=30,
                height=20,
                )
body.place(x=0, y=62)

input_1_str = tk.StringVar()
input_1_str.set('')
input_1 = tk.Entry(window, textvariable=input_1_str, font=('Microsoft YaHei', 16), width=8, justify='right')
input_1.place(x=6, y=70)

sign_str = tk.StringVar()
sign_str.set('?')
sign = tk.Label(window,
                textvariable=sign_str,
                bg='#ffffff',
                font=('Microsoft YaHei', 16),
                width=2,
                height=1,
                justify='center'
                )
sign.place(x=112, y=70)

input_2_str = tk.StringVar()
input_2_str.set('')
input_2 = tk.Entry(window, textvariable=input_2_str, font=('Microsoft YaHei', 16), width=8, justify='right')
input_2.place(x=149, y=70)

deng = tk.Label(window,
                text='=',
                bg='#ffffff',
                font=('Microsoft YaHei', 16),
                width=2,
                height=1,
                justify='center'
                )
deng.place(x=255, y=70)

input_3_str = tk.StringVar()
input_3_str.set('')
input_3 = tk.Entry(window, textvariable=input_3_str, font=('Microsoft YaHei', 16), width=8, justify='right')
input_3.place(x=292, y=70)


def click_jia_button():
    sign_str.set('+')


bt_jia = tk.Button(window,
                   text='+',
                   font=('Microsoft YaHei', 16),
                   width=3,
                   height=1,

                   justify='center',
                   command=click_jia_button
                   )
bt_jia.place(x=6, y=120)


def click_jian_button():
    sign_str.set('-')


bt_jian = tk.Button(window,
                    text='-',
                    font=('Microsoft YaHei', 16),
                    width=3,
                    height=1,
                    justify='center',
                    command=click_jian_button
                    )
bt_jian.place(x=76, y=120)


def click_cheng_button():
    sign_str.set('×')


bt_cheng = tk.Button(window,
                     text='×',
                     font=('Microsoft YaHei', 16),
                     width=3,
                     height=1,
                     justify='center',
                     command=click_cheng_button
                     )
bt_cheng.place(x=146, y=120)


def click_chu_button():
    sign_str.set('÷')


bt_chu = tk.Button(window,
                   text='÷',
                   font=('Microsoft YaHei', 16),
                   width=3,
                   height=1,
                   justify='center',
                   command=click_chu_button
                   )
bt_chu.place(x=216, y=120)


def click_jisuan_button():
    try:
        a = int(input_1_str.get())
        b = int(input_2_str.get())
        s = sign_str.get()
        if s == '+':
            input_3_str.set(str(a + b))
        elif s == '-':
            input_3_str.set(str(a - b))
        elif s == '×':
            input_3_str.set(str(a * b))
        elif s == '÷':
            input_3_str.set(str(a / b))
    except Exception as e:
        tk.messagebox.showerror('计算错误', e)


bt_jisuan = tk.Button(window,
                      text='计算',
                      font=('Microsoft YaHei', 16),
                      width=5,
                      height=1,
                      justify='center',
                      command=click_jisuan_button
                      )
bt_jisuan.place(x=284, y=120)
window.mainloop()
