print("======================")

text = "ice cream"

print( text[0] )

# whole str can be changed
# but, python doesn't support single character change in a string
# text[0]='j'

# it include 0, exclude 3
print( text[0:3] )
print( text[4:9] )

# from 0 to end of string
print( text[0:] )

# from start to 4. exclude 5
print( text[:5] )

print("======================")

# arrangement of Quotation
text="it's good."
print( text )

text='Hello "World"'
print( text )

print("======================")

# Use of 3 Quotation
text='''Hi,
Hope tou are well.
See you soon.'''
print( text )

print("======================")

# without datatype conversation, Concatenation doesn't work
# text="House no."
# address=15
# print( text+' '+address )

# print("======================")

text="House no."
address=15
print( text+' '+str(address) )

print("======================")