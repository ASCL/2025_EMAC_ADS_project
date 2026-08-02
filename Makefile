#
#

.PHONY:  help

# 1=verified   2=unverified  3=all
# note unverified do not have an EMAC CID
URL1 = https://emac.gsfc.nasa.gov/api/resource-links
URL2 = https://emac.gsfc.nasa.gov/api/inlit-resources
URL3 = https://emac.gsfc.nasa.gov/api/all-resources

DATE = `date +%Y-%m-%d`

## help:      This Help
help : Makefile
	@sed -n 's/^##//p' $<

## json:      get a new emac.json and compare to the previous one
json:
	cp emac.json emac.json.backup
	-curl $(URL3)  > emac.json
	cp emac.json emacs_$(DATE).json
	diff emac.json emac.json.backup

## list:      create list of EMACS CID, ready for git ingest
list:
	@./emac.py emac.json | sort > emac.list
	@echo "There are `cat emac.list | wc -l` entries in emac.list. The latest entry:"
	@tail -1 emac.list

## git:        update using 'git pull'
git:
	@git pull

## count:      count occurances per month
count:
	awk -F- '{print $$1}' emac.list | uniq -c

