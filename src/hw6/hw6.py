import requests
import pprint

pp = pprint.PrettyPrinter(depth=5)

url = "https://rozetka.com.ua/ua/sport-i-uvlecheniya/"
respond_text = ''

respond = requests.get(url)

if respond.ok:
    respond_text = respond.text

# Task1
ls = []
ls1 = respond_text.split('/&q;,&q;title&q;:&q;')
for item in ls1[1::]:
    item.replace('image_header_list&g;,&q;order&q', '')
    ls.append(item.split('&g;,&q;order&q;:')[0])
pp.pprint(ls)


# Task2
from_link = respond_text.split('.jpg&q:,&q;link&q;:&q;')[1::]
link = []

for item in from_link:
    item.replace('image_header_list&q;,&q;order&q', '')
    link.append(item.split('&q;,&q;title&q;:&q;')[0])

dict_link = {}
for index in range(len(ls)):
    dict_link[ls[index]] = link[index]
pp.pprint(dict_link)

# Task3
div = []
number = 0
for index in range(len(ls)):
    if index <= 14:
        div_1 = '"' + link[index] + '"'
        div_2 = '"' + link[index + 1] + '"'
        first_p = respond_text.split(div_1)[2].split(div_2)[0]
    else:
        diver = '"' + link[index] + '"'
        first_p = respond_text.split(diver)[2].split('widget-list')[0]
    div.append(first_p)

result = []
for element in div:
    pron_result = []
    for item in element.split(' title="')[2::]:
        pron_result.append(item.split('" class=""')[0])
    result.append(pron_result)




