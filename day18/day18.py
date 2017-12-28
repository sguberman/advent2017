from collections import defaultdict, deque


class Duet:

    def __init__(self, instructions=None, from_file=None):
        self.registers = defaultdict(int)

        if instructions is None:
            self.instructions = []
        else:
            self.instructions = instructions

        if from_file:
            with open(from_file) as f:
                self.instructions = [line.strip() for line in f]

        self.ops = {'snd': self.snd,
                    'set': self.set,
                    'add': self.add,
                    'mul': self.mul,
                    'mod': self.mod,
                    'rcv': self.rcv,
                    'jgz': self.jgz}

        self.played = []
        self.location = 0
        self.recovered = []

    def operate(self, instruction):
        op, *args = instruction.split()
        self.ops[op](*args)

    def resolve(self, x):
        try:
            value = int(x)
        except ValueError:
            value = self.registers[x]
        return value

    def snd(self, x):
        value = self.resolve(x)
        self.played.append(value)
        self.location += 1

    def set(self, register, y):
        value = self.resolve(y)
        self.registers[register] = value
        self.location += 1

    def add(self, register, y):
        value = self.resolve(y)
        self.registers[register] += value
        self.location += 1

    def mul(self, register, y):
        value = self.resolve(y)
        self.registers[register] *= value
        self.location += 1

    def mod(self, register, y):
        value = self.resolve(y)
        self.registers[register] %= value
        self.location += 1

    def rcv(self, x):
        if self.resolve(x) != 0:
            self.recovered.append(self.played[-1])
        self.location += 1

    def jgz(self, x, y):
        if self.resolve(x) > 0:
            self.location += self.resolve(y)
        else:
            self.location += 1

    def execute_until_recovery(self):
        while not self.recovered:
            self.operate(self.instructions[self.location])
        return self.recovered[0]


class Program(Duet):

    def __init__(self, instructions=None, from_file=None, pid=0):
        super().__init__(instructions, from_file)
        self.registers['p'] = pid
        self.pid = pid
        self.sent = []
        self.outbox = []
        self.received = deque()
        self.locked = False

    def snd(self, x):
        value = self.resolve(x)
        self.sent.append(value)
        self.outbox.append(value)
        self.location += 1

    def rcv(self, x):
        try:
            self.registers[x] = self.received.popleft()
            self.location += 1
            self.locked = False
        except IndexError:
            self.locked = True

    def execute_step(self):
        if self.location not in range(len(self.instructions)):
            return 'terminated'
        self.operate(self.instructions[self.location])
        return 'locked' if self.locked else 'normal'

    def total_sent(self):
        return len(self.sent)

    def get_outbox(self):
        to_send = [x for x in self.outbox]
        self.outbox = []
        return to_send

    def add_received(self, received):
        self.received.extend(received)


class Duets:

    def __init__(self, from_file):
        self.p0 = Program(from_file=from_file, pid=0)
        self.p1 = Program(from_file=from_file, pid=1)
        self.status = ('normal', 'normal')
        self.history = [self.status]

    def send_and_receive(self):
        self.p0.add_received(self.p1.get_outbox())
        self.p1.add_received(self.p0.get_outbox())

    def run_until_termination(self):
        while 'normal' in self.status:
            self.send_and_receive()
            self.status = self.p0.execute_step(), self.p1.execute_step()
            self.history.append(self.status)
        return self.p0.total_sent(), self.p1.total_sent()


def part1():
    d = Duet(from_file='input.txt')
    first_recovered = d.execute_until_recovery()
    return first_recovered


def part2():
    d = Duets(from_file='input.txt')
    return d.run_until_termination()


if __name__ == '__main__':
    print(part1())  # 3423
    print(part2())  # (7620, 7493)
