'''
Given two DNA strands return the Hamming distance between the two DNA strands

Hamming distance is the difference between two strands of DNA

Only for sequences of equal length
If two sequences of unequal length calculate the Hamming distance over the shorter length

DS: len to compare lengths of strings, str, for loop to compare characters,
    int return number of differences aka

COMPARE THE DIFFERENCE IN CHARACTERS OF TWO DNA STRANDS
RETURN THE DIFFERENCES

    Set strand to strand
    Set count to zero
    For each character in strand and distance
        If characters are not equal to each other
            Add 1 to count
    Return count
'''

class DNA:
    def __init__(self, strand):
        self._strand = strand

    @property
    def strand(self):
        return self._strand

    def hamming_distance(self, compare):
        strand = self.strand
        count = 0

        for char1, char2 in zip(strand, compare):
            if char1 != char2:
                count += 1

        return count

