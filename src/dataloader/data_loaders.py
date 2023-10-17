from base import BaseTrainDataLoader
from datasets.nlp_papers import AnnotatedPaperTextDataset


class AnnotatedPaperTextDataLoader(BaseTrainDataLoader):
    """
    data loading demo using BaseDataLoader
    """

    def __init__(
        self,
        data_dir,
        batch_size,
        seq_length,
        vocab_from_pretrained=False,
        do_lower_case=False,
        vocab_size=None,
        vocab=None,
        shuffle=True,
        validation_split=0.0,
        num_workers=1,
        training=True,
    ):
        self.dataset = AnnotatedPaperTextDataset(
            data_dir=data_dir,
            vocab_size=vocab_size,
            vocab=vocab,
            seq_length=seq_length,
            vocab_from_pretrained=vocab_from_pretrained,
            do_lower_case=do_lower_case,
            training=training,
        )

        self.dataloader_kwargs = {
            "batch_size": batch_size,
            "shuffle": shuffle,
            "num_workers": num_workers,
        }
        super(AnnotatedPaperTextDataLoader, self).__init__(
            self.dataset,
            validation_split=validation_split,
            **self.dataloader_kwargs
        )

    def get_validation(self):
        return self.split_validation()
