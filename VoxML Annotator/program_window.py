import tkinter as tk
from tkinter.ttk import *
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import tooltip
import framer
from tkinter import *


class ProgramWindow:
    """
     Window for annotating VoxML Programs like "hold", "switch", "shuffle"
     """

    def __init__(self):
        self.arglist = []
        self.subeventlist = []

        self.clearall_button = Button(framer.Progrframe, text="clear", command=lambda: self.clear())
        self.clearall_button.config(image=framer.cancelbtnpic, borderwidth=0, bg="#fa7878", activebackground="#fa7878",
                                    compound=CENTER, foreground="white", activeforeground="#fa7878", font=(None, 13))
        self.clearall_button.place(x=560, y=590)
        tooltip.CreateToolTip(self.clearall_button, text='Tooltip:\n\n'
                                                         'Klick this button to discard your modifications\n'
                                                         'and clear all checkboxes, option menus and text fields')

        self.exec_button = Button(framer.Progrframe, text="save",
                                  command=lambda: self.getvals())
        self.exec_button.config(image=framer.smallbtnpic, borderwidth=0, bg="#a3ff8f", activebackground="#a3ff8f",
                                compound=CENTER, foreground="white", activeforeground="#a3ff8f", font=(None, 13))
        self.exec_button.place(x=560, y=636)
        tooltip.CreateToolTip(self.exec_button, text='Tooltip:\n\n'
                                                     'Klick this button to save your modifications\n'
                                                     'to a VoxML conform XML document')

        self.debug_textfield = tk.Text(framer.Progrframe, height=4, width=48)
        self.debug_textfield.configure(relief=RIDGE, bd=2, foreground="white", insertbackground="white",
                                       background="#505050", font=(None, 12))
        self.debug_textfield.place(x=100, y=590)

        self.group_label = Label(framer.Progrframe, text="Group:", foreground="white", background="#404040",
                                 font=(None, 14))
        self.group_label.place(x=360, y=50)
        tooltip.CreateToolTip(self.group_label, text='Tooltip:\n\n'
                                                     'Use Integers to refer to groups of parts,\n'
                                                     'habitats or affordance formulas')

        self.lex_label = Label(framer.Progrframe, text="<Lex>", foreground="white", background="#404040",
                               font=(None, 14))
        self.lex_label.place(x=50, y=50)

        self.pred_label = Label(framer.Progrframe, text="Predicate:", foreground="white", background="#404040",
                                font=(None, 12))
        self.pred_label.place(x=100, y=80)

        self.pred_entry = Entry(framer.Progrframe)
        self.pred_entry.configure(relief=RIDGE, width=17, bd=2, foreground="white", insertbackground="white",
                                  background="#505050", font=(None, 12))
        self.pred_entry.place(x=190, y=80)

        self.typesub_label = Label(framer.Progrframe, text="Type:", foreground="white", background="#404040",
                                   font=(None, 12))
        self.typesub_label.place(x=100, y=110)

        self.typeVar = StringVar()
        self.typeVar.set("process")

        self.option = OptionMenu(framer.Progrframe, self.typeVar, "process", "state", "transition_event")
        self.option.place(x=190, y=110)
        self.option.config(width=145, height=14, image=framer.menutickpic, anchor="w", bd=0, indicatoron=0,
                           compound=LEFT,
                           bg="#404040", activebackground="#404040", foreground="white", activeforeground="#a3ff8f",
                           font=(None, 12))

        self.type_label = Label(framer.Progrframe, text="<Type>", foreground="white", background="#404040",
                                font=(None, 14))
        self.type_label.place(x=50, y=140)

        self.head_label = Label(framer.Progrframe, text="Head:", foreground="white", background="#404040",
                                font=(None, 12))
        self.head_label.place(x=100, y=170)

        self.headVar = StringVar()
        self.headVar.set("process")
        self.optionmenuhead = OptionMenu(framer.Progrframe, self.headVar, "process", "state", "transition")
        self.optionmenuhead.place(x=190, y=170)
        self.optionmenuhead.config(width=145, height=14, image=framer.menutickpic, anchor="w", borderwidth=0,
                                   indicatoron=0,
                                   compound=LEFT, bg="#404040", activebackground="#404040", foreground="white",
                                   activeforeground="#a3ff8f", font=(None, 11))

        self.arguments_label = Label(framer.Progrframe, text="Argument:", foreground="white", background="#404040",
                                     font=(None, 12))
        self.arguments_label.place(x=100, y=200)

        self.optionVarArgtype = StringVar()
        self.optionVarArgtype.set("agent")

        self.optionmenuargtype = OptionMenu(framer.Progrframe, self.optionVarArgtype, "agent", "location", "physobj")
        self.optionmenuargtype.place(x=190, y=200)
        self.optionmenuargtype.config(width=145, height=14, image=framer.menutickpic, anchor="w", borderwidth=0,
                                      indicatoron=0, compound=LEFT, bg="#404040", activebackground="#404040",
                                      foreground="white", activeforeground="#a3ff8f", font=(None, 11))

        self.argvar_entry = Entry(framer.Progrframe, width=4)
        self.argvar_entry.configure(relief=RIDGE, width=3, bd=2, foreground="white", insertbackground="white",
                                    background="#505050", font=(None, 12))
        self.argvar_entry.place(x=370, y=200)

        self.add_argument_button = Button(framer.Progrframe, text="add",
                                          command=lambda: self.addargument(self.optionVarArgtype.get(),
                                                                           self.argvar_entry.get()))
        self.add_argument_button.config(image=framer.smallbtnpic, borderwidth=0, bg="#a3ff8f",
                                        activebackground="#a3ff8f",
                                        compound=CENTER, foreground="white", activeforeground="#a3ff8f",
                                        font=(None, 13))
        self.add_argument_button.place(x=560, y=198)
        tooltip.CreateToolTip(self.add_argument_button, text='Tooltip:\n\n'
                                                             'Klick this button to add a component\n'
                                                             'to the componentlist of the current object')

        self.body_label = Label(framer.Progrframe, text="<Body>", foreground="white", background="#404040",
                                font=(None, 14))
        self.body_label.place(x=50, y=230)

        self.subevent_label = Label(framer.Progrframe, text="Subevent:", foreground="white", background="#404040",
                                    font=(None, 12))
        self.subevent_label.place(x=100, y=260)

        self.subevent_entry = Entry(framer.Progrframe)
        self.subevent_entry.configure(relief=RIDGE, width=17, bd=2, foreground="white", insertbackground="white",
                                      background="#505050", font=(None, 12))
        self.subevent_entry.place(x=190, y=260)

        self.add_subevent_button = Button(framer.Progrframe, text="add", command=lambda: self.addsubevent())
        self.add_subevent_button.config(image=framer.smallbtnpic, borderwidth=0, bg="#a3ff8f",
                                        activebackground="#a3ff8f",
                                        compound=CENTER, foreground="white", activeforeground="#a3ff8f",
                                        font=(None, 13))
        self.add_subevent_button.place(x=560, y=258)

        drdwnlist = [self.option, self.optionmenuhead, self.optionmenuargtype]
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
        text_file = open("voxmldocs/programs/" + filename + ".xml", "w")
        text_file.truncate()
        text_file.write(rep)
        text_file.close()

    def createtree(self, pred, typ, head, argtyp, argvar):
        VoxML = ET.Element("VoxML")
        VoxML.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
        VoxML.set('xmlns:xsd', "http://www.w3.org/2001/XMLSchema")

        Entity = ET.SubElement(VoxML, "Entity", Type="Program")

        Lex = ET.SubElement(VoxML, "Lex")
        Pred = ET.SubElement(Lex, "Pred")
        Pred.text = pred
        SubType = ET.SubElement(Lex, "Type")
        SubType.text = typ

        Type = ET.SubElement(VoxML, "Type")
        Head = ET.SubElement(Type, "Head")
        Head.text = typ
        Args = ET.SubElement(Type, "Args")
        for i in self.arglist:
            new_arg = ET.SubElement(Args, "Arg", Value=i)
        Body = ET.SubElement(Type, "Body")
        for i in self.subeventlist:
            new_subevent = ET.SubElement(Body, "Subevent", Value=i)

        self.prettify(VoxML, pred)

    def addsubevent(self, event):
        self.subeventlist.append(event)
        self.debug_textfield.delete('1.0', tk.END)
        self.debug_textfield.insert(tk.INSERT, "Subevent has been added!")

    def addargument(self, vartyp, varname):
        fullarg = varname + ":" + vartyp
        self.arglist.append(fullarg)
        self.debug_textfield.delete('1.0', tk.END)
        self.debug_textfield.insert(tk.INSERT, "Argument has been added!")

    def getvals(self):
        predstring = self.pred_entry.get()
        optVar = self.typeVar.get()
        headVar = self.headVar.get()
        argtypstring = self.optionVarArgtype.get()
        argvarstring = self.argvar_entry.get()

        self.createtree(predstring, optVar, headVar, argtypstring, argvarstring)

    def clear(self):
        self.__init__()
