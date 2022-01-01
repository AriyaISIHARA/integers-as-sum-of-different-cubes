def _q(already, new, updates, elems, new_elem):
    if new > 0:
        if new not in already:
            updates[new] = (*elems, new_elem)
    elif new < 0:
        if -new not in already:
            updates[-new] = tuple(-e for e in (*elems, new_elem))


def _main():
    res = {0: ()}
    n = 1
    wanted = 1
    while True:
        c = n ** 3
        updates = {}
        for i, breakdown in res.items():
            _q(res, i + c, updates, breakdown, n)
            _q(res, i - c, updates, breakdown, -n)
        while wanted in updates:
            print(f"{wanted}: {updates[wanted]}")
            wanted += 1
        res.update(updates)
        n += 1


if __name__ == '__main__':
    _main()

