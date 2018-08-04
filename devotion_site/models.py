from django.db import models
from django.contrib.auth import get_user_model
from datetime import date, datetime, timedelta
from .bible_chapters import bible_versions, chapter_list


class DailyBiblePlan(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    version = models.CharField(max_length=3, choices=bible_versions)

    def now_chapter(self):
        days_since_start = (date.today() - self.start_date).days
        return [chapter_list[days_since_start % len(chapter_list)]]

    def cache_chapters(self):
        for day in range(7):
            day = (date.today() - self.start_date).days + day
            yield chapter_list[day % len(chapter_list)]

    def get_audio_url(self, *args):
        from .bible_chapters import get_audio
        return get_audio(self.version, *args)


class MorningEveningPlan(models.Model):
    plan = 'morning_evening'

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def now_chapter(self):
        from .morning_evening import month_names, time_names

        month, day = date.today().month, date.today().day
        month = month_names[month]
        time = time_names[datetime.now().hour]
        return month, day, time

    def cache_chapters(self):
        from .morning_evening import month_names, time_names
        for day in range(7):
            day = date.today() + timedelta(days=day)
            month, day = day.month, day.day
            month = month_names[month]
            time = time_names[datetime.now().hour]
            return month, day, time

    def get_audio_url(self, *args):
        from .morning_evening import get_audio_path
        return [get_audio_path(*args)]


plans = [DailyBiblePlan, MorningEveningPlan]
