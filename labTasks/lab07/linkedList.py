import dtb

class linked_list:
    def __init__( self ):
        self . head = None

    def push( self, car ):
        new_Node = Node( car )
        if not self.head:
            self.head = new_Node
            return
        tmp_node = self.head
        while tmp_node.next:
            tmp_node = tmp_node.next
        tmp_node.next = new_Node

    def print_items( self ):
        tmp_node = self.head
        while tmp_node.next:
            print( tmp_node.car )
            tmp_node = tmp_node.next

    def pop( self ):
        car_to_return = self.head.car
        self.head = self.head.next
        return car_to_return

class Node:
    def __init__( self, car ):
        self . car = car
        self . next = None


ll = linked_list()
ll.push( dtb.Car( "BMW", 100000 ) )
ll.push( dtb.Car( "VW", 77777 ) )
ll.push( dtb.Car( "KIA", 900 ) )
ll.push( dtb.Car( "Audi", 5000 ) )
ll.print_items()
print( "POPPED:", ll.pop() )
ll.print_items()
