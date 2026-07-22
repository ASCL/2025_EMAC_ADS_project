#
#

.PHONY:  help

URL1 = https://emac.gsfc.nasa.gov/api/resource-links

DATE = `date +%Y-%m-%d`

## help:      This Help
help : Makefile
	@sed -n 's/^##//p' $<

## json:      get a new emac.json and compare to the previous one
json:
	cp emac.json emac.json.backup
	-curl $(URL1)  > emac.json
	cp emac.json emacs_$(DATE).json
	diff emac.json emac.json.backup

## list:      create list, ready for git ingest
list:
	@./emac.py emac.json > emac.list
	@echo "There are `cat emac.list | wc -l` entries in emac.list. The latest entry:"
	@tail -1 emac.list

## git:        update using 'git pull'
git:
	@git pull
