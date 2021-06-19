import tkinter as tk
from tkinter.ttk import *
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from tkinter import *
import tooltip
import framer


class ObjectWindow:
    """
     Window for annotating VoxML Objects"
     """

    def __init__(self):
        self.componentlist = []
        self.intrinsiclist = []
        self.intrinsicvaluelist = []
        self.extrinsiclist = []
        self.extrinsicvaluelist = []
        self.affordanceformulalist = []

        self.clearall_button = Button(framer.Objframe, text="clear", command=lambda: self.clear())
        self.clearall_button.config(image=framer.cancelbtnpic, borderwidth=0, bg="#fa7878", activebackground="#fa7878",
                                    compound=CENTER, foreground="white", activeforeground="#fa7878", font=(None, 13))
        self.clearall_button.place(x=560, y=590)
        tooltip.CreateToolTip(self.clearall_button, text='Tooltip:\n\n'
                                                         'Klick this button to discard your modifications\n'
                                                         'and clear all checkboxes, option menus and text fields')

        self.exec_button = Button(framer.Objframe, text="save",
                                  command=lambda: self.getvals())
        self.exec_button.config(image=framer.smallbtnpic, borderwidth=0, bg="#a3ff8f", activebackground="#a3ff8f",
                                compound=CENTER, foreground="white", activeforeground="#a3ff8f", font=(None, 13))
        self.exec_button.place(x=560, y=636)
        tooltip.CreateToolTip(self.exec_button, text='Tooltip:\n\n'
                                                     'Klick this button to save your modifications\n'
                                                     'to a VoxML conform XML document')

        self.debug_textfield = tk.Text(framer.Objframe, height=4, width=48)
        self.debug_textfield.configure(relief=RIDGE, bd=2, foreground="white", insertbackground="white",
                                       background="#505050",
                                       font=(None, 12))
        self.debug_textfield.place(x=100, y=590)

        self.group_label = Label(framer.Objframe, text="Group:", foreground="white", background="#404040",
                                 font=(None, 14))
        self.group_label.place(x=360, y=50)
        tooltip.CreateToolTip(self.group_label, text='Tooltip:\n\n'
                                                     'Use Integers to refer to groups of parts,\n'
                                                     'habitats or affordance formulas')

        self.args_label = Label(framer.Objframe, text="Arguments:", foreground="white", background="#404040",
                                font=(None, 14))
        self.args_label.place(x=440, y=50)
        tooltip.CreateToolTip(self.args_label, text='Tooltip:\n\n'
                                                    'Insert functions arguments in entry fields\n'
                                                    'below')

        self.lex_label = Label(framer.Objframe, text="<Lex>", foreground="white", background="#404040", font=(None, 14))
        self.lex_label.place(x=50, y=50)

        self.pred_label = Label(framer.Objframe, text="Predicate:", foreground="white", background="#404040",
                                font=(None, 12))
        self.pred_label.place(x=100, y=80)

        self.pred_entry = Entry(framer.Objframe)
        self.pred_entry.configure(relief=RIDGE, width=17, bd=2, foreground="white", insertbackground="white",
                                  background="#505050", font=(None, 12))
        self.pred_entry.place(x=190, y=80)

        self.typesub_label = Label(framer.Objframe, text="Type:", foreground="white", background="#404040",
                                   font=(None, 12))
        self.typesub_label.place(x=100, y=110)

        self.optionVar = StringVar()
        self.optionVar.set("physobj")

        self.option = OptionMenu(framer.Objframe, self.optionVar, "physobj", "physobj*artifact")
        self.option.place(x=190, y=110)
        self.option.config(width=145, height=14, image=framer.menutickpic, anchor="w", bd=0, indicatoron=0,
                           compound=LEFT,
                           bg="#404040", activebackground="#404040", foreground="white", activeforeground="#a3ff8f",
                           font=(None, 12))

        self.type_label = Label(framer.Objframe, text="<Type>", foreground="white", background="#404040",
                                font=(None, 14))
        self.type_label.place(x=50, y=140)

        self.head_label = Label(framer.Objframe, text="Head:", foreground="white", background="#404040",
                                font=(None, 12))
        self.head_label.place(x=100, y=170)

        self.headgroup_entry = Entry(framer.Objframe, width=4)
        self.headgroup_entry.configure(relief=RIDGE, width=3, bd=2, foreground="white", insertbackground="white",
                                       background="#505050", font=(None, 12))
        self.headgroup_entry.place(x=370, y=170)
        tooltip.CreateToolTip(self.headgroup_entry, text='Tooltip:\n\n'
                                                         '*OPTIONAL*')

        self.optionVarHead = StringVar()
        self.optionVarHead.set("ellipsoid")

        self.optionmenuhead = OptionMenu(framer.Objframe, self.optionVarHead, "ellipsoid", "bipyramid", "cylindroid",
                                         "cupola",
                                         "frustum",
                                         "hemiellipsoid", "parallelepiped", "prismatoid", "pyramid",
                                         "rectangular_prism",
                                         "sheet",
                                         "toroid", "wedge")
        self.optionmenuhead.place(x=190, y=170)
        self.optionmenuhead.config(width=145, height=14, image=framer.menutickpic, anchor="w", borderwidth=0,
                                   indicatoron=0,
                                   compound=LEFT, bg="#404040", activebackground="#404040", foreground="white",
                                   activeforeground="#a3ff8f", font=(None, 11))

        self.component_label = Label(framer.Objframe, text="Component:", foreground="white", background="#404040",
                                     font=(None, 12))
        self.component_label.place(x=100, y=200)

        self.component_entry = Entry(framer.Objframe)
        self.component_entry.configure(relief=RIDGE, width=17, bd=2, foreground="white", insertbackground="white",
                                       background="#505050", font=(None, 12))
        self.component_entry.place(x=190, y=200)

        self.componentgroup_entry = Entry(framer.Objframe, width=4)
        self.componentgroup_entry.configure(relief=RIDGE, width=3, bd=2, foreground="white", insertbackground="white",
                                            background="#505050", font=(None, 12))
        self.componentgroup_entry.place(x=370, y=200)
        tooltip.CreateToolTip(self.componentgroup_entry, text='Tooltip:\n\n'
                                                              '*OPTIONAL*')
        self.duplicatevar = IntVar()
        self.duplicatevar.set(0)

        self.dupecheckbutton = Checkbutton(framer.Objframe, text="", variable=self.duplicatevar)
        self.dupecheckbutton.var = self.duplicatevar
        self.dupecheckbutton.config(borderwidth=0, background="#404040", activebackground="#404040",
                                    foreground="#404040",
                                    font=(None, 12))
        self.dupecheckbutton.place(x=470, y=200)
        tooltip.CreateToolTip(self.dupecheckbutton, text='Tooltip:\n\n'
                                                         'Check this box if the Object has multiple instances\n'
                                                         'or copies of that same part\n\n *OPTIONAL*')

        self.add_component_button = Button(framer.Objframe, text="add",
                                           command=lambda: self.addcomponent())
        self.add_component_button.config(image=framer.smallbtnpic, borderwidth=0, bg="#a3ff8f",
                                         activebackground="#a3ff8f",
                                         compound=CENTER, foreground="white", activeforeground="#a3ff8f",
                                         font=(None, 13))
        self.add_component_button.place(x=560, y=198)
        tooltip.CreateToolTip(self.add_component_button, text='Tooltip:\n\n'
                                                              'Klick this button to add a component\n'
                                                              'to the componentlist of the current object')

        self.concavity_label = Label(framer.Objframe, text="Concavity:", foreground="white", background="#404040",
                                     font=(None, 12))
        self.concavity_label.place(x=100, y=230)

        self.optionVarConc = StringVar()
        self.optionVarConc.set("Flat")

        self.optionmenuconc = OptionMenu(framer.Objframe, self.optionVarConc, "Flat", "Concave", "Convex")
        self.optionmenuconc.place(x=190, y=230)
        self.optionmenuconc.config(width=145, height=14, image=framer.menutickpic, anchor="w", borderwidth=0,
                                   indicatoron=0,
                                   compound=LEFT, bg="#404040", activebackground="#404040", foreground="white",
                                   activeforeground="#a3ff8f", font=(None, 12))

        self.concavitygroup_entry = Entry(framer.Objframe, width=4)
        self.concavitygroup_entry.configure(relief=RIDGE, width=3, bd=2, foreground="white", insertbackground="white",
                                            background="#505050", font=(None, 12))
        self.concavitygroup_entry.place(x=370, y=230)
        tooltip.CreateToolTip(self.concavitygroup_entry, text='Tooltip:\n\n'
                                                              '*OPTIONAL*')

        self.rotatsym_label = Label(framer.Objframe, text="Rotatsym:", foreground="white", background="#404040",
                                    font=(None, 12))
        self.rotatsym_label.place(x=100, y=260)

        self.rotvalx = IntVar()
        self.rotvalx.set(0)
        self.rotvaly = IntVar()
        self.rotvaly.set(0)
        self.rotvalz = IntVar()
        self.rotvalz.set(0)

        self.rotxcheckbutton = Checkbutton(framer.Objframe, text="X", variable=self.rotvalx)
        self.rotxcheckbutton.var = self.rotvalx
        self.rotxcheckbutton.config(borderwidth=0, background="#404040", activebackground="#404040",
                                    foreground="#404040",
                                    activeforeground="#404040", font=(None, 12))
        self.rotxcheckbutton.place(x=190, y=260)

        self.rotxcheckbuttonlabel = Label(framer.Objframe, text="X")
        self.rotxcheckbuttonlabel.config(borderwidth=0, background="#404040", activebackground="#404040",
                                         foreground="white",
                                         font=(None, 12))
        self.rotxcheckbuttonlabel.place(x=210, y=262)

        self.rotycheckbutton = Checkbutton(framer.Objframe, text="Y", variable=self.rotvaly)
        self.rotycheckbutton.var = self.rotvaly
        self.rotycheckbutton.config(borderwidth=0, background="#404040", activebackground="#404040",
                                    foreground="#404040",
                                    activeforeground="#404040", font=(None, 12))
        self.rotycheckbutton.place(x=230, y=260)

        self.rotycheckbuttonlabel = Label(framer.Objframe, text="Y")
        self.rotycheckbuttonlabel.config(borderwidth=0, background="#404040", activebackground="#404040",
                                         foreground="white",
                                         font=(None, 12))
        self.rotycheckbuttonlabel.place(x=250, y=262)

        self.rotzcheckbutton = Checkbutton(framer.Objframe, text="Z", variable=self.rotvalz)
        self.rotzcheckbutton.var = self.rotvalz
        self.rotzcheckbutton.config(borderwidth=0, background="#404040", activebackground="#404040",
                                    foreground="#404040",
                                    activeforeground="#404040", font=(None, 12))
        self.rotzcheckbutton.place(x=270, y=260)

        self.rotzcheckbuttonlabel = Label(framer.Objframe, text="Z")
        self.rotzcheckbuttonlabel.config(borderwidth=0, background="#404040", activebackground="#404040",
                                         foreground="white",
                                         font=(None, 12))
        self.rotzcheckbuttonlabel.place(x=290, y=262)

        self.reflsym_label = Label(framer.Objframe, text="Reflsym:", foreground="white", background="#404040",
                                   font=(None, 12))
        self.reflsym_label.place(x=100, y=290)

        self.reflvalxy = IntVar()
        self.reflvalxy.set(0)
        self.reflvalxz = IntVar()
        self.reflvalxz.set(0)
        self.reflvalyz = IntVar()
        self.reflvalyz.set(0)

        self.reflxycheckbutton = Checkbutton(framer.Objframe, text="XY", variable=self.reflvalxy)
        self.reflxycheckbutton.var = self.reflvalxy
        self.reflxycheckbutton.config(borderwidth=0, background="#404040", activebackground="#404040",
                                      foreground="#404040",
                                      activeforeground="#404040", font=(None, 12))
        self.reflxycheckbutton.place(x=190, y=290)

        self.reflxycheckbuttonlabel = Label(framer.Objframe, text="XY")
        self.reflxycheckbuttonlabel.config(borderwidth=0, background="#404040", activebackground="#404040",
                                           foreground="white",
                                           font=(None, 12))
        self.reflxycheckbuttonlabel.place(x=210, y=292)

        self.reflxzcheckbutton = Checkbutton(framer.Objframe, text="XZ", variable=self.reflvalxz)
        self.reflxzcheckbutton.var = self.reflvalxz
        self.reflxzcheckbutton.config(borderwidth=0, background="#404040", activebackground="#404040",
                                      foreground="#404040",
                                      activeforeground="#404040", font=(None, 12))
        self.reflxzcheckbutton.place(x=240, y=290)

        self.reflxzcheckbuttonlabel = Label(framer.Objframe, text="XZ")
        self.reflxzcheckbuttonlabel.config(borderwidth=0, background="#404040", activebackground="#404040",
                                           foreground="white",
                                           font=(None, 12))
        self.reflxzcheckbuttonlabel.place(x=260, y=292)

        self.reflyzcheckbutton = Checkbutton(framer.Objframe, text="YZ", variable=self.reflvalyz)
        self.reflyzcheckbutton.var = self.reflvalyz
        self.reflyzcheckbutton.config(borderwidth=0, background="#404040", activebackground="#404040",
                                      foreground="#404040",
                                      activeforeground="#404040", font=(None, 12))
        self.reflyzcheckbutton.place(x=290, y=290)

        self.reflyzcheckbuttonlabel = Label(framer.Objframe, text="YZ")
        self.reflyzcheckbuttonlabel.config(borderwidth=0, background="#404040", activebackground="#404040",
                                           foreground="white",
                                           font=(None, 12))
        self.reflyzcheckbuttonlabel.place(x=310, y=292)

        self.habitat_label = Label(framer.Objframe, text="<Habitat>", foreground="white", background="#404040",
                                   font=(None, 14))
        self.habitat_label.place(x=50, y=320)

        self.intrinsic_label = Label(framer.Objframe, text="Intrinsic:", foreground="white", background="#404040",
                                     font=(None, 12))
        self.intrinsic_label.place(x=100, y=350)

        self.optionVarIntr = StringVar()
        self.optionVarIntr.set("UP")

        self.optionmenuint = OptionMenu(framer.Objframe, self.optionVarIntr, "UP", "TOP", "NEAR", "FRONT")
        self.optionmenuint.place(x=190, y=350)
        self.optionmenuint.config(width=145, height=14, image=framer.menutickpic, anchor="w", borderwidth=0,
                                  indicatoron=0,
                                  compound=LEFT, bg="#404040", activebackground="#404040", foreground="white",
                                  activeforeground="#a3ff8f", font=(None, 12))

        self.intrinsicgroup_entry = Entry(framer.Objframe, width=4)
        self.intrinsicgroup_entry.place(x=370, y=350)
        self.intrinsicgroup_entry.configure(relief=RIDGE, width=3, bd=2, foreground="white", insertbackground="white",
                                            background="#505050", font=(None, 12))
        tooltip.CreateToolTip(self.intrinsicgroup_entry, text='Tooltip:\n\n'
                                                              '*OPTIONAL*')

        self.intrinsicarg1_entry = Entry(framer.Objframe, width=4)
        self.intrinsicarg1_entry.configure(relief=RIDGE, width=3, bd=2, foreground="white", insertbackground="white",
                                           background="#505050", font=(None, 12))
        self.intrinsicarg1_entry.place(x=440, y=350)

        self.intrinsicarg2_entry = Entry(framer.Objframe, width=4)
        self.intrinsicarg2_entry.configure(relief=RIDGE, width=3, bd=2, foreground="white", insertbackground="white",
                                           background="#505050", font=(None, 12))
        self.intrinsicarg2_entry.place(x=485, y=350)

        self.add_intrinsic_button = Button(framer.Objframe, text="add",
                                           command=lambda: self.addhabitat(self.optionVarIntr,
                                                                           self.intrinsicgroup_entry,
                                                                           self.intrinsicarg1_entry,
                                                                           self.intrinsicarg2_entry, self.intrinsiclist,
                                                                           self.intrinsicvaluelist,
                                                                           "intr"))
        self.add_intrinsic_button.config(image=framer.smallbtnpic, borderwidth=0, bg="#a3ff8f",
                                         activebackground="#a3ff8f",
                                         compound=CENTER, foreground="white", activeforeground="#a3ff8f",
                                         font=(None, 13))
        self.add_intrinsic_button.place(x=560, y=348)

        tooltip.CreateToolTip(self.add_intrinsic_button, text='Tooltip:\n\n'
                                                              'Klick this button to add an intrinsic habitat\n'
                                                              'to the list of intrinsic habitats of the current object')

        self.extrinsic_label = Label(framer.Objframe, text="Extrinsic:", foreground="white", background="#404040",
                                     font=(None, 12))
        self.extrinsic_label.place(x=100, y=380)

        self.optionVarExtr = StringVar()
        self.optionVarExtr.set("UP")

        self.optionmenuext = OptionMenu(framer.Objframe, self.optionVarExtr, "UP", "TOP", "NEAR", "FRONT")
        self.optionmenuext.place(x=190, y=380)
        self.optionmenuext.config(width=145, height=14, image=framer.menutickpic, anchor="w", borderwidth=0,
                                  indicatoron=0,
                                  compound=LEFT, bg="#404040", activebackground="#404040", foreground="white",
                                  activeforeground="#a3ff8f", font=(None, 12))

        self.extrinsicgroup_entry = Entry(framer.Objframe, width=4)
        self.extrinsicgroup_entry.configure(relief=RIDGE, width=3, bd=2, foreground="white", insertbackground="white",
                                            background="#505050", font=(None, 12))
        self.extrinsicgroup_entry.place(x=370, y=380)
        tooltip.CreateToolTip(self.extrinsicgroup_entry, text='Tooltip:\n\n'
                                                              '*OPTIONAL*')

        self.extrinsicarg1_entry = Entry(framer.Objframe, width=4)
        self.extrinsicarg1_entry.configure(relief=RIDGE, width=3, bd=2, foreground="white", insertbackground="white",
                                           background="#505050", font=(None, 12))
        self.extrinsicarg1_entry.place(x=440, y=380)

        self.extrinsicarg2_entry = Entry(framer.Objframe, width=4)
        self.extrinsicarg2_entry.configure(relief=RIDGE, width=3, bd=2, foreground="white", insertbackground="white",
                                           background="#505050", font=(None, 12))
        self.extrinsicarg2_entry.place(x=485, y=380)

        self.add_extrinsic_button = Button(framer.Objframe, text="add",
                                           command=lambda: self.addhabitat(self.optionVarExtr,
                                                                           self.extrinsicgroup_entry,
                                                                           self.extrinsicarg1_entry,
                                                                           self.extrinsicarg2_entry, self.extrinsiclist,
                                                                           self.extrinsicvaluelist,
                                                                           "extr"))
        self.add_extrinsic_button.config(image=framer.smallbtnpic, borderwidth=0, bg="#a3ff8f",
                                         activebackground="#a3ff8f",
                                         compound=CENTER, foreground="white", activeforeground="#a3ff8f",
                                         font=(None, 13))
        self.add_extrinsic_button.place(x=560, y=378)

        tooltip.CreateToolTip(self.add_extrinsic_button, text='Tooltip:\n\n'
                                                              'Klick this button to add an extrinsic habitat\n'
                                                              'to the list of extrinsic habitats of the current object')

        self.affordance_label = Label(framer.Objframe, text="<Affordances>", foreground="white", background="#404040",
                                      font=(None, 14))
        self.affordance_label.place(x=50, y=410)

        self.affordanceformula_label = Label(framer.Objframe, text="Formula:", foreground="white", background="#404040",
                                             font=(None, 12))
        self.affordanceformula_label.place(x=100, y=440)

        self.optionVarAfford = StringVar()
        self.optionVarAfford.set("grasp")

        self.optionmenuafford = OptionMenu(framer.Objframe, self.optionVarAfford, "grasp", "lift", "roll", "slide",
                                           "put_on",
                                           "put_in")
        self.optionmenuafford.place(x=190, y=440)
        self.optionmenuafford.config(width=145, height=14, image=framer.menutickpic, anchor="w", borderwidth=0,
                                     indicatoron=0,
                                     compound=LEFT, bg="#404040", activebackground="#404040", foreground="white",
                                     activeforeground="#a3ff8f", font=(None, 12))

        self.affordanceformulagroup_entry = Entry(framer.Objframe, width=4)
        self.affordanceformulagroup_entry.configure(relief=RIDGE, width=3, bd=2, foreground="white",
                                                    insertbackground="white",
                                                    background="#505050", font=(None, 12))
        self.affordanceformulagroup_entry.place(x=370, y=440)

        self.affordarg1_entry = Entry(framer.Objframe, width=4)
        self.affordarg1_entry.configure(relief=RIDGE, width=3, bd=2, foreground="white", insertbackground="white",
                                        background="#505050", font=(None, 12))
        self.affordarg1_entry.place(x=440, y=440)

        self.affordarg2_entry = Entry(framer.Objframe, width=4)
        self.affordarg2_entry.configure(relief=RIDGE, width=3, bd=2, foreground="white", insertbackground="white",
                                        background="#505050", font=(None, 12))
        self.affordarg2_entry.place(x=485, y=440)

        self.add_affordanceformula_button = Button(framer.Objframe, text="add",
                                                   command=lambda: self.addformula())
        self.add_affordanceformula_button.config(image=framer.smallbtnpic, borderwidth=0, bg="#a3ff8f",
                                                 activebackground="#a3ff8f", compound=CENTER, foreground="white",
                                                 activeforeground="#a3ff8f", font=(None, 13))
        self.add_affordanceformula_button.place(x=560, y=438)

        tooltip.CreateToolTip(self.add_affordanceformula_button, text='Tooltip:\n\n'
                                                                      'Klick this button to add an affordance formula\n'
                                                                      'to the list of affordance formulas of the current object')

        self.embodiement_label = Label(framer.Objframe, text="<Embodiement>", foreground="white", background="#404040",
                                       font=(None, 14))
        self.embodiement_label.place(x=50, y=470)

        self.scale_label = Label(framer.Objframe, text="Scale:", foreground="white", background="#404040",
                                 font=(None, 12))
        self.scale_label.place(x=100, y=500)

        self.optionVarScale = StringVar()
        self.optionVarScale.set("agent")

        self.OptionMenuScale = OptionMenu(framer.Objframe, self.optionVarScale, "< agent", "agent", "> agent")
        self.OptionMenuScale.place(x=190, y=500)
        self.OptionMenuScale.config(width=145, height=14, image=framer.menutickpic, anchor="w", borderwidth=0,
                                    indicatoron=0,
                                    compound=LEFT, bg="#404040", activebackground="#404040", foreground="white",
                                    activeforeground="#a3ff8f", font=(None, 12))

        self.movable_label = Label(framer.Objframe, text="Movable:", foreground="white", background="#404040",
                                   font=(None, 12))
        self.movable_label.place(x=100, y=530)

        self.optionVarMovable = StringVar()
        self.optionVarMovable.set("True")

        self.OptionMenuMovable = OptionMenu(framer.Objframe, self.optionVarMovable, "True", "False")
        self.OptionMenuMovable.place(x=190, y=530)
        self.OptionMenuMovable.config(width=145, height=14, image=framer.menutickpic, anchor="w", borderwidth=0,
                                      indicatoron=0,
                                      compound=LEFT, bg="#404040", activebackground="#404040", foreground="white",
                                      activeforeground="#a3ff8f", font=(None, 12))

        self.componentlist_label = Label(framer.Objframe, text="File Preview:", foreground="white",
                                         background="#404040",
                                         font=(None, 14))
        self.componentlist_label.place(x=670, y=50)

        self.componentlist_textfield = tk.Text(framer.Objframe, height=10, width=40)
        self.componentlist_textfield.configure(relief=RIDGE, bd=2, foreground="white", insertbackground="white",
                                               background="#505050", font=(None, 12))
        self.componentlist_textfield.place(x=670, y=80)

        self.optionVarComponentlist = StringVar()
        self.optionVarComponentlist.set("Select Component")

        self.OptionMenuComponentlist = OptionMenu(framer.Objframe, self.optionVarComponentlist, "Select Component")
        self.OptionMenuComponentlist.place(x=670, y=300)
        self.OptionMenuComponentlist.config(width=250, height=16, image=framer.cancelmenupic, anchor="w", borderwidth=0,
                                            indicatoron=0, compound=LEFT, bg="#404040", activebackground="#404040",
                                            foreground="white", activeforeground="#fa7878", font=(None, 12))
        self.OptionMenuComponentlist['menu'].entryconfig(1, background="#404040", activebackground="#404040",
                                                         foreground="white",
                                                         activeforeground="#fa7878")

        self.removecompo_button = Button(framer.Objframe, text="remove",
                                         command=lambda: self.removefromlist(self.componentlist,
                                                                             self.OptionMenuComponentlist,
                                                                             self.optionVarComponentlist,
                                                                             ))
        self.removecompo_button.config(image=framer.cancelbtnpic, borderwidth=0, bg="#fa7878",
                                       activebackground="#fa7878",
                                       compound=CENTER, foreground="white", activeforeground="#fa7878", font=(None, 13))
        self.removecompo_button.place(x=960, y=300)

        self.optionVarIntrinsiclist = StringVar()
        self.optionVarIntrinsiclist.set("Select Intrinsic Habitat")

        self.OptionMenuIntrinsiclist = OptionMenu(framer.Objframe, self.optionVarIntrinsiclist,
                                                  "Select Intrinsic Habitat")
        self.OptionMenuIntrinsiclist.place(x=670, y=348)
        self.OptionMenuIntrinsiclist.config(width=250, height=16, image=framer.cancelmenupic, anchor="w", borderwidth=0,
                                            indicatoron=0, compound=LEFT, bg="#404040", activebackground="#404040",
                                            foreground="white", activeforeground="#fa7878", font=(None, 12))

        self.removeintr_button = Button(framer.Objframe, text="remove",
                                        command=lambda: self.removefromlist(self.intrinsiclist,
                                                                            self.OptionMenuIntrinsiclist,
                                                                            self.optionVarIntrinsiclist,
                                                                            ))
        self.removeintr_button.config(image=framer.cancelbtnpic, borderwidth=0, bg="#fa7878",
                                      activebackground="#fa7878",
                                      compound=CENTER, foreground="white", activeforeground="#fa7878", font=(None, 13))
        self.removeintr_button.place(x=960, y=348)

        self.optionVarExtrinsiclist = StringVar()
        self.optionVarExtrinsiclist.set("Select Extrinsic Habitat")

        self.OptionMenuExtrinsiclist = OptionMenu(framer.Objframe, self.optionVarExtrinsiclist,
                                                  "Select Extrinsic Habitat")
        self.OptionMenuExtrinsiclist.place(x=670, y=380)
        self.OptionMenuExtrinsiclist.config(width=250, height=16, image=framer.cancelmenupic, anchor="w", borderwidth=0,
                                            indicatoron=0, compound=LEFT, bg="#404040", activebackground="#404040",
                                            foreground="white", activeforeground="#fa7878", font=(None, 12))

        self.removeextr_button = Button(framer.Objframe, text="remove",
                                        command=lambda: self.removefromlist(self.extrinsiclist,
                                                                            self.OptionMenuExtrinsiclist,
                                                                            self.optionVarExtrinsiclist,
                                                                            ))
        self.removeextr_button.config(image=framer.cancelbtnpic, borderwidth=0, bg="#fa7878",
                                      activebackground="#fa7878",
                                      compound=CENTER, foreground="white", activeforeground="#fa7878", font=(None, 13))
        self.removeextr_button.place(x=960, y=380)

        self.optionVarAffordancelist = StringVar()
        self.optionVarAffordancelist.set("Select Affordance Formula")

        self.OptionMenuAffordancelist = OptionMenu(framer.Objframe, self.optionVarAffordancelist,
                                                   "Select Affordance Formula")
        self.OptionMenuAffordancelist.place(x=670, y=440)
        self.OptionMenuAffordancelist.config(width=250, height=16, image=framer.cancelmenupic, anchor="w",
                                             borderwidth=0,
                                             indicatoron=0, compound=LEFT, bg="#404040", activebackground="#404040",
                                             foreground="white", activeforeground="#fa7878", font=(None, 12))

        self.removeAffordance_button = Button(framer.Objframe, text="remove",
                                              command=lambda: self.removefromlist(self.affordanceformulalist,
                                                                                  self.OptionMenuAffordancelist,
                                                                                  self.optionVarAffordancelist
                                                                                  ))
        self.removeAffordance_button.config(image=framer.cancelbtnpic, borderwidth=0, bg="#fa7878",
                                            activebackground="#fa7878",
                                            compound=CENTER, foreground="white", activeforeground="#fa7878",
                                            font=(None, 13))
        self.removeAffordance_button.place(x=960, y=440)

        drdwnlistgrn = [self.option, self.optionmenuhead, self.optionmenuconc, self.optionmenuint, self.optionmenuext,
                        self.optionmenuafford,
                        self.OptionMenuScale, self.OptionMenuMovable]
        drdwnlistred = [self.OptionMenuComponentlist, self.OptionMenuIntrinsiclist, self.OptionMenuExtrinsiclist,
                        self.OptionMenuAffordancelist]
        for drdwn in drdwnlistgrn:
            i = 0
            while i < drdwn['menu'].index('end') + 1:
                drdwn['menu'].entryconfig(i, background="#404040", activebackground="#505050", foreground="white",
                                          activeforeground="#a3ff8f")
                i += 1

        for drdwn in drdwnlistred:
            i = 0
            while i < drdwn['menu'].index('end') + 1:
                drdwn['menu'].entryconfig(i, background="#404040", activebackground="#505050", foreground="white",
                                          activeforeground="#fa7878")
                i += 1
            drdwn['menu'].add_command(label="                                                                       ",
                                      command=tk._setit(self.optionVarComponentlist, "Select Component"))
            drdwn['menu'].entryconfig(1, background="#404040", activebackground="#404040", foreground="white",
                                      activeforeground="#fa7878")

    def prettify(self, elem, filename):
        rough_string = ET.tostring(elem, 'us-ascii')
        reparsed = minidom.parseString(rough_string)
        rep = reparsed.toprettyxml(encoding='us-ascii', indent="\t").decode()
        print(rep)
        text_file = open("voxmldocs/objects/" + filename + ".xml", "w")
        text_file.truncate()
        text_file.write(rep)
        text_file.close()

    def addtotree(self, list1, vallist, tagname, tag):
        counter = 0
        for j in list1:
            if j[:2] == "UP":
                new_intr = ET.SubElement(tag, tagname, Name=j, Value="align(" + vallist[counter] + ")")
                counter = counter + 1
            elif j[:3] == "TOP":
                new_intr = ET.SubElement(tag, tagname, Name=j, Value="top(" + vallist[counter] + ")")
                counter = counter + 1
            elif j[:4] == "NEAR":
                new_intr = ET.SubElement(tag, tagname, Name=j, Value="align(" + vallist[counter] + ")")
                counter = counter + 1
            elif j[:5] == "FRONT":
                new_intr = ET.SubElement(tag, tagname, Name=j, Value="front(" + vallist[counter] + ")")
                counter = counter + 1

    def addrotsymtotree(self, rotx, roty, rotz, tag):
        rotatsymstr = ""
        if rotx == 0:
            if roty == 0:
                if rotz == 0:
                    rotatsymstr = ""
                elif rotz == 1:
                    rotatsymstr = "Z"
            elif roty == 1:
                if rotz == 0:
                    rotatsymstr = "Y"
                elif rotz == 1:
                    rotatsymstr = "Y,Z"
        elif rotx == 1:
            if roty == 0:
                if rotz == 0:
                    rotatsymstr = "X"
                elif rotz == 1:
                    rotatsymstr = "X,Z"
            elif roty == 1:
                if rotz == 0:
                    rotatsymstr = "X,Y"
                elif rotz == 1:
                    rotatsymstr = "X,Y,Z"
        tag.text = rotatsymstr

    def addreflsymtotree(self, reflxy, reflxz, reflyz, tag):
        reflsymstr = ""
        if reflxy == 0:
            if reflxz == 0:
                if reflyz == 0:
                    reflsymstr = ""
                elif reflyz == 1:
                    reflsymstr = "YZ"
            elif reflxz == 1:
                if reflyz == 0:
                    reflsymstr = "XZ"
                elif reflyz == 1:
                    reflsymstr = "XZ,YZ"
        elif reflxy == 1:
            if reflxz == 0:
                if reflyz == 0:
                    reflsymstr = "XY"
                elif reflyz == 1:
                    reflsymstr = "XY,YZ"
            elif reflxz == 1:
                if reflyz == 0:
                    reflsymstr = "XY,XZ"
                elif reflyz == 1:
                    reflsymstr = "XY,XZ,YZ"
        tag.text = reflsymstr

    def addheadtotree(self, headv, headg, tag):
        if headg != "":
            tag.text = headv + "[" + headg + "]"
        elif headg == "":
            tag.text = headv

    def addafftotree(self, list1, tagname, tag):
        for j in list1:
            new_aff = ET.SubElement(tag, tagname, Formula=j)

    def createtree(self, pred, typ, headv, headg, concstr, concgrp, rotx, roty, rotz, reflxy, reflxz, reflyz, scalestr,
                   movablestr):
        VoxML = ET.Element("VoxML")
        VoxML.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
        VoxML.set('xmlns:xsd', "http://www.w3.org/2001/XMLSchema")

        Entity = ET.SubElement(VoxML, "Entity", Type="Object")

        Lex = ET.SubElement(VoxML, "Lex")
        Pred = ET.SubElement(Lex, "Pred")
        Pred.text = pred
        SubType = ET.SubElement(Lex, "Type")
        SubType.text = typ

        Type = ET.SubElement(VoxML, "Type")
        Head = ET.SubElement(Type, "Head")
        self.addheadtotree(headv, headg, Head)
        Components = ET.SubElement(Type, "Components")
        for i in self.componentlist:
            new_comp = ET.SubElement(Components, "Component", Value=i)
        Concavity = ET.SubElement(Type, "Concavity")
        if concgrp != "":
            Concavity.text = concstr + "[" + concgrp + "]"
        elif concgrp == "":
            Concavity.text = concstr
        else:
            pass
        RotatSym = ET.SubElement(Type, "RotatSym")
        self.addrotsymtotree(rotx, roty, rotz, RotatSym)

        ReflSym = ET.SubElement(Type, "ReflSym")
        self.addreflsymtotree(reflxy, reflxz, reflyz, ReflSym)

        Habitat = ET.SubElement(VoxML, "Habitat")
        Intrinsic = ET.SubElement(Habitat, "Intrinsic")
        self.addtotree(self.intrinsiclist, self.intrinsicvaluelist, "Intr", Intrinsic)
        Extrinsic = ET.SubElement(Habitat, "Extrinsic")
        self.addtotree(self.extrinsiclist, self.extrinsicvaluelist, "Extr", Extrinsic)

        Afford_Str = ET.SubElement(VoxML, "Afford_Str")
        Affordances = ET.SubElement(Afford_Str, "Affordances")
        self.addafftotree(self.affordanceformulalist, "Affordance", Affordances)

        Embodiement = ET.SubElement(VoxML, "Embodiement")
        Scale = ET.SubElement(Embodiement, "Scale")
        Scale.text = scalestr
        Movable = ET.SubElement(Embodiement, "Movable")
        Movable.text = movablestr

        self.prettify(VoxML, pred)

    def addcomponent(self):
        # OptionMenuComponentlist
        newcomponentpre = None
        if self.duplicatevar.get() == 0:
            newcomponentpre = self.component_entry.get()
        elif self.duplicatevar.get() == 1:
            newcomponentpre = self.component_entry.get() + "+"
        else:
            pass

        newcomponent = None
        if self.componentgroup_entry.get() != "":
            newcomponent = newcomponentpre + "[" + self.componentgroup_entry.get() + "]"
        elif self.componentgroup_entry.get() == "":
            newcomponent = newcomponentpre
        else:
            pass

        self.componentlist.append(newcomponent)
        self.debug_textfield.delete('1.0', tk.END)
        self.debug_textfield.insert(tk.INSERT, "Component has been added!")
        self.OptionMenuComponentlist['menu'].delete(0, 'end')

        self.update_component_delete()
        self.configlistwindow()

    def update_component_delete(self):
        newchoices = self.componentlist
        i = 0
        for choice in newchoices:
            self.OptionMenuComponentlist['menu'].add_command(label=choice,
                                                             command=tk._setit(self.optionVarComponentlist, choice))
            self.OptionMenuComponentlist['menu'].entryconfig(i, background="#404040", activebackground="#505050",
                                                             foreground="white",
                                                             activeforeground="#fa7878")
            i += 1
        self.OptionMenuComponentlist['menu'].add_command(
            label="                                                                      ",
            command=tk._setit(self.optionVarComponentlist, "Select Component"))
        self.OptionMenuComponentlist['menu'].entryconfig(len(self.componentlist) + 1, background="#404040",
                                                         activebackground="#404040",
                                                         foreground="white", activeforeground="white")

    def addhabitat(self, var, grp, arg1, arg2, list1, vallist, intorext):
        if grp.get() == "":
            self.debug_textfield.delete('1.0', tk.END)
            self.debug_textfield.insert(tk.INSERT, "Please add an Argument")
        elif grp.get() != "":
            if arg2.get() == "":
                newargstr = arg1.get()
                vallist.append(newargstr)
            elif arg2.get() != "":
                newargstr = arg1.get() + "," + arg2.get()
                vallist.append(newargstr)

            newhab = var.get() + "[" + grp.get() + "]"
            list1.append(newhab)
            self.debug_textfield.delete('1.0', tk.END)
            if intorext == "intr":
                self.debug_textfield.insert(tk.INSERT, "Intrinsic habitat has been added!")
                self.update_intrinsic_habitat_delete()
            elif intorext == "extr":
                self.debug_textfield.insert(tk.INSERT, "Extrinsic habitat has been added!")
                self.update_extrinsic_habitat_delete()
        else:
            pass

        self.configlistwindow()

    def update_intrinsic_habitat_delete(self):
        self.OptionMenuIntrinsiclist['menu'].delete(0, 'end')
        i = 0
        for choice in self.intrinsiclist:
            self.OptionMenuIntrinsiclist['menu'].add_command(label=choice,
                                                             command=tk._setit(self.optionVarIntrinsiclist, choice))
            self.OptionMenuIntrinsiclist['menu'].entryconfig(i, background="#404040", activebackground="#505050",
                                                             foreground="white",
                                                             activeforeground="#fa7878")
            i = i + 1
        self.OptionMenuIntrinsiclist['menu'].add_command(
            label="                                                                       ",
            command=tk._setit(self.optionVarIntrinsiclist, "Select Entry"))
        self.OptionMenuIntrinsiclist['menu'].entryconfig(1, background="#404040", activebackground="#404040",
                                                         foreground="white",
                                                         activeforeground="#fa7878")

    def update_extrinsic_habitat_delete(self):
        self.OptionMenuExtrinsiclist['menu'].delete(0, 'end')
        i = 0
        for choice in self.extrinsiclist:
            self.OptionMenuExtrinsiclist['menu'].add_command(label=choice,
                                                             command=tk._setit(self.optionVarExtrinsiclist, choice))
            self.OptionMenuExtrinsiclist['menu'].entryconfig(i, background="#404040", activebackground="#505050",
                                                             foreground="white",
                                                             activeforeground="#fa7878")
            i = i + 1
        self.OptionMenuExtrinsiclist['menu'].add_command(
            label="                                                                       ",
            command=tk._setit(self.optionVarExtrinsiclist, "Select Entry"))
        self.OptionMenuExtrinsiclist['menu'].entryconfig(1, background="#404040", activebackground="#404040",
                                                         foreground="white",
                                                         activeforeground="#fa7878")

    def addformula(self):
        # , OptionMenuAffordancelist
        prefix = ""
        form = ""
        argu1 = self.affordarg1_entry.get()
        argu2 = self.affordarg2_entry.get()
        if argu1.isnumeric():
            argu1 = "[" + self.affordarg1_entry.get() + "]"
        elif argu2.isnumeric():
            argu2 = "[" + self.affordarg2_entry.get() + "]"

        if self.affordanceformulagroup_entry.get() == "":
            prefix = "H->["
        elif self.affordanceformulagroup_entry.get() != "":
            prefix = "H[" + self.affordanceformulagroup_entry.get() + "]->["
        else:
            pass

        if self.affordarg1_entry.get() != "" and self.affordarg2_entry.get() != "":
            if self.optionVarAfford.get() == "put_on":
                form = "put(" + argu1 + ", on(" + argu2 + "))]support(" + argu2 + ", " + argu1 + ")"
            elif self.optionVarAfford.get() == "put_in":
                form = "put(" + argu1 + ", in(" + argu2 + "))]contain(" + argu2 + ", " + argu1 + ")"
            elif self.optionVarAfford.get() == "lift":
                form = self.optionVarAfford.get() + "(" + argu1 + ", " + argu2 + ")]hold(" + argu1 + ", " + argu2 + ")"
            else:
                form = self.optionVarAfford.get() + "(" + argu1 + ", " + argu2 + ")]"
            newformula = prefix + form
            self.affordanceformulalist.append(newformula)
            self.debug_textfield.delete('1.0', tk.END)
            self.debug_textfield.insert(tk.INSERT, "Affordance Formula has been added!")
        else:
            self.debug_textfield.delete('1.0', tk.END)
            self.debug_textfield.insert(tk.INSERT, "Please add more Arguments")

        self.update_formula_delete()
        self.configlistwindow()

    def update_formula_delete(self):
        self.OptionMenuAffordancelist['menu'].delete(0, 'end')
        i = 0
        for choice in self.affordanceformulalist:
            self.OptionMenuAffordancelist['menu'].add_command(label=choice,
                                                              command=tk._setit(self.optionVarAffordancelist,
                                                                                choice))
            self.OptionMenuAffordancelist['menu'].entryconfig(i, background="#404040", activebackground="#505050",
                                                              foreground="white",
                                                              activeforeground="#fa7878")
            i = i + 1
        self.OptionMenuAffordancelist['menu'].add_command(
            label="                                                                       ",
            command=tk._setit(self.optionVarAffordancelist, "Select Entry"))
        self.OptionMenuAffordancelist['menu'].entryconfig(1, background="#404040", activebackground="#404040",
                                                          foreground="white",
                                                          activeforeground="#fa7878")

    def getvals(self):
        predstring = self.pred_entry.get()
        optVar = self.optionVar.get()
        headVar = self.optionVarHead.get()
        headGroup = self.headgroup_entry.get()
        concavitystring = self.optionVarConc.get()
        concavitygrp = self.concavitygroup_entry.get()
        rotstrx = self.rotvalx.get()
        rotstry = self.rotvaly.get()
        rotstrz = self.rotvalz.get()
        reflxystr = self.reflvalxy.get()
        reflxzstr = self.reflvalxz.get()
        reflyzstr = self.reflvalyz.get()
        scalestr = self.optionVarScale.get()
        movablestr = self.optionVarMovable.get()

        self.createtree(predstring, optVar, headVar, headGroup, concavitystring, concavitygrp, rotstrx,
                        rotstry, rotstrz, reflxystr, reflxzstr, reflyzstr, scalestr, movablestr)

    def clear(self):
        self.__init__()

    def removefromlist(self, lists, opmenu, opmenuvar):
        value = opmenuvar.get()
        if value in lists:
            lists.remove(value)
        else:
            print("no such item in list")
        opmenu['menu'].delete(0, 'end')
        newchoices = lists
        i = 0
        for choice in newchoices:
            opmenu['menu'].add_command(label=choice, command=tk._setit(opmenuvar, choice))
            opmenu['menu'].entryconfig(i, background="#404040", activebackground="#505050", foreground="white",
                                       activeforeground="#fa7878")
            i = i + 1
        opmenu['menu'].add_command(label="                                                                      ",
                                   command=tk._setit(opmenuvar, "click to select"))
        opmenu['menu'].entryconfig(len(lists) + 1, background="#404040", activebackground="#404040", foreground="white",
                                   activeforeground="white")
        self.debug_textfield.delete('1.0', tk.END)
        self.debug_textfield.insert(tk.INSERT, value + "  Has been removed!")
        self.configlistwindow()

    def configlistwindow(self):
        count = 0
        lists = [self.componentlist, self.intrinsiclist, self.extrinsiclist, self.affordanceformulalist]
        self.componentlist_textfield.delete('1.0', tk.END)
        for j in lists:
            if count == 0:
                self.componentlist_textfield.insert(tk.INSERT, "Components:" + "\n")
            elif count == 1:
                self.componentlist_textfield.insert(tk.INSERT, "Intrinsic Habitats:" + "\n")
            elif count == 2:
                self.componentlist_textfield.insert(tk.INSERT, "Extrinsic Habitats:" + "\n")
            elif count == 3:
                self.componentlist_textfield.insert(tk.INSERT, "Affordance Formulas:" + "\n")
            count = count + 1
            for i in j:
                self.componentlist_textfield.insert(tk.INSERT, i + "\n")
