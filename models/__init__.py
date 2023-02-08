#!/usr/bin/python3
"""Module that executes each time that models packages is imported"""
from models.engine.file_storage
import FileStorage

storage = FileStorage()
storage.reload()