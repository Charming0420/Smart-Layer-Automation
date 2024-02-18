from web3 import Web3
import time
from web3.exceptions import TimeExhausted
from config import b_wallet_address, b_private_key, contract_address, infura_url, cat_ids_B

web3 = Web3(Web3.HTTPProvider(infura_url))
contract = web3.eth.contract(address=contract_address, abi=[{"inputs":[],"name":"InvalidInitialization","type":"error"},{"inputs":[],"name":"NotInitializing","type":"error"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"OwnableInvalidOwner","type":"error"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"OwnableUnauthorizedAccount","type":"error"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint64","name":"version","type":"uint64"}],"name":"Initialized","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":False,"internalType":"uint8","name":"level","type":"uint8"},{"indexed":False,"internalType":"uint256","name":"pointsBalance","type":"uint256"}],"name":"LevelUp","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"inviter","type":"uint256"}],"name":"acceptPlayDate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"authorisedProxyAddresses","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"canClean","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"canFeed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"canLevelUp","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"canPlay","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"catIds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"catStates","outputs":[{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint16","name":"numFeeds","type":"uint16"},{"internalType":"uint256","name":"lastFeed","type":"uint256"},{"internalType":"uint16","name":"numPlays","type":"uint16"},{"internalType":"uint256","name":"lastPlay","type":"uint256"},{"internalType":"uint16","name":"numCleans","type":"uint16"},{"internalType":"uint256","name":"lastClean","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"cleanCat","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"feedCat","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"offset","type":"uint256"},{"internalType":"uint16","name":"pageSize","type":"uint16"}],"name":"getAllCats","outputs":[{"components":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256","name":"pointsBalance","type":"uint256"}],"internalType":"struct SmartCatProxyV3.AllCatListItem[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getCatInfo","outputs":[{"components":[{"components":[{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint16","name":"numFeeds","type":"uint16"},{"internalType":"uint256","name":"lastFeed","type":"uint256"},{"internalType":"uint16","name":"numPlays","type":"uint16"},{"internalType":"uint256","name":"lastPlay","type":"uint256"},{"internalType":"uint16","name":"numCleans","type":"uint16"},{"internalType":"uint256","name":"lastClean","type":"uint256"},{"internalType":"uint256[]","name":"friends","type":"uint256[]"}],"internalType":"struct SmartCatProxyV3.CatState","name":"state","type":"tuple"},{"internalType":"uint256","name":"pointsBalance","type":"uint256"},{"internalType":"uint256","name":"actionLimitReset","type":"uint256"}],"internalType":"struct SmartCatProxyV3.CatInfo","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getCatInfo2","outputs":[{"components":[{"components":[{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint16","name":"numFeeds","type":"uint16"},{"internalType":"uint256","name":"lastFeed","type":"uint256"},{"internalType":"uint16","name":"numPlays","type":"uint16"},{"internalType":"uint256","name":"lastPlay","type":"uint256"},{"internalType":"uint16","name":"numCleans","type":"uint16"},{"internalType":"uint256","name":"lastClean","type":"uint256"},{"internalType":"uint256[]","name":"friends","type":"uint256[]"}],"internalType":"struct SmartCatProxyV3.CatState","name":"state","type":"tuple"},{"internalType":"uint256","name":"pointsBalance","type":"uint256"},{"internalType":"uint256","name":"actionLimitReset","type":"uint256"},{"internalType":"uint16","name":"actionLimitCount","type":"uint16"}],"internalType":"struct SmartCatProxyV3.CatInfo2","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getCatInfo3","outputs":[{"components":[{"components":[{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint16","name":"numFeeds","type":"uint16"},{"internalType":"uint256","name":"lastFeed","type":"uint256"},{"internalType":"uint16","name":"numPlays","type":"uint16"},{"internalType":"uint256","name":"lastPlay","type":"uint256"},{"internalType":"uint16","name":"numCleans","type":"uint16"},{"internalType":"uint256","name":"lastClean","type":"uint256"},{"internalType":"uint256[]","name":"friends","type":"uint256[]"}],"internalType":"struct SmartCatProxyV3.CatState","name":"state","type":"tuple"},{"internalType":"uint256","name":"pointsBalance","type":"uint256"},{"internalType":"uint256","name":"actionLimitReset","type":"uint256"},{"internalType":"uint16","name":"actionLimitCount","type":"uint16"},{"internalType":"bool","name":"canFeed","type":"bool"},{"internalType":"bool","name":"canPlay","type":"bool"},{"internalType":"bool","name":"canClean","type":"bool"},{"internalType":"bool","name":"canLevelUp","type":"bool"}],"internalType":"struct SmartCatProxyV3.CatInfo3","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getCatState","outputs":[{"components":[{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint16","name":"numFeeds","type":"uint16"},{"internalType":"uint256","name":"lastFeed","type":"uint256"},{"internalType":"uint16","name":"numPlays","type":"uint16"},{"internalType":"uint256","name":"lastPlay","type":"uint256"},{"internalType":"uint16","name":"numCleans","type":"uint16"},{"internalType":"uint256","name":"lastClean","type":"uint256"},{"internalType":"uint256[]","name":"friends","type":"uint256[]"}],"internalType":"struct SmartCatProxyV3.CatState","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getConfig","outputs":[{"internalType":"uint256[3]","name":"","type":"uint256[3]"},{"internalType":"uint16[3]","name":"","type":"uint16[3]"},{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getConfig2","outputs":[{"internalType":"uint256[3]","name":"","type":"uint256[3]"},{"internalType":"uint16[3]","name":"","type":"uint16[3]"},{"internalType":"uint8","name":"","type":"uint8"},{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getFriendsList","outputs":[{"components":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"string","name":"tokenUri","type":"string"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"bool","name":"canPlay","type":"bool"}],"internalType":"struct SmartCatProxyV3.CatListItem[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getLevel","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getPendingInvitesList","outputs":[{"components":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"string","name":"tokenUri","type":"string"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"bool","name":"canPlay","type":"bool"}],"internalType":"struct SmartCatProxyV3.CatListItem[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getPlayInviteIds","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getPlayInvitesList","outputs":[{"components":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"string","name":"tokenUri","type":"string"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"bool","name":"canPlay","type":"bool"}],"internalType":"struct SmartCatProxyV3.CatListItem[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"name":"getPointBalances","outputs":[{"components":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"pointsBalance","type":"uint256"}],"internalType":"struct SmartCatProxyV3.PointsRecord[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getPointsBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nftContractAddress","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"invitee","type":"uint256"}],"name":"inviteCatForPlaying","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"levelAwards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"levelUp","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"maxActionState","outputs":[{"internalType":"uint256","name":"firstActionTimestamp","type":"uint256"},{"internalType":"uint16","name":"count","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxLevel","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"pendingInvites","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"playInvites","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"pointBalances","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_authorisedProxyAddresses","type":"address[]"}],"name":"setAuthedProxyAddresses","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_levelAwards","type":"uint256[]"}],"name":"setLevelAwards","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_maxActions","type":"uint16"},{"internalType":"uint256","name":"_maxActionsInterval","type":"uint256"}],"name":"setMaxActionConfig","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8","name":"_maxLevel","type":"uint8"}],"name":"setMaxLevel","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[3]","name":"_minIntervals","type":"uint256[3]"}],"name":"setMinIntervals","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16[3]","name":"_minLevelUpScores","type":"uint16[3]"}],"name":"setMinLevelUpScores","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_nftContractAddress","type":"address"}],"name":"setNftContractAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"name":"tokenIdArrayToTokenList","outputs":[{"components":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"string","name":"tokenUri","type":"string"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"bool","name":"canPlay","type":"bool"}],"internalType":"struct SmartCatProxyV3.CatListItem[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}])  

def can_perform_action(cat_id, action):
    cat_state = contract.functions.catStates(cat_id).call()
    num_feeds = cat_state[1]  
    num_cleans = cat_state[5] 
    
    if action == "levelUp":
        can_level_up = contract.functions.canLevelUp(cat_id).call()
        if not can_level_up:
            print(f"[CHECK - LEVELUP1] Cat ID {cat_id} cannot level up at the moment.")
        return can_level_up
    if action == "feed" and num_feeds:
        can_feed = contract.functions.canFeed(cat_id).call()
        if not can_feed:
            print(f"[CHECK - FEED1] Cat ID {cat_id} cannot be fed at the moment.")
        return can_feed
    if action == "clean" and num_cleans:
        can_clean = contract.functions.canClean(cat_id).call()
        if not can_clean:
            print(f"[CHECK - CLEAN1] Cat ID {cat_id} cannot be cleaned at the moment.")
        return can_clean
    
    else:
        return False



def perform_action(cat_id, action):
    gas_price = web3.eth.gas_price  
    # print(f"Current gas price: {gas_price}")
    txn = None
    gas_price = web3.eth.gas_price
    increased_gas_price = int(gas_price * 1.3) 
    if action == "clean":
        can_clean = contract.functions.canClean(cat_id).call()
        print(f"[CHECK - CLEAN2] Checking if Cat ID {cat_id} can be cleaned: {can_clean}")
        if can_clean:
            txn = contract.functions.cleanCat(cat_id).build_transaction({
                'from': b_wallet_address,
                'nonce': web3.eth.get_transaction_count(b_wallet_address),
                'gas': 120000,  
                'gasPrice': increased_gas_price
            })
    elif action == "feed":
        can_feed = contract.functions.canFeed(cat_id).call()
        print(f"[CHECK - FEED2] Checking if Cat ID {cat_id} can be fed: {can_feed}")
        if can_feed:
            txn = contract.functions.feedCat(cat_id).build_transaction({
                'from': b_wallet_address,
                'nonce': web3.eth.get_transaction_count(b_wallet_address),
                'gas': 87000,  
                'gasPrice': increased_gas_price
            })
    elif action == "levelUp":
        can_level_up = contract.functions.canLevelUp(cat_id).call()
        print(f"[CHECK3 - LEVELUP2] Checking if Cat ID {cat_id} can be level up: {can_level_up}")
        if can_level_up:
            txn = contract.functions.levelUp(cat_id).build_transaction({
                'from': b_wallet_address,
                'nonce': web3.eth.get_transaction_count(b_wallet_address),
                'gas': 120000, 
                'gasPrice': increased_gas_price
            })

    if txn is not None:
        try:
            signed_txn = web3.eth.account.sign_transaction(txn, private_key=b_private_key)
            txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            receipt = web3.eth.wait_for_transaction_receipt(txn_hash, timeout=240)  
            if receipt.status == 1:
                print(f"Successfully performed {action} action for Cat ID {cat_id}, transaction hash: {txn_hash.hex()}")
            else:
                print(f"Failed to perform {action} action for Cat ID {cat_id}, transaction hash: {txn_hash.hex()}")
        except TimeExhausted as e:
            print(f"Timeout waiting for transaction to be mined: {e}")


def main():
    actions = ["feed", "clean", "play", "levelUp"]
    
    while True:
        for cat_id in cat_ids_B:
            for action in actions:
                if can_perform_action(cat_id, action):
                    perform_action(cat_id, action)
                    time.sleep(2)  
        time.sleep(2)  

if __name__ == "__main__":
    main()
