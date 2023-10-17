from base import BaseDataset


class AnnotatedPaperTextDataset(BaseDataset):
    """ Wrapper class to process and produce training samples """

    def __init__(
        self,
        data_dir,
        vocab_size=None,
        vocab=None,
        seq_length=40,
        training=False,
        vocab_from_pretrained="bert-base-uncased",
        do_lower_case=True,
    ):

        self.data_dir = data_dir

    def validation(self):
        # TODO
        pass

    def train(self):
        # TODO
        pass

    def test(self):
        # TODO
        pass

    def __len__(self):
        # TODO
        pass

    def __getitem__(self, idx):
        # TODO
        pass
