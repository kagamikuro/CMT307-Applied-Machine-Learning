#Create training / validation sets

# Need to manually create a folder ( inside the VOC2012 folder): datasets 
# Then, create the folders (inside datasets folder): train_set, val_set 
# Also create the folder (inside both train_set and val_set): Labels 

#I ran this program inside the VOC2012 folder
    

import_file= []
for line in open('ImageSets/layout/val.txt', 'r', encoding="utf8"):
    import_file.append(line.strip())

train_file = []
for item in import_file:
    item = item[:11]
    train_file.append(item)

import shutil    
for item in train_file: 
    shutil.copyfile('JPEGImages/' + (str(item) + '.jpg'), 'datasets/val_set/' + (str(item) + '.jpg')) 
    shutil.copyfile('Annotations/' + (str(item) + '.xml'), 'datasets/val_set/Labels/' + (str(item) + '.xml')) 

import_file= []
for line in open('ImageSets/layout/train.txt', 'r', encoding="utf8"):
    import_file.append(line.strip())

train_file = []
for item in import_file:
    item = item[:11]
    train_file.append(item)

import shutil    
for item in train_file: 
    shutil.copyfile('JPEGImages/' + (str(item) + '.jpg'), 'datasets/train_set/' + (str(item) + '.jpg')) 
    shutil.copyfile('Annotations/' + (str(item) + '.xml'), 'datasets/train_set/Labels/' + (str(item) + '.xml')) 