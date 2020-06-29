import sys
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)



# def merge_a(xs, ys):
#     result = []
#     while True:
#         for i in xs:
#             if i in xs and i in ys:
#                 if i not in result:
#                     result.append(i)
#     return result
#
#
# def merge_b(xs, ys):
#     result = []
#     while True:
#         for i in xs:
#             if i in xs and i not in ys:
#                 if i not in result:
#                     result.append(i)
#     return result
#
#
# def merge_c(xs, ys):
#     result = []
#     while True:
#         for i in ys:
#             if i in ys and i not in xs:
#                 if i not in result:
#                     result.append(i)
#     return result
#
#
# def merge_d(xs, ys):
#     result = []
#     while True:
#         for i in xs:
#             if i in xs or i in ys:
#                 if i not in result:
#                     result.append(i)
#     while True:
#         for i in ys:
#             if i in xs or i in ys:
#                 if i not in result:
#                     result.append(i)
#     return result
#
#
# def merge_e(xs, ys):
#     while True:
#         for i in xs:
#             if i in ys:
#                 xs.remove(i)
#                 ys.remove(i)
#         return xs


xs = [1, 2, 3]
ys = [1, 4, 5]


def merge_a_correct(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            return result

        if xs[xi] == ys[yi]:
            result.append(xs[xi])
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            xi += 1
        else:
            yi += 1


def merge_b_correct(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            yi += 1


def merge_c_correct(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            result.append(ys[yi])
            xi += 1
        else:
            yi += 1


def merge_d_correct(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        else:
            result.append(ys[yi])
            result.append(xs[xi])
            xi += 1
            yi += 1


def test_suite():
    # test(merge_b_correct(xs, []) == xs)
    # test(merge_b_correct([], ys) == [])
    # test(merge_b_correct(xs, ys) == [2, 8])
    # test(merge_c_correct(xs, ys) == [4, 9])
    test(merge_d_correct(xs, ys) == [4, 2, 5, 3])


test_suite()
