def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    character_frequency_dict = count_character_frequency(text)
    character_frequency_list = convert_frequency_dict_to_list(character_frequency_dict)
    sorted_char_freq_list = sort_frequency_list(character_frequency_list)

    print("--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_char_freq_list:
        print(f"The '{item['character']}' character was found {item['count']} times")
        
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def count_character_frequency(text):
    """
    Counts the frequency of each character in the given text.
    Converts all characters to lowercase to avoid duplicates.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """

    text = text.lower()
    frequency = {}

    for char in text:
        if char.isalpha():
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    return frequency            


def convert_frequency_dict_to_list(frequency: dict) -> list:
    """
    Converts a frequency dictionary into a list of dictionaries
    
    Args:
        frequency (dict): A dictionary with characters as keys and counts as values.
        
    Returns:
        list: A list of dictionaries with each character and its count.
    """

    return[{"character": char, "count": count} for char, count in frequency.items()]


def sort_on(d):
    return d["count"]


def sort_frequency_list(frequency_list: list) -> list:
    """
    Sorts a list of dictionaries by the sort_on key in descending order.
    
    Args:
        frequency_list (list): A list of dictionaries with character counts.
        
    Returns:
        list: The sorted list of dictionaries.
    """

    frequency_list.sort(key=sort_on, reverse=True)
    return frequency_list

main()