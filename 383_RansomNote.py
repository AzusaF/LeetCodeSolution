class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        matchingIndex = [False]*len(ransomNote)

        if len(ransomNote) > len(magazine):
            return False
        
        for i in range(0,len(ransomNote),1):
            # print("i:",i)
            for j in range(0,len(magazine),1):
                # print(len(magazine))
                # print(magazine)
                # print("j:",j)
                if ransomNote[i] == magazine[j]:
                    matchingIndex[i] = True
                    magazine = magazine[0:j]+ magazine[j+1:len(magazine)]
                    # print("matched")
                    break
        for i in range(0,len(ransomNote),1):
            if matchingIndex[i] == False:
                return False
        return True