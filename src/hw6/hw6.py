import  requests
import pprint

pp = pprint.PrettyPrinter(depth=5)

url = "https://rozetka.com.ua/ua/sport-i-uvlecheniya/"
respond_text = ''

respond = requests.get(url)

if respond.ok:
    respond_text = respond.te6
ls = []
ls1 = respond_text.split('/&q;,&q;title&q;:&q;')
for item in ls1[1::]:
    item.replace('image_header_list&g;,&q;order&q', '')
    ls.append(item.split('&g;,&q;order&q;:')[0])
pp.pprint(ls)
