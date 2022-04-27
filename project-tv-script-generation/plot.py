from matplotlib.pyplot import xticks
import plotly.express as px
import re


def plot(f):
    text = f.read()
    text = re.sub("\n", " ", text)
    text = re.sub(":", " ", text)
    text_list = text.split(" ")
    text_list = list(filter(None, text_list))
    epoch_list = []
    for i in range(len(text_list)):
        if text_list[i] == "Epoch":
            epoch_list.append(text_list[i + 1])

    c = 0
    for i in range(len(epoch_list)):
        suffix = ".{}".format(c)
        try:
            epoch_list[i] = re.sub("/15", suffix, epoch_list[i])
            epoch_list[i] = re.sub("/10", suffix, epoch_list[i])
            epoch_list[i] = re.sub("/20", suffix, epoch_list[i])
        except:
            print("cringe")
        c += 1
        if c == 13:
            c = 0

    # print(epoch_list)
    loss_list = []
    for i in range(len(text_list)):
        if text_list[i] == "Loss":
            loss_list.append(text_list[i + 1])
    loss_list = list(map(float, loss_list))
    fig = px.line(x=epoch_list, y=loss_list)
    fig.update_layout(
        title="Loss vs Epoch", xaxis_title="Epoch", yaxis_title="Loss"
    )
    fig.add_shape(
        type="line",
        x0=0,
        y0=3.5,
        x1=len(epoch_list),
        y1=3.5,
        line=dict(color="red", width=2),
    )
    fig.show()


plot(f=open(r"e20b128.txt", "r"))
plot(f=open(r"e15b128.txt", "r"))
plot(f=open(r"e10b128.txt", "r"))