# intentional new finding for Cybrot Gate new-vs-base test
import os
password = "SuperSecretPassword123!"
os.system("ls " + password)  # command injection + hardcoded secret
eval(password)
