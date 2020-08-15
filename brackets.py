# python3

#from collections import namedtuple

#Bracket = namedtuple("Bracket", ["char", "position"])


#def are_matching(left, right):
    #return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            if(i==len(text)-1):
                return i+1

        elif next in ")]}":
            # Process closing bracket, write your code here
            if(len(opening_brackets_stack)==0):
                return i+1
            else:
                top=opening_brackets_stack.pop(len(opening_brackets_stack)-1)
                if(top=='[' and next!=']' or top=='(' and next!=')' or top=='{' and next!='}'):
                    return i+1
        
    if(len(opening_brackets_stack)!=0):
        return (text.index(opening_brackets_stack[0])+1)
    return "Success"                
                    

#def main():
text = input()
mismatch = find_mismatch(text)
# Printing answer, write your code here
print(mismatch)


#if __name__ == "__main__":
#    main()
