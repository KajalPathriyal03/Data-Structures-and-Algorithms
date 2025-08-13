class Solution:

    def colorTheGrid(self, n: int, m: int) -> int:
        colStates=[]
        mod=10**9+7
        dp={}

        def generateColstates(cur_state, prev_ch, length):
            if length==n:
                colStates.append(cur_state)
                return 
            for ch in {"R", "G", "B"}:
                if prev_ch==ch:
                    continue
                generateColstates(cur_state+ch, ch, length+1)

        def solve(remaining_col, prev_ind, ln):
            if remaining_col==0:
                return 1
            if (remaining_col, prev_ind) in dp:
                return dp[(remaining_col, prev_ind)]
            ways=0
            prev_state=colStates[prev_ind]
            for i in range(ln):
                if i==prev_ind: continue

                cur_state=colStates[i]
                flag=True

                for j in range(n):
                    if prev_state[j]==cur_state[j]:
                        flag=False
                        break
                if flag:
                    ways+=(solve(remaining_col-1, i, ln))%mod
            dp[(remaining_col, prev_ind)]=(ways)%mod
            return (dp[(remaining_col, prev_ind)])%mod

        generateColstates("", "#", 0)
        ln=len(colStates)
        res=0
        for i in range(ln):
            res=(res+solve(m-1, i, ln))%mod
        
        return res




        