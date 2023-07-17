class Player:
    def __init__(self, speed, power, accuracy, stamina):
        self.speed = speed
        self.power = power
        self.accuracy = accuracy
        self.stamina = stamina

class Atacker(Player):
    def __init__(self, speed, power, accuracy, stamina):
        super().__init__(speed, power, accuracy, stamina)

    def goal(self):
        print('Забил гол!')

class Goalkeeper(Player):
    def __init__(self, speed, power, accuracy, stamina):
        super().__init__(speed, power, accuracy, stamina)

    def keep_goal(self):
        print('Удержал мяч и не дал забить!')

class Defender(Player):
    def __init__(self, speed, power, accuracy, stamina):
        super().__init__(speed, power, accuracy, stamina)

    def ball(self):
        print('Перехватил мяч!')

class Half_Defender(Player):
    def __init__(self, speed, power, accuracy, stamina):
        super().__init__(speed, power, accuracy, stamina)

    def assist(self):
        print('Помог забить гол!')

