from tkinter import*
import random
a=Tk()
a.title("stone paper scissor Game")
a.geometry("460x370")
a.resizable(0,0)

ar=['s','p','sc']
a.config(bg='black')

def countdown(count):
    label['text'] = count
    if count > 0:
        a.after(1000, countdown, count-1)
    else:
        Label(a,text='Game Over',fg='red',width=460,height=370,font='vardana 50 bold',bg='black').pack()


label = Label(a,font='vardana 20',fg='#062f4d',bg='black')
label.place(x=155, y=0)
Label(a,text='Time left : ',font='vardana 20',fg='#062f4d',bg='black').place(x=0,y=0)
countdown(20)
scr1=0
scr2=0
l1=Label(a,text='your score : 0',fg='green',font='vardana 20',bg='black')
l1.place(x=1,y=41)
l2=Label(a,text='comp. score : 0',fg='red',font='vardna 20',bg='black')
l2.place(x=250,y=41)
ds=Label(a,font='vardana 20',bg='black')
ds.place(x=170,y=260)
n=Label(a,fg='#9999ff',font='vardana 20',bg='black')
n.place(x=110,y=300)

def s1(): # computer score
    global scr1
    scr1=scr1+1
    return scr1
def s2(): # your score
    global scr2
    scr2=scr2+1
    return scr2
def pr():#paper
    i=random.randint(0,2)
    if ar[i]=='p':
        a.after(100)
        ds.config(text='Drawn!!',fg='#5994d9')
    elif ar[i]=='s':
        a.after(100)
        ds.config(text='you won!!',fg='green',bg='black')
        l1.config(text='your score : '+str(s1()))
        n.config(text='paper     '+'   stone')
    else:
        a.after(100)
        ds.config(text='you loss!!',fg='red')
        n.config(text='paper     '+'   scissor')
        l2.config(text='comp. score : '+str(s2()))
def s():#stone
    i=random.randint(0,2)
    if ar[i]=='p':
        a.after(100)
        ds.config(text='you loss!!',fg='red')
        n.config(text='stone     '+'   paper')
        l2.config(text='comp. score : '+str(s2()))
    elif ar[i]=='s':
        a.after(100)
        ds.config(text='Drawn!!',fg='#5994d9')
    else:
        a.after(100)
        ds.config(text='you won!!',fg='green')
        n.config(text='stone    '+'    scissor')
        l1.config(text='your score : '+str(s1()))
def sc():#scissor
    i=random.randint(0,2)
    if ar[i]=='p':
        a.after(100)
        ds.config(text='you won!!',fg='green')
        n.config(text='scissor   '+'   paper')
        l1.config(text='your score : '+str(s1()))
    elif ar[i]=='s':
        a.after(100)
        ds.config(text='you loss!!',fg='red')
        n.config(text='scissor   '+'   stone')
        l2.config(text='comp. score : '+str(s2()))
    else:
        a.after(100)
        ds.config(text='Drawn!!',fg='#5994d9')
#ar=['s','p','sc']
canvas1=Canvas(a,width=115,height=115)
canvas1.place(x=30,y=95)
my1=PhotoImage(file='sic.png')
canvas1.create_image(0,0,anchor=NW,image=my1)

canvas2=Canvas(a,width=115,height=115)
canvas2.place(x=150,y=95)
my2=PhotoImage(file='pr.png')
canvas2.create_image(0,0,anchor=NW,image=my2)

canvas3=Canvas(a,width=115,height=115)
canvas3.place(x=270,y=95)
my3=PhotoImage(file='ston.png')
canvas3.create_image(0,0,anchor=NW,image=my3)

sc=Button(text='SCISSOR',font='vardana 12 bold',fg='#003380',command=sc,bg='black')
sc.place(x=60,y=215)
pp=Button(text='PAPER',font='vardana 12 bold',command=pr,fg='#003380',bg='black')
pp.place(x=180,y=215)
st=Button(text='STONE',font='vardana 12 bold',command=s,fg='#003380',bg='black')
st.place(x=300,y=215)

def st1(event):
    st.config(font='vardana 15 bold',fg='orange')
def st2(event):
    st.config(font='vardana 12 bold',fg='#003380')

st.bind("<Enter>",st1)
st.bind("<Leave>",st2)

def pp1(event):
    pp.config(font='vardana 15 bold',fg='red')
def pp2(event):
    pp.config(font='vardana 12 bold',fg='#003380')

pp.bind("<Enter>",pp1)
pp.bind("<Leave>",pp2)

def sc1(event):
    sc.config(font='vardana 15 bold',fg='green')
def sc2(event):
    sc.config(font='vardana 12 bold',fg='#003380')

sc.bind("<Enter>",sc1)
sc.bind("<Leave>",sc2)

a.mainloop()