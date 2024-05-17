import shapes.circle, shapes.rectangle #import single modules from package name
# import shapes # AttributeError: module 'shapes' has no attribute 'circle'
# you may import a module by refencing its name only
# you may NOT import a package thus
# from shapes.rectangle import * #import ALL modules from package name
r = 10
circ = shapes.circle.circumference(r)
print(circ)
'''
output with __init__.py file
shapes.py
loaded <shapes> package
62.83185307179586

output WITHOUT __init__.py file
shapes.py
62.83185307179586
'''
# print(shapes.rectangle.cms_to_inches(5))#can call un-exported methods directly
# print(cms_to_inches(5))#CANNOT call un-exported methods at all when using the wildcard import
# print(area(5))#methods included in the __all__ method work ok
# print(perimeter(5))#methods included in the __all__ method work ok