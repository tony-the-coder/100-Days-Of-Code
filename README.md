# Basic Python Review

A Python review using the 100 Days of Code from Udemy. 
I did learn a few new things and shortcuts.
This repo is mostly for practice and so I can
go and look up something I forgot how to do. 


## Basic list comprehension



### With a range and doubling the items in the range
```
my_range = [x*2 for x in range(1,5)]
print(my_range)
```

### Basic comprehension with a conditional
```
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

names_list = [name for name in names if len(name) < 5 ]
print(names_list)
```

The basic format of a list comprehension is 
```new_list = [new_item for item in list]```

## Basic dictionary comprehension

```
new_dict = {new_key:new_value for (key, value() in dict.items() if test}
```

### Using a random number as a value
```
student_scores = {student:random.randint(1,100) for student in names}
student_scores
passed_students = {students:score for (students, score) in student_scores.items() if score >=60}
passed_students
```

### Basic math with an C to F conversion
```
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:((temp * 9/5)+32) for (day, temp) in weather_c.items()}

print(weather_f)
```

### With Panda DataFrances

```
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:((temp * 9/5)+32) for (day, temp) in weather_c.items()}

print(weather_f)


for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)

```