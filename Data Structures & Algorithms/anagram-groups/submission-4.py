class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for w in strs:
            sorted_word = "".join(sorted(w))
            if sorted_word in group:
                group[sorted_word].append(w)
            else:
                group[sorted_word]=[w]
        return list(group.values())