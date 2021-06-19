from tk_html_widgets import *
from tkinter import filedialog
import shutil
import os.path
import framer


def createwindow():
    """
     Opening PartNet .html for opening objectstructures
    """
    partdir = filedialog.askdirectory()
    print(partdir)
    dest = os.getcwd() + '/parts_render'
    print(dest)

    shutil.copytree(partdir + '/parts_render', dest)

    with open(partdir + '/tree_hier.html', 'r') as file:
        data = file.read()

    html_label = HTMLLabel(framer.Inspectframe, width=56, height=48, html=data)

    html_label.place(x=0, y=0)

    shutil.rmtree(dest)
    framer.Inspectframe.tkraise()


def main():
    createwindow()
