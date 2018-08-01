from django.db import models
from django.contrib.auth import get_user_model


class DailyBiblePlan(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=True)

    def now_chapter(self):
        from .bible_chapters import chapter_list
        from datetime import date

        days_since_start = (date.today() - self.start_date).days
        return chapter_list[days_since_start % len(chapter_list)]

    def get_audio_url(self, *args):
        from .bible_chapters import get_audio
        return get_audio(*args)


class MorningEveningPlan(models.Model):
    plan = 'morning_evening'

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def now_chapter(self):
        from .morning_evening import month_names, time_names
        from datetime import datetime, date

        month, day = date.today().month, date.today().day
        month = month_names[month]
        time = time_names[datetime.now().hour]
        return month, day, time

    def get_audio_url(self, *args):
        from .morning_evening import get_audio_path
        return get_audio_path(*args)
