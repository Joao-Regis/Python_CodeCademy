highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)
print('\n')

highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list)
print('\n')

highlighted_poems_stripped = []
for info in highlighted_poems_list:
  highlighted_poems_stripped.append(info.strip())
print(highlighted_poems_stripped)
print('\n')

highlighted_poems_details = []
for p_info in highlighted_poems_stripped:
  highlighted_poems_details.append(p_info.split(':'))
print(highlighted_poems_details)
print('\n')

titles = []
poets = []
dates = []

for specs in highlighted_poems_details:
  titles.append(specs[0])
  poets.append(specs[1])
  dates.append(specs[2])
    
print(titles)
print('\n')

print(poets)
print('\n')

print(dates)
print('\n')

for i in range(len(titles)):
  #p_titles = titles[i]
  #p_poets = poets[i]
  #p_dates = dates[i]
  print ('The poem {p_titles} was published by {p_poets} in {p_dates}.'.format(p_titles=titles[i], p_poets=poets[i], p_dates=dates[i]))
  print('\n')
  
