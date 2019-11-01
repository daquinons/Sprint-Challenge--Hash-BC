#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for index, weight in enumerate(weights):
        hash_table_insert(ht, weight, index)

    for index, weight in enumerate(weights):
        retrieved_element_index = hash_table_retrieve(ht, limit - weight)
        if retrieved_element_index is not None:
            return (retrieved_element_index, index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
