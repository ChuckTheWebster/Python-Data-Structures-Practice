def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # for char in phrase:
    #     if to_swap == char and to_swap.lower == char:
    #         char.upper()
    #     elif to_swap == char and to_swap.upper == char:
    #         char.lower()

    for item in enumerate(phrase):
        if to_swap == item[1] and to_swap.lower == item[1]:
            phrase[item[0]] = item[1].upper()
        elif to_swap == item[1] and to_swap.upper == item[1]:
            phrase[item[0]] = item[1].lower()

    return phrase