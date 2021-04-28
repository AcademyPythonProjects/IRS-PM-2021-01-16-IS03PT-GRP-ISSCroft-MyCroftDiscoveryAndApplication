import numpy as np
import math
from math import radians, sin, cos, acos


def compute_manhattan_distance_matrix(locations):
    """Creates callback to return distance between points."""
    distances = {}
    for from_counter, from_node in enumerate(locations):
        distances[from_counter] = {}
        for to_counter, to_node in enumerate(locations):
            if from_counter == to_counter:
                distances[from_counter][to_counter] = 0
            else:
                distances[from_counter][to_counter] = manhattan_distance (
                    from_node[0], from_node[1], to_node[0], to_node[1])
                
    return distances


def manhattan_distance(origin_lat, origin_lon, destination_lat, destination_lon):
    # Origin coordinates
    p = np.stack(np.array([origin_lat, origin_lon]).reshape(-1,1), axis = 1)
    # Destination coordinates
    d = np.stack(np.array([destination_lat, destination_lon]).reshape(-1,1), axis = 1)
    theta1 = np.radians(-28.904)
    theta2 = np.radians(28.904)
    ## Rotation matrix
    R1 = np.array([[np.cos(theta1), np.sin(theta1)], 
                   [-np.sin(theta1), np.cos(theta1)]])
    R2 = np.array([[np.cos(theta2), np.sin(theta2)], 
                   [-np.sin(theta2), np.cos(theta2)]])
    # Rotate Origin and Destination coordinates by -29 degrees
    pT = R1 @ p.T  
    dT = R1 @ d.T
    
    # Coordinates of hinge point in the rotated world 
    vT = np.stack((pT[0,:], dT[1,:]))
    # Coordinates of Hinge point in the real world 
    v = R2 @ vT
    return (great_circle_distance(p.T[0], p.T[1], v[0], v[1]) +
            great_circle_distance(v[0],v[1], d.T[0],d.T[1] ))



def great_circle_distance(origin_lat, origin_lon, destination_lat, destination_lon):
    r = 6371 #earth radius in KM
    phi1 = np.radians(origin_lat)
    phi2 = np.radians(destination_lat)
    delta_phi = np.radians(destination_lat - origin_lat)
    delta_lambda = np.radians(destination_lon - origin_lon)
    a = np.sin(delta_phi/2)**2 + np.cos(phi1)*np.cos(phi2)*np.sin(delta_lambda/2)**2
    res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return np.round(res, 2)