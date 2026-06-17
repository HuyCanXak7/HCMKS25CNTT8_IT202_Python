def calculate_average(scores):

    valid_scores = [
        score
        for score in scores
        if isinstance(score, (int, float))
    ]

    if not valid_scores:
        return 0

    return sum(valid_scores) / len(valid_scores)


def classify_student(average):

    if average >= 8:
        return "Giỏi"

    if average >= 6.5:
        return "Khá"

    if average >= 5:
        return "Trung bình"

    return "Yếu"