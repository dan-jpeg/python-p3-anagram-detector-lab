# your code goes he

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        ana_list = []
        for w in word_list:
            if sorted(w) == sorted(self.word):
                ana_list.append(w)
        return ana_list