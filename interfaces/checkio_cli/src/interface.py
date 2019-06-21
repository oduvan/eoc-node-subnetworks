
from handlers.simple_output import SimplePrintHandler
from server import TCPConsoleServer


class ServerController(TCPConsoleServer):
    cls_handler = SimplePrintHandler

    FUNCTION_NAMES = {
        "python_3": "subnetworks",
        "js_node": "subnetworks"
    }
    