# import logging
# logging.basicConfig(
#     filename = "app.log",
#     level = logging.INFO,
#     format = "%(asctime)s - %(levelname)s - %(message)s"
# )

# logging.debug("This is debug message")
# logging.info("program started")
# logging.warning("low disk space dected")
# logging.error("Somthing failded")
# logging.critical("program cannot continue")



'''
\d - any single digit(0-9)
\D - any char that is not a digit
\W - any "word" char (letter, digits,underScroe)
\S - any whitespace (Space, TAb,newline)
. - any single char (Except new line)
+ - one or more of the previous thing
* - Zero or more of the previous thing
'''

import re
text = "My phone number is 979 - 069 - 2210"
match = re.search(r"\d{3}\S*-\S*\d{3}\S*-\S*\d{4}",text)
if match:
    print("found a phone number",match.group())
else:
    print("No phone mumber")
