import datetime

import requests
from bs4 import BeautifulSoup
from lxml import html


class SelectorProcessor(object):

    def __init__(self, selector, processor=None, parser_type='bs4', attribute=None) -> None:
        super().__init__()
        self.selector = selector
        self.processor = processor
        self.parser_type = parser_type
        self.attribute = attribute

    def process(self, value):
        return self.processor(value)


class Selectors(object):

    def __init__(self,
                 last_updated_selector: SelectorProcessor = None,
                 odp_selector: SelectorProcessor = None,
                 odp_death_selector: SelectorProcessor = None,
                 odp_done_selector: SelectorProcessor = None,
                 total_odp_selector: SelectorProcessor = None,
                 total_pdp_selector: SelectorProcessor = None,
                 total_positive_selector: SelectorProcessor = None,
                 pdp_selector: SelectorProcessor = None,
                 pdp_done_selector: SelectorProcessor = None,
                 pdp_death_selector: SelectorProcessor = None,
                 positive_death_selector: SelectorProcessor = None,
                 positive_selector: SelectorProcessor = None,
                 positive_recovered_selector: SelectorProcessor = None,
                 unknown_recovered_selector: SelectorProcessor = None,
                 unknown_death_selector: SelectorProcessor = None
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

        self.total_odp_selector = total_odp_selector
        self.total_pdp_selector = total_pdp_selector
        self.total_positive_selector = total_positive_selector


class GenericScraperTemplate(object):
    def __init__(self,
                 region,
                 url,
                 selectors: Selectors = None,
                 exec_type='GET',
                 call=None,
                 result_postprocessor=None) -> None:
        super().__init__()
        self.url = url
        self.selectors = selectors
        self.exec_type = exec_type
        self.region = region
        self.call = call
        self.result_postprocessor = result_postprocessor

    def execute(self):
        result = {'scraped_datetime': str(datetime.datetime.now())}
        try:
          if self.exec_type == 'GET':
              site = requests.get(self.url, verify=False)
              for key, selector in self.selectors.__dict__.items():
                  if selector is not None:
                      if selector.parser_type == 'bs4':
                          try:
                              page = BeautifulSoup(site.text, features="lxml")
                              
                              if selector.attribute is None:
                                result[key.replace('_selector', '')] =  page.select_one(selector.selector).get_text()
                              else :
                                result[key.replace('_selector', '')] =  page.select_one(selector.selector).get(selector.attribute)

                              if selector.processor is not None:
                                  result[key.replace('_selector', '')] = selector.processor(
                                      page.select_one(selector.selector).get_text())
                          except Exception as e:
                              result[key.replace('_selector', '')] = str(e)
                      else:
                          try:
                              page = html.fromstring(site.text)
                              result[key.replace('_selector', '')] = page.findall(selector.selector)[0].text
                              if selector.processor is not None:
                                  result[key.replace('_selector', '')] = selector.processor(
                                      page.findall(selector.selector)[0].text)
                          except Exception as e:
                              result[key.replace('_selector', '')] = str(e)
          else:
              result = self.call()
        except Exception as e:
          print(e)

        if self.result_postprocessor is not None:
            result = self.result_postprocessor(result)

        result['region'] = self.region
        result['source_type'] = 'individual_website'
        print("{} : {}".format(self.region, result))
        return result

