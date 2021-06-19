import tkinter as tk
from tkinter.ttk import *
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import tooltip
import framer
from tkinter import *


class RelationWindow:
    """
    Window for annotating VoxML Relations like "behind", "in", "in_front_of"
    """

    def __init__(self):
        self.arglist = []
        self.constraintlist = []
        self.corresplist = []

        self.clearall_button = Button(framer.Relatframe, text="clear",
                                      command=lambda: self.clear())
        self.clearall_button.config(image=framer.cancelbtnpic, borderwidth=0, bg="#fa7878", activebackground="#fa7878",
                                    compound=CENTER, foreground="white", activeforeground="#fa7878", font=(None, 13))
        self.clearall_button.place(x=560, y=590)
        tooltip.CreateToolTip(self.clearall_button, text='Tooltip:\n\n'
                                                         'Klick this button to discard your modifications\n'
                                                         'and clear all checkboxes, option menus and text fields')

        self.exec_button = Button(framer.Relatframe, text="save",
                                  command=lambda: self.getvals())
        self.exec_button.config(image=framer.smallbtnpic, borderwidth=0, bg="#a3ff8f", activebackground="#a3ff8f",
                                compound=CENTER, foreground="white", activeforeground="#a3ff8f", font=(None, 13))
        self.exec_button.place(x=560, y=636)
        tooltip.CreateToolTip(self.exec_button, text='Tooltip:\n\n'
                                                     'Klick this button to save your modifications\n'
                                                     'to a VoxML conform XML document')

        self.debug_textfield = tk.Text(framer.Relatframe, height=4, width=48)
        self.debug_textfield.configure(relief=RIDGE, bd=2, foreground="white", insertbackground="white",
                                       background="#505050", font=(None, 12))
        self.debug_textfield.place(x=100, y=590)

        self.lex_label = Label(framer.Relatframe, text="<Lex>", foreground="white", background="#404040",
                               font=(None, 14))
        self.lex_label.place(x=50, y=50)

        self.pred_label = Label(framer.Relatframe, text="Predicate:", foreground="white", background="#404040",
                                font=(None, 12))
        self.pred_label.place(x=100, y=80)

        self.pred_entry = Entry(framer.Relatframe)
        self.pred_entry.configure(relief=RIDGE, width=17, bd=2, foreground="white", insertbackground="white",
                                  background="#505050", font=(None, 12))
        self.pred_entry.place(x=190, y=80)

        self.type_label = Label(framer.Relatframe, text="<Type>", foreground="white", background="#404040",
                                font=(None, 14))
        self.type_label.place(x=50, y=140)

        self.class_label = Label(framer.Relatframe, text="Class:", foreground="white", background="#404040",
                                 font=(None, 12))
        self.class_label.place(x=100, y=170)

        self.optionVarClass = StringVar()
        self.optionVarClass.set("config")

        self.optionmenuclass = OptionMenu(framer.Relatframe, self.optionVarClass, "config", "force_dynamic")
        self.optionmenuclass.place(x=190, y=170)
        self.optionmenuclass.config(width=145, height=14, image=framer.menutickpic, anchor="w", bd=0, indicatoron=0,
                                    compound=LEFT, bg="#404040", activebackground="#404040", foreground="white",
                                    activeforeground="#a3ff8f", font=(None, 12))

        self.arguments_label = Label(framer.Relatframe, text="Value:", foreground="white", background="#404040",
                                     font=(None, 12))
        self.arguments_label.place(x=100, y=200)

        self.optionVarValue = StringVar()
        self.optionVarValue.set("RCC8.DC")

        self.optionmenuvalue = OptionMenu(framer.Relatframe, self.optionVarValue, "RCC8.DC", "RCC8.EC", "RCC8.TPP",
                                          "RCC8.PO",
                                          "RCC8.EQ", "RCC8.TPP", "RCC8.NTPP", "RCC8.IN")
        self.optionmenuvalue.place(x=190, y=200)
        self.optionmenuvalue.config(width=145, height=14, image=framer.menutickpic, anchor="w", bd=0, indicatoron=0,
                                    compound=LEFT, bg="#404040", activebackground="#404040", foreground="white",
                                    activeforeground="#a3ff8f", font=(None, 12))

        self.arguments_label = Label(framer.Relatframe, text="Argument:", foreground="white", background="#404040",
                                     font=(None, 12))
        self.arguments_label.place(x=100, y=230)

        self.optionVarArgtype = StringVar()
        self.optionVarArgtype.set("agent")

        self.optionmenuargtype = OptionMenu(framer.Relatframe, self.optionVarArgtype, "agent", "location", "physobj")
        self.optionmenuargtype.place(x=190, y=230)
        self.optionmenuargtype.config(width=145, height=14, image=framer.menutickpic, anchor="w", bd=0, indicatoron=0,
                                      compound=LEFT, bg="#404040", activebackground="#404040", foreground="white",
                                      activeforeground="#a3ff8f", font=(None, 12))

        self.argvar_entry = Entry(framer.Relatframe, width=4)
        self.argvar_entry.configure(relief=RIDGE, width=3, bd=2, foreground="white", insertbackground="white",
                                    background="#505050", font=(None, 12))
        self.argvar_entry.place(x=370, y=230)

        self.add_argument_button = Button(framer.Relatframe, text="add",
                                          command=lambda: self.addargument(self.optionVarArgtype.get(),
                                                                           self.argvar_entry.get()))
        self.add_argument_button.config(image=framer.smallbtnpic, borderwidth=0, bg="#a3ff8f",
                                        activebackground="#a3ff8f",
                                        compound=CENTER, foreground="white", activeforeground="#a3ff8f",
                                        font=(None, 13))
        self.add_argument_button.place(x=560, y=228)
        tooltip.CreateToolTip(self.add_argument_button, text='Tooltip:\n\n'
                                                             'Klick this button to add a component\n'
                                                             'to the componentlist of the current object')

        self.constr_label = Label(framer.Relatframe, text="Constraint:", foreground="white", background="#404040",
                                  font=(None, 12))
        self.constr_label.place(x=100, y=260)

        self.constr_entry = Entry(framer.Relatframe)
        self.constr_entry.configure(relief=RIDGE, width=17, bd=2, foreground="white", insertbackground="white",
                                    background="#505050", font=(None, 12))
        self.constr_entry.place(x=190, y=260)

        self.add_constr_button = Button(framer.Relatframe, text="add",
                                        command=lambda: self.addconstr(self.constr_entry.get()))
        self.add_constr_button.config(image=framer.smallbtnpic, borderwidth=0, bg="#a3ff8f", activebackground="#a3ff8f",
                                      compound=CENTER, foreground="white", activeforeground="#a3ff8f", font=(None, 13))
        self.add_constr_button.place(x=560, y=258)

        self.corresps_label = Label(framer.Relatframe, text="Corresps.:", foreground="white", background="#404040",
                                    font=(None, 12))
        self.corresps_label.place(x=100, y=290)

        self.corresps_entry = Entry(framer.Relatframe)
        self.corresps_entry.configure(relief=RIDGE, width=17, bd=2, foreground="white", insertbackground="white",
                                      background="#505050", font=(None, 12))
        self.corresps_entry.place(x=190, y=290)

        self.add_corresps_button = Button(framer.Relatframe, text="add",
                                          command=lambda: self.addcorresp(self.corresps_entry.get()))
        self.add_corresps_button.config(image=framer.smallbtnpic, borderwidth=0, bg="#a3ff8f",
                                        activebackground="#a3ff8f",
                                        compound=CENTER, foreground="white", activeforeground="#a3ff8f",
                                        font=(None, 13))
        self.add_corresps_button.place(x=560, y=288)

        drdwnlist = [self.optionmenuclass, self.optionmenuvalue, self.optionmenuargtype]
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
        text_file = open("voxmldocs/relations/" + filename + ".xml", "w")
        text_file.truncate()
        text_file.write(rep)
        text_file.close()

    def createtree(self, pred, classent, valent, argtyp, argvar, constr, corresp):
        VoxML = ET.Element("VoxML")
        VoxML.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
        VoxML.set('xmlns:xsd', "http://www.w3.org/2001/XMLSchema")

        Entity = ET.SubElement(VoxML, "Entity", Type="Relation")

        Lex = ET.SubElement(VoxML, "Lex")
        Pred = ET.SubElement(Lex, "Pred")
        Pred.text = pred

        Type = ET.SubElement(VoxML, "Type")
        Class = ET.SubElement(Type, "Class")
        Class.text = classent
        Value = ET.SubElement(Type, "Value")
        Value.text = valent
        Args = ET.SubElement(Type, "Args")
        for i in self.arglist:
            new_arg = ET.SubElement(Args, "Arg", Value=i)
        for i in self.constraintlist:
            new_constraint = ET.SubElement(Type, "Constr")
            new_constraint.text = i
        Corresps = ET.SubElement(Type, "Corresps")
        for i in self.corresplist:
            new_corresp = ET.SubElement(Corresps, "Corresp", Value=i)

        self.prettify(VoxML, pred)

    def addargument(self, varname, vartyp):
        fullarg = varname + ":" + vartyp
        self.arglist.append(fullarg)
        self.debug_textfield.delete('1.0', tk.END)
        self.debug_textfield.insert(tk.INSERT, "Argument has been added!")

    def addconstr(self, constrstr):
        fullconstr = constrstr
        self.constraintlist.append(fullconstr)
        self.debug_textfield.delete('1.0', tk.END)
        self.debug_textfield.insert(tk.INSERT, "Constraint has been added!")

    def addcorresp(self, correspstr):
        fullcorresp = correspstr
        self.corresplist.append(fullcorresp)
        self.debug_textfield.delete('1.0', tk.END)
        self.debug_textfield.insert(tk.INSERT, "Corresp. has been added!")

    def getvals(self):
        predstring = self.pred_entry.get()
        classentstring = self.optionVarClass.get()
        valentstring = self.optionVarValue.get()
        argtypstring = self.optionVarArgtype.get()
        argvarstring = self.argvar_entry.get()
        conststring = self.constr_entry.get()
        correspstring = self.corresps_entry.get()

        self.createtree(predstring, classentstring, valentstring, argtypstring, argvarstring,
                        conststring, correspstring)

    def clear(self):
        self.__init__()
