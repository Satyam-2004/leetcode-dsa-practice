from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = Counter(s)
        
        odd_count = sum(1 for cnt in freq.values() if cnt % 2 == 1)
        if odd_count > 1:
            return ""
        
        middle = ""
        for ch, cnt in freq.items():
            if cnt % 2 == 1:
                middle = ch
                break
        
        half_len = n // 2
        half_chars = []
        for ch in sorted(freq.keys()):
            half_chars.extend([ch] * (freq[ch] // 2))
        
        def build(half_list):
            s = ''.join(half_list)
            return s + middle + s[::-1]
        
        smallest = build(half_chars)
        if smallest > target:
            return smallest
        
        target_half = target[:half_len]
        avail = Counter(half_chars)
        result = []
        
        i = 0
        matched_exactly = True
        
        while i < half_len:
            if i >= len(target_half):
                for ch in sorted(avail.keys()):
                    result.extend([ch] * avail[ch])
                matched_exactly = False
                break
            
            t_ch = target_half[i]
            
            if avail.get(t_ch, 0) > 0:
                result.append(t_ch)
                avail[t_ch] -= 1
                i += 1
            else:
                matched_exactly = False
                found = False
                for ch in sorted(avail.keys()):
                    if avail[ch] > 0 and ch > t_ch:
                        result.append(ch)
                        avail[ch] -= 1
                        for c in sorted(avail.keys()):
                            result.extend([c] * avail[c])
                        return build(result)
                
                j = len(result) - 1
                while j >= 0:
                    removed = result.pop()
                    avail[removed] += 1
                    
                    for ch in sorted(avail.keys()):
                        if avail[ch] > 0 and ch > removed:
                            result.append(ch)
                            avail[ch] -= 1
                            for c in sorted(avail.keys()):
                                result.extend([c] * avail[c])
                            return build(result)
                    j -= 1
                
                return ""
        
        pal = build(result)
        
        if pal > target:
            return pal
        
        if not matched_exactly:
            return ""
        
        j = len(result) - 1
        while j >= 0:
            removed = result.pop()
            avail[removed] += 1
            
            for ch in sorted(avail.keys()):
                if avail[ch] > 0 and ch > removed:
                    result.append(ch)
                    avail[ch] -= 1
                    for c in sorted(avail.keys()):
                        result.extend([c] * avail[c])
                    return build(result)
            j -= 1
        
        return ""