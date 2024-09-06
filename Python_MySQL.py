
import tkinter as tk

# importing remaining tkinter modules
from tkinter import *

from tkinter import ttk
from tkinter import messagebox

from Clients import *
from Connection import *


class clients_form:

    global base
    base = None

    global textBoxId
    textBoxId = None

    global textBoxNames
    textBoxNames = None

    global textBoxSurnames
    textBoxSurnames = None

    global combo
    combo = None

    global groupBox
    groupBox = None

    global tree
    tree = None


def formulry():

    global textBoxId
    global textBoxNames
    global textBoxSurnames
    global combo
    global base
    global groupBox
    global tree

    try:
        base = Tk()
        base.geometry('1200x300')
        base.title('Python form')

        groupBox = LabelFrame(base, text='Staff Data', padx=5, pady=5)
        groupBox.grid(row=0, column=0, padx=10, pady=10)

        labelId = Label(groupBox, text='Id:', width=13,
                        font=('arial', 12)).grid(row=0, column=0)
        textBoxId = Entry(groupBox)
        textBoxId.grid(row=0, column=1)

        labelNames = Label(groupBox, text='Names:', width=13, font=(
            'arial', 12)).grid(row=1, column=0)
        textBoxNames = Entry(groupBox)
        textBoxNames.grid(row=1, column=1)

        labelSurnames = Label(groupBox, text='Surnames:', width=13, font=(
            'arial', 12)).grid(row=2, column=0)
        textBoxSurnames = Entry(groupBox)
        textBoxSurnames.grid(row=2, column=1)

        labelSex = Label(groupBox, text='Sex:', width=13, font=(
            'arial', 12)).grid(row=3, column=0)
        selectedSex = tk.StringVar()
        combo = ttk.Combobox(
            groupBox, values=['Male', 'Female'], textvariable=selectedSex)
        combo.grid(row=3, column=1)
        selectedSex.set('Male')

        Button(groupBox, text='Save', width=11,
               command=saveRecords).grid(row=4, column=0)
        Button(groupBox, text='Update', width=11,
               command=modifyRecords).grid(row=4, column=1)
        Button(groupBox, text='Delete', width=11,
               command=deleteRecords).grid(row=4, column=2)

        groupBox = LabelFrame(base, text='Satff list', padx=5, pady=5,)
        groupBox.grid(row=0, column=1, padx=5, pady=5)
        # Create a TreeView

        # Colums configuration

        tree = ttk.Treeview(groupBox, columns=(
            "Id", "Names", 'Surnames', 'Sex'), show='headings', height=5,)
        tree.column('#1', anchor=CENTER)
        tree.heading('#1', text='Id')
        tree.column('#2', anchor=CENTER)
        tree.heading('#2', text='Names')
        tree.column('#3', anchor=CENTER)
        tree.heading('#3', text='Surnames')
        tree.column('#4', anchor=CENTER)
        tree.heading('#4', text='Sex')

        for row in Cclients.showClients():
            tree.insert('', "end", values=row)

        # Execute the click function and print the results in each entry

        tree.bind("<<TreeviewSelect>>", selectingRecord)

        tree.pack()

        base.mainloop()

    except ValueError as error:
        print(f'An error occurred showing interface, error{error}')


def saveRecords():

    global textBoxNames, textBoxSurnames, combo, groupBox

    try:
        if textBoxNames is None or textBoxSurnames is None or combo is None:
            print('Widgets not initialized')
            return
        names = textBoxNames.get()
        surnames = textBoxSurnames.get()
        sex = combo.get()

        Cclients.enterClients(names, surnames, sex)
        messagebox.showinfo('Information', 'Data has been saved')

        updateTreeView()

        textBoxNames.delete(0, END)
        textBoxSurnames.delete(0, END)

    except ValueError as error:
        print(f'error entering data: Error {error}')


def updateTreeView():
    global tree

    try:
        tree.delete(*tree.get_children())
        data = Cclients.showClients()
        for row in Cclients.showClients():
            tree.insert('', "end", values=row)

    except ValueError as error:
        print(f'Error updating table. Error: {error}')


def selectingRecord(event):

    try:
        selectedItem = tree.focus()

        if selectedItem:
            values = tree.item(selectedItem)['values']

            textBoxId.delete(0, END)
            textBoxId.insert(0, values[0])
            textBoxNames.delete(0, END)
            textBoxNames.insert(0, values[1])
            textBoxSurnames.delete(0, END)
            textBoxSurnames.insert(0, values[2])
            combo.set(values[3])

    except ValueError as error:
        print(f'error selectin record. Error {error}')


def modifyRecords():

    global textBoxId, textBoxNames, textBoxSurnames, combo, groupBox

    try:
        if textBoxId is None or textBoxSurnames is None or combo is None:
            print('Widgets not initialized')
            return

        userId = textBoxId.get()
        names = textBoxNames.get()
        surnames = textBoxSurnames.get()
        sex = combo.get()

        Cclients.modifyClients(userId, names, surnames, sex)
        messagebox.showinfo('Information', 'Data has been updated')

        updateTreeView()

        textBoxId.delete(0, END)
        textBoxNames.delete(0, END)
        textBoxSurnames.delete(0, END)

    except ValueError as error:
        print(f'error updating data: Error {error}')


def deleteRecords():

    global textBoxId, textBoxNames, textBoxSurnames

    try:
        if textBoxId is None:
            print('Widgets not initialized')
            return

        userId = textBoxId.get()

        Cclients.deleteClients(userId)
        messagebox.showinfo('Information', 'Data has been deleted')

        updateTreeView()

        textBoxId.delete(0, END)
        textBoxNames.delete(0, END)
        textBoxSurnames.delete(0, END)

    except ValueError as error:
        print(f'error updating data: Error {error}')


formulry()
