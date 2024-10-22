def sort_words(words):
    sorted_dict = {}
    
    for word in words:
        first_letter = word[0].lower()
        if first_letter not in sorted_dict:
            sorted_dict[first_letter] = []
            
        sorted_dict[first_letter].append(word)
    
    return sorted_dict
    
input = input("Please enter words separated by spaces: ").split(" ")
print("---")
for letter, items in sorted(sort_words(input).items()):
    print(f"{letter.upper()}: {', '.join(sorted(items))}")
