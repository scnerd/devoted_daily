import os
import json
import requests

bible_versions = [('ESV', 'ESV'), ('KJV', 'KJV')]
_key = open(os.environ['DIGITAL_BIBLE_KEY_FILE']).read().strip()


def call_dbt(url, **kwargs):
    kwargs['key'] = _key
    kwargs['v'] = 2
    return json.loads(requests.get(url, params=kwargs).content.decode())


def make_dam(language, version, collection, drama_type):
    return f'{language.upper()}{version.upper()}{collection.upper()}{drama_type}DA'


# _servers = call_dbt('https://dbt.io/audio/location', protocol='http')
_servers = [
    {
        "server": "fcbhabdm.s3.amazonaws.com",
        "root_path": "/mp3audiobibles2",
        "protocol": "http",
        "CDN": "0",
        "priority": "6"
    }
]
chapter_data = {
    'O': call_dbt('https://dbt.io/library/book', dam_id=make_dam('ENG', 'ESV', 'O', 1)),
    'N': call_dbt('https://dbt.io/library/book', dam_id=make_dam('ENG', 'ESV', 'N', 1)),
}

chapter_list = [
    (testament[0], book['book_id'], int(chapter))
    for testament in chapter_data
    for book in chapter_data[testament]
    for chapter in book['chapters'].split(',')
]


def get_audio(version, collection, book, chapter):
    for server in _servers:
        try:
            dam = make_dam('ENG', version, collection, 1)
            info = call_dbt('https://dbt.io/audio/path', dam_id=dam, book_id=book, chapter_id=chapter)[0]
            return f"https://{server['server']}{server['root_path']}/{info['path']}"
        except Exception:
            continue
    else:
        raise ValueError(f"Could not find any files for {version} {collection} {book} {chapter}")
