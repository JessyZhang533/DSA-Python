# Integer
a = 1
b = a  # a and b are pointers pointing to integer 1
print("Before updating value: \na={} \nb={}".format(a, b))
print("a points to {} \nb points to {}".format(id(a), id(b)))  # id: get the address

b = 2  # now b points to 2 but a still points to 1
print("After updating value: \na={} \nb={}".format(a, b))
print("a points to {} \nb points to {}".format(id(a), id(b)))

# Dictionary
dic1 = {'value': 1}
dic2 = dic1  # dic1 and dic2 are pointers pointing to the original dic
print("Before updating value: \ndic1={} \ndic2={}".format(dic1, dic2))
print("dic1 points to {} \ndic2 points to {}".format(id(dic1), id(dic2)))  # id: get the address

dic2['value'] = 2  # now both dic1 and dic2 point to the new dic
print("After updating value: \ndic1={} \ndic2={}".format(dic1, dic2))
print("dic1 points to {} \ndic2 points to {}".format(id(dic1), id(dic2)))
# Note that if we assign dic2 to a completely different dictionary, eg. dic2 = {'value':2}, then dic1 still points to the original dictionary
