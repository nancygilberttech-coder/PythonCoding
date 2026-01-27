
#Write a function that performs basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3

def compressedstring(given_string:str):
    given_string=given_string.lower()
    given_string=given_string.replace(" ","")
    left_index=right_index=0
    count=0
    target_string=""
    for right_index in range(len(given_string)):
        if left_index==right_index:
            target_string=target_string+(given_string[right_index])
            count+=1
        elif given_string[left_index]==given_string[right_index]:
            count+=1
            continue
        elif not given_string[left_index]==given_string[right_index]:
            left_index=right_index+1
            target_string=target_string+str(count)
            count=1
            continue
    target_string=target_string+str(count)
    return target_string


def compressedString_optimized(given_string:str):
    given_string = given_string.lower()
    given_string = given_string.replace(" ", "")
    target_string=""
    left_index=right_index=0
    count=0
    for right_index in range(len(given_string)):
        if given_string[right_index]==given_string[left_index]:
            count+=1
        else:
            target_string+=given_string[left_index]+str(count)
            count=1
            left_index=right_index
# CRITICAL: Add the very last character group after the loop ends
    target_string += given_string[left_index] + str(count)

    return target_string if len(target_string) < len(given_string) else given_string


def compressedString_optimized2(s):
    s = s.lower()
    s = s.replace(" ","")

    if not s:
        return ""

    compressed = []
    left = 0
    right = 0

    while right < len(s):
        # Move right pointer until characters don't match
        if s[right] == s[left]:
            right += 1
        else:
            # Append the character and the count (right - left)
            compressed.append(s[left])
            compressed.append(str(right - left))
            # Move left pointer to the new character
            left = right

    # Don't forget the last group of characters!
    compressed.append(s[left])
    compressed.append(str(right - left))

    result = "".join(compressed)

    # Return the shorter of the two
    return result if len(result) < len(s) else s


# Test
print(compressedstring("aabcccccaaa"))  # Output: a2b1c5a3

print(compressedString_optimized("AAAA aaa bbbCCCdddbbbaa"))
print(compressedString_optimized2("AAAA aaa bbbCCCdddbbbaa"))