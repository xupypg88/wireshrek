import sublime
import sublime_plugin
import sys
import os
#from LogLib import *
#Job.Backup_Job_For_restore.Backup.log Job.CPM_Backup__SUK__-_Daily.Backup.log



# 
buff=''
class TestexecCommand(sublime_plugin.TextCommand):
	def run(self, edit, lines):
		currvw = self.view
		texta=''
		for line in lines:
			texta += line
		self.view.insert(edit, self.view.size(), texta)

class TextgetCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		currvw = self.view
		return currvw.substr(currvw.sel()[0])


class ShowpopCommand(sublime_plugin.TextCommand):
	def run(self, edit, lines):
		#envs = self.window.extract_variables()

		currvw = self.view
		texta=''
		for line in lines:
			texta += line
		self.view.insert(edit, 0, texta)
		
		return

# SHOW INFRASTRUCTURE
class ShowmeinfrastructCommand(sublime_plugin.WindowCommand):
	def pullout_infrastructure(self, base_path):
		info_text = "Test OK!: " + base_path
		return info_text

	def run(self):

		active_v = self.window.active_view()
		file_dir_path = active_v.file_name()[:active_v.file_name().rfind("\\")]

		lines = ''

		max_depth = 30
		for i in range(0,max_depth):
			if file_dir_path.rfind("\\") > 1:
				for item in os.listdir(file_dir_path):
					if item == 'Utils':
						base_path = file_dir_path						

				file_dir_path = file_dir_path[0:file_dir_path.rfind("\\")]
			if max_depth - 1 == i:
				lines = "ERROR: !!! PATH SEARCHED STUCK IN LOOP !!!"
			if base_path != '':
				break
		self.pullout_infrastructure(base_path)

		for viewitem in self.window.views():
			if viewitem.name() == 'Infrastructure_Info':
				viewitem.set_scratch(True)
				viewitem.close()

		if 'viewv' not in locals():
				self.window.new_file()
				viewv = self.window.active_view()
				viewv.set_name('Infrastructure_Info')					
				viewv.run_command('testexec', { "lines" : lines })


		
		


#close naher window
class ClosenahuiCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.active_view().set_scratch(True)
		self.window.active_view().close()


class JobstatsCommand(sublime_plugin.WindowCommand):
	def run(self):

		v = self.window.active_view()
		envs = self.window.extract_variables()
		str(envs['file_path'] + '\\' + envs['file_name'])

		buffa = ''
		jobs = []
		for job in LogImporter.openfile(str(envs['file_path'] + '\\' + envs['file_name'])):
			jobs.append(job)

		for job in [(job) for job in LogImporter.openfile(str(envs['file_path'] + '\\' + envs['file_name']))]:
			#if i < job.entry[1] and i > job.entry[0]:
			buffa += str(job.getstat()) + '\n\n'

		
		self.window.new_file()
		viewv = self.window.active_view()
		viewv.run_command('testexec', { "lines" : buffa })
		viewv.set_syntax_file('Packages/WireShrek/WireShrek.tmLanguage')

class JobstatCommand(sublime_plugin.WindowCommand):
	def run(self):

		v = self.window.active_view()
		envs = self.window.extract_variables()
		str(envs['file_path'] + '\\' + envs['file_name'])

		buffa = ''
		jobs = []
		for job in LogImporter.openfile(str(envs['file_path'] + '\\' + envs['file_name'])):
			jobs.append(job)

		thisview = self.window.active_view()
		(pos,col) = thisview.rowcol(thisview.sel()[0].begin())


		print("POSITION: " + str(pos))
		for job in [(job) for job in LogImporter.openfile(str(envs['file_path'] + '\\' + envs['file_name']))]:
			if pos < job.entry[1] and pos > job.entry[0]:
				buffa += str('\n'.join([str(str(k) + ': ' + str(v)) for k,v in job.getstat().items()])) + '\n\n'

		
		self.window.new_file()
		viewv = self.window.active_view()
		viewv.run_command('testexec', { "lines" : buffa } )
		viewv.set_syntax_file('Packages/WireShrek/wireshrek.tmLanguage')

class NewwinCommand(sublime_plugin.WindowCommand):
	def run(self):

		v = self.window.active_view()

		regs=[]
		for pattern in v.sel():
			for ln in v.find_all(v.substr(pattern),sublime.LITERAL):
				if v.full_line(ln) not in regs:
					regs.append(v.full_line(ln))

		regs.sort()

		buffa=[]		
		for ln in regs:
			buffa.append(v.substr(ln))

		
		self.window.new_file()
		viewv = self.window.active_view()
		viewv.run_command('testexec', { "lines" : buffa })
		viewv.set_syntax_file('Packages/WireShrek/wireshrek.tmLanguage')

class PutnewwinCommand(sublime_plugin.WindowCommand):
	def run(self):
		v = self.window.active_view()

		for viewitem in self.window.views():
			if viewitem.name() == 'dumper':
				viewv = viewitem

		if 'viewv' not in locals():
			self.window.new_file()
			viewv = self.window.active_view()

			viewv.set_name('dumper')


		lines = [str(v.substr(line)) for line in v.sel() if line is not ""]
		lines.insert(0, str(v.file_name()) + '\n\n')
		lines.append('\n---   ---   ---\n')

		for l in range(0, len(lines)):
			if '\n' not in lines[l]:
				lines[l] += '\n'

		viewv.run_command('testexec', { "lines" : lines })
		viewv.set_syntax_file('Packages/WireShrek/wireshrek.tmLanguage')