class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        #take each string in the array, mark its length
        for word in strs:
            measure = str(len(word))
            marker = "!"

            encoded += measure
            encoded += marker 
            encoded += word

        return encoded



    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):
        #format: 1!word
        #to decode, create a slice of size [:n]

    
        #where n is the number before the marker
        #for [:n] add that portion to the list
      
            start = i

            while i < len(s) and s[i] != "!":
                i += 1

            length = int(s[start:i])
            i += 1  # skip marker
            
            word = s[i:i + length]
                
            result.append(word)

            i += length
            
        return result