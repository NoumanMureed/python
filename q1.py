from datetime import date

def ask_for_date(name):
    # Getting date input and checking exception
    data = input('Enter ' + name + ' (dd/mm/yyyy): ').split('/')
    try:
        return date(int(data[2]), int(data[1]), int(data[0]))
    except Exception as e:
        print(e)
        print('Invalid input. Follow the given format')
        ask_for_date(name)


def calculate_age():
    # Calculating Age
    born = ask_for_date('your date of birth')
    today = date.today()
    #extra_year = 1 if ((today.month, today.day) < (born.month, born.day)) else 0
    #aaa = today.year - born.year - extra_year
    aaa = today.year - born.year-((today.month, today.day) < (born.month, born.day))
    if(born.day == today.day and born.month == today.month):
      print("Happy Birthday")
    return aaa

bbb = calculate_age()
print("Your Age =",bbb)