import json

print("I am here")
json_file_path = "/home/shaun/Desktop/Ecommerce-Scraper/data.json"
with open(json_file_path, 'r') as j:
    data = json.loads(j.read())
mobile_phones = []
for object in data:
    for i in range(len(object['url'])):
        try:
            temp = {}
            temp['url'] = "https://www.amazon.in" + object['url'][i]
            temp['img_url'] = object['img_url'][i]
            temp['title'] = (object['title'][i]).strip()
            temp['brand'] = (object['brand'][i]).strip()
            temp['model_name'] = (object['model_name'][i]).strip()
            temp['price'] = object['price'][i]
            temp['star_rating'] = object['star_rating'][i]
            temp['colour'] = (object['colour'][i]).strip()
            temp['storage_cap'] = []
            for ele in object['storage_cap'][i]:
                ele = str(ele).strip()
                temp['storage_cap'].append(ele)
            mobile_phones.append(temp)
        except IndexError:
            break
        except:
            continue
with open("amazon-assembled.json", "w") as final:
    json.dump(mobile_phones, final)
print(len(mobile_phones))
