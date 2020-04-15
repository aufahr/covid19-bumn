from custom import kabbogor, kabcianjur, kabgarut, kabsukabumi, kotabandung
from model import GenericScraperTemplate, Selectors, SelectorProcessor
from util import get_number_only, get_number_only2, get_number_only3, get_number_only4, get_date

all_website = [
    GenericScraperTemplate(region='Kabupaten Bogor',
                           url='https://covid-19.bogorkab.go.id/',
                           exec_type='CUSTOM',
                           call=kabbogor.kab_bogor_call),
    GenericScraperTemplate(region='Kabupaten Sukabumi',
                           url='https://covid19.sukabumikota.go.id/new/index.php/welcome/grafik/2',
                           exec_type='CUSTOM',
                           call=kabsukabumi.call
                           ),
    GenericScraperTemplate(region='Kabupaten Cianjur',
                           url='https://covid19.cianjurkab.go.id/',
                           selectors=
                           Selectors(
                               last_updated_selector=SelectorProcessor(
                                   '#post-30 > div > div.fusion-fullwidth.fullwidth-box.fusion-builder-row-2.nonhundred-percent-fullwidth.non-hundred-percent-height-scrolling > div > div > div > div.fusion-text > p',
                               get_date),
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
                               last_updated_selector=SelectorProcessor(
                                   './/*[@id="statistic"]/div/div[1]/p', get_date, parser_type='lxml'),
                               odp_selector=SelectorProcessor(
                                   './/*[@id="statistic"]/div/div[5]/div/div/div/div[1]/h3/span',
                                   get_number_only,
                                   parser_type='lxml'),
                               odp_done_selector=SelectorProcessor(
                                   './/*[@id="statistic"]/div/div[5]/div/div/div/div[2]/h3/span',
                                   parser_type='lxml'),
                               pdp_selector=SelectorProcessor(
                                   './/*[@id="statistic"]/div/div[6]/div/div/div/div[1]/h3/span',
                                   parser_type='lxml'),
                               pdp_done_selector=SelectorProcessor(
                                   './/*[@id="statistic"]/div/div[6]/div/div/div/div[2]/h3/span',
                                   parser_type='lxml'),
                               positive_selector=SelectorProcessor(
                                   './/*[@id="statistic"]/div/div[2]/div/div/div[2]/h4/span[2]',
                                   parser_type='lxml'),
                               positive_recovered_selector=SelectorProcessor(
                                   './/*[@id="statistic"]/div/div[3]/div/div/div[2]/h4/span[2]',
                                   parser_type='lxml'),
                               positive_death_selector=SelectorProcessor(
                                   './/*[@id="statistic"]/div/div[4]/div/div/div[2]/h4/span[2]',
                                   parser_type='lxml')
                           )),
    GenericScraperTemplate(region='Kabupaten Garut',
                           url='https://covid19.garutkab.go.id/',
                           exec_type='CUSTOM',
                           call=kabgarut.call
                           ),
    GenericScraperTemplate(region='Kabupaten Tasikmalaya',
                           url='https://sigesit119.tasikmalayakab.go.id/',
                           exec_type='CUSTOM',
                           call=kabgarut.call
                           ),
    GenericScraperTemplate(region='Kabupaten Ciamis',
                           url='https://pikcovid19.ciamiskab.go.id/',
                           selectors=
                           Selectors(
                               last_updated_selector=SelectorProcessor(
                                   './/*[@id="post-127"]/div/div/div[5]/div/div/div[1]/div/div/div/div/div/p[2]/span/strong/span',
                                   get_date,
                                   parser_type='lxml'),
                               odp_selector=SelectorProcessor(
                                   './/*[@id="post-127"]/div/div/div[5]/div/div/div[2]/div[2]/div/div[1]/div/div/p/span[4]/strong',
                                   get_number_only,
                                   parser_type='lxml'),
                               odp_done_selector=SelectorProcessor(
                                   './/*[@id="post-127"]/div/div/div[5]/div/div/div[2]/div[2]/div/div[1]/div/div/p/span[3]/strong',
                                   get_number_only,
                                   parser_type='lxml'),
                               pdp_selector=SelectorProcessor(
                                   './/*[@id="post-127"]/div/div/div[5]/div/div/div[2]/div[2]/div/div[2]/div/div/p/span[4]/strong',
                                   get_number_only,
                                   parser_type='lxml'),
                               pdp_done_selector=SelectorProcessor(
                                   './/*[@id="post-127"]/div/div/div[5]/div/div/div[2]/div[2]/div/div[2]/div/div/p/span[3]/strong/span[1]',
                                   get_number_only,
                                   parser_type='lxml'),
                               pdp_death_selector=SelectorProcessor(
                                   './/*[@id="post-127"]/div/div/div[5]/div/div/div[2]/div[2]/div/div[2]/div/div/p/span[3]/strong/span[2]',
                                   get_number_only,
                                   parser_type='lxml'),
                               positive_selector=SelectorProcessor(
                                   './/*[@id="post-127"]/div/div/div[5]/div/div/div[2]/div[1]/div/div[1]/div/div/p/span[2]/strong',
                                   get_number_only,
                                   parser_type='lxml'),
                           )),
    GenericScraperTemplate(region='Kabupaten Kuningan',
                           url='http://covid19.kuningankab.go.id/',
                           selectors=
                           Selectors(
                               last_updated_selector=SelectorProcessor(
                                   './/*[@id="block-views-block-dashboard-judul-block-1"]/div/div/div/div/div[1]/p/time',
                                   get_date,
                                   parser_type='lxml'),
                               odp_selector=SelectorProcessor(
                                   './/*[@id="views-bootstrap-dashboard-judul-block-1"]/div/div/div/span/div[1]/div[2]/div/div[2]',
                                   get_number_only,
                                   parser_type='lxml'),
                               odp_done_selector=SelectorProcessor(
                                   './/*[@id="views-bootstrap-dashboard-judul-block-1"]/div/div/div/span/div[1]/div[2]/div/div[2]',
                                   get_number_only2,
                                   parser_type='lxml'),
                               pdp_selector=SelectorProcessor(
                                   './/*[@id="views-bootstrap-dashboard-judul-block-1"]/div/div/div/span/div[2]/div[1]/div/div[2]',
                                   get_number_only,
                                   parser_type='lxml'),
                               pdp_done_selector=SelectorProcessor(
                                   './/*[@id="about"]/div/div/div/div/div/section[7]/div/div/div[2]/div/div/section/div/div/div[2]/div/div/div/div/div/h4/span',
                                   get_number_only,
                                   parser_type='lxml'),
                               positive_selector=SelectorProcessor(
                                   './/*[@id="views-bootstrap-dashboard-judul-block-1"]/div/div/div/span/div[2]/div[2]/div/div[2]',
                                   get_number_only,
                                   parser_type='lxml'),
                               positive_recovered_selector=SelectorProcessor(
                                   './/*[@id="views-bootstrap-dashboard-judul-block-1"]/div/div/div/span/div[2]/div[2]/div/div[2]',
                                   get_number_only3,
                                   parser_type='lxml'),
                               positive_death_selector=SelectorProcessor(
                                   './/*[@id="views-bootstrap-dashboard-judul-block-1"]/div/div/div/span/div[2]/div[2]/div/div[2]',
                                   get_number_only4,
                                   parser_type='lxml'),
                           )),
    GenericScraperTemplate(region='Kabupaten Majalengka',
                           url='https://covid19.majalengkakab.go.id/',
                           selectors=
                           Selectors(
                               last_updated_selector=SelectorProcessor(
                                   './/*[@id="about"]/div/div/div/div/div/section[6]/div/div/div/div/div/div[2]/div/div/h5',
                                   get_date,
                                   parser_type='lxml'),
                               odp_selector=SelectorProcessor(
                                   './/*[@id="about"]/div/div/div/div/div/section[7]/div/div/div[1]/div/div/section/div/div/div[1]/div/div/div/div/div/h4/span',
                                   get_number_only,
                                   parser_type='lxml'),
                               odp_done_selector=SelectorProcessor(
                                   './/*[@id="about"]/div/div/div/div/div/section[7]/div/div/div[1]/div/div/section/div/div/div[2]/div/div/div/div/div/h4/span',
                                   get_number_only,
                                   parser_type='lxml'),
                               pdp_selector=SelectorProcessor(
                                   './/*[@id="about"]/div/div/div/div/div/section[7]/div/div/div[2]/div/div/section/div/div/div[1]/div/div/div/div/div/h4/span',
                                   get_number_only,
                                   parser_type='lxml'),
                               pdp_done_selector=SelectorProcessor(
                                   './/*[@id="about"]/div/div/div/div/div/section[7]/div/div/div[2]/div/div/section/div/div/div[2]/div/div/div/div/div/h4/span',
                                   parser_type='lxml'),
                               positive_selector=SelectorProcessor(
                                   './/*[@id="about"]/div/div/div/div/div/section[7]/div/div/div[3]/div/div/div[3]/div/h2',
                                   get_number_only,
                                   parser_type='lxml'),
                               positive_recovered_selector=SelectorProcessor(
                                   './/*[@id="about"]/div/div/div/div/div/section[7]/div/div/div[3]/div/div/section/div/div/div[2]/div/div/div/div/div/h4/span',
                                   get_number_only,
                                   parser_type='lxml'),
                               positive_death_selector=SelectorProcessor(
                                   './/*[@id="about"]/div/div/div/div/div/section[7]/div/div/div[3]/div/div/section/div/div/div[1]/div/div/div/div/div/h4/span',
                                   get_number_only,
                                   parser_type='lxml'),
                           )),
    GenericScraperTemplate(region='Kabupaten Sumedang',
                           url='http://covid19.sumedangkab.go.id/',
                           selectors=
                           Selectors(
                               odp_selector=SelectorProcessor(
                                   './/*[@id="features"]/div/div[2]/div/div/div/div[1]/li[4]',
                                   get_number_only,
                                   parser_type='lxml'),
                               odp_done_selector=SelectorProcessor(
                                   './/*[@id="features"]/div/div[2]/div/div/div/div[1]/li[3]', get_number_only,
                                   parser_type='lxml'),
                               pdp_selector=SelectorProcessor(
                                   './/*[@id="features"]/div/div[2]/div/div/div/div[3]/li[4]', get_number_only,
                                   parser_type='lxml'),
                               pdp_done_selector=SelectorProcessor(
                                   './/*[@id="features"]/div/div[2]/div/div/div/div[3]/li[3]',
                                   get_number_only,
                                   parser_type='lxml'),
                               positive_selector=SelectorProcessor(
                                   './/*[@id="features"]/div/div[2]/div/div/div/div[4]/li[1]', get_number_only,
                                   parser_type='lxml'),
                           )),
    GenericScraperTemplate(region='Kabupaten Indramayu',
                           url='http://covid19.indramayukab.go.id/',
                           selectors=
                           Selectors(
                               last_updated_selector=SelectorProcessor(
                                   './/*[@id="data"]/div/div/div/div[1]', get_date, parser_type='lxml'),
                               odp_selector=SelectorProcessor(
                                   './/*[@id="counter"]/div[3]/div',
                                   get_number_only,
                                   parser_type='lxml'),
                               odp_done_selector=SelectorProcessor(
                                   './/*[@id="counter"]/div[3]/p[2]', get_number_only,
                                   parser_type='lxml'),
                               pdp_selector=SelectorProcessor(
                                   './/*[@id="counter"]/div[2]/div', get_number_only,
                                   parser_type='lxml'),
                               pdp_death_selector=SelectorProcessor(
                                   './/*[@id="counter"]/div[2]/p[2]',
                                   get_number_only,
                                   parser_type='lxml'),
                               pdp_done_selector=SelectorProcessor(
                                   '#counter > div:nth-child(2) > p:nth-child(4)',
                                   get_number_only2),
                               positive_selector=SelectorProcessor(
                                   './/*[@id="counter"]/div[1]/div', get_number_only,
                                   parser_type='lxml'),
                               positive_death_selector=SelectorProcessor(
                                   '#counter > div:nth-child(1) > p:nth-child(4)', get_number_only,
                               ),
                               positive_recovered_selector=SelectorProcessor(
                                   '#counter > div:nth-child(1) > p:nth-child(4)', get_number_only2),
                           )),
    GenericScraperTemplate(region='Kabupaten Subang',
                           url='https://covid19.subang.go.id/',
                           selectors=
                           Selectors(
                               last_updated_selector=SelectorProcessor(
                                   'body > div.hlt_whitebg.hlt_wedo > div > div > div.col-lg-12.col-md-12.col-sm-12.col-xs-12 > div > p'),
                               positive_selector=SelectorProcessor(
                                   'body > div.hlt_whitebg.hlt_wedo > div > div > div:nth-child(2) > div > p > b'),
                               positive_recovered_selector=SelectorProcessor(
                                   'body > div.hlt_whitebg.hlt_wedo > div > div > div:nth-child(3) > div > p > b'),
                               positive_death_selector=SelectorProcessor(
                                   'body > div.hlt_whitebg.hlt_wedo > div > div > div:nth-child(4) > div > p > b'),
                               odp_selector=SelectorProcessor('.hlt_about_info > table > tr:nth-child(2)',
                                                              get_number_only),
                               odp_done_selector=SelectorProcessor('.hlt_about_info > table > tr:nth-child(2)',
                                                                   get_number_only2),
                               pdp_selector=SelectorProcessor(
                                   'body > div.hlt_grayebg.hlt_about > div > div > div:nth-child(2) > div:nth-child(4) > table > tr:nth-child(2)',
                                   get_number_only),
                               pdp_done_selector=SelectorProcessor(
                                   'body > div.hlt_grayebg.hlt_about > div > div > div:nth-child(2) > div:nth-child(4) > table > tr:nth-child(2)',
                                   get_number_only2),
                           )
                           ),
    GenericScraperTemplate(region='Kabupaten Karawang',
                           url='https://covid19.karawangkab.go.id/',
                           selectors=
                           Selectors(
                               last_updated_selector=SelectorProcessor(
                                   './/*[@id="peta"]/div/div/div/div/div[2]/p[2]', get_date, parser_type='lxml'),
                               odp_selector=SelectorProcessor(
                                   './/*[@id="peta"]/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/p[1]',
                                   get_number_only,
                                   parser_type='lxml'),
                               odp_done_selector=SelectorProcessor(
                                   './/*[@id="peta"]/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/p[2]',
                                   get_number_only,
                                   parser_type='lxml'),
                               pdp_selector=SelectorProcessor(
                                   './/*[@id="peta"]/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/p[1]',
                                   get_number_only,
                                   parser_type='lxml'),
                               pdp_death_selector=SelectorProcessor(
                                   './/*[@id="peta"]/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/p[3]',
                                   get_number_only,
                                   parser_type='lxml'),
                               pdp_done_selector=SelectorProcessor(
                                   './/*[@id="peta"]/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/p[2]',
                                   get_number_only,
                                   parser_type='lxml'),
                               positive_selector=SelectorProcessor(
                                   './/*[@id="peta"]/div/div/div/div/div[2]/div[2]/div[3]/div/div[2]/p[1]',
                                   get_number_only,
                                   parser_type='lxml'),
                               positive_death_selector=SelectorProcessor(
                                   './/*[@id="peta"]/div/div/div/div/div[2]/div[2]/div[3]/div/div[2]/p[3]',
                                   get_number_only,
                                   parser_type='lxml'),
                               positive_recovered_selector=SelectorProcessor(
                                   './/*[@id="peta"]/div/div/div/div/div[2]/div[2]/div[3]/div/div[2]/p[2]',
                                   get_number_only,
                                   parser_type='lxml')
                           )),
    GenericScraperTemplate(region='Kota Bandung',
                           url='https://covid19.bandung.go.id/',
                           exec_type='CUSTOM',
                           call=kotabandung.call
                           ),
    GenericScraperTemplate(region='Kota Cirebon',
                           url='http://covid19.cirebonkota.go.id/',
                           selectors=
                           Selectors(
                               last_updated_selector=SelectorProcessor(
                                   './/*[@id="beranda"]/div/div/div[6]/p', get_date, parser_type='lxml'),
                               odp_selector=SelectorProcessor(
                                   './/*[@id="beranda"]/div/div/div[5]/div/div[2]/div/div[2]/div[2]/div[1]/h5',
                                   parser_type='lxml'),
                               odp_done_selector=SelectorProcessor(
                                   './/*[@id="beranda"]/div/div/div[5]/div/div[2]/div/div[2]/div[2]/div[2]/h5',
                                   parser_type='lxml'),
                               pdp_selector=SelectorProcessor(
                                   './/*[@id="beranda"]/div/div/div[5]/div/div[3]/div/div[2]/div[2]/div[1]/h5',
                                   parser_type='lxml'),
                               pdp_done_selector=SelectorProcessor(
                                   './/*[@id="beranda"]/div/div/div[5]/div/div[3]/div/div[2]/div[2]/div[2]/h5',
                                   parser_type='lxml'),
                               positive_selector=SelectorProcessor(
                                   './/*[@id="beranda"]/div/div/div[5]/div/div[4]/div/div[2]/div[2]/div[1]/h5',
                                   parser_type='lxml'),
                               positive_death_selector=SelectorProcessor(
                                   './/*[@id="beranda"]/div/div/div[5]/div/div[4]/div/div[2]/div[3]/div/h5',
                                   parser_type='lxml'),
                               positive_recovered_selector=SelectorProcessor(
                                   './/*[@id="beranda"]/div/div/div[5]/div/div[4]/div/div[2]/div[2]/div[2]/h5',
                                   parser_type='lxml')
                           )),
    GenericScraperTemplate(region='Kota Depok',
                           url='https://ccc-19.depok.go.id/',
                           selectors=
                           Selectors(
                               last_updated_selector=SelectorProcessor(
                                   './/*[@id="content"]/main/section/div/div[2]/div[1]/h5', parser_type='lxml'),
                               odp_selector=SelectorProcessor(
                                   './/*[@id="content"]/main/section/div/div[2]/div[6]/div/div[2]/div/div[1]/h4',
                                   get_number_only,
                                   parser_type='lxml'),
                               odp_done_selector=SelectorProcessor(
                                   './/*[@id="content"]/main/section/div/div[2]/div[6]/div/div[2]/div/div[2]/h4',
                                   get_number_only,
                                   parser_type='lxml'),
                               pdp_selector=SelectorProcessor(
                                   './/*[@id="content"]/main/section/div/div[2]/div[5]/div/div[2]/div/div[1]/h4',
                                   get_number_only,
                                   parser_type='lxml'),
                               pdp_done_selector=SelectorProcessor(
                                   './/*[@id="content"]/main/section/div/div[2]/div[5]/div/div[2]/div/div[2]/h4',
                                   get_number_only,
                                   parser_type='lxml'),
                               total_positive_selector=SelectorProcessor(
                                   './/*[@id="content"]/main/section/div/div[2]/div[2]/div/div[2]/h2',
                                   get_number_only,
                                   parser_type='lxml'),
                               positive_death_selector=SelectorProcessor(
                                   './/*[@id="content"]/main/section/div/div[2]/div[4]/div/div[2]/h2',
                                   get_number_only,
                                   parser_type='lxml'
                               ),
                               positive_recovered_selector=SelectorProcessor(
                                   './/*[@id="content"]/main/section/div/div[2]/div[3]/div/div[2]/h2', get_number_only,
                                   parser_type='lxml'
                               ),
                           )),
    GenericScraperTemplate(region='Kota Cimahi',
                           url='https://covid19.cimahikota.go.id/',
                           selectors=
                           Selectors(
                               last_updated_selector=SelectorProcessor(
                                   'body > div.wrapper-boxed > div.site-wrapper > section.sec-padding.section-light > div > div > div:nth-child(3) > div > p',
                                   get_date),
                               odp_selector=SelectorProcessor(
                                   'body > div.wrapper-boxed > div.site-wrapper > section.sec-padding.section-light > div > div > div:nth-child(3) > div > h6:nth-child(4)',
                                   get_number_only),
                               odp_done_selector=SelectorProcessor(
                                   'body > div.wrapper-boxed > div.site-wrapper > section.sec-padding.section-light > div > div > div:nth-child(3) > div > h6:nth-child(5)',
                                   get_number_only),
                               pdp_selector=SelectorProcessor(
                                   'body > div.wrapper-boxed > div.site-wrapper > section.sec-padding.section-light > div > div > div:nth-child(4) > div > h6:nth-child(4)',
                                   get_number_only, ),
                               pdp_done_selector=SelectorProcessor(
                                   'body > div.wrapper-boxed > div.site-wrapper > section.sec-padding.section-light > div > div > div:nth-child(4) > div > h6:nth-child(5)',
                                   get_number_only),
                               positive_selector=SelectorProcessor(
                                   'body > div.wrapper-boxed > div.site-wrapper > section.sec-padding.section-light > div > div > div:nth-child(5) > div > h6:nth-child(4)',
                                   get_number_only),
                               positive_death_selector=SelectorProcessor(
                                   'body > div.wrapper-boxed > div.site-wrapper > section.sec-padding.section-light > div > div > div:nth-child(5) > div > h6:nth-child(6)',
                                   get_number_only,
                               ),
                               positive_recovered_selector=SelectorProcessor(
                                   'body > div.wrapper-boxed > div.site-wrapper > section.sec-padding.section-light > div > div > div:nth-child(5) > div > h6:nth-child(5)',
                                   get_number_only
                               ),
                           )),
    GenericScraperTemplate(region='Kota Tasikmalaya',
                           url='http://mikotas.tasikmalayakota.go.id/',
                           selectors=
                           Selectors(
                               last_updated_selector=SelectorProcessor(
                                   './/*[@id="main"]/div/h2[2]', get_date,
                                   parser_type='lxml'),
                               odp_selector=SelectorProcessor(
                                   '#services > div > div > div:nth-child(2) > div > p',
                                   get_number_only3),
                               odp_done_selector=SelectorProcessor(
                                   '#services > div > div > div:nth-child(2) > div > p',
                                   get_number_only2),
                               pdp_selector=SelectorProcessor(
                                   '#services > div > div > div.col-lg-4.col-md-8 > div > p', get_number_only3),
                               pdp_done_selector=SelectorProcessor(
                                   '#services > div > div > div.col-lg-4.col-md-8 > div > p',
                                   get_number_only2),
                               pdp_death_selector=SelectorProcessor(
                                   '#services > div > div > div.col-lg-4.col-md-8 > div > p',
                                   get_number_only4),
                               positive_selector=SelectorProcessor(
                                   './/*[@id="center"]/div/p/b[1]',
                                   parser_type='lxml'),
                               positive_death_selector=SelectorProcessor(
                                   './/*[@id="center"]/div/p/b[3]',
                                   parser_type='lxml'),
                               positive_recovered_selector=SelectorProcessor(
                                   './/*[@id="center"]/div/p/b[2]',
                                   parser_type='lxml'),
                           )),
    GenericScraperTemplate(region='Kota Bogor',
                           url='http://covid19.kotabogor.go.id/',
                           selectors=
                           Selectors(
                               last_updated_selector=SelectorProcessor(
                                   'body > div:nth-child(3) > div:nth-child(2) > div.col-md-9 > div:nth-child(2) > div.panel-heading.head.bluedark > strong > b:nth-child(1)',
                               get_date),
                               odp_selector=SelectorProcessor(
                                   'body > div:nth-child(3) > div:nth-child(2) > div.col-md-9 > div:nth-child(2) > div.panel-body > div > div > div:nth-child(8) > div > div.inner > h3'),
                               odp_done_selector=SelectorProcessor(
                                   'body > div:nth-child(3) > div:nth-child(2) > div.col-md-9 > div:nth-child(2) > div.panel-body > div > div > div:nth-child(7) > div > div.inner > h3'),
                               pdp_selector=SelectorProcessor(
                                   'body > div:nth-child(3) > div:nth-child(2) > div.col-md-9 > div:nth-child(2) > div.panel-body > div > div > div:nth-child(13) > div > div.inner > h3'),
                               pdp_death_selector=SelectorProcessor(
                                   'body > div:nth-child(3) > div:nth-child(2) > div.col-md-9 > div:nth-child(2) > div.panel-body > div > div > div:nth-child(14) > div > div.inner > h3'),
                               pdp_done_selector=SelectorProcessor(
                                   'body > div:nth-child(3) > div:nth-child(2) > div.col-md-9 > div:nth-child(2) > div.panel-body > div > div > div:nth-child(12) > div > div.inner > h3'),
                               positive_selector=SelectorProcessor(
                                   'body > div:nth-child(3) > div:nth-child(2) > div.col-md-9 > div:nth-child(2) > div.panel-body > div > div > div:nth-child(18) > div > div.inner > h3'),
                               positive_death_selector=SelectorProcessor(
                                   'body > div:nth-child(3) > div:nth-child(2) > div.col-md-9 > div:nth-child(2) > div.panel-body > div > div > div:nth-child(19) > div > div.inner > h3'),
                               positive_recovered_selector=SelectorProcessor(
                                   'body > div:nth-child(3) > div:nth-child(2) > div.col-md-9 > div:nth-child(2) > div.panel-body > div > div > div:nth-child(17) > div > div.inner > h3')
                           )),
]
