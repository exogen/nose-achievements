from datetime import timedelta
from noseachievements.achievements.base import Achievement


class InstantFeedback(Achievement):
    title = "Instant Feedback"

    def finalize(self, data, result):
        if not data['result.errors'] and data['result.tests'] >= 50:
            elapsed_time = data['time.finish'] - data['time.start']
            if elapsed_time < timedelta(seconds=1):
                data.unlock(self, (data['result.tests'], elapsed_time))

