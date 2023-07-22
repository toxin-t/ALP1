'''
In these tasks you will be given one or more examples of code.

- Look at each example , study it carefully.
- Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms list, item and index in your predictions.
- Run the code, compare what happens to your prediction.
- Add comments to note down and differences between your prediction and what actually happened.

'''

# Example Code 1 this code prints the entire list, followed by the second item in the list. The list is then modified by appending the word "life" to the end and replacing the fifth item ("bright") with "sunny"

Sentence = ["Always", "look", "on", "the", "bright", "side", "of",]
print(Sentence)
print(Sentence[1])
Sentence.append("life")
Sentence[4] = "sunny"
print(Sentence[4])
print(Sentence[0] + " " + Sentence[3])
print(Sentence)