from html.parser import HTMLParser
from html.entities import name2codepoint

class PyHTMLParser(HTMLParser):
    def __init__(self, *, convert_charrefs=True):
        super().__init__()
        self._event_loc_flag = False
        self._event_time_flag = False
        self._event_name_flag = False

    def handle_starttag(self, tag, attrs):
        if 'h3' == tag and len(attrs) > 0 and attrs[0][1] == 'event-title':
            self._event_name_flag = True
        elif 'time' == tag and len(attrs) > 0 and attrs[0][0] == 'datetime':
            self._event_time_flag = True
        elif 'span' == tag and len(attrs) > 0 and attrs[0][1] == 'event-location':
            self._event_loc_flag = True

    def handle_data(self, data):
        if self._event_name_flag:
            print('event name: %s' % data)
        elif self._event_time_flag:
            print('event time: %s' % data)
        elif self._event_loc_flag:
            print('event loc: %s' % data)

    def handle_endtag(self, tag):
        self._event_name_flag = False
        self._event_time_flag = False
        self._event_loc_flag = False


def get_html_content():
    with open('/Users/zhaogao/Downloads/events.html', 'r') as f:
        data = f.read()
    return data


py_parser = PyHTMLParser()
py_parser.feed(get_html_content())