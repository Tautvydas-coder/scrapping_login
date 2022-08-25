import csv
from bs4 import BeautifulSoup
from lxml import html
from resources.page_info import *
import json
from resources.variables import *


# --------SOUP-----------
# page = requests.get(url=URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find('body').find('div').find_all('label')
# print(results)
# body = BeautifulSoup('<a class="pointer" href="http://www.degalukainos.lt" title="Degalų kainos Lietuvoje" xpath="1"><img src="/img/logo_2.gif" width="142" height="62" alt="logo"></a>','html.parser')
# body = soup.find('body').find_all('div')
# for link in results:
# print(link.get_text())
# print(link)
# print(link.img['alt'])
# print(soup)

# -------LXML-----------
# page = requests.get(url=URL)
# root = html.fromstring(page.content)
# element = root.xpath('/html/body/div[1]/div[4]/div[2]/p[1]')
# elementy = ('//html/body/div/div[2]/div[2]/div/form/div/div[2]/table/tr[2]/td[10]/div[1]/img')
# last=elementy.split('/')
# print(last[-1])
# print(element)
# print(element[0].text)
# print(type(print(element[0].text)))
# tree = root.getroottree()
# results = root.xpath('/html/body/div//*')
# print(results)
# dom = etree.HTML(str(root))
# elementr = root.xpath('/html/body/main/div/form/div[2]/div/input')
# print(elementr[0].get('type'))
# if elementr[0].get('type') in login_name_pass:
#     atr_type = elementr[0].get('type')
#     print("type" + "," + atr_type)
# else:
#     print('no')
# if elementr[0].get('id') is True:
#     print(elementr[0].get('id'))
# --------------------------------


def fetch_page_content(web_page):
    page_content = html.fromstring(web_page.content)
    return page_content


def fetch_root_tree(root):
    web_html_tree = root.getroottree()
    return web_html_tree


def fetch_web_element_info(root):
    web_elements = root.xpath(xpath_start)
    return web_elements


def fetch_data_from_txt():
    with open(data, 'r', encoding='utf-8') as txt:
        contents = txt.read().splitlines()
    return contents


def write_to_csv(results, tree, root, vocabulary):
    temp = 0
    with open(csv_name, 'w', encoding='windows-1257', errors="xmlcharrefreplace") as file:
        file.write(column_names)
        for result in results:
            xpath = tree.getpath(result)
            if xpath.__contains__('input') or xpath.__contains__('label'):
                elements = root.xpath(xpath)
                content_text = elements[0].text
                if elements[0].get('type') in vocabulary:
                    atr_type = elements[0].get('type')
                    file.write("type" + "," + atr_type + "," + "/" + xpath)
                    temp += 1
                    if temp < 4: file.write(",")
                elif elements[0].get('id') in vocabulary:
                    atr_id = elements[0].get('id')
                    file.write("id" + "," + atr_id + "," + "/" + xpath)
                    temp += 1
                    if temp < 4: file.write(",")
                elif elements[0].get('class') in vocabulary:
                    atr_class = elements[0].get('class')
                    file.write("class" + "," + atr_class + "," + "/" + xpath)
                    temp += 1
                    if temp < 4: file.write(",")
                elif elements[0].get('placeholder') in vocabulary:
                    atr_placeholder = elements[0].get('placeholder')
                    file.write("placeholder" + "," + atr_placeholder + "," + "/" + xpath)
                    temp += 1
                    if temp < 4: file.write(",")
                if content_text in vocabulary:
                    file.write(content_text + "," + "/" + xpath)
                    temp += 1
                    if temp < 4: file.write(",")


def fetch_json_list():
    with open(csv_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        json_array = [row for row in csv_reader]
    return json_array


def fetch_json_format(json_list):
    json_str = json.dumps(json_list, indent=4, ensure_ascii=False)
    return json_str


def write_to_json_file(json_string):
    with open(json_name, 'w') as json_file:
        json_file.write(json_string)


if __name__ == '__main__':
    page = check_web_status()
    web_root = fetch_page_content(page)
    web_tree = fetch_root_tree(web_root)
    web_results = fetch_web_element_info(web_root)
    vocabulary = fetch_data_from_txt()
    write_to_csv(web_results, web_tree, web_root, vocabulary)
    json_list = fetch_json_list()
    json_string = fetch_json_format(json_list)
    write_to_json_file(json_string)
