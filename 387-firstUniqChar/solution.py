from typing import List

class Solution: # Quadratic
    def firstUniqChar(self, s: str) -> int:  
        for i in range(len(s)):
            l1 = s[i]
            encontrou = False
            for j in range(i+1, len(s)):
                l2 = s[j]
                if l1 == l2:
                    encontrou = True
                    break
            if not encontrou:
                return i
        return -1  # Return -1 if no unique character is found

class Solution2: # Linear
    def firstUniqChar(self, s: str) -> int:
        D = {}
        for l in s:
            if l not in D:
                D[l] = 0
            D[l] += 1
        
        for i, l in enumerate(s):
            if D[l] == 1:
                return i
        return -1  # Return -1 if no unique character is found

class Solution3: # Linear
    def firstUniqChar(self, s: str) -> int:
        def pos(l):
            return ord(l) - ord('a')        

        vet = [0] * (pos('z') - pos('a') + 1)     
   
        for l in s:
            vet[pos(l)] += 1

        for i, l in enumerate(s):
            if vet[pos(l)] == 1:
                return i
        return -1  # Return -1 if no unique character is found

def main():
    # Create an instance of Solution
    sol = Solution()
    
    # Call the firstUniqChar method and print the result
    resultado = sol.firstUniqChar("leetcode")
    print(resultado)  # Expected output: 0

if __name__ == "__main__":
    main()
