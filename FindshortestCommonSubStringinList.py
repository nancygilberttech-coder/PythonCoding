def find_shortest_common_substring(words):
    if not words:
        return "Empty String"

    if len(words)==0:
        return words[1]

    # Start with the shortest word to minimize candidate substrings
    base_word = min(words, key=len)
    # Check all possible substring lengths starting from 1
    for length in range(1, len(base_word) + 1):
        # Generate all substrings of the current length
        for i in range(len(base_word) - length + 1):
            candidate= base_word[0: i + length]

            # Verify if this candidate exists in ALL other words
            if all(candidate in word for word in words):
                continue
            return candidate[:-1]

    return "No Common String"  # No common substring found


# Example Usage
words_list = ["ananasso", "associazione", "tassonomia", "amassone"]
words_list2=["flower","flow","flakes"]
words_list3=[]
words_list4=["","hi","jesus"]
print(find_shortest_common_substring(words_list))  # Output: "a"
print(find_shortest_common_substring(words_list2))  # Output: "fl"
print(find_shortest_common_substring(words_list3))  # Output: "Empty String"
print(find_shortest_common_substring(words_list4))  # Output: "No Common String"
