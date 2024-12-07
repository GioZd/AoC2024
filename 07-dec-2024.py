def task_1(equations: list[str]) -> int:
    equations = [eq.strip().split(': ') for eq in equations]
    equations = [(int(t[0]), list(map(int, t[1].split()))) for t in equations]
    def equality(n: int, expr: list[int]) -> bool:
        if len(expr) == 1:
            return n == expr[0]
        return equality(n-expr[-1], expr[:-1]) or equality(n/expr[-1], expr[:-1])
    return sum(lhs for lhs, rhs in equations if equality(lhs, rhs))


def task_2(equations: list[str]) -> int:
    equations = [eq.strip().split(': ') for eq in equations]
    equations = [(int(t[0]), list(map(int, t[1].split()))) for t in equations]
    def isint(a):
        return int(a) == a
    def root(total: int, suffix: int) -> int:
        return int(str(total).removesuffix(str(suffix)))
    def equality(n: int, expr: list[int]) -> bool:
        if len(expr) == 1:
            return n == expr[0]
        return (
            equality(n-expr[-1], expr[:-1]) 
            or (equality(n/expr[-1], expr[:-1]) if isint(n/expr[-1]) else False)
            or (equality(root(n, expr[-1]), expr[:-1]) if str(n).endswith(str(expr[-1])) else False)
        )
    # return equality(192, [17, 8, 14])
    return sum(lhs for lhs, rhs in equations if equality(lhs, rhs))


if __name__ == '__main__':
    with open('07-dec-2024-input.txt', 'r') as data_input:
        equations = data_input.readlines()
    print(task_1(equations))
    print(task_2(equations))