"""Part of the stretch goal solution."""


import unicodedata
import unittest

import mp5


class StringCompareTest(unittest.TestCase):
    
    # English cases.
    
    def testEnglishIdentity(self):
        self.assertTrue(mp5.string_compare("hot dog", "hot dog"))
    
    def testEnglishCaseIdentity(self):
        self.assertTrue(mp5.string_compare("Bibimbap", "bibimbap"))
        
    def testEnglishNonIdentity(self):
        self.assertFalse(mp5.string_compare("ssam", "kama"))
        
    # Estonian cases.
    
    def testEstonianIdentity(self):
       self.assertTrue(mp5.string_compare("kiluvõileib", "kiluvõileib"))
                         
    def testEstonianUnicodeIdentity(self):
        nfc = unicodedata.normalize("NFC", "kiluvõileib")
        nfd = unicodedata.normalize("NFD", "kiluvõileib")
        self.assertTrue(mp5.string_compare(nfc, nfd))
                         
    # Korean cases.
                         
    def testKoreanIdentity(self):
        self.assertTrue("비빔밥", "비빔밥")
    
    def testKoreanUnicodeIdentity(self):
        nfc = unicodedata.normalize("NFC", "쌈")
        nfd = unicodedata.normalize("NFD", "쌈")
        self.assertTrue(mp5.string_compare(nfc, nfd))


if __name__ == "__main__":
   unittest.main()
