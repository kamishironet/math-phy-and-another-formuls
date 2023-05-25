from tkinter import *
from tkinter import ttk,messagebox 
import tkinter

def Vieta():
    messagebox.showinfo('Виета', 'x^2+px+q=0    D>= 0   x1+x2 = -p  x1 * x2=q')

def Disc():
    messagebox.showinfo('дискриминант', 'D=b^2 − 4ac    x1,2 = (-b+-**D)/2')

def formM_a_b2():
    messagebox.showinfo('сокращенное умножение', '(a+b)^2 = a^2+2ab+b^2')

def formM_a__b2():
    messagebox.showinfo('сокращенное умножение', '(a-b)^2 = a^2-2ab+b^2')

def formM_a_b3():
    messagebox.showinfo('сокращенное умножение', '(a+b)^3 = a^3+3a^2b+3ab^2+b^3')

def formM_a__b3():
    messagebox.showinfo('сокращенное умножение', '(a-b)^3 = a^3-3ab^2+3ab^2-b^3')

def formM_a2__b2():
    messagebox.showinfo('сокращенное умножение', 'a^2-b^2=(a-b)(a+b)')

def formM_a3_b3():
    messagebox.showinfo('сокращенное умножение', 'a^3+b^3=(a+b)(a^2-ab+b^2)')

def formM_a3__b3():
    messagebox.showinfo('сокращенное умножение', 'a^3-b^3=(a-b)(a^2+ab+b^2)')

def formFA():
    messagebox.showinfo('Сила Архимеда', 'Fa = r*g*V')
def formFF():
    messagebox.showinfo('Энергия','F кин = mv^2/2, E пот = m*g*h ')
def formFEl():
    messagebox.showinfo('Электрический ток', 'U=A/q, I=q/t')
def formFR():
    messagebox.showinfo('Сопротивление', 'R=U/I, 1/R = 1/R1 + 1/R2')
def formFQ():
    messagebox.showinfo('Кол-во теплоты', 'A=Q = IUt')
def formFN():
    messagebox.showinfo('Мощность','N=A/t')
def pravRH():
    messagebox.showinfo('Правило правой руки','Правило правой руки: «Если ладонь правой руки расположить так, чтобы в неё входили силовые линии магнитного поля, а отогнутый большой палец направить по движению проводника, то четыре вытянутых пальца укажут направление индукционного тока»')
def pravLH():
    messagebox.showinfo('Правило левой руки', 'Если левую руку расположить так, чтобы линии магнитной индукции входили в ладонь перпендикулярно ей, а четыре пальца указывали направление тока, то отставленный большой палец покажет направление действующей на проводник силы Ампера.')
def pamC():
    messagebox.showinfo('3H2', '3H2 - три молекулы водорода, каждая из которых состоит из двух атомов хим элемента водорода')
def pamC1():
    messagebox.showinfo('10H2SO4','10H2SO4 - десять молекул серной кислоты, содержащих по два атома водорода, одному атому серы и четрые авома кислорода')
def pamC2():
    messagebox.showinfo('2Mg(OH)2', '2Mg(OH)2 - две формульные единицы гидроксида магния, состоящие из одного атома магния, двух атомов кислорода и двух атомов водорода')
def pamC3():
    messagebox.showinfo('Валентность','Валентность - свойство атома химического элемента присоединять или замещать определенное число атомов другого элемента')
def pamC4():
    messagebox.showinfo('Моль','Моль - количество вещества, в котором содержится число частиц равное числу атомов в 0.012 кг углерода^12 C')
def pamC5():
    messagebox.showinfo('Атом','Атом- мельчайшая химическая неделимая частица вещества')

def text_menu_inst():
    messagebox.showinfo('welcome', ' Привет, это программа - сборник формул по некоторым предметам')

def txt_inst():
    messagebox.showinfo('Instruction', 'Вверху находяться вкладки с предметами, нужно выбрать предмет, а затем нажмите на формулу, вам будет представленна более полная форма ')





window=Tk()
f_top = Frame(window)
f_bot = Frame(window)

window.title("formuls app")
window.geometry('300x500')
tab_control = ttk.Notebook(window)
tab = ttk.Frame(tab_control)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab_control.add(tab,text='menu')
tab_control.add(tab1, text='math')
tab_control.add(tab2, text='Physics')
tab_control.add(tab3, text='chemistry')

lbl = Label(tab, text='')
lbl.grid(column=1000, row=1000)
lbl1 = Label(tab1, text='')
lbl1.grid(column=1000, row=1000)
lbl2 = Label(tab2, text='')
lbl2.grid(column=1000, row=1000)
lbl3 = Label(tab3, text='')
lbl3.grid(column=1000, row= 1000)

txt1 = Button(lbl, text="нажми что бы увидеть больше", command=text_menu_inst, padx=10, pady=10)
txt2 = Button(lbl, text="Инструкция", command=txt_inst, padx=10, pady=10 )

btn1 = Button(lbl1, text="дискриминант", command=Disc, padx=10, pady=10)
btn2 = Button(lbl1, text="формулы Виета", command= Vieta, padx=10, pady=10)
btn3 = Button(lbl1, text="су (a+b)^2 ", command=formM_a_b2, padx=10, pady=10)
btn4 = Button(lbl1, text="су (a-b)^2 ", command=formM_a__b2, padx=10, pady=10)
btn5 = Button(lbl1, text="су (a+b)^3 ", command=formM_a_b3, padx=10, pady=10)
btn6 = Button(lbl1, text="су (a-b)^3 ", command=formM_a__b3, padx=10, pady=10)
btn7 = Button(lbl1, text="су a^2-b^2 ", command=formM_a2__b2, padx=10, pady=10)
btn8 = Button(lbl1, text="су a^3+b^3", command=formM_a3_b3, padx=10, pady=10)
btn9 = Button(lbl1, text="су a^3-b^3", command=formM_a3__b3, padx=10, pady=10)

btn10 = Button(lbl2, text="Сила Архи", command=formFA,padx=10, pady=10)
btn11 = Button(lbl2, text="Энергия", command=formFF,padx=10, pady=10)
btn12 =Button(lbl2, text="Электр ток ", command=formFEl,padx=10, pady=10)
btn13 = Button(lbl2, text="Сопротивление", command=formFR,padx=10, pady=10)
btn14 = Button(lbl2, text="Кол-во Теплоты", command=formFQ, padx=10, pady=10)
btn15 = Button(lbl2 , text="Мощность", command=formFN, padx=10, pady=10)
btn16 = Button(lbl2, text="Правая рука", command=pravRH, padx=10, pady=10)
btn17 = Button(lbl2, text="Левая рука", command=pravLH,padx=10, pady=10)

btn18 = Button(lbl3, text="Атом", command=pamC5,padx=10, pady=10)
btn19 = Button(lbl3, text="Моль", command=pamC4,padx=10, pady=10)
btn20 = Button(lbl3, text="Валентность", command=pamC3,padx=10, pady=10)
btn21 = Button(lbl3, text="Пояснение формулы 1", command=pamC,padx=10, pady=10)
btn22 = Button(lbl3, text="Пояснение формулы 2", command= pamC1,padx=10, pady=10)
btn23 = Button(lbl3, text="Пояснение формулы 3", command= pamC2,padx=10, pady=10)


f_top.pack()
f_bot.pack()
txt2.pack(side=BOTTOM)
txt1.pack(side=BOTTOM)

btn1.pack(side=BOTTOM)
btn2.pack(side=BOTTOM)
btn3.pack(side=BOTTOM)
btn4.pack(side=BOTTOM)
btn5.pack(side=BOTTOM)
btn6.pack(side=BOTTOM)
btn7.pack(side=BOTTOM)
btn8.pack(side=BOTTOM)
btn9.pack(side=BOTTOM)
btn10.pack(side=BOTTOM)
btn11.pack(side=BOTTOM)
btn12.pack(side=BOTTOM)
btn13.pack(side=BOTTOM)
btn14.pack(side=BOTTOM)
btn15.pack(side=BOTTOM)
btn16.pack(side=BOTTOM)
btn17.pack(side=BOTTOM)
btn23.pack(side=BOTTOM)
btn22.pack(side=BOTTOM)
btn21.pack(side=BOTTOM)
btn20.pack(side=BOTTOM)
btn19.pack(side=BOTTOM)
btn18.pack(side=BOTTOM)

tab_control.pack(expand=1, fill='both') 

window.mainloop()