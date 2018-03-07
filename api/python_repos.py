# -*- coding: utf-8 -*-
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightStyle as LS
from pygal.style import RedBlueStyle


#执行API调用并储存响应

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ",r.status_code)

#将API响应存储在一个变量中

response_dirc = r.json()

print("total repositories: ",response_dirc['total_count'])
#搜索油管厂那个苦的信息
repo_dicts = response_dirc['items']
names,plot_dicts = [],[]
#print("repositories returned: ",len(repo_dicts))
#研究第一个厂库
#repo_dict = repo_dicts[0]
#print('\nall repositories' )

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':str(repo_dict['description']),
        'xlink':repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)

#可视化
my_style = RedBlueStyle
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 4
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)
chart.title = 'most stars in github'
chart.x_labels = names

chart.add('32',plot_dicts)
chart.render_to_file('preavent.svg')
    #print('\nname: ',repo_dict['name'])
    #print('repository: ',repo_dict['html_url'])
   # print('stars: ',repo_dict['stargazers_count'])