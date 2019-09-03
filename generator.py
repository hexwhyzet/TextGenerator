import random
import pickle
import os


class TextModel:
    data = dict(dict())
    save_path = str()

    def __init__(self, save_path_inp: str = "save.pickle"):
        self.save_path = save_path_inp
        self.load(save_path_inp)

    def fit(self, text_input: str):
        pure_words = self.delete_trash_chars(text_input.lower()).split()
        for i in range(len(pure_words) - 1):
            self.add_pair(pure_words[i], pure_words[i + 1])

    def add_pair(self, first_word: str, second_word: str):
        if first_word not in self.data.keys():
            self.data[first_word] = dict()
        if second_word not in self.data[first_word].keys():
            self.data[first_word][second_word] = 0
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

    def generate(self, start_word: str, length: int) -> [str]:
        result_sentence = [start_word]
        for i in range(length - 1):
            result_sentence.append(self.next_word(result_sentence[-1]))
        return result_sentence

    def clear_model(self):
        self.data = dict(dict())

    def save(self, path_inp: str = None):
        path = path_inp if path_inp is not None else self.save_path
        with open(path, "wb") as f:
            pickle.dump(self.data, f)

    def load(self, path_inp: str):
        path = path_inp if path_inp is not None else self.save_path
        with open(path, "rb") as f:
            if not os.stat(path).st_size == 0:
                self.data = pickle.load(f)


if __name__ == '__main__':
    in_data = open("lorem.txt", "r", encoding="utf8")
    out_data = open("result.txt", "w", encoding="utf8")
    textModel = TextModel()
    textModel.fit(in_data.read())
    textModel.save()
    print(" ".join(textModel.generate("Lol", 100)).capitalize() + '.', file=out_data)
    # print(os.stat(textModel.save_path).st_size)
