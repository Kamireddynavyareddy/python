unames=['navya','vijay','divya','sai']
enames=('navya','vijay','divya','sai')
eids={101,102,103,104,105}
emp={'eid':101,'ename':'navya'}

ename='navya'
values=range(5,51,5)
#how to verify  element present in seq in operators
print('navya' in unames)#true
print('vijay' in enames)#true
print('raju' in enames)#false
print('105' in eids)#true
print('106' in eids)#false