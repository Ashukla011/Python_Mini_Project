from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root,width=35,borderwidth=2,)
e.grid(column=0,row=0,padx=30,pady=50,columnspan=3)




def button_click(number):
  current = e.get()
  e.delete(0,END)
  e.insert(0,str(current)+str(number))

def Button_clear():
  e.delete(0,END)  

def Button_Add():
  first_num = e.get()
  global f_n 
  global math 
  math = 'addition'
  f_n = int(first_num)
  e.delete(0,END)

def Button_Sep():
  first_num = e.get()
  global f_n 
  global math 
  math ='septraction'
  f_n = int(first_num)
  e.delete(0,END)

def Button_Mul():
  first_num = e.get()
  global f_n 
  global math 
  math ='multiplication'
  f_n = int(first_num)
  e.delete(0,END)

def Button_Div():
  first_num = e.get()
  global f_n 
  global math 
  math ='division'
  f_n = int(first_num)
  e.delete(0,END)

def Button_Per():
  first_num = e.get()
  global f_n 
  global math 
  math ='percentage'
  f_n = int(first_num)
  e.delete(0,END)

def Button_Equal():
  second_num = e.get()
  e.delete(0,END)
  if math == 'addition':
   e.insert(0,f_n + int(second_num))

  if math == 'septraction':
   e.insert(0,f_n - int(second_num))

  if math == 'multiplication':
   e.insert(0,f_n * int(second_num))

  if math == 'division':
   e.insert(0,f_n / int(second_num))

  if math == 'percentage':
   e.insert(0,f_n * int(second_num))

button_1 = Button(root,text="1",padx=40,pady=20,bg='#5549eb',fg="#fff",border=None,command=lambda:button_click(1))
button_2 = Button(root,text="2",padx=40,pady=20,bg='#5549eb',fg="#fff",border=None,command=lambda:button_click(2))
button_3 = Button(root,text="3",padx=40,pady=20,bg='#5549eb',fg="#fff",border=None,command=lambda:button_click(3))

button_4 = Button(root,text="4",padx=40,pady=20,bg='#5549eb',fg="#fff",border=None,command=lambda:button_click(4))
button_5 = Button(root,text="5",padx=40,pady=20,bg='#5549eb',fg="#fff",border=None,command=lambda:button_click(5))
button_6 = Button(root,text="6",padx=40,pady=20,bg='#5549eb',fg="#fff",border=None,command=lambda:button_click(6))

button_7 = Button(root,text="7",padx=40,pady=20,bg='#5549eb',fg="#fff",border=None,command=lambda:button_click(7))
button_8 = Button(root,text="8",padx=40,pady=20,bg='#5549eb',fg="#fff",border=None,command=lambda:button_click(8))
button_9 = Button(root,text="9",padx=40,pady=20,bg='#5549eb',fg="#fff",border=None,command=lambda:button_click(9))

button_0 = Button(root,text="0",padx=40,pady=20,bg='#5549eb',fg="#fff",border=None,command=lambda:button_click(0))
button_equal = Button(root,text="=",padx=87,pady=20,bg='#5549eb',fg="#fff",border=None,command=Button_Equal)

button_clear = Button(root,text="C",padx=40,pady=20,bg='#5549eb',fg="#fff",border=None,command=lambda:Button_clear())
button_add = Button(root,text="+",padx=40,pady=20,bg='#5549eb',fg="#fff",border=None,command=Button_Add)
button_sep = Button(root,text="-",padx=40,pady=20,bg='#5549eb',fg="#fff",border=None, command=Button_Sep)

button_per = Button(root,text="%",padx=40,pady=20,bg='#5549eb',fg="#fff",border=None,command=Button_Per)
button_mul = Button(root,text="x",padx=40,pady=20,bg='#5549eb',fg="#fff",border=None,command=Button_Mul)
button_div = Button(root,text="/",padx=40,pady=20,bg='#5549eb',fg="#fff",border=None,command=Button_Div)

button_1 = button_1.grid(column=0,row=3)
button_2 = button_2.grid(column=1,row=3)
button_3 = button_3.grid(column=2,row=3)

button_4 = button_4.grid(column=0,row=2)
button_5 = button_5.grid(column=1,row=2)
button_6 = button_6.grid(column=2,row=2)

button_7 = button_7.grid(column=0,row=1)
button_8 = button_8.grid(column=1,row=1)
button_9 = button_9.grid(column=2,row=1)

button_0 = button_0.grid(column=0,row=4)
button_equal = button_equal.grid(column=1,row=4,columnspan="2")

button_clear = button_clear.grid(column=0,row=5)
button_add = button_add.grid(column=1,row=5)
button_sep = button_sep.grid(column=2,row=5)

button_per = button_per.grid(column=0,row=6)
button_mul = button_mul.grid(column=1,row=6)
button_div = button_div.grid(column=2,row=6)

root.mainloop()