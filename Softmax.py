import math


def softmax(scores: List[float]) -> List[float]:  
    exp_scores = [math.exp(score) for score in scores]  
    sum_exp_scores = sum(exp_scores)  
    probabilities = [round(score / sum_exp_scores, 4) for score in exp_scores] 
    return probabilities

scores = [1, 2, 3]  
probabilities = softmax(scores)  
print(probabilities)  
