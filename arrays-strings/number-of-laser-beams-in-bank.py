class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total_beams = 0
        prev = 0

        for row in bank:
            current_row = row.count('1')

            if current_row > 0:
                total_beams += current_row * prev

                prev = current_row
        
        return total_beams