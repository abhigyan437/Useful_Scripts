import pandas as pd
data = pd.read_excel("info.xlsx")
all_links = []
keywords = ['Sand Crusher Machine','Traub Machine']
types=data['Business Type']
cities = data['Gl_City_Name']
for key in keywords:
    for type in types:
        for city in cities:
            main_link = "https://www.google.com/search?rlz=1C1ONGR_enIN980IN980&tbs=lf:1,lf_ui:2&tbm=lcl&sxsrf=AOaemvJLq-hEeIQASXXS2-K2xrzUNGcdXA:1640273999681&q={}"
            all_links.append(main_link.format(f'{key}+{type}+in+{city}'))
pd.Series(all_links).to_csv('all keyword links.csv', index=False)