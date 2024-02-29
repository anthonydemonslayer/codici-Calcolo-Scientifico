# -*- coding: utf-8 -*-
"""
Created on Mon May 15 12:05:01 2023

@author: Antonio
"""

from matplotlib import pyplot as plt
import numpy as np
import pathlib
import metodi_diretti_completo as metdir
import metodi_iterativi as metiter
import metodo_potenze as metpot
import surfer as surfer

def main():
    root = "http://www.unina.it"
    toll = 1e-3
    nmax = 1000
    depth = 200
    x0 = np.full((depth, 1),1/depth)
    p = 0.85
    
    U, G = surfer.surfer(root, depth, verbose=False)
    pathFile = pathlib.path(_file_).parent
    plt.figure(1)
    plt.imshow(G,interpolation="none")
    plt.savefig(pathFile/"spyg")
    
    A, A0, b = surfer.pagerank(G, p)
    