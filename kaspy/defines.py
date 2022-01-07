from .utils.version_control import version as ver

MAINNET = 'mainnet'
TESTNET = 'testnet'
DEVNET = 'devnet'
SIMNET = 'simnet'

DEFAULT_PORT = 16110
KASPAD_VERSION = ver(0, 11, 9)
SUBNETWORKS = (MAINNET,TESTNET,DEVNET,SIMNET)

ABORT = '[aborted]'
SUCCESS = '[successs]'

class log_messages:
        
    CHECK_NODE = lambda node : f'''[{node}]: checking node...'''
    SCANNING_FOR_NODES = f'''searching for nodes'''
    FINDING_NODES = lambda dns_server : f'''[{dns_server}]: finding nodes in dns seed server'''
    FOUND_NODES = lambda dns_server, nodes : f'''[{dns_server}]: found the following nodes: {nodes}''' 
    PORT_OPEN = lambda node : f'''[{node}]: port is OPEN {SUCCESS}'''
    PORT_CLOSED = lambda node : f'''[{node}]: port is CLOSED {ABORT}'''
    RETRIVED_NODE = lambda host, port : f'''found node @ {port}:{host}'''
    RETRIVING_SERVER_INFO = lambda node : f'''[{node}]: retriving server info '''
    OLD_VERSION_ABORT = lambda node, version, allowed_version: f'''[{node}]: running kaspad {version} minimum is {allowed_version} {ABORT}'''
    DISSALLOWED_NETWORK_ABORT = lambda node, network, allowed_networks: f'''[{node}]: running on {network}, should be one of {allowed_networks} {ABORT}'''
    PASSED_VALIDITY_CHECKS = lambda node, version, network, : f'''[{node}]: keeping connection - running {version} on {network}, all checks passed {SUCCESS}'''
    CONNECTING_TO_NODE = lambda node : f'''[{node}]: Connecting to node...'''
    CONNECTED_TO_NODE = lambda node : f'''[{node}] : Connection established'''
    CLOSING_CHANNEL = lambda node : f'''[{node}]: Closing connection...'''
    REQUEST_MESSAGE = lambda command, node : f'''[{node}]:[{command}]: Sending request..'''
    SERIALIZING_DATA = lambda node, command : f'''[{node}]:[{command}]: Serializing data...'''
    RETRIVED_MESSAGE = lambda message_type, command, node : f'''[{node}]:[{command}]: retrived response {message_type} {SUCCESS}'''
