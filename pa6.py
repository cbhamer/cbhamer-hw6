

def make_change(total):
    """
    doc...
    """
    coins = [1, 5, 10, 25, 100]
    combos = []
    
    def backtrack(remaining, current_combo, start_index):
        if remaining == 0:
            combos.append(current_combo[:])
            return
        for i in range(start_index, len(coins)):
            coin = coins[i]
            if coin <= remaining:
                current_combo.append(coin)
                backtrack(remaining - coin, current_combo, i)
                current_combo.pop()
    
    backtrack(total, [], 0)
    
    return combos

def dict_filter(func, dic):
    """
    doc....
    """
    new_dic = {}
    for key, val in dic.items():
        if func(key, val):
            new_dic[key] = val
    return new_dic

class KVTree:
    """
    doc...
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def treemap(func, tree):
    """
    doc...
    """
    tree.key, tree.value = func(tree.key, tree.value)
    for child in tree.children:
        treemap(func, child)

class DTree:
    """
    doc...
    """
    def __init__(self, variable, threshold, lessequal, greater, outcome):
        if (variable is None and threshold is None and lessequal is None and greater is None) != (outcome is None):
            raise ValueError("Either first four arguments or the outcome should not be none, but not both.")
        self.variable = variable
        self.threshold = threshold
        self.lessequal = lessequal
        self.greater = greater
        self.outcome = outcome

    def tuple_atleast(self):
        """
        doc...
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
        doc...
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
        doc...
        """
        seen_variables = set()

        def helper(node):
            if node is None:
                return True
            if node.variable in seen_variables:
                return False
            seen_variables.add(node.variable)
            return helper(node.lessequal) and helper(node.greater)

        return helper(self)