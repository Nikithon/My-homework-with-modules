def roman_to_int(s : str) -> int: #перенос римских цифр в арабские
    nachalnoe_znachenie = 0
    list_of_roman_numbers_to_arabican={'CM':900, 'CD':400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV':4,
        'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for k in list_of_roman_numbers_to_arabican:
        nachalnoe_znachenie += list_of_roman_numbers_to_arabican[k]*s.count(k)
        s = s.replace(k, '')
    return nachalnoe_znachenie

def int_to_roman(num : int) -> str: #перенос арабских цифр в римские
    info = ['I', 'X', 'C', 'M'] 
    weird_number = ''
    i = 0
    while num != 0:
        n = num % 10
        weird_number = info[i]*n + weird_number
        num//=10
        i += 1
    nachalnoe_znachenie = weird_number
    nachalnoe_znachenie = nachalnoe_znachenie.replace('IIIIIIIII','IX')
    nachalnoe_znachenie = nachalnoe_znachenie.replace('IIIII', 'V')
    nachalnoe_znachenie = nachalnoe_znachenie.replace('IIII', 'IV')
    nachalnoe_znachenie = nachalnoe_znachenie.replace('XXXXXXXXX','XC')
    nachalnoe_znachenie = nachalnoe_znachenie.replace('XXXXX','L')
    nachalnoe_znachenie = nachalnoe_znachenie.replace('XXXX','XL')
    nachalnoe_znachenie = nachalnoe_znachenie.replace('CCCCCCCCC','CM')
    nachalnoe_znachenie = nachalnoe_znachenie.replace('CCCCC','D')
    nachalnoe_znachenie = nachalnoe_znachenie.replace('CCCC','CD')
    return nachalnoe_znachenie


