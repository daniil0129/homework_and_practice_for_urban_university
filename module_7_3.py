class WordsFinder:
    def __init__(self, *files):
        self.file_names = list(files)

    def get_all_words(self):
        all_words = {}
        chars_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file in self.file_names:
            with open(file, "r", encoding="utf-8") as f:
                all_words[file] = "".join(" " if i == "\n" else i.lower()  for i in f.read() if i not in chars_to_remove).split()
                return all_words

    def find(self, word):
        all_words = self.get_all_words()

        for f_name, list_words in all_words.items():
            for word_index, _word in enumerate(list_words, 1):
                if _word == word.lower():
                    return {f_name: word_index}
            return {f_name: "Совпадений не найдено."}



    def count(self, word):
        all_words = self.get_all_words()
        word = word.lower()

        for f_name, words in all_words.items():
            return {f_name: words.count(word)}


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего



