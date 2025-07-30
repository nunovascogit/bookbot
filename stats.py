def sort_on(character_new):
    return character_new["num"]
def get_num_words(book_text):
    return len(book_text.split()) 

def get_char_count(book_text):
    char_count = {}
    for char in book_text.lower():
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1
    return char_count 
def get_sorted_characters_list(char_count):
    
    character_new = []
    for character, count in char_count.items():
        if character.isalpha() == True:
            character_new.append({"char": character, "num": count})
    character_new.sort(reverse=True, key=sort_on)
    return character_new      
