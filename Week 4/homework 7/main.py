import os

PATH = os.getcwd()
number_of_words_in_chapters = []


def roman_number_to_arabic(roman_num: str) -> int:
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    arabic_number = 0
    try:
        for index, number in enumerate(roman_num):
            if len(roman_num) >= index + 2:
                if roman_values[number] < roman_values[roman_num[index + 1]]:
                    arabic_number -= roman_values[number]
                else:
                    arabic_number += roman_values[number]
            else:
                arabic_number += roman_values[number]
    except KeyError:
        print("Brojevi poglavlja moraju biti rimski brojevi.")
    return arabic_number


def make_part_directory(current_part_num: int) -> None:
    try:
        part_path = os.path.join(PATH, f"PART_{current_part_num}")
        os.mkdir(part_path)
    except FileExistsError:
        print(f"Direktorijum 'PART_{current_part_num}' vec postoji.")


# Za ovaj drugi except mora ovako inace ne radi (jer u knjizi ne pise part 1, vec krece odmah od chaptera)
def make_chapter_directory(current_part_num: int, current_chapter_num: int) -> str:
    part_path = os.path.join(PATH, f"PART_{current_part_num}")
    path_to_chapter = os.path.join(part_path, f"CHAPTER_{current_chapter_num}")
    try:
        os.mkdir(path_to_chapter)
    except FileExistsError:
        print(f"Direktorijum CHAPTER_{current_chapter_num} vec postoji.")
    except FileNotFoundError:
        make_part_directory(current_part_num)
        os.mkdir(path_to_chapter)
        part_path = os.path.join(PATH, f"PART_{current_part_num}")
        path_to_chapter = os.path.join(part_path, f"CHAPTER_{current_chapter_num}")
    return path_to_chapter


def make_text_files(path_to_chapter: str, current_chapter_num: int) -> str:
    path_text_file = os.path.join(path_to_chapter, f"Text.txt")
    analyses_file_path = os.path.join(path_to_chapter, f"Analytics_CHAPTER_{current_chapter_num}.txt")
    try:
        with open(path_text_file, "w") as text_file:
            text_file.write("")
        with open(analyses_file_path, "w") as analyses_file:
            analyses_file.write("")
    except FileExistsError:
        print("Fajlovi vec postoje.")
    return path_text_file


def rename_file(path_text_file: str, root_path: str) -> str:
    title = ""
    with open(path_text_file) as f:
        text = f.readline()
        while True:
            if "." in text:
                title += text
                break
            else:
                title += text.strip("\n")
            text = f.readline()
    new_title = title.split(".")[0]
    title = ""
    for char in new_title:
        if ord(char) in range(65, 91) or ord(char) in range(97, 123) or char == " ":
            title += char
    new_path = os.path.join(PATH, root_path, f"{title}.txt")
    try:
        os.rename(path_text_file, new_path)
    except FileExistsError:
        print(f"Fajl {title}.txt vec postoji.")
    return new_path


def frequency_of_word(path_text_file: str) -> tuple:
    result_dict = {}
    words = []
    with open(path_text_file) as file_sentences:
        sentences = file_sentences.readlines()
    for item in sentences:
        words += [w.lower() for w in list(item.split())]
    total_num_of_words = len(words)
    while words:
        current_word = words[0]
        result_dict[current_word] = round(words.count(current_word) / total_num_of_words * 100, 2)
        while current_word in words:
            words.remove(current_word)
    return result_dict, total_num_of_words


def write_in_analytics(analytics_file_path: str, frequency_dictionary: dict) -> None:
    try:
        with open(analytics_file_path, "a") as file_analytics:
            for word in frequency_dictionary:
                file_analytics.write(f"{word}: {frequency_dictionary[word]}\n")
    except FileNotFoundError:
        print("Ne mozemo upisati analizu u fajl koji ne postoji.")


def iterate_and_do_functions(part_of_book: str) -> None:
    for root, dirs, files in os.walk(part_of_book):
        if not files:
            continue
        else:
            for name_of_file in files:
                if name_of_file.startswith("Analytics"):
                    chapter = part_of_book + "_" + name_of_file[10:-4]
                    analytics_file_path = os.path.join(PATH, root, name_of_file)
                else:
                    path_text_file = os.path.join(PATH, root, name_of_file)
                    new_path_to_file = rename_file(path_text_file, root)
            if os.path.exists(os.path.join(PATH, root, "Text.txt")):
                os.remove(os.path.join(PATH, root, "Text.txt"))
            frequency_dictionary, total_num_of_words = frequency_of_word(new_path_to_file)
            number_of_words_in_chapters.append([chapter, total_num_of_words])
            write_in_analytics(analytics_file_path, frequency_dictionary)


def make_all_analytics(number_words_in_chapters: list) -> None:
    try:
        all_analytics_path = os.path.join(PATH, "all_analytics")
        os.mkdir(all_analytics_path)
        folder_path_all_analytics = os.path.join(all_analytics_path, "all_analytics.txt")
        with open(folder_path_all_analytics, "w") as datafile:
            for i in number_words_in_chapters:
                datafile.write(f"{i[0]}: ukupno {i[1]} reci\n")
    except FileExistsError:
        print("Fajl za analizu - all_analytics.txt vec postoji.")


def main():
    current_part = 1
    with open("20000 leagues-under-Jules-Verne-[ebooksread.com].txt") as file:
        line = file.readline()
        while line:
            if line.startswith("CHAPTER"):
                current_chapter = roman_number_to_arabic(line.split()[1].strip("."))
                chapter_path = make_chapter_directory(current_part, current_chapter)
                text_file_path = make_text_files(chapter_path, current_chapter)
            elif line.startswith("PART"):
                current_part = roman_number_to_arabic(line.split()[1].strip("."))
                make_part_directory(current_part)
            else:
                with open(text_file_path, "a") as textfile:
                    textfile.write(line)
            line = file.readline()

    book = ["PART_1", "PART_2"]
    for part in book:
        iterate_and_do_functions(part)
    number_of_words_in_chapters.sort(key=lambda x: x[1], reverse=True)
    make_all_analytics(number_of_words_in_chapters)


if __name__ == "__main__":
    main()
