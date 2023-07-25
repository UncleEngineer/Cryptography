# -*- coding: utf-8 -*-
"""Basic Cryptography-decrypt.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nj4-HB5WrHJrBd1ercF6T44X8pU18UGv
"""

text = b'gAAAAABkv8vjWz9WPVwjYpIZVvbxyE9qzstUx68-cM-89s_CjNVVHNzI_8wYUtTr_kOtrZCHiZRB3jtbNEJ9017UVZGQWfr8Lf55Hu3xPpjk9S2_0Jhe4lse_WirR7MN_wBd1O0wShxfNWQBHj9mFu5PSGf62KEwC6Cl-SbKlgPjQJ5BvePzlbA='

key = b'K4IpscUeZGZp33unyxsyI5JcXwB6o1tkVGZ3e8gAyI8='

from cryptography.fernet import Fernet

f = Fernet(key)
message = f.decrypt(text).decode('utf-8')
print(message)

