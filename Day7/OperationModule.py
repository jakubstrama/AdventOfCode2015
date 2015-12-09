class Operation:
    collection = None
    left = None
    right = None
    target = None
    operator = None
    command = None
    done = False

    def __init__(self, collection, left, right, target, operator):
        self.done = False
        self.collection = collection
        self.left = left
        self.right = right
        self.target = target
        self.operator = operator
        self.command = self._getActions()[operator]


    def _getActions(self):
        actions = {
        'AND': lambda a,b: a & b,
        'OR': lambda a,b: a | b,
        'LSHIFT': lambda a, num: a << num,
        'RSHIFT': lambda a, num: a >> num,
        'NOT': lambda a: ~a,
        'ASSIGN': lambda a: a
        }
        return actions


    def runCommand(self):
        if(self.operator == "NOT" or self.operator == "ASSIGN"):
            self.collection[self.target] = self.command(self._resolveVar(self.left))
        else:
            self.collection[self.target] = self.command(self._resolveVar(self.left), self._resolveVar(self.right))

        self.done = True


    def isReady(self):
        if(self.done):
            return False

        if(self.operator == "AND" or self.operator == "OR"):
            return self._isVarSet(self.left) and self._isVarSet(self.right)
        else:
            return self._isVarSet(self.left)


    def _resolveVar(self, var):
        if(var.isdigit()):
            return int(var)
        else:
            return self.collection[var]

    def _isVarSet(self, var):
        if(var.isdigit()):
            return True
        else:
            return var in self.collection

    def __str__(self):
        return "{0} - Left: {1}; Right: {2}; Target: {3}; Done: {4}".format(self.operator, self.left, self.right, self.target, self.done)
