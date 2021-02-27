number_of_cities = 5
number_of_bridge = 3
number_of_bridge_allowed = 1
linear_way = [1,2,1,4]
bridges = [[1,2,3],[1,3,2],[3,4,1]]

allowed_bridges = [[1,3,2]]

def linear_cost(current):
    cost = 0
    for x in range(0, current-1):
        cost = cost + linear_way[x]
    return cost


def check_bridge_upto_current(current):
    for x in range(1, current+1):
        bridge = check_bridge_exists(x, current)
        if(bridge[0] != 'a' ):
            return bridge
    return ['a']

#this will return bridge if bridge exist and if the bridge needs to be used
def check_bridge_exists(source, destination):
    for bridge in bridges:
        if (bridge[0] == source and bridge[1]==destination):
            print("bridge found")
            #now checking if found bridge is allowed or not
            for b in allowed_bridges:
                if (b[0] == source and b[1]==destination):
                    return b
    return ['a']


def travel_bridge():
    cost = 0
    for x in range(1, len(linear_way)+1):
        source = x
        destination = x+1
        bridge_check = check_bridge_exists(source, destination)
        # print("bridge_check",bridge_check)
        if(bridge_check[0] != 'a' ):
            cost = cost + bridge_check[2]
        else:
            cost = cost + linear_way[x-1]

        linear_cost_upto_current = linear_cost(destination)
        bridge_check = check_bridge_upto_current(destination)
        if(bridge_check[0] != 'a' ):
            print("tatatta....", bridge_check)
            cost = cost - abs(bridge_check[2]-linear_cost_upto_current)
    print("cost...................",cost)
  


    

# def bridge_which_to_use(linear_way, bridges):
#     print("some")

# def linear_cost(linear_way):
#     print(sum(linear_way))

# print(bridges[1][1])
# linear_cost(linear_way)
travel_bridge()

 
# for t in range(0, len(bridges)):
#     #checking if bridge exists

#     print(bridges[t])
