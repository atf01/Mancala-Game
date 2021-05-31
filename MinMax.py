def AlphaBetaAlg(node, depth, alpha, beta, isMaximizing):
    infinity = float('inf')
    if depth == 0 or node.isterminal():
        return node.value
    if isMaximizing:
        value = -infinity
        maximzer_best_prunning_list=[] #this list should be sorted in descending order
        for i in node.getChildren():
            maximzer_best_prunning_list.append(i.value)
            value = max(value, AlphaBetaAlg(i, depth - 1, alpha, beta, isMaximizing=False))
            alpha = max(alpha, value)
            if alpha >= beta:  # cutoff
                break
        return value,sorted(maximzer_best_prunning_list,reverse=True)
    else:  # minimizing player
        value = +infinity
        minimzer_best_prunning=[] #this list should be sorted in ascending order
        for i in node.children:
            minimzer_best_prunning.append(i.value)
            value = min(value, AlphaBetaAlg(i, depth - 1, alpha, beta, isMaximizing=True))
            beta = min(beta, value)
            if alpha >= beta:  # cutoff
                break
        return value,sorted(minimzer_best_prunning,reverse=False)