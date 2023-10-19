#!/usr/bin/python3
import unittest
import tempfile
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def test_new_and_all(self):
        storage = FileStorage()
        # Create a sample object
        sample_obj = BaseModel()
        sample_obj.id = "sample_id"
        storage.new(sample_obj)

        # Check if the object was added
        self.assertEqual(storage.all(), {"SampleObject.sample_id": sample_obj})

    def test_save_and_reload(self):
        storage = FileStorage()
        # Create a sample object
        sample_obj = BaseModel()
        sample_obj.id = "sample_id"
        storage.new(sample_obj)

        # Save the objects to the temporary file
        storage.save()

        # Create a new storage instance to test reload
        new_storage = FileStorage()
        new_storage.reload()

        # Check if the reloaded object matches the original object
        self.assertEqual(new_storage.all(), {"SampleObject.sample_id": sample_obj})

    def test_save(self):
        storage = FileStorage()
        # Create a sample object
        sample_obj = BaseModel()
        sample_obj.id = "sample_id"
        storage.new(sample_obj)

        # Save the objects to the temporary file
        storage.save()

        self.assertTrue(os.path.exists(storage.__file_path))


if __name__ == "__main__":
    unittest.main()
