from tkinter import *
window = Tk()
window.title("8086 Simulator")
window.resizable(False,False)
window.state("zoomed")
Registers = ["AX", "BX", "CX", "DX", "SI", "DI", "BP", "SP"]
Reg_Values = ["0x1234", "0x9523", "0x5432",
              "0x3215", "0x1245", "0x6142", "0x1632", "0x7341"]
Mems = ["0x3010", "0x3011", "0x3012", "0x3013", "0x3014", "0x3015", "0x3016",
        "0x3017", "0x3018", "0x3019", "0x301A", "0x301B", "0x301C", "0x301D", "0x301E", "0x301F"]
Mem_Values = ["0x00A0", "0x00B0", "0x00C0", "0x00D0", "0x00E0", "0x00F0", "0x00AB",
              "0x00AC", "0x00AD", "0x00AE", "0x00AF", "0x00BA", "0x00BB", "0x00BC", "0x00BD", "0x00BE"]
Reg_Table = ["000", "011", "001", "010", "110", "111", "101", "100"]
Instructions = ["MOV", "DIV", "MUL", "ADD", "CDQ", "XCHG", "SUB", "INC", "DEC", "AND", "OR", "NOT", "XOR", "SHR", "SHL"]

Ins = ["1000 10", "1111 01", "1111 01", "0000 00", "1001 1001", "1000 01", "0010 10", "1111 11", "1111 11", "0010 00", "0000 10", "1111 01", "0011 00", "1100 00", "1100 00"]
bg = PhotoImage(file="vecteezy_abstract-futuristic-background-blue-glowing-technology-sci_.png")

lbl = Label(window, image=bg)
lbl.place(x=0, y=0)
p1 = PhotoImage(
    file="cpu-icon-microprocessor-and-processor-symbol-vector-5524341.png")
window.iconphoto(False, p1)
buttoncolor = '#010329'
headercolor = 'white'
textbackground = '#010329'
buttontextbackground = 'white'

framecolor = "black"

# Helpers
def convert(value):
    value = value[2:]
    value = int(value, 16)
    temp = format(value, "b")
    while (len(temp) != 16):
        temp = "0" + temp
    temp1 = temp[8:12]
    temp2 = temp[12:16]
    temp3 = temp[0:4]
    temp4 = temp[4:8]
    value = temp1 + " " + temp2 + " " + temp3 + " " + temp4 
    return value

def filler(value):
    value = value[2:]
    while len(value) != 4:
        value = "0"+value
    value = "0x" + value.upper()
    return value


def destruct(master):
    master.destroy()


def validate(value):
    try:
        value = int(value, 16)
        if value < 0 or value > 65535:
            return 0
        else:
            return 1
    except:
        return 0

def validate2(value):
    try:
        value = int(value)
        if value < 0:
            return 0
        else:
            return 1
    except:
        return 0
#XChange

def xchg_check(E1, E2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    S1 = E2.get()
    if S not in Registers:
        error.config(text="Invalid Input(s)")
    elif S1.upper() not in Registers and S1 not in Mems:
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        i = Registers.index(S)
        if S1.upper() in Registers:
            i2 = Registers.index(S1)
            temp = Reg_Values[i]
            Reg_Values[i] = Reg_Values[i2]
            Reg_Values[i2] = temp
            reg_labels[i].config(text=S + " : " + Reg_Values[i])
            reg_labels[i2].config(text=S1 + " : " + Reg_Values[i2])
            Mod = "11"
            R_M = Reg_Table[i2]
        elif S1 in Mems:
            i2 = Mems.index(S1)
            temp = Reg_Values[i]
            Reg_Values[i] = Mem_Values[i2]
            Mem_Values[i2] = temp
            reg_labels[i].config(text=S + " : " + Reg_Values[i])
            Meg_labels[i2].config(text=S1 + " : " + Mem_Values[i2])
            R_M = "110"
            Mod = "00"
        opcode = Ins[5]
        D = "1"
        WORD = "1"
        Reg = Reg_Table[i]
        opcodegen.config(text = opcode + D + WORD + " " + Mod + Reg[0:2] + " " + Reg[2:3] + R_M )

        destruct(newWindow)


def xchg_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg: ", bg='#010329', fg='white')
    templabel.grid(row=0, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=0, column=1)
    templabel2 = Label(newWindow, text="Reg/Mem: ", bg='#010329', fg='white')
    templabel2.grid(row=1, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: xchg_check(entry1, entry2), fg='white', bg='#010329')
    btn.grid(row=0, column=2, rowspan=2)

#Left Shift
def shl_check(E1,entry2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    S1 = entry2.get()
    if S not in Registers or validate2(S1) == 0:
        error.config(text="Invalid Input(s)")
    else:
        S2 = int(S1)
        error.config(text="")
        global Reg_Values
        global reg_labels
        i = Registers.index(S)
        r1 = Reg_Values[i]
        r3 = int(r1, 16)
        r3 = r3<<S2
        s3 = hex(r3)
        if (r3 > 65535):
            s3 = s3[3:]
            s3 = "0x"+s3
            # r - r
        Reg_Values[i] = filler(s3)
        reg_labels[i].config(text=S + ": " + Reg_Values[i])
        Opcode = "1100 00"
        D = "0"
        WORD = "1"
        Mod = "00"
        Reg = "100"
        R_M = Reg_Table[i]
        opcodegen.config(text=Opcode + D + WORD + " " + Mod + Reg[0:2] + " " + Reg[2:3] + R_M)
        destruct(newWindow)

def shl_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg: ", fg='white', bg='#010329')
    templabel.grid(row=0, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=0, column=1)
    templabel2 = Label(newWindow, text="Num places: ", fg='white', bg='#010329')
    templabel2.grid(row=1, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=1, column=1)

    btn = Button(newWindow, text="Enter",
                 command=lambda: shl_check(entry1, entry2), fg='white', bg='#010329')
    btn.grid(row=0, column=2, rowspan=2)

#Right Shift
def shr_check(E1,E2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    S1 = E2.get()
    if S not in Registers or validate2(S1) == 0:
        error.config(text="Invalid Input(s)")
    else:
        S2 = int(S1)
        error.config(text="")
        global Reg_Values
        global reg_labels
        i = Registers.index(S)
        r1 = Reg_Values[i]
        r3 = int(r1, 16)
        r3 = r3>>S2
        if (r3 > 65535):
            error.config(text="Error: Shift greater than 0xFFFF.")
        else:
            s3 = hex(r3)
            # r - r
            Reg_Values[i] = filler(s3)
            reg_labels[i].config(text=S + ": " + Reg_Values[i])
            Opcode = "1100 00"
            D = "0"
            WORD = "1"
            Mod = "00"
            Reg = "101"
            R_M = Reg_Table[i]
            opcodegen.config(text=Opcode + D + WORD + " " + Mod + Reg[0:2] + " " + Reg[2:3] + R_M)
            destruct(newWindow)

def shr_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg: ",bg='#010329',fg='white')
    templabel.grid(row=0, column=0)
    entry1 = Entry(newWindow,bg='black',fg='white')
    entry1.grid(row=0, column=1)
    templabel2 = Label(newWindow, text="Num places: ",bg='#010329',fg='white')
    templabel2.grid(row=1, column=0)
    entry2 = Entry(newWindow,bg='black',fg='white')
    entry2.grid(row=1, column=1)

    btn = Button(newWindow, text="Enter",
                 command=lambda: shr_check(entry1,entry2),bg='#010329',fg='white')
    btn.grid(row=0, column=2, rowspan=2)


#XOR instruction
def XOR_getEntry(entry1, entry2):
    global Registers
    global Reg_Values
    global reg_labels
    x = entry1
    y = entry2
    i = Registers.index(x)
    i2 = Registers.index(y)
    r1 = Reg_Values[i]
    r2 = Reg_Values[i2]
    r3 = int(r1, 16)
    r3 = format(r3, "b")
    r4 = int(r2, 16)
    r4 = format(r4, "b")
    while(len(r3)!= 16):
            r3 = "0"+r3
    while(len(r4)!= 16):
            r4 = "0"+r4
    list1 = []
    list2 = []
    list3 = []
    list1[:0] = r3
    list2[:0] = r4
    for a,b in zip(list1, list2):
        if a == "1" and b == "0":
            list3.append("1")
        elif a == "0" and b == "1":
            list3.append("1")
        else:
            list3.append("0")
    r3 = "".join(list3)
    r3 = int(r3, 2)
    s3 = hex(r3)
    Reg_Values[i] = filler(s3)
    reg_labels[i].config(text=x + ": " + Reg_Values[i])
    Opcode = Ins[12];
    D = "1"
    Word = "1"
    Mod = "11"
    Reg = Reg_Table[i]
    R_M = Reg_Table[i2]
    opcodegen.config(text = Opcode + D + Word + " " + Mod + Reg[0:2] + " " + Reg[2:3] + R_M)
    destruct(newWindow)

def XOR_check(E1, E2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    S1 = E2.get()
    S1 = S1.upper()
    if S and S1 not in Registers:
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        XOR_getEntry(S, S1)


def XOR_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("XOR Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg 1: ", bg='#010329', fg='white')
    templabel.grid(row=0, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=0, column=1)
    templabel2 = Label(newWindow, text="Reg 2: ", bg='#010329', fg='white')
    templabel2.grid(row=1, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: XOR_check(entry1, entry2), bg='#010329', fg='white')
    btn.grid(row=0, column=2, rowspan=2)

#Multiply
def mul_check(text1, E1):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    temp = "Do"
    S = E1.get()
    if text1 == "Reg":
        if (S.upper() not in Registers):
            error.config(text="Invalid Input(s)")
        else:
            error.config(text="")
            i2 = Registers.index(S)
            temp = Reg_Values[i2]
            R_M = Reg_Table[i2]
            Mod = "11"
    elif text1 == "Mem":
        if (S not in Mems):
            error.config(text="Invalid Input(s)")
        else:
            error.config(text="")
            i2 = Mems.index(S)
            temp = Mems[i2]
            Mod = "00"
            R_M = "110"
            Disp = convert(Mems[i2])
    if temp != "Do":
        temp2 = int(temp, 16) * int(Reg_Values[0], 16)
        if (temp2 > 4294967295):
            error.config(text="Error: Product greater than 0 x FFFF FFFF.")
        else:
            temp3 = hex(temp2)
            temp3 = temp3[2:]
            while len(temp3) != 8:
                temp3 = "0" + temp3
            temp3 = temp3.upper()
            Reg_Values[0] = "0x" + temp3[4:8]
            Reg_Values[3] = "0x" + temp3[0:4]
            reg_labels[0].config(text=Registers[0] + " : " + Reg_Values[0])
            reg_labels[3].config(text=Registers[3] + " : " + Reg_Values[3])
            Opcode = Ins[2]
            D = "1"
            W = "1"
            Reg = "100"
            if text1 == "Reg":
                opcodegen.config(text = Opcode + D + W + " " + Mod + Reg[0:2] + " " + Reg[2:3] + R_M)
            else: 
                opcodegen.config(text = Opcode + D + W + " " + Mod + Reg[0:2] + " " + Reg[2:3] + R_M + " " + Disp)
            destruct(newWindow)

def mul_createFormUni(text1):
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text=text1 + ": ", bg='#010329', fg='white')
    templabel.grid(row=1, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: mul_check(text1, entry1), bg='#010329', fg='white')
    btn.grid(row=1, column=2, rowspan=1)


def mul_formselect():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Select multiplier: ", bg='#010329', fg='white')
    templabel.grid(row=0, column=0)
    btn1 = Button(newWindow, text="Reg", height=2, width=15,
                  command=lambda: mul_createFormUni("Reg"), bg='#010329', fg='white')
    btn1.grid(row=1, column=0, rowspan=1)
    btn2 = Button(newWindow, text="Mem", height=2, width=15,
                  command=lambda: mul_createFormUni("Mem"), bg='#010329', fg='white')
    btn2.grid(row=2, column=0, rowspan=1)
    btn3 = Button(newWindow, text="Value", height=2, width=15,
                  command=lambda: mul_createFormUni("Value"), bg='#010329', fg='white')
    btn3.grid(row=3, column=0, rowspan=1)

#Division
def div_check(text1, E1):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    temp = "Do"
    S = E1.get()
    if text1 == "Reg":
        if (S.upper() not in Registers):
            error.config(text="Invalid Input(s)")
        else:
            error.config(text="")
            i2 = Registers.index(S)
            temp = Reg_Values[i2]
            R_M = Reg_Table[i2]
            Mod = "11"
    elif text1 == "Mem":
        if (S not in Mems):
            error.config(text="Invalid Input(s)")
        else:
            error.config(text="")
            i2 = Mems.index(S)
            temp = Mem_Values[i2]
            Mod = "00"
            R_M = "110"
            Disp = convert(Mems[i2])
    if temp != "Do":
        DX_AX = Reg_Values[3][2:6] + Reg_Values[0][2:6]
        tempQ = int(DX_AX, 16) // int(temp, 16)
        if tempQ > 65535:
            error.config(text="Error: Quotient > 16 bits. Cannot store.")
        else:
            tempR = int(DX_AX, 16) % int(temp, 16)
            tempAX = hex(tempQ)
            tempDX = hex(tempR)
            Reg_Values[0] = filler(tempAX)
            Reg_Values[3] = filler(tempDX)
            reg_labels[0].config(text=Registers[0] + " : " + Reg_Values[0])
            reg_labels[3].config(text=Registers[3] + " : " + Reg_Values[3])
            Opcode = Ins[1]
            D = "1"
            W = "1"
            Reg = "110"
            if text1 == "Reg":
                opcodegen.config(text = Opcode + D + W + " " + Mod + Reg[0:2] + " " + Reg[2:3] + R_M)
            else: 
                opcodegen.config(text = Opcode + D + W + " " + Mod + Reg[0:2] + " " + Reg[2:3] + R_M + " " + Disp)
            destruct(newWindow)
