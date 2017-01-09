# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 15:14:51 2017

@author: Ge Liu 
"""

import MySQLdb
import os
from CifFile import CifFile

cif_dir = '/fs4/masi/huoy1/COD/cod/cif'

db = MySQLdb.connect(
    host='www.crystallography.net',
    port = 3306,
    user='cod_reader',
    passwd='',
    db='cod',
    )
    
    
# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "select file from data"
cursor.execute(sql)
allFiles = cursor.fetchall()

for i in range(0,len(allFiles)):
    fileNum = str(allFiles[i][0])
    fileName = "%s.cif" % fileNum
    
    dir_level1 = fileNum[0]
    dir_level2 = fileNum[1:3]
    dir_level3 = fileNum[3:5]
    
    cif_full_dir = os.path.join(cif_dir,dir_level1,dir_level2,dir_level3)
    cif_full_file = os.path.join(cif_full_dir,fileName)
    
    if (not os.path.exists(cif_full_file)):
        raise IOError("CIF file '%s' was not found!" % (fileName))
    else:
        cf = CifFile(cif_full_file)
        cb = cf[cf.keys()[0]]
        cb['_symmetry_cell_setting']
        cb['_symmetry_space_group_name_Hall']
        cb['_symmetry_space_group_name_H-M']
        cb['_atom_site_label']
        cb['_atom_site_fract_x']
        cb['_atom_site_fract_y']
        cb['_atom_site_fract_z']   
    

