def print_tables(objects, colnames):
    for col in colnames:
        print('{:>10s}'.format(col), end=' ')
    print()

    for obj in objects:
        for col in colnames:
            print('{:>10s}'.format(str(getattr(obj,col))), end=' ')

        print()
