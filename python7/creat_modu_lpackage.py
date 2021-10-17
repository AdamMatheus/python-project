# from upper_package import my_package1,my_package2
# from upper_package.my_package1 import my_module_1,my_module_2



# from upper_package import my_package2
# from upper_package.my_package2 import my_module_3,my_module_4
# print(dir(my_package2))

# print(my_module_2.divide(15,3))

# print(my_module_1.addition(4,5))

# print(my_module_3.repeater("afyonkarahisar",3))


from upper_package.my_package1 import my_module_1
import upper_package
from upper_package.my_package1.my_module_2 import divide,hello

print(divide(24,12))

print(my_module_1.__doc__)

