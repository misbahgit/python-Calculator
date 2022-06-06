from tkinter import *  
parent=Tk()

simple = LabelFrame(parent,text='Simple calculator',width=250, padx=5,pady=5)
numpad=LabelFrame(parent,text='Number Pad',width=150,padx=5 ,pady=5)
number=StringVar()
msg=StringVar()
ne1=Entry(parent,textvariable=number,width=22,borderwidth=2,font=('arial',20,'bold'),justify=RIGHT)
ne1.grid(row=1,column=0,padx=5,pady=5)  
ne1.focus();
ne2=Entry(parent,textvariable=msg,width=44,borderwidth=2,font=('arial',12,'bold'),justify=RIGHT,state=DISABLED)
ne2.grid(row=0,column=0,padx=5,pady=5)
numpad.grid(row=2,column=0,padx=5,pady=5)
simple.grid(row=3,column=0,padx=5,pady=5)
# 
parent.title('Calculator')  
 
#simple = Frame(simple)
Scientific = Frame(simple)
exp=''
opr=False
result=0.0
short=True
def operator(op):
    global opr
    global exp
    opr=True
    exp=ne1.get()
    exp=exp+" "+ str(op)
    num1=ne1.get()
    #ne1.delete(0, END)
    global n1
    start=num1.find('=')
    num1=num1[start+1:]
    n1=float(num1)

def btn_val(n):
    #n=btn.text
    global opr
    if opr:
        ne1.delete(0,END)
        opr=False
    val=ne1.get()
    ne1.delete(0,END)
    #valstr(n)
    val=val+str(n)
    adjust(val)
    ne1.insert(0,val)

def adjust(str_res):
    n=len(str_res)
    #global short
    if n<22:
        ne1.config(width=22,font=('arial',20,'bold'))
    elif n>=22 and n<33:
        ne1.config(width=44,font=('arial',14,'bold'))
    else:
        ne1.config(width=66,font=('arial',8,'bold'))

def calc():
    global exp
    global result
    global opr
    ne2.config(state='normal')
    ne2.delete(0,END)
    num2=ne1.get()
    if len(exp)>1:
        start=exp.find('=')
        exp=exp[start+1:]
        exp=exp+num2
    else:
        exp=num2

    ne1.delete(0, END)
    start=exp.find('=')
    exp=exp[start+1:]
    ne2.insert(0, 'Expr='+exp)
    ne2.config(state='disabled')
    
    result=eval(exp)
    str_res=str(result)
    adjust(str_res)
    ne1.insert(0, 'Ans='+str(result))
    opr=False
    exp=''

def clear():
    ne1.delete(0, END)

def backspace():
    n=len(ne1.get())-1
    ne1.delete(n,END)
#number2= StringVar()
btn1= Button(numpad,text='1',padx=40, pady=20,command=lambda:btn_val(1),activebackground='skyblue',font=('arial',12,'bold'))
btn1.grid(row=1,column=0,padx=2,pady=2)
btn2= Button(numpad,text='2',padx=40, pady=20,command=lambda:btn_val(2),activebackground='skyblue',font=('arial',12,'bold'))
btn2.grid(row=1,column=1,padx=2,pady=2)
btn3= Button(numpad,text='3',padx=40, pady=20,command=lambda:btn_val(3),activebackground='skyblue',font=('arial',12,'bold'))
btn3.grid(row=1,column=2,padx=2,pady=2)

btn4= Button(numpad,text='4',padx=40, pady=20,command=lambda:btn_val(4),activebackground='skyblue',font=('arial',12,'bold'))
btn4.grid(row=2,column=0,padx=2,pady=2)
btn5= Button(numpad,text='5',padx=40, pady=20,command=lambda:btn_val(5),activebackground='skyblue',font=('arial',12,'bold'))
btn5.grid(row=2,column=1,padx=2,pady=2)
btn6= Button(numpad,text='6',padx=40, pady=20,command=lambda:btn_val(6),activebackground='skyblue',font=('arial',12,'bold'))
btn6.grid(row=2,column=2,padx=2,pady=2)

btn7= Button(numpad,text='7',padx=40, pady=20,command=lambda:btn_val(7),activebackground='skyblue',font=('arial',12,'bold'))
btn7.grid(row=3,column=0,padx=2,pady=2)
btn8= Button(numpad,text='8',padx=40, pady=20,command=lambda:btn_val(8),activebackground='skyblue',font=('arial',12,'bold'))
btn8.grid(row=3,column=1,padx=2,pady=2)
btn9= Button(numpad,text='9',padx=40, pady=20,command=lambda:btn_val(9),activebackground='skyblue',font=('arial',12,'bold'))
btn9.grid(row=3,column=2,padx=2,pady=2)

btn10= Button(numpad,text='0',padx=40, pady=20,command=lambda:btn_val(0),activebackground='skyblue',font=('arial',12,'bold'))
btn10.grid(row=4,column=0,padx=2,pady=2)

btn11= Button(numpad,text='.',padx=40, pady=20,command=lambda:btn_val('.'),activebackground='skyblue',font=('arial',12,'bold'))
btn11.grid(row=4,column=1,columnspan=1,padx=2,pady=2)

btn_back= Button(numpad,text='Backspace', padx=2,pady=20,command=backspace,activebackground='skyblue',font=('arial',12,'bold'))
btn_back.grid(row=4,column=2,columnspan=1,padx=2,pady=2)

btn_plus= Button(simple,text='+',padx=39, pady=20,command=lambda:operator('+'),activebackground='skyblue',font=('arial',12,'bold'))
btn_plus.grid(row=5,column=0,padx=2,pady=2)

btn_minus= Button(simple,text='-',padx=39, pady=20,command=lambda:operator('-'),activebackground='skyblue',font=('arial',12,'bold'))
btn_minus.grid(row=5,column=1,padx=2,pady=2)

btn_mult= Button(simple,text='*',padx=39, pady=20,command=lambda:operator('*'),activebackground='skyblue',font=('arial',12,'bold'))
btn_mult.grid(row=5,column=2,padx=2,pady=2)

btn_div= Button(simple,text='/',padx=40, pady=20,command=lambda:operator('/'),activebackground='skyblue',font=('arial',12,'bold'))
btn_div.grid(row=6,column=0,padx=2,pady=2)

btn_percent= Button(simple,text='%',padx=36, pady=20,command=lambda:operator('%'),activebackground='skyblue',font=('arial',12,'bold'))
btn_percent.grid(row=6,column=1,padx=2,pady=2)

btn_power= Button(simple,text='^',padx=39, pady=20,command=lambda:operator('**'),activebackground='skyblue',font=('arial',12,'bold'))
btn_power.grid(row=6,column=2,padx=2,pady=2)

btn_cal= Button(simple,text='Calculate', padx=64,pady=20,command=calc,activebackground='skyblue',font=('arial',12,'bold'))
btn_cal.grid(row=7,column=0,columnspan=2,padx=2,pady=2)

btn_clear= Button(simple,text='Clear', padx=22,pady=20,command=clear,activebackground='skyblue',font=('arial',12,'bold'))
btn_clear.grid(row=7,column=2,columnspan=1,padx=2,pady=2)

#buttonCal =  Button(simple, text="Calculate", command=lambda : call_result(labelResult,number1,number2)).grid(row=3, column=0)  
  
simple.mainloop()  