# Web3.Py_Proto

Requirements:

PipENV, Python, few brain cells.




$pipenv install

--install dep 

$pipenv shell

--open shell inside virtual environment

>>>app.py

--executes 




INFO::


app.py

----Main function, scaffolded as the TODO for any scripting.



>>tests

----We don't do those. Not yet anyways.



>>scripts

>>>>connect.py

--------Confers with virtual environment settings (venv) in environment folder, uses API_KEYS defined to connect to and handle web3 HTTPS websocket

>>>>terminate.py

--------Use your imagination



>>registry

>>>>xxxDict.py

--------uses classes for each contract you'd like to register/import/dict. Assign attributes and return for clean calls, not much else.



>>interfaces

>>>>xxxinterfaces

>>>>>>>>somecontract.txt

-----------------paste raw .txt of ABI, supply PATH in registry class for contract.

