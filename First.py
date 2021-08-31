from tkinter import *
from tkinter import messagebox
from random import randint
root_info=Tk()
root_info.title("Information")
root_info.geometry("400x200+250+150")

mode=IntVar()
E1_txt=StringVar()
E2_txt=StringVar()
E3_txt=StringVar()
Rounds=0
rw=0
cl=0
def check_btn():
    global mode
    if mode.get() == 1:
        Player1_E.config(state=NORMAL)
        Player2_E.config(state=NORMAL)
    else:
        Player1_E.config(state=DISABLED)
        E1_txt.set("")
        Player2_E.config(state=DISABLED)
        E2_txt.set("")
def strt():
    global Rounds
    if mode.get()==1 and E1_txt.get()!="" and E2_txt.get()!="" and E3_txt.get()!="":
        Rounds=int(E3_txt.get())
        root_info.destroy()
    if mode.get()==0 and E3_txt.get()!="":
        E1_txt.set("Вы")
        E2_txt.set("Компьютер")
        Rounds = int(E3_txt.get())
        root_info.destroy()
Variant1=Checkbutton(root_info,text="Два игрока", variable=mode, command=check_btn)
Variant1.grid(row=0, column=0)
Player1_E=Entry(root_info, font="10", state=DISABLED, textvariable=E1_txt)
Player1_E.grid(row=1, column=1)
Player2_E=Entry(root_info, font="10", state=DISABLED, textvariable=E2_txt)
Player2_E.grid(row=2, column=1)
Player1=Label(root_info, fg="#f00", font="10", text="Игрок 1")
Player1.grid(row=1, column=0)
Player2=Label(root_info, fg="#00f", font="10", text="Игрок 2")
Player2.grid(row=2, column=0)
Long=Label(root_info, font="10", text="Число раундов")
Long.grid(row=3, column=0)
Long_E=Entry(root_info, font="10", textvariable=E3_txt)
Long_E.grid(row=3, column=1)
Press_Start=Button(root_info, text="Press Start", font=15, fg="#0a0", command=strt)
Press_Start.grid(row=4, column=1, pady=20)

root_info.mainloop()

root=Tk()
root.title("GAME")
root.geometry("480x600+200+100")
bl=0
rd=0
round=1
buttonlst=[ list(range(3)) for i in range(3)]
buttonind=[ list(range(3)) for j in range(3)]

for i in range(3):
    for j in range(3):
        buttonind[i][j]=0

name1_txt=StringVar()
name1_txt.set(E1_txt.get()+" *")
name1=Label(root,textvariable=name1_txt, height=5, font="15", fg="#f00")
name1.grid(row=0, column=0)

name2_txt=StringVar()
name2_txt.set(E2_txt.get())
name2=Label(root,textvariable=name2_txt, height=5, font="15", fg="#00f")
name2.grid(row=0, column=2)

count_txt=StringVar()
count_txt.set("Раунд {} \n {}:{}".format(round,rd,bl))
count=Label(root,textvariable=count_txt, height=5, font="15")
count.grid(row=0, column=1)

player=True
def check():
    for i in range(3):
        k1=0
        k2=buttonind[i][0]
        for j in range(3):
            if k2!=buttonind[i][j]:
                k1=1
                break
        if k1==0 and k2!=0:
            return 1
    for i in range(3):
        k1=0
        k2 = buttonind[0][i]
        for j in range(3):
            if k2 != buttonind[j][i]:
                k1 = 1
                break
        if k1 == 0 and k2 != 0:
            return 1
    if buttonind[2][0] == buttonind[1][1] and buttonind[2][0] == buttonind[0][2] and buttonind[2][0] != 0:
        return 1
    if buttonind[0][0] == buttonind[1][1] and buttonind[0][0] == buttonind[2][2] and buttonind[0][0]!=0:
        return 1
    for i in range(3):
        for j in range(3):
            if buttonind[i][j]==0:
                return 0
    return 2
def check_later():
    global round, bl, rd, Rounds, player
    if check()==1:
        round+=1
        if player:
            bl+=1
            player=False
            name1_txt.set(E1_txt.get())
            name2_txt.set(E2_txt.get() + " *")
        else:
            name2_txt.set(E2_txt.get())
            name1_txt.set(E1_txt.get() + " *")
            rd+=1
            player=True
        if round > Rounds:
            show_message()
            root.destroy()
            return 0
        clear()
        count_txt.set("Раунд {} \n {}:{}".format(round, rd, bl))
    if check()==2:
        round+=1
        if player:
            name2_txt.set(E2_txt.get())
            name1_txt.set(E1_txt.get()+" *")
        else:
            name1_txt.set(E1_txt.get())
            name2_txt.set(E2_txt.get() + " *")
        if round > Rounds:
            show_message()
            root.destroy()
            return 0
        clear()
        count_txt.set("Раунд {} \n {}:{}".format(round, rd, bl))
def clear():
    global player
    for i in range(3):
        for j in range(3):
            buttonlst[i][j].config(bg="#fff", state=NORMAL)
            buttonind[i][j]=0
def Color(button):
    global player, round, bl, rd
    gr = button.grid_info()
    x = gr['column']
    y = gr['row']
    if player:
        button.config(bg="#f00", state=DISABLED)
        player=False
        buttonind[x][y-1] = 2
    else:
        button.config(bg="#00f", state=DISABLED)
        player = True
        buttonind[x][y-1] = 1
    check_later()

def Color_AI(button):
    global player
    gr = button.grid_info()
    x = gr['column']
    y = gr['row']
    button.config(bg="#f00", state=DISABLED)
    buttonind[x][y-1] = 2
    player=False
    check_later()
    while player==False:
        lst=AI_count()
        buttonlst[lst[0]][lst[1]].config(bg="#00f", state=DISABLED)
        buttonind[lst[0]][lst[1]]=1
        player=True
        check_later()
def AI_count():
    zero = 0
    mrk = 0
    for i in range(3):
        for j in range(3):
            if buttonind[i][j] == 0:
                zero += 1
            if buttonind[i][j] == 1:
                mrk += 1
        if mrk == 2 and zero == 1:
            for ij in range(3):
                if buttonind[i][ij] == 0:
                    return i, ij
        else:
            mrk = 0
            zero = 0
    for i in range(3):
        for j in range(3):
            if buttonind[j][i] == 0:
                zero += 1
            if buttonind[j][i] == 1:
                mrk += 1
        if mrk == 2 and zero == 1:
            for ij in range(3):
                if buttonind[ij][i] == 0:
                    return ij, i
        else:
            mrk = 0
            zero = 0
    for i in range(3):
        if buttonind[i][i] == 0:
            zero += 1
        if buttonind[i][i] == 1:
            mrk += 1
    if mrk == 2 and zero == 1:
        for i in range(3):
            if buttonind[i][i] == 0:
                return i, i
    else:
        mrk = 0
        zero = 0
    for i in range(3):
        if buttonind[i][2 - i] == 0:
            zero += 1
        if buttonind[i][2 - i] == 1:
            mrk += 1
    if mrk == 2 and zero == 1:
        for i in range(3):
            if buttonind[i][2 - i] == 0:
                return i, 2-i
    else:
        mrk = 0
        zero = 0
    for i in range(3):
        for j in range(3):
            if buttonind[i][j] == 0:
                zero += 1
            if buttonind[i][j] == 2:
                mrk += 1
        if mrk == 2 and zero == 1:
            for ij in range(3):
                if buttonind[i][ij] == 0:
                    return i, ij
        else:
            mrk = 0
            zero = 0
    for i in range(3):
        for j in range(3):
            if buttonind[j][i] == 0:
                zero += 1
            if buttonind[j][i] == 2:
                mrk += 1
        if mrk == 2 and zero == 1:
            for ij in range(3):
                if buttonind[ij][i] == 0:
                    return ij, i
        else:
            mrk = 0
            zero = 0
    for i in range(3):
        if buttonind[i][i] == 0:
            zero += 1
        if buttonind[i][i] == 2:
            mrk += 1
    if mrk == 2 and zero == 1:
        for i in range(3):
            if buttonind[i][i] == 0:
                return i, i
    else:
        mrk = 0
        zero = 0
    for i in range(3):
        if buttonind[i][2 - i] == 0:
            zero += 1
        if buttonind[i][2 - i] == 2:
            mrk += 1
    if mrk == 2 and zero == 1:
        for i in range(3):
            if buttonind[i][2 - i] == 0:
                return i, 2-i
    k=0
    for i in range(3):
        for j in range(3):
            if buttonind[i][j] == 0:
                k+=1
    choise = randint(1, k)
    ind = 1
    for i in range(3):
        for j in range(3):
            if buttonind[i][j] == 0:
                if ind == choise:
                    return i, j
                else:
                    ind+=1
for i in range(3):
    for j in range(3):
        btn = Button(root,height=10, width=10, bg="#fff")
        if mode.get()==1:
            btn.configure(command=lambda button=btn: Color(button))
        else:
            btn.configure(command=lambda button=btn: Color_AI(button))
        btn.grid(row=j+1, column=i, ipadx=40, ipady=0, padx=0, pady=0)
        buttonlst[i][j]=btn
def show_message():
    if rd>bl:
        if mode.get()==1:
            messagebox.showinfo("Game over",E1_txt.get() +" won!")
        else:
            messagebox.showinfo("Game over!", "Victory!")
    elif rd < bl:
        if mode.get() == 1:
            messagebox.showinfo("Game over", E2_txt.get() + " won!")
        else:
            messagebox.showinfo("Game over!", "Defeat!")
    else:
        messagebox.showinfo("Game over", "Draw...")
root.mainloop()