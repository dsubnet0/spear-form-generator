from flask import Flask, render_template
import random
app = Flask('Spear Form Generator')

TROJAN_HORSE = ['Hands on hips','Arms folded', 'Negotiator', 'Half negotiator', 'Jack Benny']
COMBATIVES = ['Index palm', 'Rear index palm', 'SPEAR stance',
                'Full SPEAR', 'Rear up elbow','Front horizontal elbow', 
                'Downward half-SPEAR', 'Punching knee', 'Jackhammer front kick',
                'Downward full SPEAR', 'X-axis shin kick', 'Low SPEAR']

def generate_random_move_list(number_of_moves=10):
    my_list = []
    # Random number of de-escalation stances
    for d in range(random.randint(0,4)):
        next_move = ''
        next_move = random.choice(TROJAN_HORSE)
        if len(my_list)>0 and next_move == my_list[-1]: continue
        my_list.append(next_move)
        
    while len(my_list) < number_of_moves:
        next_move = ''
        next_move = random.choice(COMBATIVES)
        if len(my_list)>0 and next_move == my_list[-1]: continue
        my_list.append(next_move)
    return my_list

@app.route('/')
def index():
    move_list = generate_random_move_list()
    return render_template("index.html", move_list=move_list)

app.run(debug=True)
