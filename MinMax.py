import time
def AlphaBetaAlg(node, depth, alpha, beta, isMaximizing,start_time,threshold):
    infinity = float('inf')
    if depth == 0 or node.isterminal():
        return node.value
    if isMaximizing:
        value = -infinity
        for i in node.getChildren():
            value = max(value, AlphaBetaAlg(i, depth - 1, alpha, beta, isMaximizing=False))
            alpha = max(alpha, value)
            if alpha >= beta:  # cutoff
                break
            if time.time()-start_time > threshold+10:
                return value
        return value
    else:  # minimizing player
        value = +infinity
        for i in node.children:
            value = min(value, AlphaBetaAlg(i, depth - 1, alpha, beta, isMaximizing=True))
            beta = min(beta, value)
            if alpha >= beta:  # cutoff
                break
        return value