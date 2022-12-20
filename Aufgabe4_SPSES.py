#!/usr/bin/env python3
import csv
import os
import random
from enum import Enum

from numpy.core.defchararray import upper


class game_symbols(Enum):
    STONE = 1
    PAPER = 2
    SCISSORS = 3
    SPOCK = 4
    LIZARD = 5

def compare_values(symbol1, symbol2):
    winner = 0
    if symbol1 == game_symbols.STONE:
        if symbol2 == game_symbols.PAPER:
            winner = 2
        if symbol2 == game_symbols.SPOCK:
            winner = 2
        if symbol2 == game_symbols.SCISSORS:
            winner = 1
        if symbol2 == game_symbols.LIZARD:
            winner = 1
    if symbol1 == game_symbols.PAPER:
        if symbol2 == game_symbols.PAPER:
            winner = 2
        if symbol2 == game_symbols.SCISSORS:
            winner = 2
        if symbol2 == game_symbols.LIZARD:
            winner = 1
        if symbol2 == game_symbols.STONE:
            winner = 1
    if symbol1 == game_symbols.SCISSORS:
        if symbol2 == game_symbols.STONE:
            winner = 2
        if symbol2 == game_symbols.SPOCK:
            winner = 2
        if symbol2 == game_symbols.PAPER:
            winner = 1
        if symbol2 == game_symbols.LIZARD:
            winner = 1
    if symbol1 == game_symbols.LIZARD:
        if symbol2 == game_symbols.SCISSORS:
            winner = 2
        if symbol2 == game_symbols.STONE:
            winner = 2
        if symbol2 == game_symbols.PAPER:
            winner = 1
        if symbol2 == game_symbols.SPOCK:
            winner = 1
    if symbol1 == game_symbols.SPOCK:
        if symbol2 == game_symbols.LIZARD:
            winner = 2
        if symbol2 == game_symbols.PAPER:
            winner = 2
        if symbol2 == game_symbols.SCISSORS:
            winner = 1
        if symbol2 == game_symbols.STONE:
            winner = 1
    if symbol1 == symbol2:
        winner = 0
    return winner

def generate_dict():
    dict = {}
    dict["TotalPlays"] = 0
    dict["PlayerWins"] = 0
    dict["CompWins"] = 0
    dict["Tie"] = 0
    for i in game_symbols:
        dict[f"{i.name}ChosenP"] = 0
    for i in game_symbols:
        dict[f"{i.name}ChosenC"] = 0
    return dict

def insert_dict(dict, player_symbol,computer_symbol, winner):
    dict["TotalPlays"] += 1
    if winner == 1:
        dict["PlayerWins"] += 1
    elif winner == 2:
        dict["CompWins"] +=1
    else:
        dict["Tie"] +=1
    dict[f"{player_symbol.name}ChosenP"] += 1
    dict[f"{computer_symbol.name}ChosenC"] += 1


def game():
    restart = 1
    round = 1
    dict = generate_dict()
    print(str(dict))
    print("Welcome to Stone, Paper, Scissors, Lizard, Spock!")
    while restart == 1:
        print(f"Round {round}!")
        player_input = upper(input("What will you choose?"))
        print(player_input)
        player_symbol = game_symbols[str(player_input)]
        print("The Computer is choosing")
        computer_symbol = game_symbols(random.randint(1,5))
        print(f"Computer has chosen {computer_symbol.name}")
        result = compare_values(player_symbol, computer_symbol)
        if result == 1:
            print("You Win!")
        elif result == 2:
            print("Computer Wins!")
        else:
            print("Tie!")
        insert_dict(dict, player_symbol, computer_symbol, result)
        restart_question = upper(input("Restart? Y/N"))
        round += 1
        if restart_question == 'N':
            restart = 0
    print("Thank you for playing!")
    stats = dict
    return stats

def print_stats():
    saved_data = {}
    with open("statistics.csv", "r") as data:
        output = csv.DictReader(data, delimiter=";")
        for item in output:
            saved_data = item
    for item in saved_data:
        print(f"{item}: {saved_data[item]}")

def upload(dicti):
    if not os.path.exists('statistics.csv'):

        w = csv.DictWriter(open("statistics.csv", "w"), delimiter=";", fieldnames=dicti.keys())
        w.writeheader()
        w.writerow(dicti)
    else:
        saved_data = {}
        with open("statistics.csv", "r") as data:
            output = csv.DictReader(data, delimiter=";")
            for item in output:
                saved_data = item
        for key in saved_data:
            if key in dicti:
                saved_data[key] = int(saved_data[key]) + int(dicti[key])
        w = csv.DictWriter(open("statistics.csv", "w"), delimiter=";", fieldnames=dicti.keys())
        w.writeheader()
        w.writerow(saved_data)


def game_menu():
    game_running = True
    saved_stats = {}
    while game_running:
        print("PLAY, See STATISTICS, or UPLOAD data?")
        pinput = upper(input())
        if pinput == "PLAY":
            saved_stats = game()
        elif pinput == "STATISTICS":
            print_stats()
        elif pinput == "UPLOAD":
            if not saved_stats == None:
                upload(saved_stats)
        elif pinput == "END":
            print("Thank you for playing!")
            game_running = False

if __name__ == '__main__':
    game_menu()