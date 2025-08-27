def new_list():
    newlist = {
        "elements" :[],
        "size" : 0
    }
    return newlist

def get_element(my_list, index):
    return my_list["elements"] [index]

def is_present(my_list, element, cmp_function) :
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"] [keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
    if keyexist:
        return keypos
    return -1

def is_empty(my_list):
    return my_list["size"] == 0

def add_first(my_list, element):
    if my_list["size"] == 0:
        my_list["elements"].append(element)
        my_list["size"] += 1
    else:
        x = [element]
        for i in my_list["elements"]:
            x.append(i)
        my_list["elements"] = x
        my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    if my_list["size"] == 0:
        my_list["elements"].append(element)
        my_list["size"] += 1 
    else:
        my_list["elements"].append(element)
        my_list["size"] += 1
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    return my_list["elements"][0]

def last_element(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    return my_list["elements"][my_list["size"]-1]

def delete_element(my_list, pos):
    if my_list["size"] > 0 and pos >= 0 and pos < my_list["size"]:
        my_list["elements"].pop(pos)   
        my_list["size"] -= 1  
        
        return my_list
    else:
        raise IndexError("list index out of range")

def remove_first(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    
    if my_list["size"] > 0:
        element = my_list["elements"].pop(0)
        my_list["size"] -= 1
        return element

def remove_last(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    
    if my_list["size"] > 0:
        element = my_list["elements"].pop()
        my_list["size"] -= 1
        return element

def insert_element(my_list, element, pos):
    if pos >= 0 and pos <= my_list["size"]:
        x = []
        for i in range(0, pos):
            x.append(my_list["elements"][i])
        x.append(element)
        for j in range(pos, my_list["size"]):
            x.append(my_list["elements"][j])
        my_list["elements"] = x
        my_list["size"] += 1
        return my_list

def change_info(my_list, pos, new_info):
    if my_list["size"] > 0 and pos >= 0 and pos < my_list["size"]:
        my_list["elements"][pos] = new_info
        return my_list

def exchange(my_list, pos1, pos2):
    if my_list["size"] > 0 and pos1 >= 0 and pos1 < my_list["size"] and pos2 >= 0 and pos2 < my_list["size"]:
        temporal = my_list["elements"][pos1]
        my_list["elements"][pos1] = my_list["elements"][pos2]
        my_list["elements"][pos2] = temporal
        return my_list
    
def sub_list(my_list, pos_i, num_elements):
    if my_list["size"] > 0 and pos_i >= 0 and pos_i < my_list["size"] and num_elements > 0 and (pos_i + num_elements) <= my_list["size"]:
        sublist = new_list()
        for i in range(pos_i, pos_i + num_elements):
            add_last(sublist, my_list["elements"][i])
        return sublist