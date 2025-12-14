class tool:
    def to_exit(self,UsernameList,Usernsme):
        i=0
        status=False
        while i<len(UsernameList):
            if UsernameList[i]==Usernsme:
                status=True
                break
            i += 1
        return status
