import re
import random as r


class MarsURLEncoder:

    # PATTERN: str = '(http|https):\/\/(.*?)\/'
    hash = 0

    def __init__(self):
        self.link_storage: dict[str: str] = {}

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        short_url = re.search(self.PATTERN, long_url)
        for item in long_url[short_url.span()[1]::5]:
            self.hash += r.randint(1, 10000)
        self.link_storage[str(self.hash)] = long_url
        return long_url[short_url.span()[0]:
                        short_url.span()[1]] + str(self.hash)

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        protocol_domain = re.search(self.PATTERN, short_url)
        hash_short_link = short_url[protocol_domain.span()[1]:]
        return self.link_storage[hash_short_link]

#  (http|https):\/\/(.*?)\/ - regular_expressioin


test = MarsURLEncoder()
short_link = test.encode(('https://tsup.ru/mars/marsohod-1'
                         '/01-09-2023/daily_job.html'))
long_link = test.decode(short_link)
print(short_link)
print(long_link)
