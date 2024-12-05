from functools import cmp_to_key

def task_1(rules: list[tuple[int, int]], 
           updates: list[list[int]]) -> tuple[list[list[int]], list[list[int]]]:
    conditions: dict[int, set[int]] = dict.fromkeys(t[0] for t in rules)
    for cond in conditions:
        conditions[cond] = set()
    for l, r in rules:
        conditions[l].add(r)
    valid_updates = []
    invalid_updates = []
    for update in updates:
        valid = True
        for idx, page in enumerate(update):
            cond = conditions.get(page, [update[-1]])
            if any(idx > update.index(c) for c in (cond & set(update))):
                valid = False
        if valid:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    # print(conditions)
    return valid_updates, invalid_updates

def task_2(rules: list[tuple[int, int]],
           updates: list[list[int]]) -> list[list[int]]:
    conditions: dict[int, set[int]] = dict.fromkeys(t[0] for t in rules)
    for cond in conditions:
        conditions[cond] = set()
    for l, r in rules:
        conditions[l].add(r)
    def a_lt_b(a, b):
        if a not in conditions:
            return False
        if b not in conditions[a]:
            return False
        return True
        
    # print([sorted(update, key=cmp_to_key(cmp_key)) for update in updates])
    # return [sorted(update, key=cmp_to_key(cmp_key)) for update in updates]
    sorted_values = []
    for update in updates:
        tmp = update.copy()
        for i in range(len(update)):
            for j in range(i, len(update)):
                if a_lt_b(tmp[j], tmp[i]):
                    tmp[i], tmp[j] = tmp[j], tmp[i]
        sorted_values.append(tmp)
    return sorted_values


if __name__ == '__main__':
    with open('05-dec-2024-input.txt', 'r') as data_input:
        rules, updates = data_input.read().split('\n\n')
        rules = [tuple(map(int, t.split('|'))) for t in rules.split('\n')]
        updates = [list(map(int, update.split(','))) for update in updates.strip().split('\n')]
    print(sum(update[len(update)//2] for update in task_1(rules, updates)[0]))
    print(sum(update[len(update)//2] for update in task_2(rules, task_1(rules, updates)[1])))