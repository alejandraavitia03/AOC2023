word_to_digit = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None]*26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch)-ord('a')

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl.isEndOfWord


numbers = ["one", "two", "three", "four",
           "five", "six", "seven", "eight", "nine"]
t = Trie()
for n in numbers:
    t.insert(n)


values = open('Dec1\calibration-values.txt', 'r')
lines = values.readlines()
sum = 0

for line in lines:

    # list for the numbers we will find at the current line
    nums = []
    l = 0
    # In case that the line is a single digit
    #   ex: line -> 7 then sum += 77
    if len(line) == 1 and line.isdigit():
        temp = line + line
        sum += int(temp)
    # Anything longer than a single character
    elif len(line) > 1:

        for char in line:
            i = 0
            # we hit a number
            if char.isdigit():
                nums.append(char)
            # we have a letter
            else:
                size = len(line) + 1
                k = line.find(char, l)
                i = k + 1

                while (i < size):
                    temp = line[line.find(char, k): i]

                    end = temp[len(temp) - 1]

                    if end.isdigit():

                        i = size
                    elif i == len(line):
                        i = size
                    elif t.search(temp) is True:
                        nums.append(temp)
                        i = size

                    else:
                        i += 1
            l += 1

        f = nums[0]
        l = nums[-1]

        if f.isalpha():
            f = word_to_digit[f]
        if l.isalpha():
            l = word_to_digit[l]
        x = f + l
        sum += int(x)
print(sum)
