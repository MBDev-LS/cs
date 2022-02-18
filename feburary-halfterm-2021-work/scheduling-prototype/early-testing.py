
class Topic():
    def __init__(self) -> None:
        self.topicName = str()
        self.timeCreated = int()
        self.dateFirstReviewed = 'datetime?'

        self.nextReviewTargetDate = 'datetime?'
        self.currentDifficultyRating = int()

        self.reviewHistory = [
            {
                'time': int(),
                'ratingGiven': int(),
            }
        ]


