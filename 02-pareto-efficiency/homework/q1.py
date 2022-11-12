from typing import List

class Agent:
    """
    This class describes an agent who gets as an input a dictionary with value for each option
    """
    def __init__(self, options:dict[int, int]):
        self.options = options
    
    def value(self, option:int)->float:
        """
        INPUT: the index of an option.
        OUTPUT: the value of the option to the agent.
        """
        return self.options.get(option)


def isParetoImprovement(agents:List[Agent], option1: int, option2: int) -> bool:
    """
    This func gets as an input a list of agents and two options and checks is option1 is a pareto improvment of option2
    """
    flag = True # would be false if option1's value is smaller than option2's value
    counter = 0
    for agent in agents:
        if agent.value(option1) < agent.value(option2):
            flag = False
        elif agent.value(option1) == agent.value(option2):
            pass
        else:
            counter = counter + 1
    
    return flag and counter > 0

def isParetoOptimal(agents: List[Agent], option: int, allOptions: List[int]) -> bool:
    """
    This func gets as an input a list of agents, an option number and a list of all the options and checks if the given option is a pareto improvment
    """
    for option2 in allOptions:
        if isParetoImprovement(agents, option, option2) == False:
            return False
    
    return True


