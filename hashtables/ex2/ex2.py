#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    first_flight = hash_table_retrieve(hashtable, "NONE")
    route[0] = first_flight

    for index, element in enumerate(route):
        if index < len(route) - 1:
            route[index + 1] = hash_table_retrieve(hashtable, route[index])

    return route
