from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur_words, num_letters = [], 0
        for w in words:
            if num_letters + len(w) + len(cur_words) > maxWidth:
                for i in range(maxWidth - num_letters):
                    cur_words[i % (len(cur_words)-1 or 1)] += ' '
                res.append(''.join(cur_words))
                cur_words, num_letters = [], 0
            cur_words.append(w)
            num_letters += len(w)
        return res + [' '.join(cur_words).ljust(maxWidth)]
