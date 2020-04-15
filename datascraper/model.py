import datetime

import requests
from bs4 import BeautifulSoup
from lxml import html


class SelectorProcessor(object):

    def __init__(self, selector, processor=None, parser_type='bs4') -> None:
        super().__init__()
        self.selector = selector
        self.processor = processor
        self.parser_type = parser_type

    def process(self, value):
        return self.processor(value)


class Selectors(object):

    def __init__(self,
                 last_updated_selector: SelectorProcessor = None,
                 odp_selector: SelectorProcessor = None,
                 odp_death_selector: SelectorProcessor = None,
                 odp_done_selector: SelectorProcessor = None,
                 pdp_selector: SelectorProcessor = None,
                 pdp_done_selector: SelectorProcessor = None,
                 pdp_death_selector: SelectorProcessor = None,
                 positive_death_selector: SelectorProcessor = None,
                 positive_selector: SelectorProcessor = None,
                 positive_recovered_selector: SelectorProcessor = None,
                 unknown_recovered_selector: SelectorProcessor = None,
                 unknown_death_selector: SelectorProcessor = None,
                 ) -> None:
        super().__init__()
        self.last_updated_selector = last_updated_selector
        self.odp_selector = odp_selector
        self.odp_death_selector = odp_death_selector
        self.odp_done_selector = odp_done_selector
        self.pdp_selector = pdp_selector
        self.pdp_done_selector = pdp_done_selector
        self.pdp_death_selector = pdp_death_selector
        self.positive_selector = positive_selector
        self.positive_recovered_selector = positive_recovered_selector
        self.positive_death_selector = positive_death_selector
        self.unknown_recovered_selector = unknown_recovered_selector
        self.unknown_death_selector = unknown_death_selector


class GenericScraperTemplate(object):
    def __init__(self,
                 region,
                 url,
                 selectors: Selectors = None,
                 exec_type='GET',
                 call=None) -> None:
        super().__init__()
        self.url = url
        self.selectors = selectors
        self.exec_type = exec_type
        self.region = region
        self.call = call

    def execute(self):
        result = {'scraped_datetime': str(datetime.datetime.now())}

        if self.exec_type is 'GET':
            site = requests.get(self.url)
            for key, selector in self.selectors.__dict__.items():
                if selector is not None:

                    if selector.parser_type is 'bs4':
                        try:
                            page = BeautifulSoup(site.text, features="lxml")
                            result[key.replace('_selector', '')] = page.select_one(selector.selector).get_text()
                            if selector.processor is not None:
                                result[key.replace('_selector', '')] = selector.processor(
                                    page.select_one(selector.selector).get_text())
                        except Exception as e:
                            result[key.replace('_selector', '')] = e
                    else:
                        try:
                            page = html.fromstring(site.text)
                            result[key.replace('_selector', '')] = page.findall(selector.selector)[0].text
                            if selector.processor is not None:
                                result[key.replace('_selector', '')] = selector.processor(
                                    page.findall(selector.selector)[0].text)
                        except Exception as e:
                            result[key.replace('_selector', '')] = e
        else:
            result = self.call()

        print(result)
        return result

