import hashlib
import pandas as pd

def parser(file_name,column_names):
    f = pd.read_csv(file_name)
    no_null = f.dropna(axis=0, how='any',subset=[column_names])
    updated = no_null[column_names].apply(str).apply(hasher)
    no_null['Hashed_ID']=updated
    return no_null
    

def hasher(patient_id):
    ho = hashlib.sha224()
    ho.update(patient_id.encode())
    return ho.hexdigest()

# def hashed(file_name, limit2, limit1=0):
#     parsed = parser(file_name)[limit1:limit2]
#     for par in parsed:
#         par[0] = hasher(par[0])
#     return parsed

parsed = parser('diabetic_data.csv','encounter_id')
del parsed['encounter_id']
cols = parsed.columns.tolist()
cols = cols[-1:] + cols[:-1]
rearranged = parsed[cols]


rearranged.to_csv('hashed.csv', sep=',')