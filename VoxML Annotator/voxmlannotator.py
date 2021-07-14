from tkinter.ttk import *
import inspector
import componentloader
import framer
from tkinter import *
import changelog_window
import help_window
import torch
from classificator.model import DGCNN
import torch.nn as nn


def quitapplication():
    framer.Window.destroy()


def initmodel():
    device = torch.device("cpu")
    model = DGCNN().to(device)
    model = nn.DataParallel(model)
    model.load_state_dict(torch.load("classificator/pretrained/custommodelorig.t7", map_location=torch.device('cpu')))
    model = model.eval()
    return model


def createwindow():

    model = initmodel()

    """
    Create MainWindow of the VoxML Annotator
    """
    entity_types_bg_label = Label(framer.Topframe, image=framer.enttypeslabelpic, bg="#a3ff8f", width=557, height=35)
    entity_types_bg_label.image = framer.enttypeslabelpic
    entity_types_bg_label.place(x=0, y=81)

    otherfuns_bg_label = Label(framer.Topframe, image=framer.otherfunslabelpic, bg="#a3ff8f", width=222, height=35)
    otherfuns_bg_label.image = framer.otherfunslabelpic
    otherfuns_bg_label.place(x=650, y=81)

    htmlfuns_bg_label = Label(framer.Topframe, image=framer.htmlfunslabelpic, bg="#a3ff8f", width=394, height=35)
    htmlfuns_bg_label.image = framer.htmlfunslabelpic
    htmlfuns_bg_label.place(x=1150, y=81)

    loadvoxml_button = Button(framer.Topframe, text="Open VoxML", command=lambda: componentloader.loadVoxMLFile())
    loadvoxml_button.config(image=framer.largebtnpic, borderwidth=0, bg="#a3ff8f", activebackground="#a3ff8f",
                            compound=CENTER, foreground="white", activeforeground="#a3ff8f", font=(None, 14))
    loadvoxml_button.place(x=1150, y=118)

    loadhtml_button = Button(framer.Topframe, text="Open HTML", command=lambda: inspector.createhtmlwindow())
    loadhtml_button.config(image=framer.largebtnpic, borderwidth=0, bg="#a3ff8f", activebackground="#a3ff8f",
                           compound=CENTER, foreground="white", activeforeground="#a3ff8f", font=(None, 14))
    loadhtml_button.place(x=1282, y=118)

    loadobj_button = Button(framer.Topframe, text="Open 3D Obj", command=lambda: componentloader.load3dobj(model))
    loadobj_button.config(image=framer.largebtnpic, borderwidth=0, bg="#a3ff8f", activebackground="#a3ff8f",
                             compound=CENTER, foreground="white", activeforeground="#a3ff8f", font=(None, 14))
    loadobj_button.place(x=1414, y=118)

    openhelp_button = Button(framer.Topframe, text="Help", command=lambda: help_window.createwindow())
    openhelp_button.config(image=framer.btnpic, borderwidth=0, bg="#a3ff8f", activebackground="#a3ff8f",
                           compound=CENTER, foreground="white", activeforeground="#a3ff8f", font=(None, 14))
    openhelp_button.place(x=650, y=118)

    openchangelog_button = Button(framer.Topframe, text="Changelog", command=lambda: changelog_window.createwindow())
    openchangelog_button.config(image=framer.btnpic, borderwidth=0, bg="#a3ff8f", activebackground="#a3ff8f",
                                compound=CENTER, foreground="white", activeforeground="#a3ff8f", font=(None, 14))
    openchangelog_button.place(x=762, y=118)

    # quit_button = Button(framer.Topframe, text="exit", command = lambda: quitapplication())
    # quit_button.config(image = framer.cancelbtnpic, borderwidth = 0, bg = "#fa7878", activebackground= "#fa7878", compound = CENTER, foreground = "white", activeforeground = "#fa7878", font=(None, 14))
    # quit_button.place ( x = 1520, y = 7 )

    object_button = Button(framer.Topframe, text="Object", command=lambda: framer.Objframe.tkraise())
    object_button.config(image=framer.btnpic, borderwidth=0, bg="#a3ff8f", activebackground="#a3ff8f", compound=CENTER,
                         foreground="white", activeforeground="#a3ff8f", font=(None, 14))
    object_button.place(x=0, y=118)

    programm_button = Button(framer.Topframe, text="Programm", command=lambda: framer.Progrframe.tkraise())
    programm_button.config(image=framer.btnpic, borderwidth=0, bg="#a3ff8f", activebackground="#a3ff8f",
                           compound=CENTER, foreground="white", activeforeground="#a3ff8f", font=(None, 14))
    programm_button.place(x=112, y=118)

    attribute_button = Button(framer.Topframe, text="Attribute", command=lambda: framer.Attrframe.tkraise())
    attribute_button.config(image=framer.btnpic, borderwidth=0, bg="#a3ff8f", activebackground="#a3ff8f",
                            compound=CENTER, foreground="white", activeforeground="#a3ff8f", font=(None, 14))
    attribute_button.place(x=223, y=118)

    relation_button = Button(framer.Topframe, text="Relation", command=lambda: framer.Relatframe.tkraise())
    relation_button.config(image=framer.btnpic, borderwidth=0, bg="#a3ff8f", activebackground="#a3ff8f",
                           compound=CENTER, foreground="white", activeforeground="#a3ff8f", font=(None, 14))
    relation_button.place(x=335, y=118)

    function_button = Button(framer.Topframe, text="Function", command=lambda: framer.Funcframe.tkraise())
    function_button.config(image=framer.btnpic, borderwidth=0, bg="#a3ff8f", activebackground="#a3ff8f",
                           compound=CENTER, foreground="white", activeforeground="#a3ff8f", font=(None, 14))
    function_button.place(x=447, y=118)


if __name__ == "__main__":
    createwindow()
    framer.mainloop()
