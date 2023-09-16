from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []

        i = 0
        while i < len(words):
            # count words for one row
            cur_len = 0
            j = i
            word_lens = 0
            # while cur_len < maxWidth and (cur_len + len(words[j])) <= maxWidth:
            while j < len(words) and (cur_len + len(words[j])) <= maxWidth:
                cur_len += len(words[j])
                word_lens += len(words[j])
                j += 1
                # # last word fills exactly in the line 
                # if cur_len == maxWidth - 1:
                #     break
                # min space needed
                if j != 0:
                    cur_len += 1
            
            if j != len(words):
                row = ""
                total_spaces = maxWidth - word_lens
                if j - 1 - i> 0:
                    each_space_count = total_spaces // (j - 1 - i)
                    extra_space_count = total_spaces % (j - 1 - i)
                    while i < j:
                        row += words[i]
                        if (i + 1) != j:
                            row += " " * each_space_count
                        if extra_space_count > 0:
                            row += " "
                            extra_space_count -= 1
                        i += 1
                else:
                    # one word for a row
                    each_space_count = total_spaces
                    extra_space_count = 0
                    row += words[i]
                    row += " " * each_space_count
                    i += 1

                ret.append(row)
            else:
                row = " ".join(words[i:j])
                row += " " * (maxWidth - len(row)) 
                ret.append(row)
                return ret

        return ret
                