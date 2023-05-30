run: venv
	. venv/bin/activate; python ./main.py

run_get_hashes: venv
	. venv/bin/activate; python ./get_txn_hashs.py

venv: venv/touchfile

venv/touchfile: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

clean:
	rm -rf venv
	find -iname "*.pyc" -delete
