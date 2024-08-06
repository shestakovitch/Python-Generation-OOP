"""Иерархия классов 🔠
С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов:
                                    H
                              /  /  |  \
                             D  E   F   G
                              \ /    \  /
                               B      C
                                \    /
                                  A
"""


class H:
    pass


class D(H):
    pass


class E(H):
    pass


class F(H):
    pass


class G(H):
    pass


class B(D, E):
    pass


class C(F, G):
    pass


class A(B, C):
    pass
