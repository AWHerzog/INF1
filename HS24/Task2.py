from unittest import TestCase
 
def validate(it):
    if len(it) < 10:
        return False
    
    foo = "".join([c.lower() for c in it if c.isalnum()])

    foobar = [c.lower() for c in foo if c in ["p", "P", "a", "A", "s", "S","w", "W", "o", "O", "r", "R", "d", "D"]]

    if ['p', 'a', 's', 's', 'w', 'o', 'r', 'd'] in foobar:
        return False
    
    return True
    

print(validate("helloworldPassword"))
    

 
class PasswordValidatorTests(TestCase):
    
    def test_length_valid(self):
        self.assertTrue(validate("Long enough"))
 
    def test_length_invalid(self):
        self.assertFalse(validate("too short"))
 
    def test_uppercase_valid(self):
        self.assertTrue(validate("Has uppercase characters"))
 
    def test_uppercase_invalid(self):
        self.assertFalse(validate("no uppercase characters"))
 
    def test_contains_password(self):
        self.assertFalse(validate("contains Password"))
 
    def test_contains_password_casing(self):
        self.assertFalse(validate("contains pASSword"))