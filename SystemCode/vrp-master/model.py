import pandas as pd
from distance_matrix import compute_manhattan_distance_matrix

""" read Pick network smart locker locations, prepare data for CVRP solver """

def create_data_model(demand, vehicle_capacity):

    """Stores the data for the CVRP solver."""
    """Compute manhattan distance matrix."""

    df = pd.read_csv('Pick_locker_locations.csv')

    data = {}
    data['locations'] = list(zip(df['LATITUDE'],df['LONGITUDE']))

    data['num_locations'] = len(data['locations'])
    num_vehicles = int(round(data['num_locations'] * demand / vehicle_capacity))

    data['distance_matrix'] = compute_manhattan_distance_matrix(data['locations'])
    data['demands'] = [demand] * 26 + [0] + [demand]* (data['num_locations'] - 26-1)
    data['num_vehicles'] = num_vehicles
    data['vehicle_capacities'] = [vehicle_capacity] * num_vehicles
    data['depot'] = 26

    return data, df

