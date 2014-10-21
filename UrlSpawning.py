import sublime, sublime_plugin
import webbrowser

class open_browser_url(sublime_plugin.TextCommand):

   def run(self,edit):
      url = self.view.file_name()
      url = url.replace('\\', '/')
      url = url.replace( '/home/faron/lib/script/htmls' ,'www.faronintel.ca')
      url = 'http://' + url
      webbrowser.open_new(url)

