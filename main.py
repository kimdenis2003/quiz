import csv
points = 0
with open("quiz.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
      print(row[0])
      print(row[1], row[2], row[3])
      i = input()
      if i == row[4].replace(' ', ''):
        points += 5
print("Вы набрали " + str(points) + " баллов")
if points <= 59:
  print("Ваша оценка F")
elif points > 59 and points <= 62:
  print("Ваша оценка D-")
elif points > 62 and points <= 66:
  print("Ваша оценка D")
elif points > 66 and points <= 69:
  print("Ваша оценка D+")
elif points > 69 and points <= 73:
  print("Ваша оценка C-")
elif points > 73 and points <= 76:
  print("Ваша оценка C")
elif points > 76 and points <= 79:
  print("Ваша оценка C+")
elif points > 79 and points <= 82:
  print("Ваша оценка B-")
elif points > 82 and points <= 86:
  print("Ваша оценка B")
elif points > 86 and points <= 89:
  print("Ваша оценка B+")
elif points > 89 and points <= 93:
  print("Ваша оценка A-")
elif points > 93 and points <= 100:
  print("Ваша оценка A")