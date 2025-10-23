import unittest
import os
import json
from todo import TodoList

class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.filename = "test_todos.json"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_add_and_list_todos(self):
        todo_list = TodoList(self.filename)
        self.assertEqual(todo_list.list_todos(), [])
        todo_list.add_todo("Test task 1")
        self.assertEqual(len(todo_list.list_todos()), 1)
        self.assertEqual(todo_list.list_todos()[0]['task'], "Test task 1")

    def test_save_and_load_from_file(self):
        todo_list1 = TodoList(self.filename)
        todo_list1.add_todo("Test task 2")

        todo_list2 = TodoList(self.filename)
        self.assertEqual(len(todo_list2.list_todos()), 1)
        self.assertEqual(todo_list2.list_todos()[0]['task'], "Test task 2")

    def test_load_from_nonexistent_file(self):
        todo_list = TodoList("nonexistent.json")
        self.assertEqual(todo_list.list_todos(), [])

    def test_load_from_invalid_json_file(self):
        with open(self.filename, 'w') as f:
            f.write("invalid json")

        todo_list = TodoList(self.filename)
        self.assertEqual(todo_list.list_todos(), [])

if __name__ == '__main__':
    unittest.main()
