#code to write to a csv file which can be formatted with kivy at a later stage
import pathlib
import csv

modules_loc = {'.':'Nothing Scheduled'}
start_time = 6 #time starts at 6am
next_time = 7
avail_days = [
	'monday',
	'tuesday',
	'wednesday',
	'thursday',
	'friday',
	'saturday',
	'sunday',
]
time_slot_list = []
module_per_slot = {} #dictionary for writing to csv

def fill_out_modules():
	modules = input('type module - location , \n') #Take all module names
	#split them in order to be able to determine separate values
	all_modules = modules.replace(', ', ',')
	all_modules = modules.replace('- ', '-')
	all_modules = modules.replace(' -', '-')
	all_modules = modules.replace('. ', '.')
	all_modules = modules.replace(' .', '.')
	#split modules
	all_modules = all_modules.split(',')
	for mod in all_modules:
		#split module and location
		m = mod.split('-')
		modules_loc[m[0]] = m[1]

	return modules_loc

#function to ask what needs to be put at each time
def ask_time():
	print(f'modules list: {modules_loc}')
	print(f'Planning time: {start_time}h-{next_time}h')
	user_answer = input('What module do you want put here? Enter "."" for nothing')
	return user_answer

#function to create the timetable in a csv file
def create_table():
	tt_path = pathlib.Path.cwd() / 'My_Timetable.csv'

	with open(tt_path,'w') as tt_file:
		write_tt = csv.writer(tt_file)

		head = ['Time']
		head.extend(avail_days)
		write_tt.writerow(head)



#input of data (module times etc.) need to make this less time consuming
def main():
	global start_time
	global next_time
	print(fill_out_modules())
	for day in avail_days:
		start_time = 6
		next_time = 7
		time = 6
		print('\n---------------------------')
		print(f'{day.capitalize()} timetable')
		print('---------------------------\n')
		while time < 8:
			if next_time == 24:
				next_time == 0
			time_format = f'{start_time}h-{next_time}h'

			if not time_format in time_slot_list:
				time_slot_list.append('time_format')
			chosen_module = ask_time()
			while not chosen_module in modules_loc:
				print(f'{chosen_module} is not in modules list.')
				print('Choose another module')
				chosen_module = ask_time()
			start_time += 1
			next_time += 1
			time += 1

	create_table()


if __name__ == '__main__':
	main()
