GH_PAGES_SOURCES = shopify_trois setup.py requirements.txt README.md LICENSE CHANGES
test:
	nosetests tests --with-coverage --cover-erase --cover-html --cover-package=shopify_trois --nocapture

gh-pages:
	git checkout gh-pages
	git checkout master $(GH_PAGES_SOURCES) docs
	git reset HEAD
	rm -rf build _sources _static
	python setup.py install
	cd docs/ && make html
	cd ..
	mv -fv docs/_build/html/* ./
	rm -rf $(GH_PAGES_SOURCES) docs dist build shopify_trois.egg-info
	git add -A
	git commit -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`" && git push origin gh-pages ; git checkout master
