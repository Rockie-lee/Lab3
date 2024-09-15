def get_username():

    username = input("Enter your desired username: ").strip()
    return username.upper()

def get_group():

    group = input("Enter the group name you'd like to join: ").strip()
    return group.upper()

def get_message():

    message = input("Enter your message: ").strip()
    return message


**Parameters:**
- (UNSURE)

**Returns:**
- (UNSURE)

**Notes:**
- (UNSURE)

## Function: join_group

**Parameters:**
- (UNSURE)

**Returns:**
- (UNSURE)

**Notes:**
- (UNSURE)

## Function: get_communication_channel

**Parameters:**
- (UNSURE)

**Returns:**
- (UNSURE)

**Notes:**
- (UNSURE)

import lab_chat as lc  # Adjust import based on your actual module

def initialize_chat():

    username = get_username()
    group = get_group()

    # Connect as a peer node
    peer_node = lc.get_peer_node()

    # Join the group
    channel = lc.join_group(peer_node, group)

    return channel

def start_chat():

    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break

    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")