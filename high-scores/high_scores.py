def latest(scores):
    if len(scores) == 0:
        raise Exception("There are no scores yet")
    return scores[-1]


def personal_best(scores):
    if len(scores) == 0:
        raise Exception("There are no scores yet")
    sorted_scores = sorted(scores, reverse=True)
    return sorted_scores[0]


def personal_top_three(scores):
    if len(scores) == 0:
        raise Exception("There are no scores yet")
    sorted_scores = sorted(scores, reverse=True)
    return sorted_scores[0:3]
