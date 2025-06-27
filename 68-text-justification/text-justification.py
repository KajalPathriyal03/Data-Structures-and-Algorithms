class Solution:
    def fullJustify(self, words: List[str], mx: int) -> List[str]:
        res=[]
        line, length=[], 0
        i=0
        while i<len(words):
            if length+len(words[i])+len(line)>mx:
                # Line complete
                extra_space=mx-length
                space=extra_space // max(1, len(line)-1)
                reminder=extra_space%max(1, len(line)-1)
                for j in range(max(1, len(line)-1)):
                    line[j]+=" "*space
                    if reminder:
                        line[j]+=" "
                        reminder-=1
                res.append("".join(line))
                line, length=[], 0
            line.append(words[i])
            length+=len(words[i])
            i+=1

        # handling last line
        last_line=" ".join(line)
        trail_spaces=mx-len(last_line)
        last_line+=" "*trail_spaces
        res.append(last_line )
        return res
        