"""
Copyright 2024 Vlad Emelianov
"""

from boto3.session import Session

session = Session("aws_access_key_id", "aws_secret_access_key", "aws_session_token", "region_name")
session = Session(None, "aws_secret_access_key", "aws_session_token")
session = Session(123, "aws_secret_access_key", "aws_session_token")
