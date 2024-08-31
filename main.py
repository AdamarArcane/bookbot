def main():
    bookPath = "books/frankenstein.txt"
    text = get_text(bookPath)
    numWords = count_words(text)
    charsDict = count_chars(text)
    cleanedList = dict_to_list_only_alpha(charsDict)
    sortedCleanedList = sort_list_by_count_reverse(cleanedList)
    print(f"There are {numWords} words in this book!")
    char_count_print(sortedCleanedList)
    
        

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    loweredText = text.lower()
    charCount = {}
    for char in loweredText:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1
    return charCount

def sort_on(dict):
    return dict["count"]

def sort_list_by_count_reverse(list):
    list.sort(reverse=True, key=sort_on)
    return list

def dict_to_list_only_alpha(dict):
    initList = []
    for char in dict:
        if char.isalpha():
            charDict = {}
            charDict["char"] = char
            charDict["count"] = dict[char]
            initList.append(charDict)
    return initList

def char_count_print(sclist):
    for char in sclist:
        print(f"The '{char["char"]}' character was found {char["count"]} times")

def get_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()


main()