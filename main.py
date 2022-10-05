import json
import os

class MadLibs:
    def __init__(self, word_descriptions, template):
        self.template = template
        self.word_descriptions = word_descriptions

    @classmethod
    def from_json(cls, name, path='./templates'):
        file_path = os.path.join(path, name)
        with open(file_path, "r") as f:
            data = json.load(f)
        mad_lib = cls(**data)
        return mad_lib

def get_words_from_user(word_descriptions):
    words = []
    print('Please provide the following words: ')
    for desc in word_descriptions:
        user_input = input(desc + ' ')
        words.append(user_input)
    return words


#Build story
def build_story(template, words):
    story = template.format(*words)
    return story


temp_name = "zoo_day.json"
mad_lib = MadLibs.from_json(temp_name)
words = get_words_from_user(mad_lib.word_descriptions)
story = build_story(mad_lib.template, words)

print(story)