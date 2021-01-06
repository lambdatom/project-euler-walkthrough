from lxml import html, etree
import requests
from string import Template
import os


class Problem:

    _pid_max = 740  # Prevent overzealous scraping

    def __init__(self, pid):
        if isinstance(pid, int) and (0 < pid <= Problem._pid_max):
            self._pid = pid

        self.url = 'https://projecteuler.net/problem=' + str(self._pid)
        self.url_min = 'https://projecteuler.net/minimal=' + str(self._pid)

        self.title = ''
        self.problem_html = ''

    def fetch_info(self):
        headers = {'Content-Type': 'text/html'}
        response = requests.get(self.url, headers=headers)
        if response.ok and len(response.content) > 1000 and 'class="problem_content"' in response.text:
            tree = html.fromstring(response.text)
            self.title = tree.xpath('//div[@id="content"]/h2/text()')[0]
            problem_elem = tree.xpath('//div[@id="content"]//div[@class="problem_content"]')[0]
            self.problem_html = html.tostring(problem_elem).decode('utf-8')
        else:
            raise Exception('Response content missing')

    def generate_md(self):
        self.fetch_info()
        if self.title != '' and self.problem_html != '':
            filename_fmt = 'p{:04d}.md'
            filename = filename_fmt.format(self._pid)
            t = Template('###### $title\n$problem')
            md = t.substitute(title=self.title, problem=self.problem_html)
            with open(os.path.join(os.path.dirname(__file__), 'problems', filename), "w") as f:
                f.write(md)
        else:
            raise Exception('Title or problem data empty')

    def print(self):
        print(self._pid)
        print(self.title)
        print(self.problem_html)

if __name__ == "__main__":
    p1 = Problem(1)
    p1.fetch_info()
    p1.print()
    # p1.generate_md()
