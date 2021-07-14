import random
import torch
import trimesh
import math


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

    maxdist = 0
    for each in rightlensample:
        dist = math.sqrt((each[0] ** 2) + (each[1] ** 2) + (each[2] ** 2))
        if dist >= maxdist:
            maxdist = dist

    rightlensample2 = []
    for each in cloud2:
        rightlensample2.append(each)

    converted = torch.FloatTensor(rightlensample2)
    return converted
