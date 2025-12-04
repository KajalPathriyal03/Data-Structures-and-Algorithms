''' if number 
if char 
if [ -- before [ always there will be a number 
if ] 
'''
class Solution:
    def decodeString(self, s: str) -> str:
        number=0
        i=0
        string=""
        st=[]
        while i<len(s):
            if s[i].isdigit():
                number=number*10+int(s[i])
            elif s[i]=="[":
                st.append(string)
                st.append(number)
                number=0
                string=""
            elif s[i]=="]":
                num=st.pop()
                char=st.pop()
                string=char+num*string
            else:
                string+=s[i]
            i+=1

        return string




        