import os
import unittest
import get_labels


class TestGetLabels(unittest.TestCase):
    def setUp(self):
        pass # Nothing for now

    def tearDown(self):
        pass # Nothing for now

    def test_get_labels(self):
        # To test the get_urls function using "test_papers.csv" file

        labels = get_labels.get_labels("test_papers.csv")

        self.assertEqual(3, len(labels))

        first_labels = labels[0]
        second_labels = labels[1]
        third_labels = labels[2]
        self.assertEqual(["Store energy","Modify/convert mechanical energy"], first_labels)
        self.assertEqual(["Attach temporarily","Manage stress/strain","Manage impact"], second_labels)
        self.assertEqual(["Manage impact","Manage shear","Prevent fracture/rupture"], third_labels)

if __name__ == '__main__':
    unittest.main()