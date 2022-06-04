inputText = Element("inputText")    

output = Element("output")

def clear(*args, **kwargs):
    inputText.clear()

def count(*args, **kwargs):
    number = len(inputText.value)
    output.write(number)