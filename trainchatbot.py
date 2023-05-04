import json
from ntlk_utils import Tokenize, Stem, bag_of_words
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from Brain import NeuralNetwork

# load intents from json file
with open("C:\\Users\\Admin\\OneDrive\\Desktop\\MyVoiceAssistant\\voiceenv\\intents.json", "r") as f:
    intents = json.load(f)

# initialize lists for storing all words and tags
all_words = []
tags = []
# create tuples of patterns and tags and tokenize the patterns
# then append them to all_words and tags respectively
xy = []
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = Tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

# ignore certain words
ignore_words = ['?', '!', ',', '/', '_']
# stem all words and keep only unique words
all_words = [Stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
# sort tags alphabetically and create a list of unique tags
tags = sorted(set(tags))

# initialize lists for storing x_train and y_train
x_train = []
y_train = []
# create bag of words for each pattern_sentence and append it to x_train
# append the index of the corresponding tag to y_train
for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    x_train.append(bag)

    label = tags.index(tag)
    y_train.append(label)

# convert x_train and y_train to numpy arrays
x_train = np.array(x_train)
y_train = np.array(y_train, dtype=np.int64)


# create a custom dataset class
class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train

    # get item at given index
    # dataset[idx]
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    # get length of dataset
    def __len__(self):
        return self.n_samples


# set batch size and hyperparameters for neural network
batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(x_train[0])
learning_rate = 0.001
num_epochs = 1000

# initialize dataset and dataloader
dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)

# set device to cuda if available, otherwise cpu
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# initialize neural network
model = NeuralNetwork(input_size, hidden_size, output_size).to(device)

# define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# train the neural network
global loss
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        word_s = words.to(device)
        label_s = labels.to(device)

        output = model(word_s)
        loss = criterion(output, label_s)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # print loss every 100 epochs
    if (epoch +1) % 100 == 0:
        print(f"epoch {epoch+1}/{num_epochs}, loss={loss.item():.4f}")

# print final training loss
print(f"final loss, loss={loss.item():.4f}")

data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "hidden_size": hidden_size,
    "output_size": output_size,
    "all_words": all_words,
    "tags": tags
}

# save trained model
FILE = "ChatbotData.pth"
torch.save(data, FILE)

print(f"Traning Completed, File Saved to {FILE}")
