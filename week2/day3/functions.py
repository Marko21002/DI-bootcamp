def calculation(a: int, b: int) -> tuple[int, int]:
    res1 = a - b
    res2 = a + b
    return res1, res2


res = calculation(5, 10)
print(res)


def sunny_dark(hour: int) -> str | None:
    if 10 < hour < 18:
        return "sunny"
    elif 24 > hour > 18 or 0 < hour < 10:
        return "dark"
    else:
        return None


print(
    sunny_dark(15))
