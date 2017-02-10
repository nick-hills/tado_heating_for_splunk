import splunk.admin as admin
import splunk.entity as en

class configApp(admin.MConfigHandler):
	def setup(self):
		if self.requestedAction == admin.ACTION_EDIT:
			for arg in ['username']:
				self.supportedArgs.addOptArg(arg)

	def handleList(self, confInfo):
		confDict = self.readConf('tadosetup')
		if None != confDict:
			for stanza, settings in confDict.items():
				for key, val in settings.items():
					if key in ['username'] and val in [None, '']:
						val = confInfo[stanza].append(key, val)

	def handleEdit(self, confInfo):
		name = self.callerArgs.id
		args = self.callerArgs
		self.writeConf('tadosetup','tado_config', self.callerArgs.data)

admin.init(configApp, admin.CONTEXT_NONE)
		
