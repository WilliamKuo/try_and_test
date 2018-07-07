from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
    )

# Train based on the english corpus
#chatbot.train("chatterbot.corpus.english")

# Get a response to an input statement
while True:
    input_str = raw_input('question?')

    print chatbot.get_response(input_str)
