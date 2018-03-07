import pygal

wm = pygal.Worldmap()
wm.title = 'Populations of Countries in North America'
wm.add('north america',{'ca':234324,'us':343455,'mx':434545})

wm.render_to_file('na_populatoins.svg')