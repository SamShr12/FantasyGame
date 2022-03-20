import random
import question


class Game:
    health = 3
    invent = {
        'Ropes': 0,
        'Food': 0,
        'Water': 0,
        'Stick': 0
    }

    questions = question.ques
    answers = question.answer

    def __init__(self):
        while self.health != 0:
            self.first_popup()
            self.quest()


    def first_popup(self):
        print(f'------------Dragon is Chasing------------')
        print(f'-----------------Survive-----------------')

    def received_items(self):
        for value in self.invent.values():
            invent_ran = random.randint(0, 4)
            invent_ran2 = random.randint(0, 4)
            invent_ran3 = random.randint(1, 5)
            invent_ran4 = random.randint(0, 3)
            print(value)

            sum1 = value + invent_ran
        # sum2 = value + invent_ran2
        # sum3 = value + invent_ran3
        # sum4 = value + invent_ran4

        self.invent['Ropes'] = sum1
        self.invent['Food'] = sum1
        self.invent['Water'] = sum1
        self.invent['Stick'] = sum1

        print(f'You have received {invent_ran2} Ropes')
        print(f'You have received {invent_ran} Food')
        print(f'You have received {invent_ran4} Water')
        print(f'You have received {invent_ran3} Water')

    def stats(self):
        if self.health == 1:
            potion = input('Do you want to consume a food?')
            if potion.lower() == 'yes':
                self.health += 1
                print(f'You have gained a heart, {self.health} remaining ')

            if potion.lower() == 'no':
                pass

        if self.health == 0:
            print(f'You died')


    def quest(self):
        length_ques = len(self.questions) - 1
        ran = random.randint(0, length_ques)
        user_answer = self.answers[ran]
        user_enter = input(self.questions[ran])

        if user_enter == user_answer:
            self.received_items()
            print(self.invent)
        else:
            self.health -= 1
            print('You have lost a heart')
            print(f'You have {self.health} hearts')

        self.stats()

c = Game()
