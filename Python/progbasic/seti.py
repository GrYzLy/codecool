#projekt codecool SETI
#https://journey.code.cool/v2/project/curriculum/project/seti/solo/python

def list_to_string(list):
    str1 = ""
    for ele in list:
        str1 += str(ele)
    
    return str1

def  decimal_to_binary(decimal_number):
    
    binary_number_list = []
    
    while decimal_number > 0:
        div = decimal_number // 2
        modulo = decimal_number % 2
        decimal_number = div
        binary_number_list.insert(0,modulo)
        
    return binary_number_list

print(list_to_string(decimal_to_binary(22)))

if true : 
    else:
        pass