import math

def calculateLumberProbability(total_logs, defected_logs, logs_needed):
    # Step 1: Edge case checks
    if defected_logs > total_logs:
        return 0
    if logs_needed > total_logs:
        return 0
    
    # Step 2: Calculate the non-defective logs
    non_defective_logs = total_logs - defected_logs
    
    # Step 3: If there aren't enough non-defective logs to pick
    if logs_needed > non_defective_logs:
        return 0
    
    # Step 4: Calculate the combinations
    # Ways to choose logs_needed from non_defective_logs
    ways_to_choose_non_defective = math.comb(non_defective_logs, logs_needed)
    
    # Ways to choose logs_needed from total_logs
    ways_to_choose_total = math.comb(total_logs, logs_needed)
    
    # Step 5: Calculate the probability
    probability = ways_to_choose_non_defective / ways_to_choose_total
    
    return probability
