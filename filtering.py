import numpy as np

age=np.array([[15,20,30,78,45,32,54],
              [78,12,49,18,66,70,42]])
#minors=age[age<18]
#adults=age[(age>18) & (age<45)]

#at first two, those are boolean indexing what changes the actual array into 1D that's why if we want to keep the dimensions  same we need to use 'where' clause with below syntax, where, the 'fill_value' is the  value which take place of missing value after filtering. 

#       np.where(array_condition,array, fill_value)    
seniors=np.where(age>=45,age,0)
print(seniors)