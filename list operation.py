import numpy as np
array=np.array([321,1234,123,52,234])
print("original array:",array)
new_array=np.append(array,[6,7])
print("array after append:",new_array)
new_array=np.delete(new_array,2)
print("array after removal:",new_array)
new_array=np.append(new_array[8,9])
print("array after second append:",new_array)
new_array=np.delete(new_array,np.where(new_array,[8,9]))
print("array after removing number 52:",new_array)