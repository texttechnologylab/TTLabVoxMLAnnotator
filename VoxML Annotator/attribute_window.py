import tkinter as tk
from tkinter.ttk import *
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import tooltip
import framer
from tkinter import *


class AttributeWindow:
    """
     Window for annotating VoxML Programs like "red"
     """

    def __init__(self):
        self.arglist = []

        self.clearall_button = Button(framer.Attrframe, text="clear", command=lambda: self.clear())
        self.clearall_button.config(image=framer.cancelbtnpic, borderwidth=0, bg="#fa7878", activebackground="#fa7878",
                                    compound=CENTER, foreground="white", activeforeground="#fa7878", font=(None, 13))
        self.clearall_button.place(x=560, y=590)
        tooltip.CreateToolTip(self.clearall_button, text='Tooltip:\n\n'
                                                         'Klick this button to discard your modifications\n'
                                                         'and clear all checkboxes, option menus and text fields')

        self.exec_button = Button(framer.Attrframe, text="save",
                                  command=lambda: self.getvals())
        self.exec_button.config(image=framer.smallbtnpic, borderwidth=0, bg="#a3ff8f", activebackground="#a3ff8f",
                                compound=CENTER, foreground="white", activeforeground="#a3ff8f", font=(None, 13))
        self.exec_button.place(x=560, y=636)
        tooltip.CreateToolTip(self.exec_button, text='Tooltip:\n\n'
                                                     'Klick this button to save your modifications\n'
                                                     'to a VoxML conform XML document')

        self.debug_textfield = tk.Text(framer.Attrframe, height=4, width=48)
        self.debug_textfield.configure(relief=RIDGE, bd=2, foreground="white", insertbackground="white",
                                       background="#505050", font=(None, 12))
        self.debug_textfield.place(x=100, y=590)

        self.lex_label = Label(framer.Attrframe, text="<Lex>", foreground="white", background="#404040",
                               font=(None, 14))
        self.lex_label.place(x=50, y=50)

        self.pred_label = Label(framer.Attrframe, text="Predicate:", foreground="white", background="#404040",
                                font=(None, 12))
        self.pred_label.place(x=100, y=80)

        self.pred_entry = Entry(framer.Attrframe)
        self.pred_entry.configure(relief=RIDGE, width=17, bd=2, foreground="white", insertbackground="white",
                                  background="#505050", font=(None, 12))
        self.pred_entry.place(x=190, y=80)

        self.type_label = Label(framer.Attrframe, text="<Type>", foreground="white", background="#404040",
                                font=(None, 14))
        self.type_label.place(x=50, y=140)

        self.arguments_label = Label(framer.Attrframe, text="Argument:", foreground="white", background="#404040",
                                     font=(None, 12))
        self.arguments_label.place(x=100, y=200)

        self.optionVarArgtype = StringVar()
        self.optionVarArgtype.set("agent")

        self.optionmenuargtype = OptionMenu(framer.Attrframe, self.optionVarArgtype, "agent", "location", "physobj")
        self.optionmenuargtype.place(x=190, y=200)
        self.optionmenuargtype.config(width=145, height=14, image=framer.menutickpic, anchor="w", bd=0, indicatoron=0,
                                      compound=LEFT, bg="#404040", activebackground="#404040", foreground="white",
                                      activeforeground="#a3ff8f", font=(None, 12))

        self.argvar_entry = Entry(framer.Attrframe, width=4)
        self.argvar_entry.configure(relief=RIDGE, width=3, bd=2, foreground="white", insertbackground="white",
                                    background="#505050", font=(None, 12))
        self.argvar_entry.place(x=370, y=200)

        self.add_argument_button = Button(framer.Attrframe, text="add",
                                          command=lambda: self.addargument(self.argvar_entry.get(),
                                                                           self.optionVarArgtype.get()))
        self.add_argument_button.config(image=framer.smallbtnpic, borderwidth=0, bg="#a3ff8f",
                                        activebackground="#a3ff8f", compound=CENTER, foreground="white",
                                        activeforeground="#a3ff8f", font=(None, 13))
        self.add_argument_button.place(x=480, y=198)
        tooltip.CreateToolTip(self.add_argument_button, text='Tooltip:\n\n'
                                                             'Klick this button to add a component\n'
                                                             'to the componentlist of the current object')

        self.scale_label = Label(framer.Attrframe, text="Scale:", foreground="white", background="#404040",
                                 font=(None, 12))
        self.scale_label.place(x=100, y=230)

        self.optionVarScale = StringVar()
        self.optionVarScale.set("binary")

        self.optionmenuscale = OptionMenu(framer.Attrframe, self.optionVarScale, "binary", "nominal", "ordinal",
                                          "intervall", "rational")
        self.optionmenuscale.place(x=190, y=230)
        self.optionmenuscale.config(width=145, height=14, image=framer.menutickpic, anchor="w", bd=0, indicatoron=0,
                                    compound=LEFT, bg="#404040", activebackground="#404040", foreground="white",
                                    activeforeground="#a3ff8f", font=(None, 12))

        self.arity_label = Label(framer.Attrframe, text="Arity:", foreground="white", background="#404040",
                                 font=(None, 12))
        self.arity_label.place(x=100, y=260)

        self.optionVarArity = StringVar()
        self.optionVarArity.set("intransitive")

        self.optionmenuarity = OptionMenu(framer.Attrframe, self.optionVarArity, "intransitive", "transitive")
        self.optionmenuarity.place(x=190, y=260)
        self.optionmenuarity.config(width=145, height=14, image=framer.menutickpic, anchor="w", bd=0, indicatoron=0,
                                    compound=LEFT, bg="#404040", activebackground="#404040", foreground="white",
                                    activeforeground="#a3ff8f", font=(None, 12))

        drdwnlist = [self.optionmenuargtype, self.optionmenuscale, self.optionmenuarity]
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
        text_file = open("voxmldocs/attributes/" + filename + ".xml", "w")
        text_file.truncate()
        text_file.write(rep)
        text_file.close()

    def createtree(self, pred, argtyp, argvar, scale, arity):
        VoxML = ET.Element("VoxML")
        VoxML.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
        VoxML.set('xmlns:xsd', "http://www.w3.org/2001/XMLSchema")

        ET.SubElement(VoxML, "Entity", Type="Attribute")

        Lex = ET.SubElement(VoxML, "Lex")
        Pred = ET.SubElement(Lex, "Pred")
        Pred.text = pred

        Type = ET.SubElement(VoxML, "Type")
        Args = ET.SubElement(Type, "Args")
        for i in self.arglist:
            ET.SubElement(Args, "Arg", Value=i)
        Scale = ET.SubElement(Type, "Scale")
        Scale.text = scale
        Arity = ET.SubElement(Type, "Arity")
        Arity.text = arity

        self.prettify(VoxML, pred)

    def addargument(self, optionVarArgtype, argvar_entry):
        fullarg = argvar_entry + ":" + optionVarArgtype
        self.arglist.append(fullarg)
        self.debug_textfield.delete('1.0', tk.END)
        self.debug_textfield.insert(tk.INSERT, "Argument has been added!")

    def getvals(self):
        predstring = self.pred_entry.get()
        argtypstring = self.optionVarArgtype.get()
        argvarstring = self.argvar_entry.get()
        scalestring = self.optionVarScale.get()
        aritystring = self.optionVarArity.get()

        self.createtree(predstring, argtypstring, argvarstring, scalestring, aritystring)

    def clear(self):
        self.__init__()
