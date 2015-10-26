# -*- coding: utf-8 -*-

def func(x,y,z):
	template = u"%d時の%sは%.1f"
	print template % (x,y,z)

func(12,u"気温",22.4)

#12時の気温は22.4
