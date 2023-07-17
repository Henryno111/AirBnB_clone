#!/usr/bin/python3
"""define unittests for models/base_model.py

Unittest classes:
    TestBaseModel_initialization
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import unittest
import os
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
import models


class TestBaseModel_initialization(unittest.TestCase):
    """represent the class to test initialization of the Base"""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_created_at_is_public(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        bm = BaseModel()
        d = datetime.today()
        d_repr = repr(d)
        bm.id = "11345"
        bm.created_at = bm.updated_at = d
        bm_repr = bm.__str__()
        self.assertIn("[BaseModel] (11345)", bm_repr)
        self.assertIn("'id': '11345'", bm_repr)
        self.assertIn("'created_at': " + d_repr, bm_repr)
        self.assertIn("'updated_at': " + d_repr, bm_repr)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    """def test_initialization_kwargs(self):
        d = datetime.today()
        d_form = d.isoformat()
        bm = BaseModel(id = "234", created_at = d_form, updated_at = d_form)
        self.assertEqual(bm.id, "234")
        self.assertEqual(bm.created_at, d_form)
        self.assertequal(bm.updated_at, d_form)"""

    def test_initialization_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


"""
    def test_initialization_with_args_and_kwargs(self):
        d = datetime.today()
        d_form = d.isoformat()
        bm = BaseModel("12", id = "234", created_at = d_form,
        updated_at = d_form)
        self.assertEqual(bm.id, "234")
        self.assertEqual(bm.created_at, d_form)
        self.assertequal(bm.updated_at, d_form)"""
