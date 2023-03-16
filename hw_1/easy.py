def fibonacci(quantity: int) -> str:
    """

    :param quantity:
    :return:
    """
    assert quantity >= 0, "The length of the sequence cannot be negative"
    seq = [1, 1]
    if quantity < 2:
        return seq[:quantity]

    for _ in range(quantity - 2):
        new_el = seq[-1] + seq[-2]
        seq.append(new_el)

    return seq

