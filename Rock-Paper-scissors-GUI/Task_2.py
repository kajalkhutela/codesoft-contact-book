import random 
import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.config(bg='#f0f8ff')
root.geometry("400x400")
root.resizable(False,False)

choices=['rock','paper','scissor']
user_score=0
computer_score=0

def computer_choice():
    return random.choice(choices)
def decide_winner(user_choice):
    global user_score,computer_score
    comp_choice = computer_choice()
    # result= ""
    if user_choice==comp_choice:
        result="It's a Tie!"

    elif((user_choice=='rock' and comp_choice=='scissor')or (user_choice=='scissor' and comp_choice=='paper') or (user_choice=='paper' and comp_choice=='rock')):
        result='You win🎉🎉!'
        user_score+=1
    else:
        result='Computer Wins!😔'
        computer_score+=1

    result_label.config(text=f"computer chose: {comp_choice}\n{result}",fg='darkblue')
    score_label.config(text=f"score - You: {user_score} computer: {computer_score}",fg='green')
    play_again_button.pack(pady=10)


def reset_game():
    global user_score,computer_score
    user_score=0
    computer_score=0
    result_label.config(text='',fg='black')
    score_label.config(text=f"score- You: 0 | computer: 0")
    play_again_button.pack_forget()


title_label=tk.Label(root, text='Rock Paper Scissor',font=('Helveticoa', 18, 'bold'), bg='#f0f8ff',fg='#333')
title_label.pack(pady=15)
rock_button= tk.Button(root, text='Rock', width=15,  bg='lightblue',command=lambda: decide_winner('rock'))
rock_button.pack(pady=5)
paper_button= tk.Button(root,text='Paper', width=15, bg='lightblue',command=lambda: decide_winner('paper'))
paper_button.pack(pady=5)
scissor_button= tk.Button(root, text='Scissor', width=15, bg='lightblue', command=lambda: decide_winner('scissor'))
scissor_button.pack(pady=5)

result_label=tk.Label(root, text='',font=('Arial',14),bg='#f0f8ff',fg='darkblue',justify='center')
result_label.pack(pady=20)
score_label=tk.Label(root,text='score- you: 0 computer: 0', font=('Arial',12),bg="#f0f8ff",fg='darkblue')
score_label.pack(pady=10)

play_again_button= tk.Button(root,text='Play Again',command=reset_game,font=('Helvetica',12),bg='#f0f8ff',fg='black',width=20)
play_again_button.pack(pady=10)

root.mainloop()
