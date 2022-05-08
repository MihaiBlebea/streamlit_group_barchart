from typing import List
import os
import streamlit.components.v1 as components


_RELEASE = False


if not _RELEASE:
	_component_func = components.declare_component(
		"st_group_barchart",
		url="http://localhost:3001",
	)
else:
	parent_dir = os.path.dirname(os.path.abspath(__file__))
	build_dir = os.path.join(parent_dir, "frontend/build")
	_component_func = components.declare_component("st_group_barchart", path=build_dir)


def st_group_barchart(groups : List[str], datasets : List[dict], key=None):
	"""
	groups=[
		"2018",
		"2019",
		"2020",
		"2021"
	],
	datasets=[
		{
			"label": "Assets",
			"background_color": "pink",
			"border_color": "red",
			"data": [13, 5, 6, 7]
		},
		{
			"label": "Liabilities",
			"background_color": "lightblue",
			"border_color": "blue",
			"data": [10, 15, 6, 9]
		},
	]
	"""
	if isinstance(groups, list) == False:
		raise Exception("groups variable must be a list")

	for g in groups:
		if isinstance(g, str) == False:
			raise Exception("groups element variable must be a string") 

	if isinstance(datasets, list) == False:
		raise Exception("datasets variable must be a list")

	for d in datasets:
		if isinstance(d, dict) == False:
			raise Exception("datasets element variable must be a dict")

		if "label" not in d:
			raise Exception("missing label key from datasets dict")
		
		if "background_color" not in d:
			raise Exception("missing background_color key from datasets dict")

		if "border_color" not in d:
			raise Exception("missing border_color key from datasets dict")

		if "data" not in d:
			raise Exception("missing data key from datasets dict")

		if isinstance(d["data"], list) == False:
			raise Exception("data key must be a list")

		for el in d["data"]:
			if isinstance(el, int) == False and isinstance(el, float) == False:
				raise Exception("data element must be a int or float")

	component_value = _component_func(
		groups=groups,
		datasets=datasets,
		key=key, 
		default=0)

	return component_value


if not _RELEASE:
	import streamlit as st

	num_clicks = st_group_barchart(
		[
			"2018",
			"2019",
			"2020",
			"2021"
		],
		[
			{
				"label": "Assets",
				"background_color": "pink",
				"border_color": "red",
				"data": [13, 5, 6, 7]
			},
			{
				"label": "Liabilities",
				"background_color": "lightblue",
				"border_color": "blue",
				"data": [10, 15, 6, 9]
			},
		]
	)

