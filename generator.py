import collections
import random


class TextModel:
    data = collections.defaultdict(lambda: collections.defaultdict(int))

    def learn(self, text_input: str):
        text = self.delete_trash_chars(text_input.lower()).split()
        for i in range(len(text) - 1):
            self.add_pair(text[i], text[i + 1])

    def add_pair(self, first_word: str, second_word: str):
        self.data[first_word][second_word] += 1

    @staticmethod
    def delete_trash_chars(string: str):
        new_string = "".join(char for char in string if char.isalpha() or char in " \n")
        return new_string

    def next_word(self, last_word: str):
        if last_word in self.data.keys():
            return random.choice(list(self.data[last_word].keys()))
        else:
            return random.choice(list(self.data.keys()))

    def produce(self, start_word: str, length: int) -> [str]:
        result_sentence = [start_word]
        for i in range(length - 1):
            result_sentence.append(self.next_word(result_sentence[-1]))
        return result_sentence


if __name__ == '__main__':
    in_data = open("lorem.txt", "r", encoding="utf8")
    out_data = open("result.txt", "w", encoding="utf8")
    textModel = TextModel()
    textModel.learn(in_data.read())
    print(" ".join(textModel.produce("lol", 100)).capitalize() + '.', file=out_data)
