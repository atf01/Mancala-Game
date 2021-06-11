import time
infinity = float('inf')

def AlphaBetaAlg(start_time, node, depth=infinity, alpha=-infinity, beta=infinity, isMaximizing=True, threshold=30):
    if depth == 0 or node.isterminal(isMaximizing):  # base condition
        return node.value, node.pos
    best_pos = None
    if isMaximizing:  # maxmizer player
        value = -infinity
        Choices = node.get_children()
        maximzer_best_prunning_list = []  # this list should be sorted in descending order
        for i in Choices:
            maximzer_best_prunning_list.append(i.value)
            other = AlphaBetaAlg(start_time, i, depth - 1, alpha, beta, isMaximizing=i.is_repeated)
            if value < other[0]:
                value = other[0]
                best_pos = i.pos
            if value > alpha:
                alpha = value
            if alpha >= beta:  # cutoff
                break
            if time.time() - start_time > threshold + 10:
                return value, best_pos, sorted(maximzer_best_prunning_list, reverse=True)
        return value, best_pos, sorted(maximzer_best_prunning_list, reverse=True)

    else:  # minimizer player
        value = infinity
        Choices = node.get_opponent_children()
        minimzer_best_prunning = []  # this list should be sorted in ascending order
        for i in Choices:
            minimzer_best_prunning.append(i.value)
            other = AlphaBetaAlg(start_time, i, depth - 1, alpha, beta, isMaximizing=not i.is_repeated)
            if value > other[0]:
                value = other[0]
                best_pos = i.pos
            if value < beta:
                beta = value
            if alpha >= beta:  # cutoff
                break

            if time.time() - start_time > threshold + 10:
                return value, best_pos, sorted(minimzer_best_prunning, reverse=False)
        return value, best_pos, sorted(minimzer_best_prunning, reverse=False)
