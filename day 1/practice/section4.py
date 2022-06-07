#apprend the fruit argument to the end of the fruits list.
#after we do that we will return the list



def append_fruit(fruit):
    fruits = ['avacado', 'tamoto', 'carrot', 'orange']
    fruits.append(fruit)
    return fruits


def insert_fruit(index, fruit):
    fruits = ['avacado', 'tamoto', 'carrot', 'orange']
    fruits.insert(index, fruit)
    return fruits


insert_fruit(3, 'lime')