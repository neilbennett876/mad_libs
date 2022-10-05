#Mad libs template
class MadLibs:
    def __init__(self, word_descriptions, template):
        self.template = template
        self.word_descriptions = word_descriptions
    

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


template = 'I own a big {}. I like to {}'
words = get_words_from_user(['noun', 'verb'])
story = build_story(template, words)

print(story)