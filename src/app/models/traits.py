from abc import ABC, abstractmethod


# TODO: Find a way to use ABC when child is an sqlalchemy Model
class HasResource:
    """
    Base class indicating that the child is a Model that can be assembled and
    represented as a list of key-value pairs
    """

    @staticmethod
    def fields() -> set[str]:
        """Static function defining the properties to use"""
        raise NotImplementedError("Fields must be implemented in child class")

    @classmethod
    def from_dict(cls, data):
        self = cls()
        fields = self.fields()

        for field in filter(lambda x: x in fields, data):
            setattr(self, field, data[field])

        return self

    def to_dict(self, ofields=set()):
        fields = self.fields() | ofields
        data = {field: getattr(self, field) for field in fields}
        return data
