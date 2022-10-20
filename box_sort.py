#Author: Faith Elledge
#Githubuser: ellegef
#Date: 10/19
#Description: code sorts the volume of boxes from largest to smallest


class Box:
        def __init__(self, length, width, height):
            self._length = length
            self ._width = width
            self ._height = height

        def get_length(self):
            return self._length

        def get_width(self):
            return self._width

        def get_height(self):
            return self._height

        def get_volume(self):
            return (self._width)*(self._height)*(self._length)


        def box_list(box_inventory):
            for volume in range(1,len(box_inventory)):
                value = box_inventory[box_inventory.get_volume]
                pos = box_inventory.get_volume - 1
                while pos >= 0 and box_inventory.get_volume() > value:
                    box_inventory[pos + 1] = box_inventory[pos]
                    pos -= 1
                box_inventory[pos + 1] = value







