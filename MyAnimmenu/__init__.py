from os import environ
from Components.Language import language
from gettext import bindtextdomain, dgettext, gettext
from Tools.Directories import resolveFilename, SCOPE_PLUGINS

def localeInit():
	environ["LANGUAGE"] = language.getLanguage()[:2]
	res = resolveFilename(SCOPE_PLUGINS, "Extensions/MyAnimmenu/locale")
	bindtextdomain("MyAnimmenu", res)

def _(txt):
	t = dgettext("MyAnimmenu", txt)
	if t == txt:
		t = gettext(txt)
	return t

localeInit()
language.addCallback(localeInit)