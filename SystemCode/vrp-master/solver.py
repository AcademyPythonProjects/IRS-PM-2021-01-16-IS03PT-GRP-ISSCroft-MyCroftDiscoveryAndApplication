from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import json

"""Sovle Capacited Vehicles Routing Problem (CVRP)"""
"""Get the Vehicles Routes."""

def get_vehicles_routes(data, manager, routing, solution):
    
    total_distance = 0
    total_delivered = 0
    vehicles_routes = {}
    
    open('vehicles_routes_json.txt', 'w').close()
    open('vehicles_routes_details.txt', 'w').close()

    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id) #26,88, 89...95
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_distance = 0
        route_delivery = 0
        list_index =[]

        while not routing.IsEnd(index): #input Start index: 26, 88, 89...95
            node_index = manager.IndexToNode(index) #26, 26, 26...26
            route_delivery = route_delivery + data['demands'][node_index]
            plan_output += ' {0} Deliver({1}) -> '.format(node_index, route_delivery)
            previous_index = index #26, 66, 68...65
            index = solution.Value(routing.NextVar(index)) #66, 68...65,96

            if index < data['num_locations']:
                list_index.append(index)
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)

        plan_output += ' {0} Deliver({1})\n'.format(manager.IndexToNode(index), route_delivery) #index=Depot
        plan_output += 'Distance of the route: {}km\n'.format(route_distance)
        plan_output += 'Delivery of the route: {}\n'.format(route_delivery)

        #print(plan_output)
        with open('vehicles_routes_details.txt',"a") as f:
            f.write(plan_output)

        total_distance += route_distance
        total_delivered += route_delivery
        vehicles_routes[vehicle_id] = list_index

    # print('Total distance of all routes: {}km'.format(total_distance))
    # print('Total parcels delivered of all routes: {}'.format(total_delivered))
    with open('vehicles_routes_details.txt',"a") as f:
        f.write("\n")
        f.write('Total_distance in km: ')
        f.write(str(total_distance))
        f.write("\n")
        f.write('Total number of parcels delivered: ')
        f.write(str(total_delivered))

    with open('vehicles_routes_json.txt',"a") as f:
        json.dump(vehicles_routes, f)


    return vehicles_routes


def run_solver(data):
    """Solve the CVRP problem."""
    # Instantiate the data problem.
    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)


    # Add Capacity constraint.
    def demand_callback(from_index):
        """Returns the demand of the node."""
        # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        return data['demands'][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        data['vehicle_capacities'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
    search_parameters.time_limit.FromSeconds(1)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console. Return vehicles_routes
    
    if solution:
        return get_vehicles_routes(data, manager, routing, solution)
