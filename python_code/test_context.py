from contextlib import contextmanager

@contextmanager
def test(a):
    print 'whats up'
    try:
        yield '(:: {} ::)'.format(a)
    except Exception:
        pass
    finally:
        print 'done'

with test('A') as skate_board:
        print skate_board
        print skate_board_raise
