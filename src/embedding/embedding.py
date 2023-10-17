import torch
import torch.nn as nn

from base import BaseEmbedding


class TokenClassificationEmbedding(BaseEmbedding):
    """ Wrapper class for Token Classification embedding (encoded tokens)"""

    def __init__(self, vocab=None, name="840B", dim=100, trainable=False):
        self.vocab_size = len(vocab)
        self.vocab = vocab
        self.name = name
        self.dim = dim
        # pdb.set_trace()
        vectors = GloVe(name=self.name, dim=self.dim)
        self.weights = torch.zeros(self.vocab_size, vectors.dim)

        for i, idx in enumerate(list(self.vocab.idx2word.keys())):
            self.weights[i, :] = vectors[self.vocab[idx]]

        self.embedding = nn.Embedding(self.vocab_size, self.dim)
        self.embedding.weight.data = torch.Tensor(self.weights)

        if not trainable:
            self.embedding.weight.requires_grad = False

    def forward(self, batch):
        embeds = self.embedding(batch)
        return embeds
