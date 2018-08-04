from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import StreamingHttpResponse
import requests

from .models import plans
from .bible_chapters import get_audio


def try_get_plans(plans=plans, **kwargs):
    for plan in plans:
        try:
            yield plan.objects.get(**kwargs)
        except ObjectDoesNotExist:
            pass


@login_required()
def index(request):
    audio_files = [plan.get_audio_url(*args)
                   for plan in try_get_plans(user=request.user)
                   for args in plan.now_chapter()]
    print(audio_files)
    return render(request, 'devotion_site/index.html', context=dict(audio_files=audio_files))


@login_required()
def manifest(request):
    cache_files = [plan.get_audio_url(*args)
                   for plan in try_get_plans(user=request.user)
                   for args in plan.cache_chapters()]
    return render(request, 'devotion_site/cache.manifest', context=dict(to_cache=cache_files))


# def _stream(url, chunk_size=512 * 1024):
#     r = requests.get(url, stream=True)
#     return StreamingHttpResponse((chunk for chunk in r.iter_content(chunk_size)), content_type='audio/mpeg')
#
# @login_required()
# def bible_audio(request, version, collection, book, chapter):
#     return _stream(get_audio(version, collection, book, chapter))
