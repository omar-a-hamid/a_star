import pandas as pd
import numpy as np
import xml.etree.cElementTree as et

tree=et.parse('osm.net.xml')
root=tree.getroot()

root=tree.getroot()

junction_details = []
junction_ids = []
junction_edges = []


i = 0
for junction in root.iter('junction'):

    print(junction.attrib.get('id'))
    junction_ids.append(junction.attrib.get('id'))
    # print(junction.attrib.get('incLanes'))
    # print(junction.attrib.get('intLanes'))


# 	if (poly.attrib.get('shape')):

# 		polyDetails.append(poly.attrib)


# df = pd.DataFrame.from_dict(polyDetails) 
# df = df.dropna(subset=['shape'])
# df.to_csv (r'edges.csv', index = False, header=True)


print("Finish")