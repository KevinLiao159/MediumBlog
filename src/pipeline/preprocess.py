import unicodedata
import pandas as pd


class MediumBlogPost:
    """
    data object for parsing json file into proper format
    """
    def __init__(self, **kwargs):
        self.title = self.__text_normalize(kwargs['title'])
        self.publish_time = pd.Timestamp(kwargs['publish_time'])
        self.author = self.__text_normalize(kwargs['author'])
        self.url = kwargs['url']
        self.author_url = kwargs['author_url']
        self.headings = self.__text_normalize(kwargs['headings'])
        self.contents = self.__text_normalize(kwargs['contents'])
        self.mins_read = int(kwargs['mins_read'])
        self.claps = int(kwargs['claps'])
        self.lang = kwargs['lang']
        self.tags = list(kwargs['tags'])

    def __text_normalize(self, text):
        """
        1. unicode string normalization
        2. replace semi-colon with space
        """
        return unicodedata.normalize('NFKD', text).replace(';', ' ')

    def to_dict(self):
        return {
            'title': self.title,
            'publish_time': self.publish_time,
            'author': self.author,
            'url': self.url,
            'author_url': self.author_url,
            'headings': self.headings,
            'contents': self.contents,
            'mins_read': self.mins_read,
            'claps': self.claps,
            'lang': self.lang,
            'tags': self.tags}

    def to_frame(self):
        return pd.DataFrame({k: [v] for k, v in self.to_dict().items()})

