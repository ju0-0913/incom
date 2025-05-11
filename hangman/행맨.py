import tkinter
import time
from PIL import Image
from random import *

width = 1000
height = 800

screen = tkinter.Tk()
screen.resizable(False, False)
screen.title("행맨게임")

canvas = tkinter.Canvas(screen, width=width, height=height, bg="white")
canvas.pack()

hangman_image = tkinter.PhotoImage(file="hangman.png")
canvas.create_image(500, 270, image=hangman_image)

def play_game():
    words = ["antique", "introduce", "steadily", "industry", "qualify", "absolute", "cautious", "shipment", "article", "exclusion", "storage",
             "applicant", "requirement", "professional", "interview", "consultant", "permission", "arrangement", "negative", "assignment", "accomplish",
             "responsible", "coordinate", "accessible", "replacement", "outstanding", "replacement", "outstanding", "permanently", "subsequent",
             "additional", "appreciate", "postpone", "advertisement", "advantage", "particular", "description", "equipment", "complaint", "evaluation",
             "proposal", "direction", "represent", "package", "information", "estimate", "financial", "interested", "competitor", "schedule", "greateful"]
    word = choice(words)
    answers = list("_" * len(word))
    print(answers)

    life = 7

    game_over = False

    while not game_over:
        guess_answer = input("알파벳을 입력하세요 >>> ").lower()

        if len(guess_answer) == 1 and guess_answer.isalpha():
            for i in range(len(word)):
                if word[i] == guess_answer:
                    answers[i] = guess_answer
            print(answers)

            if "_" not in answers:
                game_over = True

                screen.deiconify()
                pass_image = tkinter.PhotoImage(file="pass.png")
                canvas.create_image(490, 730, image=pass_image)
                screen.update()
                time.sleep(1.8)
                screen.withdraw()

                print("정답입니다.")

            if guess_answer not in word:
                life -= 1

                if life == 6:
                    screen.deiconify()
                    pillar = tkinter.PhotoImage(file="pillar.png")
                    canvas.create_image(650, 380, image=pillar)
                    screen.update()
                    time.sleep(1)
                    screen.withdraw()
                elif life == 5:
                    screen.deiconify()
                    face = tkinter.PhotoImage(file="face.png")
                    canvas.create_image(360, 280, image=face)
                    screen.update()
                    time.sleep(1)
                    screen.withdraw()
                elif life == 4:
                    screen.deiconify()
                    body = tkinter.PhotoImage(file="body.png")
                    canvas.create_image(360, 418, image=body)
                    screen.update()
                    time.sleep(1)
                    screen.withdraw()
                elif life == 3:
                    screen.deiconify()
                    right_arm = tkinter.PhotoImage(file="rightarm.png")
                    canvas.create_image(418, 380, image=right_arm)
                    screen.update()
                    time.sleep(1)
                    screen.withdraw()
                elif life == 2:
                    screen.deiconify()
                    left_arm = tkinter.PhotoImage(file="leftarm.png")
                    canvas.create_image(308, 390, image=left_arm)
                    screen.update()
                    time.sleep(1)
                    screen.withdraw()
                elif life == 1:
                    screen.deiconify()
                    right_leg = tkinter.PhotoImage(file="rightleg.png")
                    canvas.create_image(440, 535, image=right_leg)
                    screen.update()
                    time.sleep(1)
                    screen.withdraw()
                elif life == 0:
                    screen.deiconify()
                    left_leg = tkinter.PhotoImage(file="leftleg.png")
                    canvas.create_image(315, 535, image=left_leg)

                    screen.deiconify()
                    fail_image = tkinter.PhotoImage(file="fail.png")
                    canvas.create_image(480, 730, image=fail_image)
                    screen.update()
                    time.sleep(1.8)
                    screen.withdraw()
                    game_over = True
                    print(f"실패하였습니다.\n정답은 {word} 입니다.")
        else:
            print("오류가 발생했습니다. 알파벳을 다시 입력하세요 >>> ")

def click_menu1():
    canvas.delete("all")
    menu1.destroy()
    menu2.destroy()
    menu3.destroy()

    screen.withdraw()

    play_game()

def click_menu2():
    new_screen = tkinter.Toplevel(screen)
    new_screen.resizable(False, False)
    new_screen.title("행맨게임_게임방법")
    canvas2 = tkinter.Canvas(new_screen, width=1000, height=800, bg="white")
    canvas2.pack()

    how_to_play = tkinter.Label(new_screen, text="1) 차례대로 단어에 사용됐을 것 같은\n알파벳을 입력합니다.\n\n2) 만약 그 알파벳이 포함되어 있다면\n해당하는 밑줄에 알파벳이 채워집니다."
                                                 "\n\n3) 그렇지 않으면\n사람이 매달린 단두대부터 1획씩 그려집니다.\n\n4) 사람이 먼저 완성되면 실패하고\n단어가 먼저 완성되면 성공입니다.", bg="white", font=("Times New Roman", 36))
    how_to_play.place(x=20, y=90)

    new_screen.mainloop()

menu1 = tkinter.Button(screen, text="게임 시작", font=("Times New Roman", 20), command=click_menu1)
menu1.place(x=420, y=500)
menu2 = tkinter.Button(screen, text="게임 방법", font=("Times New Roman", 20), command=click_menu2)
menu2.place(x=420, y=570)
menu3 = tkinter.Button(screen, text="게임 종료", font=("Times New Roman", 20), command=quit)
menu3.place(x=420, y=640)

screen.mainloop()