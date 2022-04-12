# import os
# import xml.etree.ElementTree as ET
import pandas as pd
from Bio import Entrez
import time
import json

start_time = time.time()

Merge_3_project = pd.read_csv('20220120 Merge_RISK-HUNT3R_ONTOX_PrecisionTox - Sheet1.tsv', sep='\t')
#chems = Merge_3_project['Compound Name']
chems = Merge_3_project['CAS Number']
pub_count = []
id_list = []
for chem in chems:
    # number of publications --------------------------------------------------

    # # use curl method
    # entrez_tool = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?"
    # pubmed_query = "db=pubmed&term=" + chem
    # record = os.popen("curl "+"'"+entrez_tool+pubmed_query+"'").read()
    # # tree = ET.ElementTree(ET.fromstring(res))

    # use biopython
    Entrez.email = "mu-en.chung@bioquant.uni-heidelberg.de"  # Always tell NCBI who you are
    handle = Entrez.esearch(db="pubmed", term=chem, RetMax='100000') # RetMax limit is 100,000
    record = Entrez.read(handle)
    # record.append(Entrez.read(handle))
    pub_count.append(record["Count"])
    id_list.append(record["IdList"])

chem_pubId = dict(zip(chems, id_list))
chem_count = dict(zip(chems, pub_count))
#print(pub_count)
#print(id_list)
with open('chem_pubId_cas.json', 'w') as fp:
    json.dump(chem_pubId, fp,  indent=4)

with open('chem_count_cas.json', 'w') as fp:
    json.dump(chem_count, fp,  indent=4)

print("--- %s seconds ---" % (time.time() - start_time))

