
import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import csv

def xml_to_csv(path, folder):
    xml_list = []
    n = len(folder) + 1
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for object_ in root.findall('object'):
            for i in range(0,len(object_)):
                if object_[i].tag == "name":
                    name = object_[i].text
                path_name = str(path[:-n]) + "\\" + folder + "\\" + str(root.find('filename').text)
                for size in root.iter('size'):
                    for j in range(0,len(size)):
                        if size[j].tag == 'height':
                            height = int(size[j].text)
                        elif size[j].tag == 'width':
                            width = int(size[j].text)
                if len(object_[i]) == 4:
                    for j in range(0,len(object_[i])):
                        if object_[i][j].tag == 'xmin':
                            xmin = int(object_[i][j].text)
                        elif object_[i][j].tag == 'xmax':
                            xmax = int(object_[i][j].text)
                        elif object_[i][j].tag == 'ymin':
                            ymin = int(object_[i][j].text)
                        elif object_[i][j].tag == 'ymax':
                            ymax = int(object_[i][j].text)
                    value = (path_name,width,height,name,xmin,ymin,xmax,ymax)
                    xml_list.append(value) 
                elif len(object_[i]) == 2:
                    for k in range(0,len(object_[i])):
                        if object_[i][k].tag == "name":
                            name = object_[i][k].text
                        if len(object_[i][k]) == 4:
                            for j in range(0,len(object_[i][k])):
                                if object_[i][k][j].tag == 'xmin':
                                    xmin = int(object_[i][k][j].text)
                                elif object_[i][k][j].tag == 'xmax':
                                    xmax = int(object_[i][k][j].text)
                                elif object_[i][k][j].tag == 'ymin':
                                    ymin = int(object_[i][k][j].text)
                                elif object_[i][k][j].tag == 'ymax':
                                    ymax = int(object_[i][k][j].text)
                    value = (path_name,width,height,name,xmin,ymin,xmax,ymax)
                    xml_list.append(value) 
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df

def main():
    for folder in ['train','test']:
        image_path = os.path.join(os.getcwd(), ('images/' + folder))
        xml_df = xml_to_csv(image_path, folder)
        xml_df.to_csv(('data/' + folder + '_labels.csv'), index=None)
        print('Successfully converted xml to csv.')


main()