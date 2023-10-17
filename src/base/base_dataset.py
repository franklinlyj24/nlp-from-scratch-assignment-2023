from torch.utils.data import Dataset


class BaseDataset(Dataset):
    """ Wrapper class to process and produce training samples """

    def validation(self):
        """
        Set validation dataset
        """
        raise NotImplementedError

    def train(self):
        """
        Set train dataset
        """
        raise NotImplementedError

    def test(self):
        """
        Set test dataset
        """
        raise NotImplementedError

    def __getitem__(self, idx):
        """
        Get item

        :return: Dataset outputs
        """
        raise NotImplementedError
