import voxmlannotator
# from toolkit3d.threaded_surface_sampling import SurfaceCloudsampler
import torch
import os
import random
import trimesh
import math
from classificator.model import DGCNN
import torch.nn as nn
import numpy as np


# enttypeselector.main()


def createpointcloudforfile(filepath):
    initialsize = 2048
    mesh = trimesh.load_mesh(filepath)
    sample = ((trimesh.sample.sample_surface_even(mesh, initialsize, radius=None))[0])

    if len(sample) != 2048:
        fstmul = (2048 / len(sample)) * 0.92
        initialsize = int(initialsize * fstmul)
        sample = ((trimesh.sample.sample_surface_even(mesh, initialsize, radius=None))[0])

    while len(sample) < 2048:
        initialsize = int(initialsize * 1.02)
        sample = ((trimesh.sample.sample_surface_even(mesh, initialsize, radius=None))[0])

    i = 0
    indices = []
    rightlensample = []

    if len(sample) != 2048:
        while i < 2048:
            rand_pt_idx = random.randint(0, len(sample) - 1)
            if rand_pt_idx not in indices:
                indices.append(rand_pt_idx)
                i += 1
            elif rand_pt_idx in indices:
                pass
        for each in indices:
            rightlensample.append(sample[each])
    elif len(sample) == 2048:
        rightlensample = sample

    cloud = trimesh.points.PointCloud(rightlensample)
    pccenter = cloud.centroid
    for each in rightlensample:
        each[0] = each[0] - pccenter[0]
        each[1] = each[1] - pccenter[1]
        each[2] = each[2] - pccenter[2]

    maxdist = 0
    for each in rightlensample:
        dist = math.sqrt((each[0] ** 2) + (each[1] ** 2) + (each[2] ** 2))
        if dist >= maxdist:
            maxdist = dist

    for each in rightlensample:
        each[0] = each[0] / maxdist
        each[1] = each[1] / maxdist
        each[2] = each[2] / maxdist

    cloud2 = trimesh.points.PointCloud(rightlensample)

    possible_transforms_x = [[[1, 0, 0, 0], [0, 0, -1, 0], [0, 1, 0, 0], [0, 0, 0, 1]],
                             [[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]],
                             [[1, 0, 0, 0], [0, 0, 1, 0], [0, -1, 0, 0], [0, 0, 0, 1]],
                             [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]]

    possible_transforms_y = [[[0, 0, 1, 0], [0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1]],
                             [[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]],
                             [[0, 0, -1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1]],
                             [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]]

    possible_transforms_z = [[[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
                             [[-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
                             [[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
                             [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]]

    cloud2.apply_transform(possible_transforms_x[0])

    maxdist = 0
    for each in rightlensample:
        dist = math.sqrt((each[0] ** 2) + (each[1] ** 2) + (each[2] ** 2))
        if dist >= maxdist:
            maxdist = dist

    rightlensample2 = []
    for each in cloud2:
        rightlensample2.append(each)

    converted = torch.FloatTensor(rightlensample2)
    filename = os.path.splitext(os.path.basename(str(filepath)))[0]
    print('filename: ', filename, '\noriginal sampsize: ', len(sample), '\nnum of points: ', len(converted), '\n')

    return converted


convertedobj = (createpointcloudforfile(
    "D:/Corpora/3D-FRONT/3D-FUTURE-model/3D-FUTURE-model/815965b3-4143-471f-9906-735925b80a52/normalized_model.obj")).tolist()
# convertedobj = createpointcloudforfile("C:/Users/Henlein/Downloads/3DMTK-master/allforeignstl/tisch.stl").tolist()
# convertedobj = (torch.load("classificator/to_classify/tisch.pt")).tolist()

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

with torch.no_grad():
    device = torch.device("cpu")
    model = DGCNN().to("cpu")
    model = nn.DataParallel(model).to("cpu")
    model.load_state_dict(torch.load("classificator/pretrained/custommodel.t7", map_location=torch.device('cpu')))
    model.train(mode=False)
    convertedobj = torch.tensor([convertedobj])
    print(convertedobj)
    convertedobj = convertedobj.permute(0, 2, 1).to("cpu")
    print(convertedobj)
    pred = model(convertedobj)
    print(pred)
    predicted_class = np.argmax(pred).item()
    print(predicted_class)
    print(classdict[predicted_class])
