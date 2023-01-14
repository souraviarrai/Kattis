import calendar
weeks = {
            "0":"Monday",
			"1":"Tuesday",
			"2":"Wednesday",
			"3":"Thursday",
			"4":"Friday",
			"5":"Saturday",
			"6":"Sunday"
}

day,month = map(int,input().split())
n = str(calendar.weekday(2009, month, day))
print(weeks.get(f'{n}'))
