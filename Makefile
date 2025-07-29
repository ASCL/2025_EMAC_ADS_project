#
#

.PHONY:  help

URL1 = https://emac.gsfc.nasa.gov/api/resource-links


## help:      This Help
help : Makefile
	@sed -n 's/^##//p' $<

## json:      get a new emac.json and compare to the previous one
json:
	cp emac.json emac.json.backup
	curl $(URL1)  > emac.json
	diff emac.json emac.json.backup

