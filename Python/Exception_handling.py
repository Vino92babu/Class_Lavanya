'''
try/except block 
'''

try:
    result = 10/0
except :
    print("you can't divide by zero!")

'''
catching the exact error type
'''

try:
    num = int(input("Enter the number: "))
except ValueError:
    print("The wasn't a valid number")
finally:
    print("This always runs")
# num = int(input("Enter the number: "))
# print(num)

# try:
#     num = int ("25")
# except ValueError:
#     print("Invalid number")
# else:
#     print("Conversion number: ",num)
# finally:
#     print("This always runs")

''' 
import logging
'''
import logging
logging.basicConfig(
    filename = "app.log",
    level = logging.INFO,
    format = "%(acctime)S - %(levelname)S - %(message)"
)

logging.debug("This is debug message")
logging.info("program started")
logging.Warning("low disk space dected")
logging.error("Somthing failded")
logging.critical("program cannot continue")

