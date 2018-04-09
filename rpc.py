import random
import time
import sys
from operator import itemgetter
import pickle

class Game:
    """A game of Rock/Paper/Scissors"""

    rounds = 0
    wins = 0
    ties = 0
    losses = 0

    human = ""
    computer = ""

    def __init__(self):
        print("\n\
        ##################################\n\
        ####.ROCK.PAPER.SCISSORS.#########\n\
        ##########.BY.MATIAS.RAISANEN.####\n\
        #########################.2018.###\n\
        ##matias.raisanen@gmail.com#######\n\
        ")
        self.name = input("What is your name? ")

    def score(self):
        #100pts for win, 10pts for tie. -100pts for loss. Then multiply by win rate + 1
        score = int(((self.wins*100  + self.ties*10) - self.losses*100) * ((self.wins/self.rounds)+1))
        return score


    def hiScoreExists(self):
        emptylist = []
        try:
            hiscore = open("hiscore_ksp.txt", 'rb')
            hiscore.close()
        except IOError:
            hiscore = open("hiscore_ksp.txt", 'wb')
            pickle.dump(emptylist, hiscore)
            hiscore.close()

    def saveHiScore(self):
        high_scores = []
        self.hiScoreExists()

        with open('hiscore_ksp.txt', 'rb') as f:
            high_scores = pickle.load(f)
        score = self.score()

        high_scores.append((self.name, self.rounds, self.wins, self.losses, self.ties, score))

        high_scores = sorted(high_scores, key=itemgetter(5),reverse=True)[:10]

        with  open("hiscore_ksp.txt","wb") as hiscore:
            pickle.dump(high_scores, hiscore)

    def readHiScore(self):
        high_scores = []
        self.hiScoreExists()
        print("######################.HIGH.SCORES.######################")
        rowNum = 1
        with open('hiscore_ksp.txt', 'rb') as f:
            high_scores = pickle.load(f)

        for i in high_scores:
            name, rounds, wins, losses, ties, score = i
            print(str(rowNum)+".",name,"| Rounds:",rounds,"| Wins:",wins,"| Losses:",losses,"| Ties:",ties,"| Score:",score)
            rowNum += 1
        print("######################.HIGH.SCORES.######################")
        print("\n")


    def win(self):
        """Win a round"""
        self.wins += 1
        print("You WIN!\n")

    def lose(self):
        """Lose a round"""
        self.losses += 1
        print("You LOSE!\n")

    def tie(self):
        """Tie a round"""
        self.ties += 1
        print("It's a TIE!\n")

    def timeCount(self):
        """Counts from three to one"""
        print("Three...")
        time.sleep(0.3)
        print("Two...")
        time.sleep(0.3)
        print("One...")
        time.sleep(0.3)
        print("\n")

    def endGame(self):
        """Exits the game"""
        if self.rounds > 0:
            print("\n")
            print("You played",self.rounds,"rounds.")
            print("Wins:",self.wins,"("+str(int((self.wins/self.rounds)*100))+"%)")
            print("Losses:",self.losses,"("+str(int((self.losses/self.rounds)*100))+"%)")
            print("Ties:",self.ties,"("+str(int((self.ties/self.rounds)*100))+"%)")
            print("Score:", self.score())
            self.saveHiScore()
        print("Thank you for playing!\n")
        sys.exit()

    def numToWord(self, value):
        """Converts a number input into a word"""
        value = str(value)
        if value == "1":
            return "rock"
        elif value == "2":
            return "paper"
        elif value == "3":
            return "scissors"
        else:
            pass

    def askUser(self):
        """Asks the user for input. Also the starting point of a new game."""
        print("Weapons:\n(1)rock\n(2)paper\n(3)scissors\n(4)HI-score\n(Type Quit to exit)")
        self.human = input("Take your pick: ")
        print("\n")
        if self.human=="Quit":
            self.endGame()
        if self.human=="1" or self.human=="2" or self.human=="3":
            self.human = self.numToWord(self.human)
            self.timeCount()
            self.newRound()
        if self.human=="4":
            self.readHiScore()

    def computerTurn(self):
        """Plays the computer's turn"""
        self.computer = random.randint(1,3)
        self.computer = self.numToWord(self.computer)

    def newRound(self):
        """Plays a new round"""
        self.rounds += 1
        self.computerTurn()
        self.checkRound()
        print("Score:",self.score())

    def roundText(self):
        """Prints round text"""
        print("Round", self.rounds)
        print("You chose: "+self.human)
        print("Computer chose: "+self.computer)

    def checkRound(self):
        """Checks the outcome of the round"""
        self.roundText()
        if self.human == self.computer:
            self.tie()
        elif (self.human == "rock" and self.computer == "paper") \
          or (self.human == "paper" and self.computer == "scissors") \
          or (self.human == "scissors" and self.computer == "rock"):
            self.lose()
        elif (self.human == "rock" and self.computer == "scissors") \
          or (self.human == "paper" and self.computer == "rock") \
          or (self.human == "scissors" and self.computer == "paper"):
            self.win()
        else:
            print("Something went wrong")

def main():
    try:
        newGame = Game()
        while True:
            newGame.askUser()
    except KeyboardInterrupt:
        print("Thank you for playing!")
    finally:
        sys.exit()


if __name__ == "__main__":
    main()
