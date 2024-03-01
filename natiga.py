import requests
from bs4 import BeautifulSoup
from flask import jsonify
import time


def get_natiga(ID, code):
    general_total_number = []
    general_total_percent = []
    general_total_deg_char = []
    general_total_gpa = []
    general_total_hours = []
    divs_hash_list = []
    divs_code_list = []
    divs_name_list = []
    divs_max_list = []
    divs_min_list = []
    divs_hours_list = []
    divs_points_list = []
    divs_degree_num_list = []
    divs_degree_txt_list = []
    divs_done_list = []
    term_total_list = []
    term_percent_list = []
    term_gpa_list = []
    term_hours_list = []

    while True:
        try:
            res = requests.post(
                'https://studentactivities.zu.edu.eg/Students/Registration/ed_login.aspx'
            )
            html = res.text
            soup = BeautifulSoup(html, 'html.parser')
            viewstate_input = soup.find('input', {'name': '__VIEWSTATE'})
            viewstate_value = viewstate_input['value']
            viewstate_generator_input = soup.find('input',
                                                  {'name': '__VIEWSTATEGENERATOR'})
            event_validation_input = soup.find(
                'input', {'name': '__EVENTVALIDATION'})
            viewstate_generator_value = viewstate_generator_input['value']
            event_validation_value = event_validation_input['value']
            cookies = res.cookies

            cookie_strings = []

            for cookie in cookies:
                cookie_strings.append(f"{cookie.name}={cookie.value}")

            url = "https://studentactivities.zu.edu.eg/Students/Registration/ed_login.aspx"

            headers = {
                "cookie": f"{cookie_strings[0]}",
                "content-length": "1022",
                "sec-ch-ua": '"Chromium";v="121", "Not A(Brand";v="99"',
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "cache-control": "no-cache",
                "x-microsoftajax": "Delta=true",
                "sec-ch-ua-mobile": "?0",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36",
                "sec-ch-ua-platform": '"Windows"',
                "accept": "*/*",
                "origin": "https://studentactivities.zu.edu.eg",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://studentactivities.zu.edu.eg/Students/Registration/ed_login.aspx",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "priority": "u=1, i"
            }

            # Form data
            data = {
                "ctl00$ScriptManager1": "ctl00$cntphmaster$panal1|ctl00$cntphmaster$btn_Login",
                "ctl00$cntphmaster$txt_StudCode": f"{code}",
                "ctl00$cntphmaster$txt_Nationalnum": f"{ID}",
                "__LASTFOCUS": "",
                "__EVENTTARGET": "",
                "__EVENTARGUMENT": "",
                "__VIEWSTATE": f"{viewstate_value}",
                "__VIEWSTATEGENERATOR": f"{viewstate_generator_value}",
                "__EVENTVALIDATION": f"{event_validation_value}",
                "__ASYNCPOST": "true",
                "ctl00$cntphmaster$btn_Login": "تسجيل دخول",
            }

            response = requests.post(url, headers=headers, data=data)

            url1 = "https://studentactivities.zu.edu.eg/Students/Registration/ED/OR_MAIN_PAGE.aspx"
            headers1 = {
                "cookie": f"{cookie_strings[0]}",
                "content-length": "1522",
                "sec-ch-ua": '"Chromium";v="121", "Not A(Brand";v="99"',
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "cache-control": "no-cache",
                "x-microsoftajax": "Delta=true",
                "sec-ch-ua-mobile": "?0",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36",
                "sec-ch-ua-platform": '"Windows"',
                "accept": "*/*",
                "origin": "https://studentactivities.zu.edu.eg",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://studentactivities.zu.edu.eg/Students/Registration/ED/OR_MAIN_PAGE.aspx",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "priority": "u=1, i"
            }

            data1 = {
                "ctl00$ScriptManager1": "ctl00$paneltbl|ctl00$lbDET_ACAD_SHEET_AR",
                "__EVENTTARGET": "ctl00$lbDET_ACAD_SHEET_AR",
                "__EVENTARGUMENT": "",
                "__VIEWSTATE": f"{viewstate_value}",
                "__VIEWSTATEGENERATOR": f"{viewstate_generator_value}",
                "__EVENTVALIDATION": f"{event_validation_value}",
                "__ASYNCPOST": "true",
            }

            response1 = requests.post(url1, headers=headers1, data=data1)

            url2 = "https://studentactivities.zu.edu.eg/Students/Registration/ED/DET_ACAD_SHEET_AR.aspx"
            headers2 = {

                "cookie": f"{cookie_strings[0]}",
                "sec-ch-ua": '"Chromium";v="121", "Not A(Brand";v="99"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "navigate",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "document",
                "referer": "https://studentactivities.zu.edu.eg/Students/Registration/ED/OR_MAIN_PAGE.aspx",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "priority": "u=0, i"
            }

            response2 = requests.get(url2, headers=headers2)
            response2.raise_for_status()  # Raise an HTTPError for bad responses

            soup2 = BeautifulSoup(response2.text, 'html.parser')
            iframe_tag = soup2.find('iframe')
            src_attribute_value = iframe_tag.get('src')
            GetnategaUrl = "https://studentactivities.zu.edu.eg" + src_attribute_value

            # If the request is successful, break out of the loop
            break
        except Exception as e:
            print(e)
            time.sleep(5)

    url3 = GetnategaUrl

    headers3 = {
        "cookie": f"{cookie_strings[0]}",
        "sec-ch-ua": '"Chromium";v="121", "Not A(Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "navigate",
        "sec-fetch-dest": "frame",
        "referer": "https://studentactivities.zu.edu.eg/Students/Reserved.ReportViewerWebControl.axd?OpType=DocMapReport&ClientController=ClientControllerctl00_cntphmaster_UmisReportViewer&ReportUrl=%2fStudents%2fReserved.ReportViewerWebControl.axd%3fReportSession%3d5nydqemcxz451tvuxljbxdef%26ControlID%3d1dbdfec0c1574548aa49a29e8dc6bd8d%26Culture%3d3073%26UICulture%3d3073%26ReportStack%3d1%26OpType%3dReportArea%26Controller%3dClientControllerctl00_cntphmaster_UmisReportViewer%26PageNumber%3d1%26ZoomMode%3dPercent%26ZoomPct%3d100%26ReloadDocMap%3dtrue%26SearchStartPage%3d0%26LinkTarget%3d_top",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "priority": "u=0, i",
    }

    response3 = requests.get(url3, headers=headers3)
    natigaUrl = ""
    soup3 = BeautifulSoup(response3.text, 'html.parser')
    frame_tag = soup3.find('frame', id='report')
    if frame_tag:
        src1_attribute_value = frame_tag.get('src')
        natigaUrl = "https://studentactivities.zu.edu.eg"+src1_attribute_value
    else:
        print("No frame tag with id 'report' found.")

    headers4 = {
        "cookie": f"{cookie_strings[0]}",
        "sec-ch-ua": '"Chromium";v="121", "Not A(Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "navigate",
        "sec-fetch-dest": "frame",
        "referer": f"{GetnategaUrl}",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "priority": "u=0, i",
    }

    while True:
        response4 = requests.get(natigaUrl, headers=headers4)
        if "ASP.NET session has expired" not in response4.text:
            data = response4.text
            break

    soup = BeautifulSoup(data, 'html.parser')
    numbers = soup.find(
        'div', {'id': 'oReportDiv'})
    if numbers:
        # General
        # general_total_number = numbers.find_all('td', {"class": 'a107'})
        # general_total_percent = numbers.find_all('td', {"class": 'a104'})
        # general_total_deg_char = numbers.find_all('td', {"class": 'a113'})
        # general_total_gpa = numbers.find_all('td', {"class": 'a116'})
        # general_total_hours = numbers.find_all('td', {"class": 'a110'})

        # Each Term نتيجة الفصل :
        term_table = numbers.find_all('table', {"class": 'a219'})
        for div in term_table:
            term_total = div.find_all('td', {"class": 'a205'})
            term_percent = div.find_all('td', {"class": 'a211'})
            term_gpa = div.find_all('td', {"class": 'a208'})
            term_hours = div.find_all('td', {"class": 'a214'})

            term_total_list.append([div.text.strip() for div in term_total])
            term_percent_list.append([div.text.strip()
                                      for div in term_percent])
            term_gpa_list.append([div.text.strip() for div in term_gpa])
            term_hours_list.append([div.text.strip() for div in term_hours])

        # Table * Each Term class .a219
        table = numbers.find_all('table', {"class": 'a327'})
        for div in table:
            divs_hash = div.find_all('div', {"class": 'a314'})
            divs_code = div.find_all('div', {"class": 'a310'})
            divs_name = div.find_all('div', {"class": 'a306'})
            divs_max = div.find_all('div', {"class": 'a302'})
            divs_min = div.find_all('div', {"class": 'a298'})
            divs_hours = div.find_all('div', {"class": 'a294'})
            divs_points = div.find_all('div', {"class": 'a290'})
            divs_degree_num = div.find_all('div', {"class": 'a286'})
            divs_degree_txt = div.find_all('div', {"class": 'a282'})
            divs_done = div.find_all('div', {"class": 'a278'})

            divs_hash_list.append([div.text.strip() for div in divs_hash])
            divs_code_list.append([div.text.strip() for div in divs_code])
            divs_name_list.append([div.text.strip() for div in divs_name])
            divs_max_list.append([div.text.strip() for div in divs_max])
            divs_min_list.append([div.text.strip() for div in divs_min])
            divs_hours_list.append([div.text.strip() for div in divs_hours])
            divs_points_list.append([div.text.strip() for div in divs_points])
            divs_degree_num_list.append(
                [div.text.strip() for div in divs_degree_num])
            divs_degree_txt_list.append(
                [div.text.strip() for div in divs_degree_txt])
            divs_done_list.append([div.text.strip() for div in divs_done])

    def create_variables():
        num_lists = len(divs_hash_list)
        term_array = []
        for i in range(num_lists):
            term_array.append([])
            for j in range(len(divs_hash_list[i])):
                term_array[i].append({
                    'hash': divs_hash_list[i][j],
                    'code': divs_code_list[i][j],
                    'hours': divs_hours_list[i][j],
                    'name': divs_name_list[i][j],
                    'max': divs_max_list[i][j],
                    'min': divs_min_list[i][j],
                    'points': divs_points_list[i][j],
                    'degree_num': divs_degree_num_list[i][j],
                    'degree_txt': divs_degree_txt_list[i][j],
                    'done': divs_done_list[i][j],
                })

        return term_array

    variables = create_variables()

    return jsonify({"term": variables,
                    "term_total_list": term_total_list,
                    "term_percent_list": term_percent_list,
                    "term_gpa_list": term_gpa_list,
                    "term_hours_list": term_hours_list,
                    })
