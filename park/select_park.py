

MODE_SEQ = 'sequentially'
MODE_VACANCY = 'vacancy rate'


def select_park(parks, mode):
    print(mode, parks)
    return {MODE_SEQ: sequentially,
            MODE_VACANCY: vacancy}[mode](parks)


def sequentially(parks):
    for index, park in enumerate(parks):
        if park.residual:
            print(index)
            return index

def vacancy(parks):
    pass