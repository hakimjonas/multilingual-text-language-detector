from polyglot.detect import Detector
from polyglot.text import Text

def determine_text_languages(string):

    input_object = Text(input)

    temp_list = []

    for sentence in input_object.sentences:
        detect = Detector(str(sentence))
        if len(temp_list) == 0:
            temp_list.append([sentence, detect.language.code])
        else:
            if temp_list[-1][1] == detect.language.code:
                temp_list[-1][0] = temp_list[-1][0]+" "+sentence
            else:
                temp_list.append([sentence, detect.language.code])

    new_list= []

    for i in temp_list:
        new_list.append(i[0])

    output = []

    start = 0
    end = 0
    for sentence in new_list:
        detect = Detector(str(sentence))
        end = start + len(sentence)
        position = (start, end)
        start = end + 1
        output.append((detect.language.code, position, detect.language.confidence,))
    return output

input = '''Afhentet på kaffefarmen Fragtet med fly til Danmark Din garanti for frisk kaffe. Company values matter. Every successful company has a set of company values to assist their employees in achieving their goals as well as the company’s. They are the essence of the company’s identity and summarises the purpose of their existence.'''

print(determine_text_languages(input))
