import random
lst = [random.randint(1,20) for _ in range(10)] # ქმნის და ინახავს random მონაცემებს [1,4,2,3,6,5]
print(lst)


# ვიღებთ ლისტში მყოფ 3 უდიდეს რიცხვს
max_numbers = sorted(lst)[-3:]

# დაბეჭდავს ლისტში მყოფ 3 უდიდეს რიცხვებს
print(max_numbers)