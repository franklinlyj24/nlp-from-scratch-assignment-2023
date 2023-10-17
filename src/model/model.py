import torch
from transformers import BertForSequenceClassification

from base import BaseModel


class BertClassifier(BaseModel):
    def __init__(
        self,
        name="bert-base-uncased",
        out_dim=2,
        vocab=None,
    ):
        super().__init__()

        assert vocab is not None, "Please specify vocab"
        self.vocab = vocab
        self.vocab_size = len(self.vocab)
        self.name = name
        self.out_dim = out_dim
        self.model = BertForSequenceClassification.from_pretrained(
            self.name, num_labels=self.out_dim
        )

        # TODO: check if the following can be overriden by model.train()
        for param in self.model.parameters():
            param.requires_grad = True
        for param in self.model.classifier.parameters():
            param.requires_grad = True

        self.softmax = torch.nn.Softmax(dim=1)

    def forward(self, batch):
        input_ids, attention_mask, segment_ids = batch
        batch_size = input_ids.size(0)
        outputs = self.model(input_ids, segment_ids,
                             attention_mask, labels=None)
        logits = outputs[0]
        logits = logits.view(batch_size, -1, self.out_dim)
        out = logits[:, -1]
        out = self.softmax(out)
        return out
