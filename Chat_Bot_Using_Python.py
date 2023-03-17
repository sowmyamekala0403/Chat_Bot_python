from nltk.chat.util import Chat,reflections
pairs = [
    [r'hi',['hiii']],
    [r'hii|hello|heyy',["hii there"]],
    [r'how are you',['Iam good,how do you do?']],
    [r'What is your name',['My name is chatbot']],
    [r'who invented you',['I am invented by Sowmya']],
    [r'who is your Boss',['My boss is Sowmya']],
    [r'are you mad',['Nice jokee']],
    [r'which subject do you like most',['as Iam a bot I can study all subjects but you need to give a proper training for me.']],
    [r'give one sentense about python??',['Python is a simple programming language']],
    [r'What is your wish',['As iam a chat bot I dont have any wish and I dont have any feelings!!!']],
    [r'ok Byeee!!',['Byeee ,have a nice day']]

]
chat = Chat(pairs,reflections)
chat.converse()
def quit():
    print("Hii I am chatbot.Ask me something")
if __name__=="__main__":
    quit()