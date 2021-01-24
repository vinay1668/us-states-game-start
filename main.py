import turtle
import pandas

screen = turtle.Screen()
image='blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
player = turtle.Turtle()
player.hideturtle()

connected_states=0
guessed_states = []
missed_states=[]
while len(guessed_states) < 50:

    def msg():

        answer_state = screen.textinput(title=f'{connected_states}/50 States Connect',
                                        prompt='what is another state name?')

        return answer_state

    dummy = msg()
    answer = dummy.title()
    data = pandas.read_csv('50_states.csv')
    if answer == 'Exit':
        for state in data.values:
            if state[0] not in guessed_states:
                missed_states.append(state[0])
        df = pandas.DataFrame(missed_states)
        df.to_csv('a.csv')
        break

    if answer in data.values:
        guessed_states.append(answer)
        connected_states = connected_states + 1
        data_pos = (data[data.state == answer]).values.tolist()
        data_cor = (data_pos[0][1], data_pos[0][2])
        player.ht()
        player.penup()
        player.goto(data_cor)
        player.write(answer)

