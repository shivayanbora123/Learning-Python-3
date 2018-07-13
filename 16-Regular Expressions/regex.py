import re

# patterns = ["term1","term2"]

# text = "This is a string with term1, not the other"

# for pattern in patterns:
#     print("I'm searching for: "+pattern)
#     match = re.search(pattern,text)
#     if match:
#         print("Match!")
#         print(type(match))
#         print(match.start())
        
#     else:
#         print("No match!")


# split_term = "@"
# email = "user@gmail.com"
# print(re.split(split_term,email))

# print(re.findall("match","Test phrase match in match middle"))

def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")


test_phrase = "sdsd..sssddd..sdddsddd...dsds...dsssss...sddddd"
# Pattern is s and 0 or more d's
test_pattern1 = ["sd*"]

# Pattern is s and 1 or more d's
test_pattern2 = ["sd+"]

# Pattern is s and 0 or 1 d's
test_pattern3 = ["sd?"]

# Pattern is s and exactly 3 d's
test_pattern4 = ["sd{3}"]

# Pattern is s and exactly 1 or 3 d's
test_pattern5 = ["sd{1,3}"]

# Pattern is s followed by 1 or more s's or d's
test_pattern6 = ["s[sd]+"]

#multi_re_find(test_pattern6,test_phrase)

test_phrase = "This is a string! But it has a punctuation. How can we remove it?"

# Exclude a particular character
test_pattern1 = ['[^!.?]+']

# Include all lower case characters
test_pattern2 = ['[a-z]+']


test_phrase = "This is a string with numbers 1231232 and a symbul #hashtag"
# Finding digits
test_pattern1 = [r"\d+"]

# Finding non digits
test_pattern2 = [r"\D+"]

# Finding white spaces
test_pattern3 = [r"\s+"]

# Finding alphanumeric characters
test_pattern4 = [r"\w+"]

multi_re_find(test_pattern4,test_phrase)