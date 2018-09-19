Given multilingual text, detect what languages are present in it and find its’ corresponding positions and confidence score.
>>> text = '''Afhentet på kaffefarmen Fragtet med fly til Danmark Din garanti for frisk kaffe. Company values matter. Every successful company has a set of company values to assist their employees in achieving their goals as well as the company’s. They are the essence of the company’s identity and summarises the purpose of their existence.'''

>>> determine_text_languages(text)
[
    ('da', (0, 80), 0.93443),
    ('en', (81, 327), 0.9833),
]
