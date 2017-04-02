import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext
# 인스턴스를 생성한다.
win = tk.Tk()
# 제목을 설정한다.
win.title("Python GUI")
# 리사이즈를 방지한다.
win.resizable(0, 0)
# 라벨을 추가한다.
a_label = ttk.Label(win, text="HELLO PYTHON")
a_label.grid(column=0, row=0)
b_label = ttk.Label(win, text="WECLOME TO tKinter")
b_label.grid(column=0, row=1)
# 버튼을 클릭 이벤트
# 버튼을 생성하는 것보다 콜백함수를 먼저 만들어 줘야 한다.
def click_me():
    # 글자가 바뀌고
    action.configure(text="It's clicked!")
    # 라벨의 색이 빨간색으로 바뀐다.
    a_label.configure(foreground='red')
# 액션 버튼을 만들자.
action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=1, row=0)
# 이렇게 하면 비활성화 된다.
action.configure(state='disabled')
# 또다른 버튼을 만든다.
def click_me2():
    # 글자의 길이가 0 이상이면 텍스트를 바꾼다.
    if len(name.get()) > 0:
        action2.configure(text="Hello " + name.get())
    # 아니면 그냥 얼럿 창을 띄운다.
    else:
        messagebox.showinfo("Warning..", "Please input...")
# 버튼을 만든다.
action2 = ttk.Button(win, text="set name!", command=click_me2)
action2.grid(column=1, row=1)
# 텍스트 에디트에 넣을 글자를 먼저 이런식으로 정의하고
name = tk.StringVar()
# 텍스트 에디트를 만든다.
text_edit = ttk.Entry(win, width=10, textvariable=name)
text_edit.grid(column=0, row=3)
# 콤보박스에 넣을 문자를 먼저 정의하고
number = tk.StringVar()
# 라디오 버튼을 선언하고
radio_button = ttk.Combobox(win, width=10, textvariable=number)
# 안에 들어갈 요소를 정의하고
radio_button['values'] = (1, 2, 4, 42, 100)
radio_button.grid(column=1, row=3)
# 여기서 readonly를 선언하게 되면 키보드로 값을 변경할 수 없고, 오로지 마우스 선택만 먹힌다.
radio_button.configure(state='readonly')
# 기본값 설정
radio_button.current(0)
# 체크버튼을 만들어 본다.
# 3가지 종류다.
disabled_checked_val = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=disabled_checked_val, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)
# 언쳌
unchecked_val = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=unchecked_val)
check2.deselect()
check2.grid(column=1, row=4)
# 쳌
cheked_val = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=cheked_val)
check3.select()
check3.grid(column=2, row=4, sticky=tk.E)
# 스크롤이 되는 텍스트박스는 이렇게.
scr = scrolledtext.ScrolledText(win, width=30, height=3, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)
# 프로그램 시작!
win.mainloop()

