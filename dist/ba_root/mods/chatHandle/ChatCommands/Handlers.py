# Released under the MIT License. See LICENSE for details.

from PlayersData import pdata
import ba, _ba





def clientid_to_accountid(clientid):
	"""
	Transform Clientid To Accountid 
	
	Parameters:
		clientid : int
	
	Returns:
		None 
	"""
	for i in _ba.get_game_roster():
		if i['client_id'] == clientid:
			return i['account_id']
	return None





def cheak_permissions(accountid, command):
	"""
	Checks The Permission To Player To Executive Command
	
	Parameters:
		accountid : str
		command : str
	
	Returns:
		Boolean
	"""
	roles = pdata.get_roles()
	
	for role in roles:
		if accountid in roles[role]["ids"] and command in roles[role]["commands"]:
			return True
	return False
