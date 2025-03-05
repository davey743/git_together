def reverse_string(str):
  ''' Reverse string str by modifying input array in-place 0(1) extra memomory '''
  left, right = 0, len(str) - 1

  while left < right:
    str[left], str[right] = str[right], str[left]

    left+= 1
    right-= 1 

  return str

str1 = ["h", "e", "l", "l", "o"]
reverse_string(str1)
print(str1)

str2 = ["H", "a", "n", "n", "a", "h"]
reverse_string(str2)
print(str2)