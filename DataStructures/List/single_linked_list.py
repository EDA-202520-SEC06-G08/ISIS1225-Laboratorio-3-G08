def new_single_node (element):
    node = {"next": None, "info": element}
    return node

def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0 
    }
    return newlist

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False
    
def size(my_list):
    return my_list["size"]


def add_first(my_list, element):
    node = {"info": element, "next": None}
    
    if my_list["size"] == 0:
        my_list["first"] = node
        my_list["last"] = node
        my_list["size"] += 1
    else:
        node["next"] = my_list["first"]
        my_list["first"] = node
        my_list["size"] += 1
    return my_list

def add_last(my_list,element):
    
    node = {"info": element, "next": None}
    if my_list["size"] == 0:
        my_list["first"] = node
        my_list["last"] = node
        my_list["size"] += 1
    else:
        my_list["last"]["next"] = node
        my_list["last"] = node
        my_list["size"] += 1
                   
    return my_list


def first_element(my_list):
        return my_list["first"]["info"]
    
def last_element(my_list):
        return my_list["last"]["info"]  
    
def get_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        searchpos = 0
        node = my_list["first"]
        while searchpos < pos:
            node = node["next"]
            searchpos += 1
        return node["info"]
    
    
def delete_element (my_list, pos):
    
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        if my_list["size"] == 1:
            eliminado = my_list["first"]
            my_list["first"] = None
            my_list["last"] = None
            list_eliminado = new_list()
            list_eliminado["first"] = eliminado
            list_eliminado["last"] = eliminado
        else:
            node = my_list["first"]
            i=0
            eliminado = None
            while i < my_list["size"] and eliminado == None:
                if i != pos: 
                    anterior = node
                    node = anterior["next"]
                else:
                    eliminado = node 
                    anterior["next"] = eliminado["next"]
                i+=1
                
            list_eliminado = new_list()
            list_eliminado["first"] = eliminado
            list_eliminado["last"] = eliminado
            
        my_list["size"] -= 1
        return list_eliminado
                    
            
def remove_first(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')
    else:
        eliminado = my_list["first"]["info"]

        if my_list["size"] == 1:
            my_list["first"] = None
            my_list["last"] = None
            
        else:
            new_first = my_list["first"]["next"]
            my_list["first"] = new_first
            
        my_list["size"] -= 1
        return eliminado
    
def remove_last(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')
    else:
        eliminado = my_list["last"]["info"]
        if my_list["size"] == 1:
            my_list["first"] = None
            my_list["last"] = None
        else:
            node = my_list["first"]
            i=0
            while node["next"] != None:
                node = node["next"]
            my_list["last"] = node
            
        my_list["size"] -= 1
        return eliminado
        
def insert_element(my_list, element, pos):
    
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        new_node = new_single_node(element)
        if pos == 0:  
            new_node["next"] = my_list["first"]
            my_list["first"] = new_node
            if my_list["size"] == 0:
                my_list["last"] = new_node
            
        else:
            
            node = my_list["first"]
            i=0
            encontrado = False
            while i < my_list["size"] and encontrado == False:
                if i != pos: 
                    anterior = node
                    node = anterior["next"]
                else:
                    
                    new_node["next"] = node 
                    anterior["next"] = new_node["next"]
                    encontrado =True
                i+=1
        my_list["size"] += 1
        return my_list
    
def default_function(elemen_1, element_2):

   if elemen_1 == element_2:
      return 0
   elif elemen_1 > element_2:
      return 1
   return -1


            
def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1
    return count

def change_info(my_list, pos, new_info):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        i = 0
        node = my_list["first"]
        encontrado = False
        while i < my_list["size"] and encontrado == False:
            if i != pos: 
                node = node["next"]
            else:
                node["info"] = new_info 
                encontrado = True
            i+=1
        return my_list
    
def exchange(my_list, pos_1, pos_2):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    
    if pos_1 == pos_2:
        return my_list
    
    if (pos_1 < 0 or pos_1 > size(my_list)) or (pos_2 < 0 or pos_2 > size(my_list)):
        raise Exception('IndexError: list index out of range')
    else: 
        node_pos_1 = None
        node_pos_2 = None
        pos_actual = 0
        nodo_actual = my_list["first"]
        while(pos_actual < my_list["size"]) and ((node_pos_1 is None) or (node_pos_2 is None)):
            if pos_actual == pos_1:
                node_pos_1 = nodo_actual
            if pos_actual == pos_2:
                node_pos_2 = nodo_actual
                
            nodo_actual = nodo_actual["next"]
            pos_actual += 1
        
        info_pos_1 =  node_pos_1["info"]
        node_pos_1["info"] = node_pos_2["info"]
        node_pos_2["info"] = info_pos_1
        
        return my_list
        
            
def sub_list(my_list, pos, num_elements):

    # Validamos lista vacía
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')

    # Validamos posición inicial
    if pos < 0 or pos >= my_list["size"]:
        raise Exception('IndexError: list index out of range')
    
    # Creamos una nueva lista vacía
    sublist = {"size": 0, "first": None, "last": None}

    # Avanzamos hasta la posición inicial
    nodo_actual = my_list["first"]
    pos_actual = 0
    while pos_actual < pos:
        nodo_actual = nodo_actual["next"]
        pos_actual += 1

    # Copiamos los elementos a la sublista
    count = 0
    while (nodo_actual is not None) and (count < num_elements):
        new_node = {"info": nodo_actual["info"], "next": None}

        if sublist["size"] == 0:
            sublist["first"] = new_node
            sublist["last"] = new_node
        else:
            sublist["last"]["next"] = new_node
            sublist["last"] = new_node

        sublist["size"] += 1
        count += 1
        nodo_actual = nodo_actual["next"]

    return sublist


