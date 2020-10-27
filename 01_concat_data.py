import pandas as pd

# 이름이 같은데 1 2 3이 붙어 있을 수 있다.
l = []
with open('from_data.csv') as f:
    lines = f.readlines()
    for line in lines[1:]:
        spl = line.replace('\n', '').split(',')
        name = spl[0]
        l.append({'name':name, 'addr':spl[1]})

l_target = []

with open('target_data.csv') as f:
    lines = f.readlines()
    for line in lines[1:]:
        spl = line.replace('\n', '').split(',')
        l_target.append({'name_target':spl[0], 'addr_target':''})


# name_target = l_target[1]['name_target']

l_r = []
for item_target in l_target:
    obj = {'target_name':'', 'result':'' }
    for item in l:
        name = item['name']
        target_name_origin = item_target['name_target']
        replaced = item_target['name_target'].replace(' ', '')
        obj['target_name'] = target_name_origin
        if name.find(replaced) != -1:
            obj['target_name'] = item_target['name_target']
            obj['result']  = item['addr']

    l_r.append(obj)

for l in l_r:
    print(l)

df = pd.DataFrame(l_r)
df.to_excel('result.xlsx')


