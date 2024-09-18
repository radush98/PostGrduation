import PySimpleGUI as sg
import base4recursia
import findWeight2base
import findWeight4base
import os
from tkinter import messagebox as msb

class goodBlock():
    def __init__(self, amount, value, window):
        self.avalacheTargetValue = 128;
        self.excepted = 0;
        self.value = value;
        self.window = window;
        self.checkAmount(amount);

    def checkAmount(self, amount):
        try:
            self.amount = int(amount);
            if self.amount < 0:
                self.amount = self.amount*(-1);
            if self.amount == 0:
                self.amount = 1;
        except ValueError:
            msb.showinfo("Warning!",'Incorrect value! Amount has been set by default value "1"')
            self.amount = 1;

    def calculate(self):
        with open(os.getcwd()+'//16py.txt', 'r') as f:
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

        self.window['boxes16'].update([]);
        self.value['boxes16'].append(origSbox);
        self.window.Element('boxes16').update(values = self.value['boxes16']);

        self.window['boxes256'].update([]);
        self.value['boxes256'].append(str(Sbox).replace(' ',''));
        self.window.Element('boxes256').update(values = self.value['boxes256']);

        self.excepted += 1;


def insertion(matrix, key, window):
    for i in matrix:
        temp = window[key].get()
        window[key].update(value = (temp + str(i)))

def saveSboxes(window, value):
    amount = int(value["amount"])

    with open(os.getcwd()+'//256py.txt', 'w') as f:
        for i in range(0, amount):
            box = window["boxes256"].get_list_values()[i] + '\n\n'
            f.write(box.replace(' ',''));

    msb.showinfo('Success!', 'Boxes were successfully saved!')



control_row = [sg.Text("Amount:",size=(6,1)), sg.Input(key="amount", size=(7,1)),
               sg.Button('Generate'),sg.Text(size=(130,1)), sg.Button("Save boxes", disabled=True)]
boxes16 = sg.Column([[sg.Frame(layout = [[sg.Listbox(values=[None],key="boxes16",size=(33,15),
          select_mode = sg.LISTBOX_SELECT_MODE_SINGLE)]], title="S-boxes 16:")]])
boxes256 = sg.Column([[sg.Frame(layout = [[sg.Listbox(values=[None],key="boxes256",
          size=(145,15),select_mode = sg.LISTBOX_SELECT_MODE_SINGLE)]], title="S-boxes 256:")]])
weight2 = sg.Column([[sg.Frame(layout = [[sg.Output(key="weight2",size=(88,15))]], title="2-logic weight:")]])
weight4 = sg.Column([[sg.Frame(layout = [[sg.Output(key="weight4",size=(88,15))]], title="4-logic weight:")]])

layout = [control_row,
          [boxes16, boxes256],
          [sg.Text(size=(77,1)),sg.Button("Show weight", disabled=True)],
          [weight2, weight4]]

window = sg.Window('Sbox generator', layout).Finalize()
window.Maximize()

amount = 0;

while True:
    event, value = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "Generate":
        g = goodBlock(value["amount"], value, window);
        g.calculate();
        window["amount"].update(value=g.amount)

        window["Save boxes"].update(disabled=False);
        window["Show weight"].update(disabled=False);

    if event == "Show weight":
        try:
            window["weight2"].update(value="");
            window["weight4"].update(value="");

            Sbox = eval(value["boxes256"][0]);

            insertion(findWeight2base.calculateWeight(Sbox).createFuns(), 'weight2', window);
            insertion(findWeight4base.calculateWeight(Sbox).createFuns(), 'weight4', window);

        except:
            msb.showerror("Error!", "You need to choose Sbox")

    if event == "Save boxes":
        saveSboxes(window, value)
