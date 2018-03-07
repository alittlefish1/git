import json
from countries import get_country_code
import pygal
from pygal.style import RedBlueStyle

#将数据加载到一个列表里y
filename = "population_data.json"
with open(filename) as f:
    pop_date = json.load(f)

#创建一个各地人数的字典

cc_populations = {}
#打印每个国家2010年的人口数量
#json的数据是一个由字典组成的序列
for pop_dict in pop_date:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population


cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}
for cc,pop in cc_populations.items():
    if pop <10000000:
        cc_pops_1[cc] = pop
    elif pop <1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
#查看每组有多少个国家
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))
wm_style = RedBlueStyle


wm = pygal.Worldmap(style=wm_style)
wm.title = 'world population in 2010,by country'

wm.add('0-10m',cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)

wm.render_to_file('world_population.svg')