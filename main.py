import random

num=0

def generate_random_number():
  return random.randint(0-10)

def difference_from_answer(guess, answer):
  if guess < answer:
    return "Too Low"
  if guess > answer:
    return "Too High"
  

def make_a_guess(answer):
    