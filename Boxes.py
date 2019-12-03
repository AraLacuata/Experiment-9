# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 21:14:34 2019

@author: Ara
"""

import pandas as pd
data = {'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],
        'Dimension':['Length','Width','Height','Length','Width','Height'],
        'Value':[6,4,2,5,3,4]}

boxes = pd.DataFrame(data, columns = ['Box','Dimension','Value'])

tidy_boxes = boxes.pivot(index = 'Box',
                         columns = 'Dimension',
                         values = 'Value').reset_index()

tidy_vol = tidy_boxes.assign(Volume=lambda tidy_boxes:
    tidy_boxes.Length*tidy_boxes.Height*tidy_boxes.Width)
    
print('Messy Data of Boxes:\n',boxes,'\n\n')
print('Tidy Data of Boxes:\n',tidy_boxes,'\n\n')
print('Tidy Data of Boxes with Volume:\n',tidy_vol,'\n\n')
