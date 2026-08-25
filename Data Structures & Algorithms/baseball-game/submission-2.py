class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for i in range(len(operations)):
            operation = operations[i]
            
            if operation == "+":
                scores.append(scores[len(scores)-1] + scores[len(scores)-2])
            elif operation == "D":
                scores.append(2 * scores[len(scores)-1])
            elif operation == "C":
                scores.pop()
            else:
                scores.append(int(operation))
            
        return sum(scores)