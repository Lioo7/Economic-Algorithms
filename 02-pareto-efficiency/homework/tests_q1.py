import unittest
import q1
 
class TestParetoImprovementMethods(unittest.TestCase):

    global agents
    global allOptions
    global num_of_options
    ami = q1.Agent({1: 1, 2: 2, 3: 3, 4: 4, 5: 5})
    tami = q1.Agent({1: 3, 2: 1, 3: 2, 4: 5, 5: 4})
    rami = q1.Agent({1: 3, 2: 5, 3: 5, 4: 1, 5: 1})
    agents = [ami, tami, rami]
    allOptions = [1, 2, 3, 4, 5]
    num_of_options = len(allOptions)

    def test_isParetoImprovement(self):
        actual_1 = []
        for option1 in range(1, num_of_options+1):
            for option2 in range(1, num_of_options+1):
                actual_1.append(q1.isParetoImprovement(agents, option1, option2))

        expected = [False, False, False, False, False, False, False, False, False, False, False, True, False,
                    False, False, False, False, False, False, False, False, False, False, False, False]

        self.assertEqual(actual_1, expected)

    def test_isParetoOptimal(self):
        actual_2 = []
        for option in allOptions:
            actual_2.append(q1.isParetoOptimal(agents, option, allOptions))

        expected = [False, False, False, False, False]

        self.assertEqual(actual_2, expected)


if __name__ == "__main__":
    unittest.main()
