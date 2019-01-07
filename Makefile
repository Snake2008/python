all:
			@cd ~/python
			@python3 ./src/main.py

pack:
			@cd ~/python
			@pyinstaller --windowed --onefile --clean --noconfirm ./src/main.py
			@pyinstaller --clean --noconfirm --windowed --onefile main.spec

run:
			@cd ~/python
			@./dist/main
clear:
			@cd ~/python
			@rm -rf ./dist ./build ./main.spec