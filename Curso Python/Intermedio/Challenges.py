#  * Crea un programa que funcione como una cuenta atrás.
#  *
#  * - Al iniciarlo tendrás que indicarle el día, mes, año,
#  *   hora, minuto y segundo en el que quieres que finalice.
#  * - Deberás transformar esa fecha local a UTC.
#  * - La cuenta atrás comenzará y mostrará los días, horas,
#  *   minutos y segundos que faltan.
#  * - Se actualizará cada segundo y borrará la terminal en
#  *   cada nueva representación del tiempo restante.
#  * - Una vez finalice, mostrará un mensaje.
#  * - Realiza la ejecución, si el lenguaje lo soporta, en
#  *   un hilo independiente.

# from datetime import datetime, timezone
# import os
# import time

# # Define the target date and time
# target_year = int(input("In which year do you want your countdown to end? "))
# target_month = int(input("In which month do you want your countdown to end? "))
# target_day = int(input("in which day do you want your countdown to end? "))
# target_hour = int(input("At what hour do you want your countdown to end? "))
# target_minute = int(input("At what minute do you want your countdown to end? "))
# target_second = int(input("At what second do you want your countdown to end? "))
# try:
#     target_date = datetime(target_year, target_month, target_day, target_hour, target_minute, target_second)
#     target_date = target_date.replace(tzinfo=timezone.utc)
#     target_date = target_date.astimezone(timezone.utc)

# except ValueError:
#     print("Invalid date or time format. Please try again.")
#     exit()

# while True: 
#     # Get the current date and time
#     current_date = datetime.now()

#     # Convert the target date and time to UTC
#     current_date = current_date.replace(tzinfo=timezone.utc)
#     current_date = current_date.astimezone(timezone.utc)

#     # Calculate the time difference
#     time_difference = target_date - current_date

#     # Extract days, hours, minutes, and seconds from the time difference
#     days = time_difference.days
#     hours, remainder = divmod(time_difference.seconds, 3600)
#     minutes, seconds = divmod(remainder, 60)

#     # Clear the screen
#     os.system('cls')

#     # Print the result
#     if days == 0 and hours == 0 and minutes == 0 and seconds == 0:
#         print("Time's up!")
#         break
#     print(f"Time left until {target_date}: {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds")

#     # Wait for 1 second
#     time.sleep(1)
    
    
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def IsAnagram(word_1, word_2):
    if word_1 == word_2:
        return False
    else:
        if sorted(word_1.lower()) == sorted(word_2.lower()):
            return True
        else:
            return False

def Fibonacci():
    a, b, d = 0, 1, 1
    for c in range(1, 51):
        print(f"{c}. - {a}")
        a, b = b, a + b


def IsPrime(num):
    if num == 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def HundredPrime():
    for i in range(1, 101):
        if IsPrime(i):
            print(i)

def InvertWord(word):
    chars = list(word)
    reversed = []
    for i in range(len(chars)):
        reversed.append(chars[-1 - i])
    return "".join(reversed)

print(InvertWord("Hello World"))
        