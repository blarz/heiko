import random
import swagger_client
from string import ascii_letters

import heiko.menu.log


### ItemsApi Functions

def list_items(auth, client):
    """
    Lists all items in the database to an admin

    :auth: dict
    :returns: bool
    """

    try:
        log(client.items_get())
    except swagger_client.rest.ApiException:
        log("Could not show items from the database.",serv="ERROR")

    return True

def consume_item(auth, client, itemid):
    """
    Sends request to the backend that user took 1 item out of the fridge

    :auth: dict
    :itemid: int
    :returns: bool
    """

    # Lets try to be a little funny
    cheers_msgs = [
        "Have fun!"
        "Well.. just hackspace things."
        "Nice loscher stuff <3"
        "Beer mh? How are your projects going?"
    ]

    try:
        client.items_item_id_consume_patch(itemid)
        menu.log(random.choice(cheers_msgs) + " Prost!", serv="SUCCESS")
        return True
    except swagger_client.rest.ApiException:
        menu.log("Not enough credits, dude.", serv="ERROR")
        return False
    except:
        menu.log("Something went wrong, contact developer!")
        return False

def create_item(auth, client):
    """
    Asks admin for details and creates new item in the backend

    :auth: dict
    :returns: bool
    """

    name = input("Name of Drink: ")
    if not all(c in ascii_letters+'-' for c in name):
        menu.log("Username not valid. Please be alphanumerical.", serv="ERROR")
        return False

    if len(name) > 32:
        menu.log("Name of item is too long (max: 32)", serv="ERROR")
        return False

    if len(name) < 3:
        menu.log("Name of item is too short (min: 3)", serv="ERROR")
        return False

    cost = float(input("Price in EUR: ")) * 100

    if cost < 0:
        menu.log("Negative price is not allowed ;)", serv="ERROR")
        return False

    try:
        client.items_post(name, cost)
    except:
        menu.log("Item could not be created in the backend", serv="ERROR")
        return False

    return True
