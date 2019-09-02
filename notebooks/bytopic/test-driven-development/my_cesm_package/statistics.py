def mean(num_list):
    try:
        return sum(num_list) / len(num_list)
    except ZeroDivisionError as detail:
        msg = "The algebraic mean of an empty list is undefined. Please provide a list of numbers."
        raise ZeroDivisionError(f"{detail.__str__()}\n{msg}")
