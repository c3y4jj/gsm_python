from tkinter import *

w = Tk()
w.title("계산기")
display=Entry(w, width=33, bg="pink")
display.grid(row=0, column=0, columnspan=5)
btn_list=['7','8','9','/','C',
          '4','5','6','*','<-',
          '1','2','3','-',' ',
          '0','.','=','+',' ']
def keyinput(event):
    print(event)
    if event.keysym>='0' and event.keysym <='9':
        click(event.keysym)
    elif event.keysym=='BackSpace':
        click('<-')
    elif event.keysym=='equal' or event.keysym=='Return':
        click('=')
    elif event.keysym=='asterisk':
        click('*')
    elif event.keysym=='minus':
        click('-')
    elif event.keysym=='plus':
        click('+')
    elif event.keysym=='slash':
        click('/')

def click(key):
    if key=="=":
        result=eval(display.get())
        s = str(result)
        display.delete(0,END)
        display.insert(END,"=" + s)
    elif key=="<-":
        D = len(display.get())
        display.delete(D-1,END)
    elif key=="C":
        display.delete(0,END)
    else:
        if '=' in display.get():
            display.delete(0,END)
        else:
            display.insert(END, key)
r_index=1
c_index=0
for btn_text in btn_list:
    def process(t=btn_text):
        click(t)
    Button(w, text=btn_text, width=5, command=process).grid(row=r_index,column=c_index)
    c_index+= 1;
    if c_index==5:
        r_index+=1
        c_index=0
w.bind_all('<KeyPress>', keyinput)
w.mainloop()
