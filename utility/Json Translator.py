import json
import googletrans
import os

from googletrans import Translator

def translateString(data, code):    
    converter = Translator()
    temp = converter.translate(data, dest=code)
    return temp

src_dirname = os.path.dirname("C:\\Users\\casas\\Desktop\\Russo-Ukraini\\RussiaUkraineWeiboDataset\\Segmented\\")
dst_dirname = os.path.dirname("C:\\Users\\casas\\Desktop\\Russo-Ukraini\\RussiaUkraineWeiboDataset\\TranslatedSegmented\\")

# Range of 1, 195 because there are 195 json files to run through
# Adjust as needed
for i in range(1, 195):
    src_filename = os.path.join(src_dirname, str(i)+'.json')
    dst_filename = os.path.join(dst_dirname, str(i)+'.json')
    f1 = open(src_filename, encoding="utf8")
    f2 = open(dst_filename, encoding="utf8")
    
    orig_data = json.load(f1)
    nu_data = json.load(f2)
    
    print('Translating: ' + str(i) + '.json')
    
    for j in range(len(orig_data)):
        if j % 25 == 0:
            print(str(j) + ' / ' + str(len(orig_data)))
        
        txtinfo = orig_data[j]['text']
        translatedInfo = translateString(txtinfo, 'en')
        nu_data[j]['text'] = translatedInfo.text
        
    with open(dst_filename, 'w', encoding='utf-8') as fout:
            json.dump(nu_data, fout, ensure_ascii=False, indent=4)
            
    print('Finished Translating: '+ str(i) + '.json')

