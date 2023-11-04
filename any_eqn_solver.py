import sympy
from sympy import Equality, solve, Symbol, Expr


def parse_real(expr_str: str) -> tuple[Expr, dict[str, Symbol]]:
    symbols_expr = sympy.S(expr_str)

    symbols = {
        s.name: Symbol(
            s.name, real=True, finite=True, nonnegative=True,
        )
        for s in symbols_expr.free_symbols
    }

    expr = sympy.parse_expr(expr_str, symbols)
    return expr, symbols


class EqnSystem:
    def __init__(self, left: str, right: str) -> None:
        left_expr, left_syms = parse_real(left)
        right_expr, right_syms = parse_real(right)
        self.equation = Equality(left_expr, right_expr)
        self.symbols = left_syms | right_syms

    def solve(self, **kwargs: float) -> float:
        unknown, = self.symbols.keys() - kwargs.keys()
        solved, = solve(self.equation, self.symbols[unknown])
        value = solved.subs({
            self.symbols[k]: known
            for k, known in kwargs.items()
        })
        return float(value)


DENSITY = EqnSystem('p', 'm/v')
SPEED = EqnSystem('s', 'u + a*t')
# add more equations here

def test() -> None:
    p = DENSITY.solve(m=1.23, v=1.66)
    print(f'density: {p:.2f}')

    s = SPEED.solve(u=3, a=4, t=5)
    print(f'speed: {s:.2f}')


if __name__ == '__main__':
    test()
