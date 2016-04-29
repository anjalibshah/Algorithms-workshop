# Basic Calculator Problem from Leetcode

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """
        Remove all the whitespaces from the expression string.
        
        Build an expression stack. Push operands into the stack until you encounter an operator.
        Upon encountering an operator, push the last operand and perform the operation based on the nature of
        the operator with the next operand in the expression string.
        
        Special cases:
        
        1. Parentheses: When '(' is encountered, push all expression operators and operands onto the stack
        until the ')' is ecountered. This forms a mini-expression for which the steps outlined above should be 
        repeated.
        
        """
     
 def eval_sublist(self, exprstack):  
    cal_total = 0
    sign = 1
    for i in range(len(exprstack)):
        next_item = exprstack.pop(0)
        if next_item[0] in ('-','+','') and next_item[1:].isdigit() or next_item.isdigit():
            cal_total += sign * int(next_item)
        else:
            if next_item == '+':
                sign = 1
            else:
                sign = -1
    return cal_total
 def calculate(self, s):
        
    # Remove whitespace characters from string 
    s = s.replace(" ","")

    # Convert string to list
    expression = re.split(r"(\(|\)|\+|\-)", s)
    expression = list(filter(None, expression))
           
    # Initialize expression stack
    exprstack = []
    sub_list = []
                
    for ch in range(len(expression)):
        if expression[ch] == ')':
            item = exprstack.pop()
            while  item != '(':
                sub_list.insert(0,item)
                item = exprstack.pop()
            exprstack.append(str(self.eval_sublist(sub_list)))
        else:
            exprstack.append(expression[ch])
    return self.eval_sublist(exprstack)
