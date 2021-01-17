adjacent_cost_matrix = [
    [ 0,    12,	10,	-1,	-1,	-1,	12],
    [12,	0,	8,	12,	-1,	-1,	-1],
    [10,	8,	0,	11,	3,	-1,	9],
    [-1,	12,	11,	0,	11,	10,	-1],
    [-1,	-1,	3,	11,	0,	6,	7],
    [-1,	-1,	-1,	10,	6,	0,	9],
    [12,	-1,	9,	-1,	7,	9,	0 ]
]

# print(adjacent_cost_matrix[2][4])
source_vertex = 1
# def find_cost_of(from_vertex, to_vertex):

vertex_list = [1,2,3,4,5,6,7]
# print(vertex_list[0])

def calculate_path(current, vertex_set):

    if len(vertex_set) == 0:
        return adjacent_cost_matrix[current][source_vertex]
        #but the question is if the distance between current and source_vertex = -1 meaning distance is unknown, then ?
    if len(vertex_set) == 1:
        return adjacent_cost_matrix[current][vertex_set[0]] + calculate_path(vertex_set[0], [])
        #but the question is if the distance between current and vertex_set[0] = -1 meaning distance is unknown, then ?

    new_vertex_set = vertex_set.copy()
    temp_list = []
    for vertex in vertex_set:
  
        new_vertex_set.remove(vertex)
 
        cost = adjacent_cost_matrix[current][vertex] + calculate_path(vertex, new_vertex_set)
        temp_list.append(cost)
        # not sure but here we may need to use some matrix to store the cost so that once loop gets completed we can find the minimum of all brach of vertex_set
    return min(temp_list)
calculate_path(1, vertex_list)