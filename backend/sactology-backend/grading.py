def grade_diarrhoea(extra_stools: int) -> int:
    if extra_stools < 0:
        raise ValueError("extra_stools must be a non-negative integer")

    if extra_stools >= 7:
        return 3
    elif extra_stools >= 4:
        return 2
    elif extra_stools >= 1:
        return 1
    else:
        return 0