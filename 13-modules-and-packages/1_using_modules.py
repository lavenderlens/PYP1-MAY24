import sys, platform, os, copy

for path in sys.path:
    print(path)

print(platform.architecture())
print(platform.platform())
print(platform.processor())
print(platform.system())
print(platform.version())
print(platform.python_implementation())
print(platform.python_version())

print("no. CPUs:", os.cpu_count())
print("encoding:", os.device_encoding(0))
print("encoding:", os.get_terminal_size())
os.system("cls")#Windows
os.system("clear")#Mac/Unix

my_dict = {"name":"Alan", "hobbies":["reading", "music", "film"]}

my_dict_copy = my_dict#this line copies a reference only: a "shallow" copy

my_dict_copy["name"] = "Keith"
print(my_dict_copy)
print(my_dict)#ALSO Keith in the original

# the copy module is to be used whenever immutable copies are made
# it has two main methods: copy.copy() and copy.deepcopy()

my_dict_copy_with_mod = copy.copy(my_dict_copy)#STILL a shallow copy: see below
my_dict_copy_with_mod["name"] = "Alan"
print(my_dict_copy_with_mod)
print(my_dict_copy)#original unchanged: Keith
my_dict_copy_with_mod['hobbies'].append("cycling")
print(my_dict_copy_with_mod)
print(my_dict_copy)#cycling is in BOTH!
my_deepcopy = copy.deepcopy(my_dict_copy)
my_deepcopy['hobbies'].append('Netflix')
print(my_deepcopy)
print(my_dict_copy)#original unaffected -  any number of levels of nesting