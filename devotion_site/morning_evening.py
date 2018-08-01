month_names = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

time_names = dict([(i, 'Morning') for i in range(13)] + [(i, 'Evening') for i in range(13, 25)])

def get_audio_path(month, day, time):
    raise NotImplementedError()
