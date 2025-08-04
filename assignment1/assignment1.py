# Write your code here.
#Task 1
def hello():
    return "Hello!"

print(hello())

#Task 2
def greet(name):
    return f'Hello, {name}!'

print(greet("Carlos"))

#Task 3
def calc(val1, val2, op = "multiply"):
    try:
        match op:
            case "add":
                return val1 + val2
            case "subtract":
                return val1 - val2
            case "mulitply":
                return val1 * val2
            case "divide":
                return val1 / val2
            case "modulo":
                return val1 % val2
            case "int_divide":
                return val1 // val2
            case "power":
                return val1 ** val2
            case _:
                return f'Invalid operation {op}"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except Exception:
        return "You can't multiply those values!"
    
print(calc(1, 4, "add"))
    
#Task 4
def data_type_conversion(value, type):
    try:
        if type == "int":
            return int(value)
        elif type == "float":
            return float(value)
        elif type == "str":
            return str(value)
    except Exception:
        return f"You can't convert {value} into a {type}."
    
print(data_type_conversion("184", "float"))

#Task 5
def grade(*args):
    try:
        average = sum(args) / len(args)

        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    except Exception:
        return "Invalid data was provided."
    
print(grade(50, 75, 100))
    
#Task 6
def repeat(string, count):
    result = ""

    for _ in range(count):
        result += string
    
    return result

print(repeat("hi", 8))

#Task 7
def student_scores(op, **kwargs):
    if op == "mean":
        return sum(kwargs.values()) / len(kwargs)
    elif op == "best":
        return max(kwargs, key = kwargs.get)
    else:
        return "Invalid operation"
    
print(student_scores("mean", Bill = 70, Jerry = 95, Teresa = 82))
print(student_scores("best", Bill = 70, Jerry = 95, Teresa = 82))

#Task 8 
def titleize(string):
    littleWords = {'a', 'on', 'an', 'the', 'of', 'and', 'is', 'in'}
    words = string.split()
    result = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        elif word in littleWords:
            result.append(word)
        else:
            result.append(word.capitalize())

    return " ".join(result)

print(titleize("k-pop demon hunters"))

#Task 9
def hangman(secret, guess):
    result = ""

    for char in secret:
        if char in guess:
            result += char
        else:
            result += "_"
        
    return result

print(hangman("The Weeknd", "The"))

#Task 10
def pig_latin(string):
    vowels = "aeiou"
    words = string.split()
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        elif "qu" in word:
            result.append(word[word.find("qu") + 2:] + word[:word.find("qu") + 2] + "ay")
        else:
            for i, char in enumerate(word):
                if char in vowels:
                    result.append(word[i:] + word[:i] + "ay")
                    break

    return " ".join(result)

print(pig_latin("hurry up tomorrow"))
