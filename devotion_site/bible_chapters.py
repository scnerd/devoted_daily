import os
import json

here = os.path.dirname(__file__)

chapter_data = json.load(open(os.path.jion(here, 'bible_books.json')))

chapter_list = [(book, chapter + 1)
                for testament in ['OT', 'NT']
                for book in chapter_data[testament]
                for chapter in range(chapter_data[testament][book])]


def get_audio(book, chapter):
    raise NotImplementedError()
