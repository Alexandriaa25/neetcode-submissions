class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Take the input (lists of strings) loop through each, create a key based on the letters, add them to a dictionary, and add the corresponding word into the dictionary value (list)
        #group of words dictionary, key is the letter combo, value: list of words matching that combo
        groups = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)

        return list(groups.values())




       
            