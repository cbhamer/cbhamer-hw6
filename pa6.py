

def make_change(total):
    """
    This function takes a coin value and returns the different combinations that 
    coins can add to total amount
    """
    coins = [1, 5, 10, 25, 100]
    combos = []
    
    def helper(remaining, current_combo, start_index):
        if remaining == 0:
            combos.append(current_combo[:])
            return
        for i in range(start_index, len(coins)):
            coin = coins[i]
            if coin <= remaining:
                current_combo.append(coin)
                helper(remaining - coin, current_combo, i)
                current_combo.pop()
    
    helper(total, [], 0)
    
    return combos

def dict_filter(func, dic):
    """
    This function takes a function and a dictionary, then returns a new dictionary 
    where a key,value pair remains with each other if the function returns true
    when it calls the pair
    """
    new_dic = {}
    for key, val in dic.items():
        if func(key, val):
            new_dic[key] = val
    return new_dic

class KVTree:
    """
    This class designs a tree filled with children
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def treemap(func, tree):
    """
    This function takes a function and a tree, then returns a modified version of the 
    tree that changes the values of each child based on the function
    """
    tree.key, tree.value = func(tree.key, tree.value)
    for child in tree.children:
        treemap(func, child)

class DTree:
    """
    This class designs a flow chart for someone's though-process while making a 
    decision
    """
    def __init__(self, variable, threshold, lessequal, greater, outcome):
        if (variable is not None and threshold is not None and lessequal is not None and greater is not None) is not (outcome is None):
            raise ValueError("Either first four arguments or the outcome should not be none, but not both.")
        self.variable = variable
        self.threshold = threshold
        self.lessequal = lessequal
        self.greater = greater
        self.outcome = outcome

    def tuple_atleast(self):
        """
        This method determines how many entries there need to be in the tuple
        """
        max_var = 0
        if self.lessequal:
            max_var = max(max_var, self.lessequal.tuple_atleast())
        if self.greater:
            max_var = max(max_var, self.greater.tuple_atleast())
        if self.variable is not None:
            max_var = max(max_var, self.variable + 1)
        return max_var

    def find_outcome(self, observations):
        """
        This method takes in a tuple with observations and navigates through the 
        tree to provide the outcome that matches
        """
        if self.outcome is not None:
            return self.outcome
        val = observations[self.variable]
        if val <= self.threshold:
            return self.lessequal.find_outcome(observations)
        else:
            return self.greater.find_outcome(observations)

    def no_repeats(self):
        """
        This method returns True if and only if there are not “repeats”, 
        False otherwise.
        """
        def helper_repeat(node, last_variable=None):
            if node is None:
                return True
            if node.variable == last_variable:
                return False
            return helper_repeat(node.lessequal, node.variable) and helper_repeat(node.greater, node.variable)

        return helper_repeat(self)
