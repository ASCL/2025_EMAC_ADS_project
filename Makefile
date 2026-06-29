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
	cp emac.json emac_$(DATE).json
	-curl $(URL1)  > emac.json
	diff emac.json emac_$(DATE).json

## list:      create list, ready for git ingest
list:
	./emac.py emac.json > emac.list

