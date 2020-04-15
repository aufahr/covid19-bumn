import inspect
import os
import sys

from datascraper.custom import kabbogor, kabcianjur
from datascraper.model import GenericScraperTemplate, Selectors, SelectorProcessor
from datascraper.util import get_number_only, get_number_only2


all_website = [
    GenericScraperTemplate(region='Kabupaten Bogor',
                           url='https://covid-19.bogorkab.go.id/',
                           exec_type='CUSTOM',
                           call=kabbogor.kab_bogor_call),
    GenericScraperTemplate(region='Kabupaten Sukabumi',
                           url='http://www.pikokami.sukabumikab.go.id/',
                           selectors=
                           Selectors(
                               last_updated_selector=SelectorProcessor(
                                   'body > main > div:nth-child(2) > div:nth-child(3) > div > p'),
                               positive_selector=SelectorProcessor(
                                   'body > main > div:nth-child(2) > div:nth-child(4) > div:nth-child(3) > div > div > h4',
                                   get_number_only),
                               pdp_selector=SelectorProcessor(
                                   'body > main > div:nth-child(2) > div:nth-child(4) > div:nth-child(4) > div > div > h4',
                                   get_number_only),
                               odp_selector=SelectorProcessor(
                                   'body > main > div:nth-child(2) > div:nth-child(4) > div:nth-child(5) > div > div > h4',
                                   get_number_only)
                           )),
    GenericScraperTemplate(region='Kabupaten Cianjur',
                           url='https://covid19.cianjurkab.go.id/',
                           selectors=
                           Selectors(
                               last_updated_selector=SelectorProcessor(
                                   '#post-30 > div > div.fusion-fullwidth.fullwidth-box.fusion-builder-row-2.nonhundred-percent-fullwidth.non-hundred-percent-height-scrolling > div > div > div > div.fusion-text > p'),
                               odp_selector=SelectorProcessor(
                                   './/*[@id="post-30"]/div/div[2]/div/div/div/div[3]/div[1]/div/div[2]/table/tbody/tr[3]/td[2]/h2/strong/span',
                                   get_number_only,
                                   parser_type='lxml'),
                               odp_done_selector=SelectorProcessor(
                                   './/*[@id="post-30"]/div/div[2]/div/div/div/div[3]/div[1]/div/div[2]/table/tbody/tr[2]/td[2]/h2/strong/span',
                                   get_number_only, parser_type='lxml'),
                               pdp_done_selector=SelectorProcessor(
                                   './/*[@id="post-30"]/div/div[2]/div/div/div/div[3]/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/h2/strong/span',
                                   kabcianjur.custom_cianjur_pdp_processor,
                                   parser_type='lxml'
                               ),
                               pdp_death_selector=SelectorProcessor(
                                   './/*[@id="post-30"]/div/div[2]/div/div/div/div[3]/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/h2/strong/span',
                                   get_number_only2,
                                   parser_type='lxml'
                               ),
                               pdp_selector=SelectorProcessor(
                                   './/*[@id="post-30"]/div/div[2]/div/div/div/div[3]/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/h2/strong/span',
                                   parser_type='lxml'
                               ),
                               positive_selector=SelectorProcessor(
                                   './/*[@id="post-30"]/div/div[2]/div/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[1]/td[2]/h2/strong/span',
                                   parser_type='lxml'
                               ),
                               positive_recovered_selector=SelectorProcessor(
                                   './/*[@id="post-30"]/div/div[2]/div/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/h2/strong/span',
                                   parser_type='lxml'
                               ),
                               positive_death_selector=SelectorProcessor(
                                   './/*[@id="post-30"]/div/div[2]/div/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[3]/td[2]/h2/strong/span',
                                   parser_type='lxml'
                               )
                           )),
    GenericScraperTemplate(region='Kabupaten Bandung',
                           url='https://covid19.bandungkab.go.id/',
                           selectors=
                           Selectors(
                              odp_selector=SelectorProcessor(
                                   './/*[@id="statistic"]/div/div[5]/div/div/div/div[1]/h3/span',
                                   get_number_only,
                                   parser_type='lxml'),

                           )),
]

# append project path
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

for web in all_website:
    web.execute()
