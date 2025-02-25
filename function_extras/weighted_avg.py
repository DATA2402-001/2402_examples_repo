def weighted_avg(numbers: list, weights: list = None) -> float:

    # if weights not supplied, set weights to all 1s
    if weights is None:
        weights = []
        for i in range(len(numbers)):
            weights.append(1)
    
    # now do a weighted avg
    running_sum = 0
    for i in range(len(numbers)):
        running_sum += numbers[i] * weights[i]
    
    return running_sum / sum(weights)