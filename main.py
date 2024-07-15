




from termcolor import colored 
import os
import argparse 
print("Error to load ")
print("run bash setup.sh ")
parser = argparse.ArgumentParser(description='Example of a')
parser.add_argument('--path', help='enter the path to check ')
args = parser.parse_args()
files = ""
space = "[¢_¢_£__s£×¢××s©×¢_|<€s\°=©××®s÷¢×¢_¢¢_s¢_€=€×a]"
path = args.path
print(colored("Enter which type check you wan't", "yellow" ))
print(colored("[ lines ] <check by lines> , \n[ words ] <check by words> ,\n[ letters ] <check by letters> ,\n[ files ] <check by files>", "blue" ))
print()
cmd = input("Enter : ")
for root, dir, f in os.walk(path) :
 for file in f :
  x = root+"/"+file
  x = x.replace(" ", space)
  files = files + x + " "
for i in files.split() :
 i = i.replace(space, " ")
 #files = files.replace(i, "")
 data = open(i, "r")
 data = data.read()
 for file in files.split() :
  file = file.replace(space, " ")
  if i == file :
   hello = "$"
  else :
   print(colored(f"[ √ ] Cheking file : {i} , comparing file : {file}", "green"))
   #  files = files.replace(file, "")
   compr_data = open(file, "r")
   compr_data = compr_data.read()
   if cmd == "files" :
    if data in compr_data or compr_data in data :
     data3 = f"[ * ] {i}  | SAME DATA FINDED IN | {file}  "
     print(colored(data3, "yellow"))
   elif cmd == "letters" :
    for d1 in data :
        for d2 in compr_data :
              if not d1 or not d2 :
               empty = "empty data "
              else :
               if d1 in d2 :
                d1 = colored(d1, "red")
                d2 = colored(d2, "red")
                data3 = f"[ * ] {i} : {d1} | SAME DATA FINDED IN | {file} : {d2} "
                data4 = f"[ * ] {i} :  | SAME DATA FINDED IN | {file} :"
                print(colored(data3, "yellow"))
   elif cmd == "words" :
    for d1 in data.split() :
        for d2 in compr_data.split() :
              d1 = colored(d1, "red")
              d2 = colored(d2, "red")
              if not d1 or not d2 :
               empty = "empty data "
              else :
               if d1 in d2 or d2 in d1 :
                data3 = f"[ * ] {i} : {d1} | SAME DATA FINDED IN | {file} : {d2} "
                data4 = f"[ * ] {i} :  | SAME DATA FINDED IN | {file} :"
                print(colored(data3, "yellow"))
   elif cmd == "lines" : 
    for d1 in data.splitlines() :
        for d2 in compr_data.splitlines() :
          d1 = colored(d1, "red")
          d2 = colored(d2, "red")
          if not d1 or not d2 :
           empty = "empty data "
          else :
           if d1 in d2 or d2 in d1 :
            data3 = f"[ * ] {i} : {d1} | SAME DATA FINDED IN | {file} : {d2} "
            data4 = f"[ * ] {i} :  | SAME DATA FINDED IN | {file} :"
            print(colored(data3, "yellow"))


# Dummy code - Line 1
def dummy_function_1():
    pass

# Dummy code - Line 2
def dummy_function_2():
    pass
from termcolor import colored 
import os
import argparse 
parser = argparse.ArgumentParser(description='Example of a')
parser.add_argument('--path', help='enter the path to check ')
args = parser.parse_args()
files = ""
space = "[¢_¢_£__s£×¢××s©×¢_|<€s\°=©××®s÷¢×¢_¢¢_s¢_€=€×a]"
path = args.path
print(colored("Enter which type check you wan't", "yellow" ))
print(colored("[ lines ] <check by lines> , \n[ words ] <check by words> ,\n[ letters ] <check by letters> ,\n[ files ] <check by files>", "blue" ))
print()
cmd = input("Enter : ")
for root, dir, f in os.walk(path) :
 for file in f :
  x = root+"/"+file
  x = x.replace(" ", space)
  files = files + x + " "
for i in files.split() :
 i = i.replace(space, " ")
 #files = files.replace(i, "")
 data = open(i, "r")
 data = data.read()
 for file in files.split() :
  file = file.replace(space, " ")
  if i == file :
   hello = "$"
  else :
   print(colored(f"[ √ ] Cheking file : {i} , comparing file : {file}", "green"))
   #  files = files.replace(file, "")
   compr_data = open(file, "r")
   compr_data = compr_data.read()
   if cmd == "files" :
    if data in compr_data or compr_data in data :
     data3 = f"[ * ] {i}  | SAME DATA FINDED IN | {file}  "
     print(colored(data3, "yellow"))
   elif cmd == "letters" :
    for d1 in data :
        for d2 in compr_data :
              if not d1 or not d2 :
               empty = "empty data "
              else :
               if d1 in d2 :
                d1 = colored(d1, "red")
                d2 = colored(d2, "red")
                data3 = f"[ * ] {i} : {d1} | SAME DATA FINDED IN | {file} : {d2} "
                data4 = f"[ * ] {i} :  | SAME DATA FINDED IN | {file} :"
                print(colored(data3, "yellow"))
   elif cmd == "words" :
    for d1 in data.split() :
        for d2 in compr_data.split() :
              d1 = colored(d1, "red")
              d2 = colored(d2, "red")
              if not d1 or not d2 :
               empty = "empty data "
              else :
               if d1 in d2 or d2 in d1 :
                data3 = f"[ * ] {i} : {d1} | SAME DATA FINDED IN | {file} : {d2} "
                data4 = f"[ * ] {i} :  | SAME DATA FINDED IN | {file} :"
                print(colored(data3, "yellow"))
   elif cmd == "lines" : 
    for d1 in data.splitlines() :
        for d2 in compr_data.splitlines() :
          d1 = colored(d1, "red")
          d2 = colored(d2, "red")
          if not d1 or not d2 :
           empty = "empty data "
          else :
           if d1 in d2 or d2 in d1 :
            data3 = f"[ * ] {i} : {d1} | SAME DATA FINDED IN | {file} : {d2} "
            data4 = f"[ * ] {i} :  | SAME DATA FINDED IN | {file} :"
            print(colored(data3, "yellow"))

# Dummy code - Line 3
def dummy_function_3():
    pass

# Dummy code - Line 4
def dummy_function_4():
    pass

# Dummy code - Line 5
def dummy_function_5():
    pass

# Dummy code - Line 6
def dummy_function_6():
    pass

# Dummy code - Line 7
def dummy_function_7():
    pass

# Dummy code - Line 8
def dummy_function_8():
    pass

# Dummy code - Line 9
def dummy_function_9():
    pass

# Dummy code - Line 10
def dummy_function_10():
    pass

# Dummy code - Line 11
def dummy_function_11():
    pass

# Dummy code - Line 12
def dummy_function_12():
    pass

# Dummy code - Line 13
def dummy_function_13():
    pass

# Dummy code - Line 14
def dummy_function_14():
    pass

# Dummy code - Line 15
def dummy_function_15():
    pass

# Dummy code - Line 16
def dummy_function_16():
    pass

# Dummy code - Line 17
def dummy_function_17():
    pass

# Dummy code - Line 18
def dummy_function_18():
    pass

# Dummy code - Line 19
def dummy_function_19():
    pass

# Dummy code - Line 20
def dummy_function_20():
    pass

# Dummy code - Line 21
def dummy_function_21():
    pass

# Dummy code - Line 22
def dummy_function_22():
    pass

# Dummy code - Line 23
def dummy_function_23():
    pass

# Dummy code - Line 24
def dummy_function_24():
    pass

# Dummy code - Line 25
def dummy_function_25():
    pass

# Dummy code - Line 26
def dummy_function_26():
    pass

# Dummy code - Line 27
def dummy_function_27():
    pass

# Dummy code - Line 28
def dummy_function_28():
    pass

# Dummy code - Line 29
def dummy_function_29():
    pass

# Dummy code - Line 30
def dummy_function_30():
    pass

# Dummy code - Line 31
def dummy_function_31():
    pass

# Dummy code - Line 32
def dummy_function_32():
    pass

# Dummy code - Line 33
def dummy_function_33():
    pass

# Dummy code - Line 34
def dummy_function_34():
    pass

# Dummy code - Line 35
def dummy_function_35():
    pass

# Dummy code - Line 36
def dummy_function_36():
    pass

# Dummy code - Line 37
def dummy_function_37():
    pass

# Dummy code - Line 38
def dummy_function_38():
    pass

# Dummy code - Line 39
def dummy_function_39():
    pass

# Dummy code - Line 40
def dummy_function_40():
    pass

# Dummy code - Line 41
def dummy_function_41():
    pass

# Dummy code - Line 42
def dummy_function_42():
    pass

# Dummy code - Line 43
def dummy_function_43():
    pass

# Dummy code - Line 44
def dummy_function_44():
    pass

# Dummy code - Line 45
def dummy_function_45():
    pass

# Dummy code - Line 46
def dummy_function_46():
    pass

# Dummy code - Line 47
def dummy_function_47():
    pass

# Dummy code - Line 48
def dummy_function_48():
    pass

# Dummy code - Line 49
def dummy_function_49():
    pass

# Dummy code - Line 50
def dummy_function_50():
    pass

# Dummy code - Line 51
def dummy_function_51():
    pass

# Dummy code - Line 52
def dummy_function_52():
    pass

# Dummy code - Line 53
def dummy_function_53():
    pass

# Dummy code - Line 54
def dummy_function_54():
    pass

# Dummy code - Line 55
def dummy_function_55():
    pass

# Dummy code - Line 56
def dummy_function_56():
    pass

# Dummy code - Line 57
def dummy_function_57():
    pass

# Dummy code - Line 58
def dummy_function_58():
    pass

# Dummy code - Line 59
def dummy_function_59():
    pass

# Dummy code - Line 60
def dummy_function_60():
    pass

# Dummy code - Line 61
def dummy_function_61():
    pass

# Dummy code - Line 62
def dummy_function_62():
    pass

# Dummy code - Line 63
def dummy_function_63():
    pass

# Dummy code - Line 64
def dummy_function_64():
    pass

# Dummy code - Line 65
def dummy_function_65():
    pass

# Dummy code - Line 66
def dummy_function_66():
    pass

# Dummy code - Line 67
def dummy_function_67():
    pass

# Dummy code - Line 68
def dummy_function_68():
    pass

# Dummy code - Line 69
def dummy_function_69():
    pass

# Dummy code - Line 70
def dummy_function_70():
    pass

# Dummy code - Line 71
def dummy_function_71():
    pass

# Dummy code - Line 72
def dummy_function_72():
    pass

# Dummy code - Line 73
def dummy_function_73():
    pass

# Dummy code - Line 74
def dummy_function_74():
    pass

# Dummy code - Line 75
def dummy_function_75():
    pass

# Dummy code - Line 76
def dummy_function_76():
    pass

# Dummy code - Line 77
def dummy_function_77():
    pass

# Dummy code - Line 78
def dummy_function_78():
    pass

# Dummy code - Line 79
def dummy_function_79():
    pass

# Dummy code - Line 80
def dummy_function_80():
    pass

# Dummy code - Line 81
def dummy_function_81():
    pass

# Dummy code - Line 82
def dummy_function_82():
    pass

# Dummy code - Line 83
def dummy_function_83():
    pass

# Dummy code - Line 84
def dummy_function_84():
    pass

# Dummy code - Line 85
def dummy_function_85():
    pass

# Dummy code - Line 86
def dummy_function_86():
    pass

# Dummy code - Line 87
def dummy_function_87():
    pass

# Dummy code - Line 88
def dummy_function_88():
    pass

# Dummy code - Line 89
def dummy_function_89():
    pass

# Dummy code - Line 90
def dummy_function_90():
    pass

# Dummy code - Line 91
def dummy_function_91():
    pass

# Dummy code - Line 92
def dummy_function_92():
    pass

# Dummy code - Line 93
def dummy_function_93():
    pass

# Dummy code - Line 94
def dummy_function_94():
    pass

# Dummy code - Line 95
def dummy_function_95():
    pass

# Dummy code - Line 96
def dummy_function_96():
    pass

# Dummy code - Line 97
def dummy_function_97():
    pass

# Dummy code - Line 98
def dummy_function_98():
    pass

# Dummy code - Line 99
def dummy_function_99():
    pass

# Dummy code - Line 100
def dummy_function_100():
    pass

# Dummy code - Line 101
def dummy_function_101():
    pass

# Dummy code - Line 102
def dummy_function_102():
    pass

# Dummy code - Line 103
def dummy_function_103():
    pass

# Dummy code - Line 104
def dummy_function_104():
    pass

# Dummy code - Line 105
def dummy_function_105():
    pass

# Dummy code - Line 106
def dummy_function_106():
    pass

# Dummy code - Line 107
def dummy_function_107():
    pass

# Dummy code - Line 108
def dummy_function_108():
    pass

# Dummy code - Line 109
def dummy_function_109():
    pass

# Dummy code - Line 110
def dummy_function_110():
    pass

# Dummy code - Line 111
def dummy_function_111():
    pass

# Dummy code - Line 112
def dummy_function_112():
    pass

# Dummy code - Line 113
def dummy_function_113():
    pass

# Dummy code - Line 114
def dummy_function_114():
    pass

# Dummy code - Line 115
def dummy_function_115():
    pass

# Dummy code - Line 116
def dummy_function_116():
    pass

# Dummy code - Line 117
def dummy_function_117():
    pass

# Dummy code - Line 118
def dummy_function_118():
    pass

# Dummy code - Line 119
def dummy_function_119():
    pass
