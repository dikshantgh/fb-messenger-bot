from datetime import datetime


def chat_bot(tokens):

	if 'who' in tokens:
		return "i am dikshant's creation"

	if "hello" in tokens or "hi" in tokens:		
		return ".This is me dikshant's chatter bot. I'am at testing phase. Currently Dikshant is unavailable. So, type 'facebook', 'twitter', or 'instagram' for links!" 

	if 'time' in tokens:
		return (str(datetime.now())[:16])

	if 'color' in tokens:
		return "colorless" 

	if "what" in tokens or "name" in tokens:
		return "my name is dikshant chat bot. I am here for assistance."

	if 'dikshant' in tokens:
		return "he is my developer"

	if 'capital' in tokens and 'nepal' in tokens:
		return "kathmandu"

	if 'dikshant' in tokens :
		return " He is my developer. "

	else:
		return "not in dikshant's database. Try next word. I am in testing phase"
