from typing import List, Dict
# import cvxpy as cp

def Nash_budget(total: float, subjects: List[str], preferences: List[List[str]]) -> Dict[str, float]:
    # Initialize the budget allocation for each subject to 0
    allocation = {subject: 0 for subject in subjects}

    # Calculate the Nash budget for each player
    for i, preference in enumerate(preferences):
        # Calculate the player's budget
        player_budget = total * len(preference) / len(subjects)
        # Allocate the player's budget to their preferred subjects
        for subject in preference:
            allocation[subject] += player_budget * \
                (1 - allocation[subject] / total) / len(preference)

    # Round the budget allocation for each subject
    allocation = {subject: round(allocation[subject], 2)
                  for subject in subjects}

    # Return the budget allocation for each subject and the breakdown of the budget according to the players
    return {
        'subjects': [subject for subject in subjects],
        'allocation': [allocation[subject] for subject in subjects],
        'breakdown': [(i+1, preference, allocation[subject]) for i, (preference, subject) in enumerate(zip(preferences, subjects))]
    }


def test_Nash_budget():
    # test equal allocation for two players with equal preferences
    actual = Nash_budget(100, ['Security', 'Education'], [
        ['Security'], ['Education']])
    expected = [50, 50]
    assert actual['allocation'] == expected
  
    # test equal allocation for three players with equal preferences
    actual = Nash_budget(100, ['Security', 'Education', 'Healthcare'], [
        ['Security'], ['Education'], ['Healthcare']])
    expected = [33.33, 33.33, 33.33]
    assert actual['allocation'] == expected
    
test_Nash_budget()

# did not finish yet

# def Nash_budget_optimization(total: float, subjects: List[str], preferences: List[List[str]]) -> Dict[str, float]:
#     # Initialize the budget allocation for each subject
#     allocation = cp.Variable(len(subjects))

#     # Calculate the Nash budget for each player
#     for i, preference in enumerate(preferences):
#         # Calculate the player's budget
#         player_budget = total * len(preference) / len(subjects)
#         # Allocate the player's budget to their preferred subjects
#         for j, subject in enumerate(subjects):
#             if subject in preference:
#                 allocation[j] += cp.max(0, player_budget / len(preference))

#     # Form and solve the problem
#     prob = cp.Problem(cp.Minimize(0), [allocation >= 0, allocation <= total])
#     prob.solve()

#     # Return the budget allocation for each subject and the breakdown of the budget according to the players
#     return {
#         'subjects': [subject for subject in subjects],
#         'allocation': allocation.value.tolist(),
#         'breakdown': [(i+1, preference, allocation.value[i]) for i, preference in enumerate(preferences)]
#     }

# def test_Nash_budget_optimization():
#     # Test 1
#     result = Nash_budget(100, ['Security', 'Education'], [
#         ['Security'], ['Security', 'Education']])
#     assert result == {
#         'subjects': ['Security', 'Education'],
#         'allocation': [75, 25],
#         'breakdown': [
#             (1, ['Security'], 75),
#             (2, ['Security', 'Education'], 25)
#         ]
#     },

#     # Test 2
#     result = Nash_budget(100, ['Security', 'Education', 'Healthcare'], [
#         ['Security'], ['Security', 'Education'], ['Healthcare']])
#     assert result == {
#         'subjects': ['Security', 'Education', 'Healthcare'],
#         'allocation': [50, 25, 25],
#         'breakdown': [
#             (1, ['Security'], 50),
#             (2, ['Security', 'Education'], 25),
#             (3, ['Healthcare'], 25)
#         ]
#     }
