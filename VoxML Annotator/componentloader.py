import threading
import xml.etree.ElementTree as ET
from tkinter import filedialog, constants
import torch
import framer
import re
from classificator.surface_sampling import createpointcloudforfile
import pyvista as pv
from pyvistaqt import BackgroundPlotter


def loadVoxMLFile(voxfile=None):
    """
    Load VoxMl.xml Files
    """
    if voxfile is None:
        voxfile = filedialog.askopenfilename(filetypes=[("VoxML files", ".xml .txt")])
    voxentity = None
    if voxfile.endswith(".xml") or voxfile.endswith(".txt"):
        VoxML = ET.parse(voxfile)
        entity = VoxML.find("Entity")
        if entity is not None:
            voxentity = entity.get("Type")

        if voxentity is None:
            return

        elif voxentity == "Attribute":
            framer.attribute_window.clear()
            pred = VoxML.findtext("Lex/Pred")
            framer.attribute_window.pred_entry.insert(constants.INSERT, pred)
            scale = VoxML.findtext("Type/Scale")
            framer.attribute_window.optionVarScale.set(scale)
            arity = VoxML.findtext("Type/Arity")
            framer.attribute_window.optionVarArity.set(arity)

            for arg in VoxML.findall("Type/Args/Arg"):
                arg_val = arg.get("Value").split(":")
                framer.attribute_window.addargument(arg_val[0], arg_val[1])

            framer.attribute_window.debug_textfield.delete('1.0', constants.END)
            framer.attribute_window.debug_textfield.insert(constants.INSERT, "Document loaded!")
            framer.Attrframe.tkraise()

        elif voxentity == "Program":
            framer.programm_windows.clear()
            pred = VoxML.findtext("Lex/Pred")
            framer.programm_windows.pred_entry.insert(constants.INSERT, pred)
            type = VoxML.findtext("Lex/Type")
            framer.programm_windows.typeVar.set(type)

            head = VoxML.findtext("Type/Head")
            framer.programm_windows.headVar.set(head)

            for arg in VoxML.findall("Type/Args/Arg"):
                arg_val = arg.get("Value").split(":")
                framer.programm_windows.addargument(arg_val[0], arg_val[1])

            for arg in VoxML.findall("Type/Body/Subevent"):
                framer.programm_windows.addsubevent(arg)

            framer.programm_windows.debug_textfield.delete('1.0', constants.END)
            framer.programm_windows.debug_textfield.insert(constants.INSERT, "Document loaded!")
            framer.Progrframe.tkraise()

        elif voxentity == "Function":
            framer.function_window.clear()
            pred = VoxML.findtext("Lex/Pred")
            framer.function_window.pred_entry.insert(constants.INSERT, pred)

            for arg in VoxML.findall("Type/Args/Arg"):
                arg_val = arg.get("Value").split(":")
                framer.function_window.addargument(arg_val[0], arg_val[1])

            referent = VoxML.findtext("Type/Referent")
            framer.function_window.referent_entry.insert(constants.INSERT, referent)
            mapping = VoxML.findtext("Type/Mapping")
            framer.function_window.mapping_entry.insert(constants.INSERT, mapping)

            space = VoxML.findtext("Type/Orientation/Space")
            framer.function_window.optionVarSpace.set(space)
            axis = VoxML.findtext("Type/Orientation/Axis")
            framer.function_window.axis_entry.insert(constants.INSERT, axis)
            arity = VoxML.findtext("Type/Orientation/Arity")
            framer.function_window.arity_entry.insert(constants.INSERT, arity)

            framer.function_window.debug_textfield.delete('1.0', constants.END)
            framer.function_window.debug_textfield.insert(constants.INSERT, "Document loaded!")
            framer.Funcframe.tkraise()

        elif voxentity == "Relation":
            framer.relation_window.clear()
            pred = VoxML.findtext("Lex/Pred")
            framer.relation_window.pred_entry.insert(constants.INSERT, pred)
            voxclass = VoxML.findtext("Type/Class")
            framer.relation_window.optionVarClass.set(voxclass)
            value = VoxML.findtext("Type/Value")
            framer.relation_window.optionVarValue.set(value)

            for arg in VoxML.findall("Type/Args/Arg"):
                arg_val = arg.get("Value").split(":")
                framer.relation_window.addargument(arg_val[0], arg_val[1])

            for arg in VoxML.findall("Type/Constr"):
                arg_val = arg.text
                framer.relation_window.addconstr(arg_val)

            for arg in VoxML.findall("Type/Corresps/Corresp"):
                arg_val = arg.get("Value")
                framer.relation_window.addcorresp(arg_val)

            framer.relation_window.debug_textfield.delete('1.0', constants.END)
            framer.relation_window.debug_textfield.insert(constants.INSERT, "Document loaded!")
            framer.Relatframe.tkraise()

        elif voxentity == "Object":
            framer.object_window.clear()
            pred = VoxML.findtext("Lex/Pred")
            framer.object_window.pred_entry.insert(constants.INSERT, pred)
            type = VoxML.findtext("Lex/Type")
            framer.object_window.optionVar.set(type)

            head = VoxML.findtext("Type/Head")
            headsplit = re.split(r'\[|\]', head)
            framer.object_window.optionVarHead.set(headsplit[0])
            if len(headsplit) > 1:
                framer.object_window.headgroup_entry.insert(constants.INSERT, headsplit[1])

            for component in VoxML.findall("Type/Components/Component"):
                component_val = component.get("Value")
                framer.object_window.componentlist.append(component_val)
                framer.object_window.update_component_delete()

            concav = VoxML.findtext("Type/Concavity")
            framer.object_window.optionVarConc.set(concav)

            rot = VoxML.findtext("Type/RotatSym")
            if len(rot) > 0:
                rotsplit = rot.split(",")
                for r in rotsplit:
                    if r == "X":
                        framer.object_window.rotvalx.set(1)
                    elif r == "Y":
                        framer.object_window.rotvaly.set(1)
                    elif r == "Z":
                        framer.object_window.rotvalz.set(1)

            sym = VoxML.findtext("Type/ReflSym")
            if len(sym) > 0:
                symsplit = sym.split(",")
                for s in symsplit:
                    if s == "XY":
                        framer.object_window.reflvalxy.set(1)
                    elif s == "XZ":
                        framer.object_window.reflvalxz.set(1)
                    elif s == "YZ":
                        framer.object_window.reflvalyz.set(1)

            for intr in VoxML.findall("Habitat/Intrinsic/Intr"):
                int_name = intr.get("Name")
                int_val = intr.get("Value")

                framer.object_window.intrinsiclist.append(int_name)
                framer.object_window.intrinsicvaluelist.append(int_val)
                framer.object_window.update_intrinsic_habitat_delete()

            for extr in VoxML.findall("Habitat/Extrinsic/Extr"):
                extr_name = extr.get("Name")
                extr_val = extr.get("Value")

                framer.object_window.extrinsiclist.append(extr_name)
                framer.object_window.extrinsicvaluelist.append(extr_val)
                framer.object_window.update_extrinsic_habitat_delete()

            for afford in VoxML.findall("Afford_Str/Affordances/Affordance"):
                formula = afford.get("Formula")
                framer.object_window.affordanceformulalist.append(formula)
                framer.object_window.update_formula_delete()

            scale = VoxML.findtext("Embodiement/Scale")
            framer.object_window.optionVarScale.set(scale)
            arity = VoxML.findtext("Embodiement/Movable")
            framer.object_window.optionVarMovable.set(arity)

            framer.object_window.configlistwindow()
            framer.object_window.debug_textfield.delete('1.0', constants.END)
            framer.object_window.debug_textfield.insert(constants.INSERT, "Document loaded!")
            framer.Objframe.tkraise()


classdict = {
    0: "airplane",
    1: "bathtub",
    2: "bed",
    3: "bench",
    4: "bookshelf",
    5: "bottle",
    6: "bowl",
    7: "car",
    8: "chair",
    9: "cone",
    10: "cup",
    11: "curtain",
    12: "desk",
    13: "door",
    14: "dresser",
    15: "flower_pot",
    16: "glass_box",
    17: "guitar",
    18: "keyboard",
    19: "lamp",
    20: "laptop",
    21: "mantel",
    22: "monitor",
    23: "night_stand",
    24: "person",
    25: "piano",
    26: "plant",
    27: "radio",
    28: "range_hood",
    29: "sink",
    30: "sofa",
    31: "stairs",
    32: "stool",
    33: "table",
    34: "tent",
    35: "toilet",
    36: "tv_stand",
    37: "vase",
    38: "wardrobe",
    39: "xbox",
    }


plotter = None
def load3dobj(model):
    global plotter
    objfile = filedialog.askopenfilename(filetypes=[("3D Object File", ".obj .stl .off")])
    pointcloud = createpointcloudforfile(objfile)
    pointcloud = torch.tensor([pointcloud.tolist()])
    pointcloud = pointcloud.permute(0, 2, 1)
    logits = model(pointcloud)
    guess = (logits.max(dim=1)[1]).item()
    guess_str = classdict[guess]

    loadVoxMLFile("classificator/classfiles/" + guess_str + ".txt")
    framer.object_window.debug_textfield.insert(constants.INSERT, "\nObject classified as: " + guess_str + ".")
    if plotter is not None:
        plotter.close()
    mesh = pv.read(objfile)
    plotter = BackgroundPlotter()
    plotter.add_mesh(mesh)





