import tkinter as tk
from tkinter.ttk import *
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import tooltip
import framer
from tkinter import *


class FunctionWindow:
    """
    Window for annotating VoxML Relations like "the", "a"
    """

    def __init__(self):
        self.arglist = []

        self.clearall_button = Button(framer.Funcframe, text="clear", command=lambda: self.clear())
        self.clearall_button.config(image=framer.cancelbtnpic, borderwidth=0, bg="#fa7878", activebackground="#fa7878",
                                    compound=CENTER, foreground="white", activeforeground="#fa7878", font=(None, 13))
        self.clearall_button.place(x=560, y=590)
        tooltip.CreateToolTip(self.clearall_button, text='Tooltip:\n\n'
                                                         'Klick this button to discard your modifications\n'
                                                         'and clear all checkboxes, option menus and text fields')

        self.exec_button = Button(framer.Funcframe, text="save",
                                  command=lambda: self.getvals())
        self.exec_button.config(image=framer.smallbtnpic, borderwidth=0, bg="#a3ff8f", activebackground="#a3ff8f",
                                compound=CENTER, foreground="white", activeforeground="#a3ff8f", font=(None, 13))
        self.exec_button.place(x=560, y=636)
        tooltip.CreateToolTip(self.exec_button, text='Tooltip:\n\n'
                                                     'Klick this button to save your modifications\n'
                                                     'to a VoxML conform XML document')

        self.debug_textfield = tk.Text(framer.Funcframe, height=4, width=48)
        self.debug_textfield.configure(relief=RIDGE, bd=2, foreground="white", insertbackground="white",
                                       background="#505050", font=(None, 12))
        self.debug_textfield.place(x=100, y=590)

        self.lex_label = Label(framer.Funcframe, text="<Lex>", foreground="white", background="#404040",
                               font=(None, 14))
        self.lex_label.place(x=50, y=50)

        self.pred_label = Label(framer.Funcframe, text="Predicate:", foreground="white", background="#404040",
                                font=(None, 12))
        self.pred_label.place(x=100, y=80)

        self.pred_entry = Entry(framer.Funcframe)
        self.pred_entry.configure(relief=RIDGE, width=17, bd=2, foreground="white", insertbackground="white",
                                  background="#505050", font=(None, 12))
        self.pred_entry.place(x=190, y=80)

        self.type_label = Label(framer.Funcframe, text="<Type>", foreground="white", background="#404040",
                                font=(None, 14))
        self.type_label.place(x=50, y=140)

        self.arguments_label = Label(framer.Funcframe, text="Argument:", foreground="white", background="#404040",
                                     font=(None, 12))
        self.arguments_label.place(x=100, y=170)

        self.optionVarArgtype = StringVar()
        self.optionVarArgtype.set("agent")

        self.optionmenuargtype = OptionMenu(framer.Funcframe, self.optionVarArgtype, "agent", "location", "physobj")
        self.optionmenuargtype.place(x=190, y=170)
        self.optionmenuargtype.config(width=145, height=14, image=framer.menutickpic, anchor="w", bd=0, indicatoron=0,
                                      compound=LEFT, bg="#404040", activebackground="#404040", foreground="white",
                                      activeforeground="#a3ff8f", font=(None, 12))

        self.argvar_entry = Entry(framer.Funcframe, width=4)
        self.argvar_entry.configure(relief=RIDGE, width=3, bd=2, foreground="white", insertbackground="white",
                                    background="#505050", font=(None, 12))
        self.argvar_entry.place(x=370, y=170)

        self.add_argument_button = Button(framer.Funcframe, text="add",
                                          command=lambda: self.addargument(self.optionVarArgtype.get(),
                                                                           self.argvar_entry.get()))
        self.add_argument_button.config(image=framer.smallbtnpic, borderwidth=0, bg="#a3ff8f",
                                        activebackground="#a3ff8f",
                                        compound=CENTER, foreground="white", activeforeground="#a3ff8f",
                                        font=(None, 13))
        self.add_argument_button.place(x=560, y=168)
        tooltip.CreateToolTip(self.add_argument_button, text='Tooltip:\n\n'
                                                             'Klick this button to add an argument\n'
                                                             'to the current function.')

        self.referent_label = Label(framer.Funcframe, text="Referent:", foreground="white", background="#404040",
                                    font=(None, 12))
        self.referent_label.place(x=100, y=200)

        self.referent_entry = Entry(framer.Funcframe)
        self.referent_entry.place(x=190, y=200)
        self.referent_entry.configure(relief=RIDGE, width=17, bd=2, foreground="white", insertbackground="white",
                                      background="#505050", font=(None, 12))

        self.mapping_label = Label(framer.Funcframe, text="Mapping:", foreground="white", background="#404040",
                                   font=(None, 12))
        self.mapping_label.place(x=100, y=230)

        self.mapping_entry = Entry(framer.Funcframe)
        self.mapping_entry.place(x=190, y=230)
        self.mapping_entry.configure(relief=RIDGE, width=17, bd=2, foreground="white", insertbackground="white",
                                     background="#505050", font=(None, 12))

        self.orientation_label = Label(framer.Funcframe, text="<Orientation>", foreground="white", background="#404040",
                                       font=(None, 14))
        self.orientation_label.place(x=50, y=290)

        self.space_label = Label(framer.Funcframe, text="Space:", foreground="white", background="#404040",
                                 font=(None, 12))
        self.space_label.place(x=100, y=320)

        self.optionVarSpace = StringVar()
        self.optionVarSpace.set("world")

        self.optionmenuspace = OptionMenu(framer.Funcframe, self.optionVarSpace, "world", "object")
        self.optionmenuspace.place(x=190, y=320)
        self.optionmenuspace.config(width=145, height=14, image=framer.menutickpic, anchor="w", bd=0, indicatoron=0,
                                    compound=LEFT, bg="#404040", activebackground="#404040", foreground="white",
                                    activeforeground="#a3ff8f", font=(None, 12))

        self.axis_label = Label(framer.Funcframe, text="Axis:", foreground="white", background="#404040",
                                font=(None, 12))
        self.axis_label.place(x=100, y=350)
        tooltip.CreateToolTip(self.add_argument_button, text='Tooltip:\n\n'
                                                             'add a + or - to the axis to specify\n'
                                                             'a direction')

        self.axis_entry = Entry(framer.Funcframe)
        self.axis_entry.place(x=190, y=350)
        self.axis_entry.configure(relief=RIDGE, width=17, bd=2, foreground="white", insertbackground="white",
                                  background="#505050", font=(None, 12))

        self.arity_label = Label(framer.Funcframe, text="Arity:", foreground="white", background="#404040",
                                 font=(None, 12))
        self.arity_label.place(x=100, y=380)

        self.arity_entry = Entry(framer.Funcframe)
        self.arity_entry.place(x=190, y=380)
        self.arity_entry.configure(relief=RIDGE, width=17, bd=2, foreground="white", insertbackground="white",
                                   background="#505050", font=(None, 12))

        drdwnlist = [self.optionmenuargtype, self.optionmenuspace]
        for drdwn in drdwnlist:
            i = 0
            while i < drdwn['menu'].index('end') + 1:
                drdwn['menu'].entryconfig(i, background="#404040", activebackground="#505050", foreground="white",
                                          activeforeground="#a3ff8f")
                i += 1

    def prettify(self, elem, filename):
        rough_string = ET.tostring(elem, 'us-ascii')
        reparsed = minidom.parseString(rough_string)
        rep = reparsed.toprettyxml(encoding='us-ascii', indent="\t").decode()
        print(rep)
        text_file = open("voxmldocs/functions/" + filename + ".xml", "w")
        text_file.truncate()
        text_file.write(rep)
        text_file.close()

    def createtree(self, pred, argtyp, argvar, ref, mapp, space, axis, arity):
        VoxML = ET.Element("VoxML")
        VoxML.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
        VoxML.set('xmlns:xsd', "http://www.w3.org/2001/XMLSchema")

        Entity = ET.SubElement(VoxML, "Entity", Type="Function")

        Lex = ET.SubElement(VoxML, "Lex")
        Pred = ET.SubElement(Lex, "Pred")
        Pred.text = pred

        Type = ET.SubElement(VoxML, "Type")
        Args = ET.SubElement(Type, "Args")
        for i in self.arglist:
            new_arg = ET.SubElement(Args, "Arg", Value=i)
        Referent = ET.SubElement(Type, "Referent")
        Referent.text = ref
        Mapping = ET.SubElement(Type, "Mapping")
        Mapping.text = mapp
        Orientation = ET.SubElement(Type, "Orientation")
        Space = ET.SubElement(Orientation, "Space")
        Space.text = space
        Axis = ET.SubElement(Orientation, "Axis")
        Axis.text = axis
        Arity = ET.SubElement(Orientation, "Arity")
        Arity.text = arity

        self.prettify(VoxML, pred)

    def addargument(self, vartyp, varname):
        global arglist
        fullarg = varname + ":" + vartyp
        self.arglist.append(fullarg)
        self.debug_textfield.delete('1.0', tk.END)
        self.debug_textfield.insert(tk.INSERT, "Argument has been added!")

    def getvals(self):
        predstring = self.pred_entry.get()
        argtypstring = self.optionVarArgtype.get()
        argvarstring = self.argvar_entry.get()
        refstring = self.referent_entry.get()
        mapstring = self.mapping_entry.get()
        spacestring = self.optionVarSpace.get()
        axisstring = self.axis_entry.get()
        aritystring = self.arity_entry.get()

        self.createtree(predstring, argtypstring, argvarstring, refstring, mapstring,
                        spacestring, axisstring, aritystring)

    def clear(self):
        self.__init__()
