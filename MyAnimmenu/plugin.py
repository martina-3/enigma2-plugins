# by Nikolasi
from . import _
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from Components.ConfigList import ConfigListScreen
from Components.config import config, configfile, getConfigListEntry, ConfigSelection, ConfigSubsection, ConfigYesNo, ConfigInteger

config.plugins.MyAnimmenu = ConfigSubsection()
config.plugins.MyAnimmenu.animmenu = ConfigYesNo(default=False)
config.plugins.MyAnimmenu.animmenutime = ConfigInteger(20, (10, 300))
config.plugins.MyAnimmenu.animmenuspid = ConfigInteger(10, (5, 30))
config.plugins.MyAnimmenu.animmenulog = ConfigYesNo(default=False)

class AnimmenuScreenMain(ConfigListScreen, Screen):
    skin = """
           <screen position="100,100" size="550,400" title="Animation menu config" >
           <widget name="config" position="10,5" size="520,300" scrollbarMode="showOnDemand" />
           <widget name="buttonred" position="10,360" size="100,40" backgroundColor="red" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20"/>
           <widget name="buttongreen" position="120,360" size="100,40" backgroundColor="green" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20"/>
           <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/MyAnimmenu/indb.png" position="300,357" size="208,50" alphatest="on" />
           </screen>"""

    def __init__(self, session):
        self.session = session
        Screen.__init__(self, session)
        self.list = []
        self.list.append(getConfigListEntry(_('Enable menu animations'), config.plugins.MyAnimmenu.animmenu))
        self.list.append(getConfigListEntry(_('Time for animation'), config.plugins.MyAnimmenu.animmenutime))
        self.list.append(getConfigListEntry(_('Animation speed'), config.plugins.MyAnimmenu.animmenuspid))
        self.list.append(getConfigListEntry(_('Enable menu logging'), config.plugins.MyAnimmenu.animmenulog))       
        ConfigListScreen.__init__(self, self.list)
        self['buttonred'] = Label(_('Cancel'))
        self['buttongreen'] = Label(_('ok'))
        self['setupActions'] = ActionMap(['SetupActions'], {'green': self.save,
         'red': self.cancel,
         'cancel': self.cancel,
         'save': self.save,
         'ok': self.save}, -2)
        self.onShown.append(self.setWindowTitle)

    def setWindowTitle(self):
        self.setTitle(_('Animation menu config'))

    def save(self):
        print '[MyAnimmenu] saving config'
        for x in self['config'].list:
            x[1].save()
        ConfigListScreen.keySave(self)
        configfile.save()            

    def cancel(self):
        for x in self['config'].list:
            x[1].cancel()

        self.close(False)

def main(session, **kwargs):
    session.open(AnimmenuScreenMain)

def Plugins(**kwargs):
    result = [PluginDescriptor(name=_('Animation menu config'), description=_('Animation menu Configurer by Nikolasi'), where=[PluginDescriptor.WHERE_PLUGINMENU, PluginDescriptor.WHERE_EXTENSIONSMENU], icon='plugin.png', fnc=main)]
    return result
