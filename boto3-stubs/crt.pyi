"""
Type annotations for boto3.crt module.

Copyright 2024 Vlad Emelianov
"""

import threading
from typing import Any

from botocore.client import BaseClient
from s3transfer.crt import BotocoreCRTRequestSerializer, CRTTransferManager

CRT_S3_CLIENT: CRTS3Client | None = ...
BOTOCORE_CRT_SERIALIZER: BotocoreCRTRequestSerializer | None = ...

CLIENT_CREATION_LOCK: threading.Lock = ...
PROCESS_LOCK_NAME: str = ...

def get_crt_s3_client(client: BaseClient, config: Any) -> CRTS3Client: ...

class CRTS3Client:
    def __init__(
        self, crt_client: Any, process_lock: Any, region: str, cred_provider: Any
    ) -> None: ...

def is_crt_compatible_request(client: BaseClient, crt_s3_client: CRTS3Client) -> bool: ...
def compare_identity(boto3_creds: Any, crt_s3_creds: Any) -> bool: ...
def create_crt_transfer_manager(client: BaseClient, config: Any) -> CRTTransferManager | None: ...