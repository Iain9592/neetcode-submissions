class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = []
        anagrams = dict()
        for i in strs:
            gram = ''.join(sorted(i))
            if gram in anagrams:
                anagrams[gram].append(i)
            else:
                anagrams[gram] = []
                anagrams[gram].append(i)

        return list(anagrams.values())