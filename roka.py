def gen_steps(n: int):
    """Megoldó lépések legenerálása n lyukhoz."""

    if n < 3:
        return list((1,) * n)

    diag = list(range(2, n))
    return diag + diag[::-1]


def check_for_n(n: int) -> bool:
    """Működik-e a stratégia adott n rókalyukkal?"""

    steps = gen_steps(n)
    holes = [{n} for n in range(1, n + 1)]

    for i, step in enumerate(steps):
        new_holes = [set() for _ in range(1, n + 1)]
        for i, hole in enumerate(holes):
            if i == step - 1:
                continue
            if i > 1 - 1:
                new_holes[i - 1] |= hole
            if i < n - 1:
                new_holes[i + 1] |= hole
        holes = new_holes

    return all(not hole for hole in holes)


def check_in_range(a: int, b: int) -> int:
    """
    Megnézi az összes n-et `a` és `b` között.
    Visszatér: Az első n-nel, amivel nem működik.
    Ha nincs ilyen, akkor 0.
    """
    assert a < b

    for n in range(a, b + 1):
        if not check_for_n(n):
            return n

    return 0


if __name__ == "__main__":
    a = int(input("a: "))
    try:
        print("(Ha csak n=a-ra, akkor nem kell)")
        b = int(input("b: "))
    except Exception:
        b = None

    if b is None:
        works = check_for_n(a)
        print("Működik" if works else "Nem működik...")

    else:
        err = check_in_range(a, b)
        print(
            f"n = {a}..{b} mindegyikre működik! :D"
            if err == 0
            else f"Sajnos {a}..{b} közül n={err}-re nem működik... :(",
        )
