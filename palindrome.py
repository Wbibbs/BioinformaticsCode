mystring = input()
start = int(input())
end = int(input())
Y = mystring[start:(end+1):]

offset = 0
palindrome = Y

while True:
  offset += 1
  start -= 1
  end += 1
  if start < 0 or end >= len(mystring):
    if offset == 1:
      offset = 0
    break
  if mystring[start] == 'A' and mystring[end] == 'T':
    palindrome = 'A' + palindrome + 'T'
  elif mystring[start] == 'T' and mystring[end] == 'A':
    palindrome = 'T' + palindrome + 'A'
  elif mystring[start] == 'C' and mystring[end] == 'G':
    palindrome = 'C' + palindrome + 'G'
  elif mystring[start] == 'G' and mystring[end] == 'C':
    palindrome = 'G' + palindrome + 'C'
  else:
    offset -= 1
    break

print('Y =',Y,'\n')

if offset == 0:
  print('There is no palindrome with center Y')
else:
  print('There is a palindrome with center Y')
  print('Palindrome: ',palindrome)
print('Length of palindromic sequences =',offset)
