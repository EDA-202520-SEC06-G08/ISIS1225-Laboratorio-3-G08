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

def add_first(my_list, element):
        
    if my_list["size"] == 0:
        my_list.append(element)
        return my_list
    else:
        x = [element]
        for i in my_list:
            x.append(i)
    return x
 


