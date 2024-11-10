def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(113))
print("="*30)

def number_to_string(num):
    return str(num)
print(number_to_string(10+10))

print("="*30)


 
def get_count(sentence):
    sentence = str(sentence)
    vowels = []
    for line in sentence.lower():
        if line == 'a':
            vowels.append(line)
        if line == 'e':
            vowels.append(line)
        if line == 'i':
            vowels.append(line)
        if line == 'o':
            vowels.append(line)
        if line == 'u':
            vowels.append(line)
    print(len(vowels))
    
get_count("this is a sentence.")




