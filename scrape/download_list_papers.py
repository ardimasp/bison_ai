# conda activate bison_ai

import pandas as pd
import requests

# filename list of binus authors csv
filename = "Scopus-Author-Binus.csv"

# read csv
data = pd.read_csv(filename)

# get the author id
list_author_id = list(data.get("Auth-ID"))

for counter, author_id in enumerate(list_author_id):

    cookies = {
        '__cfduid': 'd89d782ef96be25e2b79f59d8a321f3501611217086',
        'SCSessionID': '262E89D019419F381D695DCA761F4AD4.i-0d61c06fbe36b7c78',
        'scopusSessionUUID': '24d9135e-6e59-4bcd-8',
        'scopus.machineID': '3A54504250C34BA87775588E55B51157.i-0accf13bc2c18d026',
        'AWSELB': 'CB9317D502BF07938DE10C841E762B7A33C19AADB1CD1E2BB281380ED740528C8114C6EA23B53CC4DBEEE3FF9C297CC93C02AFF8FCBAFDF2ADE925350150D7900CAD0CA8A6D7CF60659819A50F643C04A93FF864D7',
        'AT_CONTENT_COOKIE': 'FEATURE_HOMEPAGE_MICRO_UI:1,',
        'AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg': '359503849%7CMCIDTS%7C18649%7CMCMID%7C76362689679856960490123798266936320297%7CMCAID%7CNONE%7CMCOPTOUT-1611288661s%7CNONE%7CMCAAMLH-1611886261%7C3%7CMCAAMB-1611886261%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-18656%7CMCCIDH%7C-1142068974%7CvVersion%7C5.0.1',
        'mbox': 'PC#bab85c927e2543a28ba412760ce00b87.36_0#1674526268|session#e273817a45fc4f768b753db56a587ed8#1611283302',
        'at_check': 'true',
        'AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg': '1',
        's_pers': '%20v8%3D1611281484213%7C1705889484213%3B%20v8_s%3DLess%2520than%25201%2520day%7C1611283284213%3B%20c19%3Dsc%253Arecord%253Aauthor%2520details%7C1611283284215%3B%20v68%3D1611281466590%7C1611283284216%3B',
        's_sess': '%20s_cpc%3D0%3B%20e78%3Daffil%2520%2528bina%2520nusantara%2529%3B%20c21%3Daf--id%252860103610%2529%2520%2526%2520autafnameidbina%2520nusantara%2520university%252360103610t%3B%20e13%3D%253A1%3B%20c13%3Daffiliation%2520%2528a-z%2529%3B%20c7%3Daffilname%253Dbina%2520nusantara%2520university%252360103610%3B%20s_cc%3Dtrue%3B%20s_sq%3Delsevier-sc-prod%25252Celsevier-global-prod%253D%252526c.%252526a.%252526activitymap.%252526page%25253Dsc%2525253Arecord%2525253Aauthor%25252520details%252526link%25253Don%252526region%25253DotherInformationCheckboxes%252526pageIDType%25253D1%252526.activitymap%252526.a%252526.c%252526pid%25253Dsc%2525253Arecord%2525253Aauthor%25252520details%252526pidt%25253D1%252526oid%25253Dfunctiononclick%25252528event%25252529%2525257BselectDeselectCheckBoxs%25252528this%25252529%2525257D%252526oidt%25253D2%252526ot%25253DCHECKBOX%3B%20s_ppvl%3Dsc%25253Asearch%25253Aauthor%252520results%252C27%252C27%252C1164%252C1440%252C826%252C1440%252C900%252C2%252CP%3B%20e41%3D1%3B%20s_ppv%3Dsc%25253Arecord%25253Aauthor%252520details%252C44%252C44%252C1458%252C1440%252C826%252C1440%252C900%252C2%252CP%3B',
        '__cfruid': 'c2e74e0b20c4060268d5aba178d41aabd65fde8d-1611222071',
    }

    headers = {
        'Host': 'www.scopus.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0',
    }

    params = (
        ('oneClickExport', '{"Format":"CSV","SelectedFields":" Authors  AuthorIds  Title  Year  EID  SourceTitle  Volume Issue ArtNo PageStart PageEnd PageCount  CitedBy  DocumentType Source  PublicationStage  DOI  OPENACCESS  Affiliations  ISSN ISBN CODEN  PubMedID  Publisher  Editors  LanguageOfOriginalDocument  CorrespondenceAddress  AbbreviatedSourceTitle  Abstract  AuthorKeywords  IndexKeywords  Number  Acronym  Sponsor  Text  Manufacturers Traden ames  ChemicalsCAS MolecularSequenceNumbers  ConferenceName ConferenceDate ConferenceLocation ConferenceCode Sponsors  References Link ","View":"SpecifyFields"}'),
        ('origin', 'AuthorProfile'),
        ('zone', 'exportDropDown'),
        ('dataCheckoutTest', 'false'),
        ('sort', 'plf-f'),
        ('tabSelected', 'docLi'),
        ('authorId', author_id),
        ('txGid', '66c06e94c9c7306d8056514c411c8cf2'),
    )
        # ('authorId', '24536664300'),

    response = requests.get('https://www.scopus.com/onclick/export.uri', headers=headers, params=params, cookies=cookies, allow_redirects=True)

    if not response.ok:
        print("Break at counter: "+str(counter)+", Auth-ID:" + str(author_id))
        break

    print("counter: "+str(counter)+", Auth-ID:" + str(author_id))
    open('./document_list/'+str(author_id)+'.csv', 'wb').write(response.content)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.scopus.com/onclick/export.uri?oneClickExport=%7b%22Format%22%3a%22CSV%22%2c%22SelectedFields%22%3a%22+Authors++AuthorIds++Title++Year++EID++SourceTitle++Volume+Issue+ArtNo+PageStart+PageEnd+PageCount++CitedBy++DocumentType+Source++PublicationStage++DOI++OPENACCESS++Affiliations++ISSN+ISBN+CODEN++PubMedID++Publisher++Editors++LanguageOfOriginalDocument++CorrespondenceAddress++AbbreviatedSourceTitle++Abstract++AuthorKeywords++IndexKeywords++Number++Acronym++Sponsor++Text++Manufacturers+Traden ames++ChemicalsCAS+MolecularSequenceNumbers++ConferenceName+ConferenceDate+ConferenceLocation+ConferenceCode+Sponsors++References+Link+%22%2c%22View%22%3a%22SpecifyFields%22%7d&origin=AuthorProfile&zone=exportDropDown&dataCheckoutTest=false&sort=plf-f&tabSelected=docLi&authorId=24536664300&txGid=66c06e94c9c7306d8056514c411c8cf2', headers=headers, cookies=cookies)
