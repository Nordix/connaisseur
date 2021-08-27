from connaisseur.image import Image


class ValidatorInterface:
    def __init__(self, name: str, **kwargs):  # pylint: disable=unused-argument
        """
        Initializes a validator based on the data from the configuration file.
        """
        self.name = name

    def validate(self, image: Image, **kwargs) -> str:
        """
        Validates an admission request, using the extra arguments from the image policy.

        Returns a list of trusted digests.
        """
        raise NotImplementedError

    @property
    def healthy(self):
        raise NotImplementedError

    def __str__(self):
        return self.name