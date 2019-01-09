import random
import swagger_client
from tabulate import tabulate

from heiko.utils import log


### ItemsApi Functions

def show_item(auth, client, itemid):
    """
    Shows detail of a single item
    :auth: dict
    :client: item_client object
    :returns: bool
    """

    log(client.items_item_id_get(itemid).to_dict())
    return True

def delete_item(auth, client):
    """
    Deletes an item from the backend
    :auth: dict
    :client: item_client object
    :returns: bool
    """

    itemid = input("What item (ID)?: ")

    item_name = client.items_item_id_get(itemid).to_dict()["name"]

    really_delete = input("Do you really want to delete %s? (y/n): " % item_name).lower()[0]

    if really_delete != 'y':
        log("Aborted")
        return False

    try:
        client.items_item_id_delete(itemid)
        log("Item with id %s was deleted" % itemid, serv="SUCCESS")
        return True
    except:
        log("Could not delete item with id %s" % itemid, serv="ERROR")
        return False


def list_items(auth, client):
    """
    Lists all items in the database to an admin

    :auth: dict
    :returns: bool
    """

    try:
        items = client.items_stats_get()
    except swagger_client.rest.ApiException:
        log("Could not show items from the database.",serv="ERROR")

    it = []
    for i in items:
        d = i.to_dict()
        it.append([d["id"], float(d["cost"])/100, d["name"], d["consumed"]])

    log(tabulate(it, headers=["ID", "Cost (EUR)", "Drink", "Consumptions"], tablefmt="presto"))


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
        "Have fun!",
        "Well.. just hackspace things.",
        "Nice loscher stuff <3",
        "Beer mh? How are your projects going?",
    ]

    try:
        client.items_item_id_consume_patch(itemid)

        # TODO: Temp hack to display correct credits in banner
        cost = float(client.items_item_id_get(itemid).to_dict()["cost"])
        auth["user"]["credits"] = auth["user"]["credits"] - cost

        log(random.choice(cheers_msgs) + " Cost: %.2f Euro. Prost!" % (cost / 100), serv="SUCCESS")
        return True
    except swagger_client.rest.ApiException:
        log("Not enough credits, dude.", serv="ERROR")
        return False
    except:
        log("Something went wrong, contact developer!", serv="ERROR")
        return False

def create_item(auth, client):
    """
    Asks admin for details and creates new item in the backend

    :auth: dict
    :returns: bool
    """

    name = input("Name of Drink: ")
    if name.isalnum() is False:
        log("Username not valid. Please be alphanumerical.", serv="ERROR")
        return False

    if len(name) > 32:
        log("Name of item is too long (max: 32)", serv="ERROR")
        return False

    if len(name) < 3:
        log("Name of item is too short (min: 3)", serv="ERROR")
        return False

    cost = float(input("Price in EUR: ")) * 100

    if cost < 0:
        log("Negative price is not allowed ;)", serv="ERROR")
        return False

    try:
        client.items_post(name, int(cost))
        log("Successfully added new item with name %s and cost %s" % (name, cost), serv="SUCCESS")
    except:
        log("Item could not be created in the backend", serv="ERROR")
        return False

    return True
