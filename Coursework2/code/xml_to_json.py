# run this from VOC2012 folder

# this script convert each image annotation to the form of json of ViA such as:
# { 'filename': '28503151_5b5b7ec140_b.jpg',
#   'regions': {
#       '0': {
#           'region_attributes': {},
#           'shape_attributes': {
#               'all_points_x': [...],
#               'all_points_y': [...],
#               'name': 'polygon'}},
#       ... more regions ...
#   },
#   'size': 100202
# }

import json
import xmltodict
import glob

from xml.etree import ElementTree as et



def xml_to_json(folder):
    path = 'datasets/'+ folder +'/labels'

    A0 = dict()
    image = []
    for xml_path in glob.glob(path + '/*.xml'):
    
        tree = et.parse(xml_path);
        root = tree.getroot()
        A = dict()
        for child_root in root:
            if child_root.tag == 'filename':
                imagePath = child_root.text
            if child_root.tag == 'size':
                for region_attribute in child_root:
                    if region_attribute.tag == 'width':
                        width = region_attribute.text
                    if region_attribute.tag == 'height':
                        height = region_attribute.text
                    if region_attribute.tag == 'depth':
                        depth = region_attribute.text
                
            if child_root.tag == 'object':
                for region_attribute in child_root:
                    if region_attribute.tag == 'name':
                        name = region_attribute.text
                    if region_attribute.tag == 'bndbox':
                        for bndbox in region_attribute:
                            if bndbox.tag == 'xmin':
                                xmin = int(bndbox.text)
                            if bndbox.tag == 'ymin':
                                ymin = int(bndbox.text)
                            if bndbox.tag == 'xmax':
                                xmax = int(bndbox.text)
                            if bndbox.tag == 'ymax':
                                ymax = int(bndbox.text)


        A['filename'] = imagePath
        
        
        regions_list = []
        regions = dict()

        region_attributes_list = []
        region_attributes = dict()


        region_attributes['name'] = name
        region_attributes['xmin'] = xmin
        region_attributes['ymin'] = ymin
        region_attributes['xmax'] = xmax
        region_attributes['ymax'] = ymax

        region_attributes_list.append(region_attributes)

        
        regions['0'] = region_attributes_list;
        regions_list.append(regions)
                
        
        A['regions'] = regions_list

        sizes_list = []
        sizes = dict()

        sizes['width'] = width
        sizes['height'] = height
        sizes['depth'] = depth

        sizes_list.append(sizes)

        A['size'] = sizes_list
        
        image.append(A)
    A0['image'] =image  
    with open('annotation_'+folder+'.json','w') as f:
        json.dump(A0,f)



def main():
    for folder in ['train_set','val_set']:
        xml_to_json(folder)
        print('Successfully converted xml to json.')



main()
