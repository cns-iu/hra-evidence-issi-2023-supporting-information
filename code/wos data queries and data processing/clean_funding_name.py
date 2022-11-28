import pandas as pd

df = pd.read_csv('C:\\Users\\yxkong\\Desktop\\agency.csv')
f = open('C:\\Users\\yxkong\\Desktop\\44.txt','w',encoding='utf-8')
for a in range(len(df)):
    if df.loc[a]['grant'][-1] ==')':
        if '(' in df.loc[a]['grant']:
            b= df.loc[a]['grant'].split('(')[0]
            print(b)
            if b !='':
                if b[-1]==' ':
                    b=b[:-1]
            f.write("UPDATE cite_10_organ_grant_agency_clean set grant_agency='" + df.loc[a]['grant'] +"' where grant_agency='" + b + "';\n")
            f.write("UPDATE cite_10_organ_grant_agency_clean set grant_agency='" + df.loc[a][
                'grant'] + "' where grant_agency='" + b.upper() + "';\n")
            f.write("UPDATE cite_10_organ_grant_agency_clean set grant_agency='" + df.loc[a][
                'grant'] + "' where grant_agency='" + df.loc[a]['grant'].split('(')[1][0:-1] + "';\n\n")

