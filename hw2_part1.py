# def get_number():
#     number = 50
#     return number
#
#
# # Complete all of the following functions. Currently they all just
# # 'pass' rather than explicitly return value, which means that they
# # implicitly return None. They all include doctests, which you can
# # test by running this file.
#
# # The doctests are just examples. Feel free to add your own doctests.
#
# # ****************************************
# # Problem 1
# # ****************************************
# def get_position(ch):
#     """str -> int
#     Return positon of letter in alphabet. If argument is not a letter function
#     should return None.
#
#     >>> get_position('A')
#     1
#     >>> get_position('z')
#     26
#     >>> get_position('Dj')
#
#     """
#     if len(ch) == 1 and ch.isalpha():
#         if ord(ch) < 97:
#             ch = ch.lower()
#         return int(ord(ch) - 96)
#     else:
#         return None
#
#
# # ****************************************
# # Problem 3
# # ****************************************
# # def compare_str(s1, s2):
# #     """(str, str) -> bool
# #     Compare two srings lexicographicly. Return True if string s1 is larger
# #     than string s2 and False otherwise. If arguments aren't string or function
# #     have different length function should return None.
# #
# #     >>> compare_str('abc', 'Abd')
# #     False
# #     >>> compare_str('zaD', 'zab')
# #     True
# #     >>> compare_str('zaD', 'Zad')
# #     False
# #     >>> compare_str('aaa', 'aaaaa')
# #
# #     >>> compare_str('2015', 2015)
# #
# #     """
# #     if isinstance(s1, str) and isinstance(s2, str):
# #         if len(s1) == len(s2):
# #             res_s1 = 0
# #             res_s2 = 0
# #             for each_let_s1 in s1:
# #                 res_s1 += ord(each_let_s1)
# #             for each_let_s2 in s2:
# #                 res_s2 += ord(each_let_s2)
# #             if res_s1 < res_s2:
# #                 return True
# #             else:
# #                 return False
# #     else:
# #         return None
#
#
# # ****************************************
# # Problem 5
# # ****************************************
# def type_by_sides(a, b, c):
#     """
#     (float, float, float) -> str
#     Detect the type of triangle by it's sides and return type as string
#     ("right angled triangle", "obutuse triangle", "acute triangle"). If there is no
#     triangle with such sides, then function should return None.
#
#     >>> type_by_sides(3, 3, 3)
#     "acute triangle"
#     >>> type_by_sides(3, 4, 5)
#     "right angled triangle"
#     >>> type_by_sides(3, 3, 2015)
#     """
#     if type(a) == int and type(b) == int and type(c) == int:
#         if a < 0 and b < 0 and c < 0 and (a + b < c or a + c < b or b + c < a):
#             return None
#         else:
#             if a == b == c:
#                 return "acute triangle"
#             if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
#                 return "right angled triangle"
#     else:
#         return None
#
# print(type_by_sides(3, 4, 589))


# ****************************************
# Problem 7
# ****************************************
# def convert_to_column(s):
#     """str -> str
#     Convert string to a column of words.
#     If argument is not a string function should return None.
#
#     >>> convert_to_column("Revenge is a dish that tastes best when served cold.")
#     revenge
#     is
#     a
#     dish
#     that
#     tastes
#     best
#     when
#     served
#     cold
#     >>> convert_to_column("Never hate your enemies. It affects your judgment.")
#     never
#     hate
#     your
#     enemies
#     it
#     affects
#     your
#     judgment
#     >>> print(convert_to_column(2015))
#     """
#     new_s = ""
#     lst = s.split(" ")
#     for i in lst:
#         new_s += i.lower().replace(".", "").replace(",", "").replace("-", "")
#         if i != lst[-1]:
#             new_s += "\n"
#     return new_s


# ****************************************
# Problem 10
# ****************************************
# def encrypt_message(s):
#     """str -> str
#
#     Replace all letters in string with next letters in aplhabet.
#     If argument is not a string function should return None.
#
#     >>> encrypt_message("Revenge is a dish that tastes best when served cold.")
#     Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.
#     >>> encrypt_message("Never hate your enemies. It affects your judgment.")
#     Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.
#     >>> encrypt_message(2015)
#
#     """
#     s_new = ""
#     if type(s) == str and (isinstance(i) for i in s):
#         for letter in s:
#             if letter.isalpha():
#                 letter = ord(letter)
#                 letter += 1
#                 s_new += chr(letter)
#             else:
#                 s_new += letter
#         return s_new
#     else:
#         return None
# print(encrypt_message("Never hate your enemies. It affects your judgment."))

# ****************************************
# Problem 11
# ****************************************
# def decrypt_message(s):
#     """
#     str -> str
#     Replace all letters in string with previous letters in aplhabet. If argument isn't a string
#     function should return None.
#
#     >>> print(decrypt_message("Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme."))
#     Revenge is a dish that tastes best when served cold.
#     >>> print(decrypt_message("Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou."))
#     Never hate your enemies. It affects your judgment.
#     >>> decrypt_message(2015)
#
#     """
#     s_new = ""
#     if type(s) == str and (isinstance(i) for i in s):
#         for letter in s:
#             if letter.isalpha():
#                 letter = ord(letter)
#                 letter -= 1
#                 s_new += chr(letter)
#             else:
#                 s_new += letter
#         return s_new
#     else:
#         return None
#
# ****************************************
# # Problem 12
# # ****************************************
# def exclude_letters(s1, s2):
#     """
#     (str, str) -> str
#     Delete all letter from string s2 in string s1.
#     If arguments aren't strings function should return None.
#
#     >>> print(exclude_letters("aaabb", "b"))
#     aaa
#     >>> print(exclude_letters("abcc", "cczzyy"))
#     ab
#     >>> exclude_letters(2015, "sasd")
#
#     """
#     if type(s1) == str and type(s2) == str:
#         new_s = ""
#         for letter in s1:
#             if letter not in s2:
#                 new_s += letter
#         return new_s
#     else:
#         return None
#
# print(exclude_letters("aaabb", "b"))

# ****************************************
# Problem 13
# ****************************************
# def create_string(lst):
#     """list -> str
#     Create and return string from histogrma of letters. If argument isn't
#     list of 26 positive integer numbers function should return None.
#
#     >>> print(create_string([0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
#     bcc
#     >>> print(create_string([4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]))
#     aaaazzzz
#     >>> create_string([4, 0, 0, 0, 0, 0])
#
#     """
#     res_str = ""
#     if type(lst) == list and len(lst) == 26 and (type(el) == int and el > 0 for el in lst):
#         for pos in range(len(lst)):
#             if lst[pos] == 1:
#                     res_str += chr(pos + 97)
#             else:
#                 for i in range(lst[pos]):
#                     res_str += chr(pos + 97)
#         return res_str
#     else:
#         return None
#
# print(create_string([4, 0, 0, 0, 0, 0]))

# ****************************************
# Problem 16
# ****************************************
def find_union(s1, s2):
    """(str, str) -> str

    Find and return string of all letters in alphabetic order that
    are present in either strings. If arguments aren't strings function should
    return None.

    >>> print(find_union("aaabb", "bbbbccc"))
    abc
    >>> print(find_union("aZAbc", "zzYYxp"))
    AYZabcpxz
    >>> find_union("sfdfsdf", 2015)

    """
    if type(s1) == str and type(s2) == str:
        letters_lst = list(i for i in s1)
        letters_lst += list(j for j in s2)
        letters_lst.sort()
        res_str = ""
        for lst_el in letters_lst:
            if lst_el in res_str:
                res_str += ""
            else:
                res_str += lst_el
        return res_str
    else:
        return None

print(find_union("aaabb", "bbbAccc"))
# ****************************************
# Problem 17
# ****************************************
# def number_of_occurence(lst, s):
#     """(list, str) -> int
#
#     Find and return number of occurence of string s in all elements of the
#     list lst. If lst isn't list of strings or s isn't string function should
#     return None.
#
#     >>> number_of_occurence(["man", "girl", "women", "boy"], "m")
#     2
#     >>> number_of_occurence(["ab", "aba", "a", "b", "ba"], "ba")
#     2
#     >>> number_of_occurence([1, 2, 2015, 1, 3], "1")
#
#     """
#     for el in lst:
#         if (type(el) != str):
#             return None
#     if type(s) != str and (type(el) != str for el in lst):
#         return None
#     else:
#         count = 0
#         for lst_el in lst:
#             if s in lst_el:
#                 count += 1
#         return count
#
# print(number_of_occurence([1, 2, 2015, 1, 3], "1"))

# ****************************************
# Problem 20
# ****************************************
def polynomial_eval(coefficients, value):
    """(list) -> int

    Return the result of the function with inputted coeficients

    >>> polynomial_eval([2,3,0,4], 4)
    180
    >>> polynomial_eval([6], 42)
    6
    >>> polynomial_eval([6,-2,-20], -1)
    -12
    >>> polynomial_eval([6,0,-8,0,-8,0], 2)
    112
    >>> polynomial_eval([6,0,-8,0,-8,0], 1)
    -10
    >>> polynomial_eval([6,0,-8,0,-8,0], 0)
    0
    """
    len_of_lst = len(coefficients)
    f = 0
    for each in range(len(coefficients)):
        f += coefficients[each] * value**(len_of_lst - each - 1)
    return f

print(polynomial_eval([2,3,0,4], 4))
#
#
# ****************************************
# Problem 22
# ****************************************
# def pattern_number(sequence):
#     """(list) -> list, int
#     Return the patern and the number of repeats of
#     the patern of the inputted list
#
#     >>> print(pattern_number([]))
#     None
#     >>> print(pattern_number([42]))
#     None
#     >>> print(pattern_number([1,2]))
#     None
#     >>> pattern_number([1,1])
#     ([1], 2)
#     >>> print(pattern_number([1,2,1]))
#     None
#     >>> pattern_number([1,2,3,1,2,3])
#     ([1, 2, 3], 2)
#     >>> print(pattern_number([1,2,3,1,2]))
#     None
#     >>> print(pattern_number([1,2,3,1,2,3,1]))
#     None
#     >>> pattern_number(list(range(10))*20)
#     ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20)
#     >>> pattern_number('мама')
#     ('ма', 2)
#     >>> print(pattern_number('барабан'))
#     None
#     """
#     if len(sequence) > 1:
#         count = 0
#         repeats_first = sequence.count(sequence[0])
#         if repeats_first == 1:
#             return None
#         step = len(sequence) // repeats_first
#         i = 0
#         while i + repeats_first <= len(sequence):
#             if sequence[i:i+step] == sequence[i+step: i+step*2]:
#                 i += step
#                 count += 1
#             else:
#                 break
#         if repeats_first - 1 == count:
#             return (sequence[:step], repeats_first)
#         else:
#             return None
#     else:
#         return None
# print(pattern_number([1,2]))
#print(pattern_number([1,2,3,1,2,3,1,2,3]))
#print(pattern_number(list(range(10))*20))
#print(pattern_number('мама'))
    # str_seq = ""
    # checked_style = 0
    # if type(sequence) == str:
    #     checked_style = 1
    #     str_seq = sequence
    #     sequence = []
    #     for let in str_seq:
    #         sequence.append(ord(let))
    # count = 0
    # repeats_first = sequence.count(sequence[0])
    # print(repeats_first, "dfgh", len(sequence))
    # if len(sequence) % repeats_first == 0:
    #     gen_sum = sum(sequence[0: len(sequence)//repeats_first])
    #     print(len(sequence) // repeats_first, len(sequence), repeats_first)
    #     for i in range(len(sequence) // repeats_first, len(sequence) - repeats_first, repeats_first):
    #         print ("fghjk", i + len(sequence) // repeats_first)
    #         print (i)
    #         if i + len(sequence) // repeats_first > len(sequence):
    #             count += 1
    #             break
    #         if gen_sum == sum(sequence[i: i + len(sequence) // repeats_first]):
    #             count += 1
    #             print(count)
    #             print(len(sequence) // repeats_first)
    #         else:
    #             return None
    #     print("fghj")
    #     if count == len(sequence) // repeats_first:
    #         # if checked_style == 1:
    #         #     str_to_lst = ""
    #         #     for each in sequence[0: len(sequence)//repeats_first]:
    #         #         str_to_lst += chr(each)
    #         #     sequence_str = [str_to_lst]
    #         #     return (sequence_str, repeats_first)
    #         # else:
    #         return (sequence[0: len(sequence)//repeats_first], repeats_first)
    #     else:
    #         return None
    # else:
    #     return None

    # pattern = ""
    # repeats_first = sequence.count(sequence[0])
    # lst_to_str = ""
    # res_pat = []
    # print(len(sequence) % repeats_first)
    # if len(sequence) % repeats_first == 0:
    #     for part_pat in range(len(sequence)//repeats_first):
    #         pattern += str(sequence[part_pat]) + "."
    #     for each in sequence:
    #         lst_to_str += str(each)
    #     print(lst_to_str)
    #     for part_pat_str in range(len(sequence)//repeats_first):
    #         if pattern.replace(".", "") in lst_to_str:
    #             lst_to_str.replace(pattern.replace(".", ""), "")
    #     print(lst_to_str)
    #     if lst_to_str == "":
    #         res_pat += pattern.split(".")
    #         return (res_pat, repeats_first)
    #     else:
    #         return None
    # else:
    #     return None
#print(pattern_number([1,2,3,1,2,3]))
#print(pattern_number(list(range(10))*20))
# print(pattern_number('мама'))

    # if len(lst) % 2 == 0:
    #     lst_to_str = ""
    #     for lst_el in lst:
    #         lst_to_str += lst_el
    #         for i in range(1, len(lst_el // 2) + 1):
    #             if
    #     return
    # else:
    #     return None


# ****************************************
# Problem 27
# ****************************************
# def turn_over(n, lst):
#     """(int, list) -> list
#     Reverse first n items of the list and return it. If n <= 0, return
#     the empty list. Do not consume MORE than n items of iterable.
#
#     >>> turn_over(4, ['f', 'o', 'o', 't', 'b', 'a', 'l', 'l'])
#     ['t', 'o', 'o', 'f', 'b', 'a', 'l', 'l']
#     >>> turn_over(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#     [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
#     >>> turn_over(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#     [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#     >>> turn_over(-5, [])
#     []
#     """
#     for i in range(n//2):
#         lst[i], lst[n - 1 - i] = lst[n - 1 - i], lst[i]
#     return lst

#
if __name__ == "__main__":
  import doctest
  print(doctest.testmod())
