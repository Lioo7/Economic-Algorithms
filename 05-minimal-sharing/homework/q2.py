import random

def is_win_win_solution(vector_a, vector_b, distribution_a, distribution_b) -> bool:
    """the function checks if is it a win-win solution"""
    # checks if the total value of both the players is equal
    if eval(vector_a, distribution_a) == eval(vector_b, distribution_b):
        # checks if there is a maximum of one item that was divided
        num_of_divided = 0
        for dist in distribution_a:
            if isinstance(dist, float):
                num_of_divided += 1
        if num_of_divided < 2:
            return True
    
    return False

def eval(vector, distribution) -> int:
    """evaluate the sum of values of the given player"""
    mul_list = []
    for i in range(len(vector)):
        mul_list.append(vector[i] * distribution[i])
    
    return round(sum(mul_list), 2)

def generate_number() -> float:
    num = random.uniform(0.0, 1.0)
    round_num = round(num, 2)
    return round_num

def generate_distributions(length):
    distribution_a = []
    distribution_b = []
    for t in range(length):
        num = generate_number()
        distribution_a.append(num)
        distribution_b.append(round(1 - num, 2))

    return distribution_a, distribution_b

def is_pareto(oritinal_eval_a, new_eval_a, original_eval_b, new_eval_b):
    return new_eval_a >= oritinal_eval_a and new_eval_b >= original_eval_b

def pareto_improvement(vector_a, vector_b, distribution_a, distribution_b):
    found = False
    count = 0
    oritinal_eval_a = eval(vector_a, distribution_a)
    original_eval_b = eval(vector_b, distribution_b)

    while not found and count < 10000:
        new_distribution_a, new_distribution_b = generate_distributions(len(distribution_a))
        new_eval_a = eval(vector_a, new_distribution_a)
        new_eval_b = eval(vector_b, new_distribution_b)
        if is_pareto(oritinal_eval_a, new_eval_a, original_eval_b, new_eval_b):
            found = True

    if found:
        print("Pareto improvement was found!")
        print("original_distribution_a:", distribution_a)
        print("new_distribution_a:", new_distribution_a)
        print("original_distribution_b:", distribution_b)
        print("new_distribution_b:", new_distribution_b)
        print(f"oritinal_eval_a|b: {oritinal_eval_a} | {original_eval_b}")
        print(f"new_eval_a|b: {new_eval_a} | {new_eval_b}")
        return new_distribution_a, new_distribution_b
    else:
        print("Pareto improvement was not found")
        print("oritinal_eval_a:", oritinal_eval_a)
        return oritinal_eval_a, original_eval_b

def run(vector_a, vector_b, distribution_a, distribution_b) -> None:
    print("is_win_win_solution?")
    if is_win_win_solution(vector_a, vector_b, distribution_a, distribution_b):
        print("Yes")
    else:
        print("No")
        pareto_improvement(vector_a, vector_b, distribution_a, distribution_b)


def main() -> None:
    vector_a = [40, 30, 20, 10]
    vector_b = [10, 20, 30, 40]
    distribution_a = [1, 0, 0.4, 0.7]
    distribution_b = [0, 1, 0.6, 0.3]

    run(vector_a, vector_b, distribution_a, distribution_b)

if __name__ == '__main__':
    main()