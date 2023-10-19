#!/usr/bin/python3
import unittest
import tempfile
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Create a temporary JSON file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()
        self.temp_file_path = self.temp_file.name

    def tearDown(self):
        # Remove the temporary JSON file after testing
        os.remove(self.temp_file_path)

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


if __name__ == "__main__":
    unittest.main()
