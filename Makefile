compile: compile-fe compile-be

compile-be:
	cd ./template && python3 setup.py bdist_wheel

compile-fe:
	cd ./template/st_group_barchart/frontend && npm run build

clear:
	sudo rm -rf ./template/dist ./template/build ./template/st_group_barchart.egg-info

publish:
	twine upload ./template/dist/* --verbose