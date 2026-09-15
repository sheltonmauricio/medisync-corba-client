import os
import sys
from pathlib import Path

from omniORB import CORBA
import CosNaming

ROOT_DIR = Path(__file__).resolve().parent.parent
GENERATED_DIR = ROOT_DIR / "generated"

sys.path.insert(0, str(GENERATED_DIR))

import Hospital

NAME_SERVICE_HOST = os.getenv(
    "CORBA_NAME_SERVICE_HOST"
)

NAME_SERVICE_PORT = os.getenv(
    "CORBA_NAME_SERVICE_PORT",
    "1050"
)

if not NAME_SERVICE_HOST:
    raise RuntimeError(
        "A variável CORBA_NAME_SERVICE_HOST não está configurada."
    )

NAME_SERVICE = (
    f"corbaloc::{NAME_SERVICE_HOST}:{NAME_SERVICE_PORT}/NameService"
)

def connect():
    orb = CORBA.ORB_init(
        ["-ORBInitRef", f"NameService={NAME_SERVICE}"],
        CORBA.ORB_ID,
    )

    naming_object = orb.resolve_initial_references("NameService")

    naming_context = naming_object._narrow(
        CosNaming.NamingContext
    )

    if naming_context is None:
        raise RuntimeError(
            "Não foi possível obter o NamingContext."
        )

    name = [
        CosNaming.NameComponent("HelloService", "")
    ]

    hello_object = naming_context.resolve(name)

    hello_service = hello_object._narrow(
        Hospital.HelloService
    )

    if hello_service is None:
        raise RuntimeError(
            "Não foi possível obter a referência de HelloService."
        )

    return orb, hello_service