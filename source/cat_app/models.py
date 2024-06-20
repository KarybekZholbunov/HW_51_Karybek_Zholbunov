from django.db import models
import random


class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    fullness = models.IntegerField(default=40)
    happiness = models.IntegerField(default=40)
    is_sleeping = models.BooleanField(default=False)
    avatar = models.CharField(max_length=100, default='images/neutral_cat.png')

    def update_avatar(self):
        if self.happiness > 70:
            self.avatar = 'images/happy_cat.png'
        elif self.happiness > 30:
            self.avatar = 'images/neutral_cat.png'
        else:
            self.avatar = 'images/sad_cat.png'

    def feed(self):
        if not self.is_sleeping:
            self.fullness = min(self.fullness + 15, 100)
            self.happiness = min(self.happiness + 5, 100)
            if self.fullness > 100:
                self.happiness = max(self.happiness - 30, 0)
            self.update_avatar()

    def play(self):
        if self.is_sleeping:
            self.is_sleeping = False
            self.happiness = max(self.happiness - 5, 0)
        else:
            self.fullness = max(self.fullness - 10, 0)
            if random.randint(1, 3) == 1:
                self.happiness = 0
            else:
                self.happiness = min(self.happiness + 15, 100)
        self.update_avatar()

    def sleep(self):
        self.is_sleeping = True
        self.fullness = max(self.fullness - 5, 0)
        self.update_avatar()
