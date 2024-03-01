import requests
from bs4 import BeautifulSoup

LOGIN_PAGE_URL = 'http://scistudent.eps.zu.edu.eg/(X(1)S(ocgyf1qhaxaijvus5aa0fsg4))/Views/StudentViews/StudentLogin'


def loginPage(id, code):
    ispaid = True
    html = requests.post(
        LOGIN_PAGE_URL
    ).text
    soup = BeautifulSoup(html, 'html.parser')
    viewstate_input = soup.find('input', {'name': '__VIEWSTATE'})
    viewstate_value = viewstate_input['value']
    viewstate_generator_input = soup.find(
        'input', {'name': '__VIEWSTATEGENERATOR'})
    event_validation_input = soup.find('input', {'name': '__EVENTVALIDATION'})
    viewstate_generator_value = viewstate_generator_input['value']
    event_validation_value = event_validation_input['value']

    headers = {
        'Host': 'scistudent.eps.zu.edu.eg',
        'Content-Length': '506',
        'Cache-Control': 'no-cache',
        'X-Requested-With': 'XMLHttpRequest',
        'X-MicrosoftAjax': 'Delta=true',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Origin': 'http://scistudent.eps.zu.edu.eg',
        'Referer': LOGIN_PAGE_URL,
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'close',
    }

    data = {
        'ctl00': 'upnlLogin|LinkButton2',
        '__EVENTTARGET': 'LinkButton2',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': f'{viewstate_value}',
        '__VIEWSTATEGENERATOR': f'{viewstate_generator_value}',
        '__EVENTVALIDATION': f'{event_validation_value}',
        'loginCode': f'{code}',
        'loginPassword': f'{id}',
        '__ASYNCPOST': 'true',
    }

    response = requests.post(LOGIN_PAGE_URL, headers=headers, data=data)
    headers2 = {
        'Host': 'scistudent.eps.zu.edu.eg',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Referer': 'http://scistudent.eps.zu.edu.eg/(X(1)S(ocgyf1qhaxaijvus5aa0fsg4))/Views/StudentViews/Landing',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': f"{ response.headers['Set-Cookie'] }",
        'Connection': 'close',
    }

    response2 = requests.get(
        "http://scistudent.eps.zu.edu.eg/(X(1)S(ocgyf1qhaxaijvus5aa0fsg4))/Views/StudentViews/ESubjectsExams", headers=headers2)

    soup = BeautifulSoup(response2.text, 'html.parser')
    dv_subjects = soup.find('div', {'id': 'ContentPlaceHolder1_dvSubjects'})
    search_form = soup.find('div', {'id': 'ContentPlaceHolder1_SearchForm'})

    input_values = {}
    subject_names = []
    # Loop through each tr element
    try:
        for tr in dv_subjects.find_all('tr'):
            td_subject_name = tr.find_all('td')
            if len(td_subject_name) > 4:
                name = td_subject_name[4].get_text(strip=True)
                subject_names.append(name)
    except:
        subject_names = []
    if "ContentPlaceHolder1_divMessage" in response2.text:
        ispaid = False
    if search_form:
        txt_phase = search_form.find(
            'input', {'id': 'ContentPlaceHolder1_txtPhase'})

        if txt_phase:
            input_values['txtPhase'] = txt_phase.get('value')

        txt_full_name = search_form.find(
            'input', {'id': 'ContentPlaceHolder1_txtFullName'})
        if txt_full_name:
            input_values['txtFullName'] = txt_full_name.get('value')

        txt_code = search_form.find(
            'input', {'id': 'ContentPlaceHolder1_txtCode'})
        if txt_code:
            input_values['txtCode'] = txt_code.get('value')
    return {
        "fullName": input_values['txtFullName'],
        "code": input_values['txtCode'],
        "level": input_values['txtPhase'],
        "subjectsName": subject_names,
        "BooksPaid": ispaid
    }
