'''
Given a decimal number return their Roman number equivalent

    Set ones to 1s place and return value at key 1s
    Set tens to 10s place and return value at key 10s subtract ones
    Set hundreds to 100s place and return value at key 100s subtract ones and tens
    Set thousaands to 1000s place and return value at key 1000s subtract ones, tens, and thousands

    Return concatenated thousands, hundreds, tens, and ones

'''

class RomanNumeral:
    NUMBER_TO_ROMAN = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        20: "XX",
        30: "XXX",
        40: "XL",
        50: "L",
        60: "LX",
        70: "LXX",
        80: "LXXX",
        90: "XC",
        100: "C",
        200: "CC",
        300: "CCC",
        400: "CD",
        500: "D",
        600: "DC",
        700: "DCC",
        800: "DCCC",
        900: "CM",
        1000: "M",
        2000: "MM",
        3000: "MMM",
    }
    
    def __init__(self, number):
        self._number = number

    @property
    def number(self):
        return self._number

    def to_roman(self):
        NUMBER_TO_ROMAN = RomanNumeral.NUMBER_TO_ROMAN
        ones = self.number % 10
        tens = self.number % 100 - ones
        hundreds = self.number % 1000 - tens - ones
        thousands = self.number % 10000 - hundreds - tens - ones

        return (
            NUMBER_TO_ROMAN.get(thousands, "") + 
            NUMBER_TO_ROMAN.get(hundreds, "") + 
            NUMBER_TO_ROMAN.get(tens, "") + 
            NUMBER_TO_ROMAN.get(ones, "")
        )