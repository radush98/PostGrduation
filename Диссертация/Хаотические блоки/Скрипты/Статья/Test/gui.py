from tkinter import*
from tkinter import messagebox as mb
import base4recursia
import findWeight2base
import findWeight4base
import os

class goodBlock():
    def __init__(self, amount):
        self.checkAmount(amount);
        self.avalacheTargetValue = 128;
        self.excepted = 0;

    def checkAmount(self, amount):
        try:
            self.amount = int(amount);
            if self.amount < 0:
                self.amount = self.amount*(-1);
            if self.amount == 0:
                self.amount = 1;
        except ValueError:
            self.amount = 1;

    def calculate(self):
        with open(os.getcwd()+'\\16py.txt', 'r') as f:
            for i in f:
                temp = base4recursia.Creation(eval(i));
                Sbox = temp.createSbox();

                temp.newSbox(Sbox);
                Sbox = temp.createSbox();

                matrix = findWeight2base.calculateWeight(Sbox).createFuns();

                self.check(matrix, Sbox, i);

                if self.excepted == self.amount:
                    return


    def check(self, matrix, Sbox, origSbox):
        for i in matrix:
            for j in i:
                if j < self.avalacheTargetValue:
                    return

        input_field.insert(END, origSbox);
        output_field.insert(END, Sbox);
        output_field.select_set(0);
        self.excepted += 1;

def start():
    input_field.delete(0,'end');
    output_field.delete(0,'end');

    g = goodBlock(box_amount.get());
    g.calculate();

    btn_show.config(state=NORMAL);
    btn_save.config(state=NORMAL);

def insertion(matrix, box):
    for i in matrix:
        box.insert(END, str(i) + '\n')

def check():
    box2.delete(1.0, END);
    box4.delete(1.0, END);

    strBox = output_field.get(output_field.curselection());
    Sbox = [int(strBox[i]) for i in range(0,len(strBox))];

    insertion(findWeight2base.calculateWeight(Sbox).createFuns(), box2);
    insertion(findWeight4base.calculateWeight(Sbox).createFuns(), box4);


def saveSboxes():
    with open(os.getcwd()+'\\256py.txt', 'w') as f:
        for i in range(0,output_field.size()):
            temp = output_field.get(i);
            box = str([temp[j] for j in range(0, len(temp))]) + '\n\n';
            f.write(box.replace(' ',''));

    mb.showinfo('Success!','Boxes were successfully saved!')

#-------------------------------------------GUI------------------------------------------------
#------Main frame----------
root =Tk();
root.geometry("%dx%d+0+0" % (root.winfo_screenwidth(), root.winfo_screenheight()));
root.title('S-box create');

#-------Labels----------
origBox_lbl = Label(root, text="S-boxes 16:");
origBox_lbl.grid(row=1, column=0, columnspan=2, pady=5);

createdBox_lbl = Label(root, text="S-boxes 256:");
createdBox_lbl.grid(row=1, column=2, columnspan=8, pady=5);

amount_lbl = Label(root, text="Amount:");
amount_lbl.grid(row=0, column=0);

boolean_lbl = Label(root, text="2-logic weight");
boolean_lbl.grid(row=7, column = 0, columnspan = 5);

boolean_lbl = Label(root, text="4-logic weight");
boolean_lbl.grid(row=7, column = 5, columnspan = 5);

#------SubFrames-----------
frame_left = Frame(root);
frame_left.grid(row=2,column=0, rowspan=3,columnspan=2, padx=10);

frame_right = Frame(root);
frame_right.grid(row=2, column=2, rowspan=3, columnspan=7,pady=5, padx=10);

frame_dleft = Frame(root);
frame_dleft.grid(row=8,column=0, rowspan=3,columnspan=5, padx=10, pady=5);

frame_dright = Frame(root);
frame_dright.grid(row=8, column=5, rowspan=3, columnspan=5,padx=10, pady=5);

#-----Original boxes------------
Yscrollbar = Scrollbar(frame_left);
Yscrollbar.pack(side=RIGHT, fill=Y);

input_field = Listbox(frame_left,
            yscrollcommand=Yscrollbar.set,width = 35,height=15);
input_field.pack(fill=Y)


#-------Created boxes-------------
xscrollbar = Scrollbar(frame_right, orient=HORIZONTAL);
xscrollbar.pack(side=BOTTOM, fill=X);

yscrollbar = Scrollbar(frame_right);
yscrollbar.pack(side=RIGHT, fill=Y);

output_field = Listbox(frame_right,
            xscrollcommand=xscrollbar.set,
            yscrollcommand=yscrollbar.set, width = 180, height=14)
output_field.pack(fill=Y);

#-----------boolean logic output-------------------
YscrollbarDL = Scrollbar(frame_dleft);
YscrollbarDL.pack(side=RIGHT, fill=Y);

box2 = Text(frame_dleft, wrap=NONE,
            yscrollcommand=YscrollbarDL.set, height=17,pady=2, width=80);
box2.pack(fill=Y)

#------------------4-logic output--------------------

YscrollbarDR = Scrollbar(frame_dright);
YscrollbarDR.pack(side=RIGHT, fill=Y);

box4 = Text(frame_dright, wrap=NONE,
            yscrollcommand=YscrollbarDR.set, height=17, pady=2,  width=80);
box4.pack(fill=Y)

#---------------Control panel---------------------
box_amount = Entry(root,width=15);
box_amount.grid(row=0, column = 1, columnspan=1, pady=15);

btn_start = Button(root, command = start, text="Generate", width=7);
btn_start.grid(row=0, column = 2, columnspan=1, pady=15);

btn_show = Button(root,command = check, text="Show weight", state=DISABLED);
btn_show.grid(row=6, column = 4, columnspan=2, pady=5);

btn_save = Button(root,command = saveSboxes, text="Save boxes", state=DISABLED);
btn_save.grid(row=0, column = 8, columnspan=3, pady=15);

root.mainloop();