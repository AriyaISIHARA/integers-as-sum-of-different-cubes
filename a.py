import sys


def _cubesumtex(items):
    return " + ".join(f"{i}^3" if i > 0 else f"({i})^3" for i in items)


def _q(already, new, updates, elems, new_elem):
    if new > 0:
        if new not in already:
            updates[new] = (*elems, new_elem)
    elif new < 0:
        if -new not in already:
            updates[-new] = tuple(-e for e in (*elems, new_elem))


def _search(sup):
    res = {0: ()}
    n = 1
    wanted = 1
    while True:
        c = n ** 3
        updates = {}
        for i, breakdown in res.items():
            _q(res, i + c, updates, breakdown, n)
            _q(res, i - c, updates, breakdown, -n)
        res.update(updates)
        while wanted in res:
            print(rf"\\{wanted} &=& {_cubesumtex(res[wanted])}")
            wanted += 1
            if wanted == sup + 1:
                return
        n += 1


def _main(sup=-1):
    print("[math]\\displaystyle\\begin{eqnarray}\n0 &=& 1+3 + (-1)^3")
    _search(sup)
    print(r"\end{eqnarray}[/math]")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        _main(int(sys.argv[1]))
    else:
        _main()
