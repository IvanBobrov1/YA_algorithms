import random as r
import re


class MarsURLEncoder:
    PATTERN = 'https://ma.rs/'
    # PATTERN_RE: str = '(http|https):\/\/(.*?)\/'

    def __init__(self):
        self.link_storage = {}
        self.hash = 0

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""

        for item in long_url[::5]:
            self.hash += r.randint(1, 10000)
        str_hash = str(self.hash)
        self.link_storage[str_hash] = long_url
        return self.PATTERN + str_hash

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        protocol_domain = re.search(self.PATTERN_RE, short_url)
        hash_short_link = short_url[protocol_domain.span()[1]:]
        return self.link_storage[hash_short_link]


test = MarsURLEncoder()
test1 = MarsURLEncoder()
short_link = test.encode(('https://tsup.ru/mars/marsohod-1'
                         '/01-09-2023/daily_job.html'))
long_link = test.decode(short_link)
print(short_link)
print(long_link)

short_link1 = test1.encode('https://mars-program.ru/all/010923/plan_B.htm')
long_link1 = test1.decode(short_link1)
print(short_link1)
print(long_link1)
