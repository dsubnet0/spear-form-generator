from flask import Flask, render_template
import random
app = Flask('Spear Form Generator')

ALL_MOVES = ['Hands on hips','Arms folded', 'Negotiator', 'Index palm']

def generate_random_move_list(number_of_moves=10):
    my_list = []
    while len(my_list) < number_of_moves:
        next_move = ''
        next_move = random.choice(ALL_MOVES)
        if len(my_list)>0 and next_move == my_list[-1]: continue
        my_list.append(next_move)
    return my_list

@app.route('/')
def index():
    move_list = generate_random_move_list()
    return render_template("index.html", move_list=move_list)

app.run(debug=True)
