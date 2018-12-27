class Unit:

    def __init__(self, units, hp, immune, weak, attackDamage, attackType, initiative):
        self.units = units
        self.hp = hp
        self.immune = immune
        self.weak = weak
        self.attackDamage = attackDamage
        self.attackType = attackType
        self.initiative = initiative

    def __repr__(self):
        return str(self.units) + " " + str(self.hp) + " " + str(self.immune) + " " + str(self.weak) + " " + str(self.attackDamage) + " " + attackType + " " + str(self.initiative)
    
    @property
    def efp(self):
        return self.units * self.attackDamage

    def damagePotential(self, enemy):
        if self.attackType in enemy.immune:
            return 0
        p = self.efp
        if self.attackType in enemy.weak:
            p *= 2
        return p
    
    def attack(self, other):
        unitsDead = self.damagePotential(other) // other.hp
        other.units = max(other.units-unitsDead, 0)
        return unitsDead
    
    def copy(self):
        return Unit(self.units, self.hp, self.immune, self.weak, self.attackDamage, self.attackType, self.initiative)

# Input parsing and representation

antibodies = []
infection = []

immuneSystem = True

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input24.txt", "r") as input:
    for line in input:
        if line == "Infection:\n":
            immuneSystem = False
        d = line.split()
        if not (d == ["Immune", "System:"] or d == ["Infection:"] or d == []):
            units = int(d[0])
            hp = int(d[4])
            immune = []
            weak = []
            # This is where the weakness and immunity
            # parentheses *might* start
            i = 7
            while d[i] != "with":
                if "weak" in d[i]:
                    i += 2
                    while not (";" in d[i] or ")" in d[i]):
                        weak.append(d[i][:-1])
                        i += 1
                    weak.append(d[i][:-1])
                    i += 1
                if "immune" in d[i]:
                    i += 2
                    while not (";" in d[i] or ")" in d[i]):
                        immune.append(d[i][:-1])
                        i += 1
                    immune.append(d[i][:-1])
                    i += 1
            attackDamage = int(d[i+5])
            attackType = d[i+6]
            initiative = int(d[-1])

            n = Unit(units, hp, immune, weak, attackDamage, attackType, initiative)
            if immuneSystem:
                antibodies += [n]
            else:
                infection += [n]

# Sorts a list of units by effective power.
def sortEFP(units):
    for passesLeft in range(len(units)-1, 0, -1):
        for index in range(passesLeft):
            if units[index].efp < units[index + 1].efp:
                units[index], units[index + 1] = units[index + 1], units[index]
            elif units[index].efp == units[index+1].efp:
                if units[index].initiative < units[index+1].initiative:
                    units[index], units[index + 1] = units[index + 1], units[index]

def trial(antibodies, infection):
    antibodies = [a.copy() for a in antibodies]
    infection = [i.copy() for i in infection]

    while antibodies and infection:
        sortEFP(antibodies)
        sortEFP(infection)
        # Targeting phase
        # antibody targeting
        iTargets = infection.copy()
        attacks = []
        for a in antibodies:
            m = 0
            mCandidate = None
            for t in iTargets:
                dmg = a.damagePotential(t)
                if dmg > m:
                    m = dmg
                    mCandidate = t
                # Tiebreakers
                elif dmg == m and mCandidate != None:
                    if t.efp > mCandidate.efp:
                        mCandidate = t
                    elif t.efp == mCandidate.efp:
                        if t.initiative > mCandidate.initiative:
                            mCandidate = t
            if m != 0:
                iTargets.remove(mCandidate)
                attacks.append([a, mCandidate])
        # infection targeting
        aTargets = antibodies.copy()
        for a in infection:
            m = 0
            mCandidate = None
            for t in aTargets:
                dmg = a.damagePotential(t)
                if dmg > m:
                    m = dmg
                    mCandidate = t
                # Tiebreakers
                elif dmg == m and mCandidate != None:
                    if t.efp > mCandidate.efp:
                        mCandidate = t
                    elif t.efp == mCandidate.efp:
                        if t.initiative > mCandidate.initiative:
                            mCandidate = t
            if m != 0:
                aTargets.remove(mCandidate)
                attacks.append([a, mCandidate])
        # Attack phase
        
        attacks = sorted(attacks, key=lambda a: -a[0].initiative)

        totalAttack = 0
        for a in attacks:
            totalAttack += a[0].attack(a[1])
            for a in antibodies:
                if a.units == 0:
                    antibodies.remove(a)
            for i in infection:
                if i.units == 0:
                    infection.remove(i)
        if totalAttack == 0:
            return 0
        
    total = 0
    for a in antibodies:
        total += a.units
    return total

def boost(antibodies, b):
    for a in antibodies:
        a.attackDamage += b

total = 0

while trial(antibodies, infection) == 0:
    total += 1
    boost(antibodies, 1)

print(trial(antibodies, infection))