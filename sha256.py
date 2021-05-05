#simple sha256 hash for the input of any string like a name or whatever
#hashlib module
import hashlib
import CapstoneMain
import CreateNameDB

Test1Word = "Test1Word"
usernum = "usernum"
presnum = "presnum"

Voter = "Capstone Project"
#send to hashing alg
HashedString = hashlib.sha256(Test1Word.encode())
HashedString = hashlib.sha256(usernum.encode())
HashedString = hashlib.sha256(presnum.encode())
#printing the hex value just to show what it actually does
#other functions can be applied other than print obviously
#whatever function to write to the wb in the excel i/o code works too
print(HashedString.hexdigest())
