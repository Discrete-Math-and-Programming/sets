# Edit this file for your solutions.

# Here is a sample solution for the cardinality of a set
size = lambda x: len(x.keys())

# `set_from_list` -- takes a list and returns a set.


# `list_from_set` -- do the reverse of above. 


# `add` -- takes a set and an element and returns a new set with the element added.


# `remove` -- takes a set and an element and returns a new set with the element removed.


# `union`


# `intersection`


# `difference`


# `symmetric_difference` -- the elements that are in exactly one of the sets.


# `is_subset_of`


# `is_superset_of`


def test():
    """Use this function to test your solutions"""

    def test_function(func, *args, expected):
        try:
            result = func(*args)
            return "[OK]" if result == expected else "[Not OK]"
        except Exception as e:
            return "[Error]"

    test_cases = {
        "set_from_list": (set_from_list, [[1, 2, 3]], {1: None, 2: None, 3: None}),
        "list_from_set": (list_from_set, [{1: None, 2: None, 3: None}], [1, 2, 3]),
        "add": (add, [{1: None, 2: None}, 3], {1: None, 2: None, 3: None}),
        "remove": (remove, [{1: None, 2: None, 3: None}, 2], {1: None, 3: None}),
        "union": (union, [{1: None, 2: None}, {2: None, 3: None}], {1: None, 2: None, 3: None}),
        "intersection": (intersection, [{1: None, 2: None}, {2: None, 3: None}], {2: None}),
        "difference": (difference, [{1: None, 2: None}, {2: None, 3: None}], {1: None}),
        "symmetric_difference": (symmetric_difference, [{1: None, 2: None}, {2: None, 3: None}], {1: None, 3: None}),
        "is_subset_of": (is_subset_of, [{1: None, 2: None}, {1: None, 2: None, 3: None}], True),
        "is_superset_of": (is_superset_of, [{1: None, 2: None, 3: None}, {1: None, 2: None}], True),
    }
    
    print("Function Name            | Status")
    print("-------------------------|--------")
    for name, (func, args, expected) in test_cases.items():
        status = test_function(func, *args, expected=expected)
        print(f"{name:<25} | {status}")
