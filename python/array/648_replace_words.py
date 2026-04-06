# Time Complexity: O(n * m)
# Space Complexity: O(d + n)

from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root_set = set(dictionary)
        words = sentence.split()

        for i in range (len(words)):
            for j in range(1, len(words[i]) + 1):
                prefix = words[i][:j]
                if prefix in root_set:
                    words[i] = prefix
                    break

        
        return " ".join(words)