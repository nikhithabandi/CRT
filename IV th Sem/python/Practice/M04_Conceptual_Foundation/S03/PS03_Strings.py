
# 1)Reverse a string
# 2)Palindrome or not
# 3)Anagram
# '''
#String==>Immutable==>' ' or " " single line string
# s="python"
# # print(s.capitalize())
# s=s.capitalize()
# print(s)
'''Reverse a string'''
# def Reverse_str(s):
#     '''type-1'''
#     # res=""
#     # for ch in s:
#     #     res=ch+res 
#     # return res
#     '''type-2'''
#     # return s[::-1]
#     '''type-3'''
#     res=""
#     stop=-1*(len(s)+1)
#     for i in range(-1,stop,-1):
#         res=res+s[i]
#     return res    



# print(Reverse_str("abc"))#"cba"
# print(Reverse_str("python"))#"nohtyp"

'''Palindrome'''
# def is_palindrome(s):
#     l=0
#     r=len(s)-1
#     while l<r:
#         if s[l]!=s[r]:
#             return False
#         l+=1
#         r-=1
#     return True


# print(is_palindrome("abc"))
# print(is_palindrome("madam"))
'''Check whether the given strings are Anagrams or not'''
''' First find .frequency count of a string charector'''
def Frequency_count(s):
    d = {}
    for ch in s:
        if ch in d:
             d[ch] += 1
        else:
            d[ch] = 1
    return d
print(Frequency_count("abcabc"))#{'aa:2,'b':2,'c':2}

def is_anagram(str1,str2):
    return Frequency_count(str1)==Frequency_count(str2)
print(is_anagram("paces","space"))#true
print(is_anagram("aabbcc","abc"))#false
