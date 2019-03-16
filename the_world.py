score = 0

questions=\
  {
    "England":"London",
    "Spain":"Madrid",
    "France":"Paris",
    "Portugal":"Lisbon",
    "New Zealand":"Wellington"
    #add more Qs here
}

for question, answer in questions.items():
    response = input("What is the capital of %s?\n--->" % question)
    if response.capitalize() != answer:
        print("No, the capital of %s is %s." % (question, answer))
    else:
        print("Yes, that's correct!")
        score += 1

print("You got %d out of %d!" % (score, len(questions)))

if score < len(questions)/3:
   print("better luck next time")
else:
 print("Well Done!")
