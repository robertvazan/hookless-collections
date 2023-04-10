# This script generates and updates project configuration files.

# Run this script with rvscaffold in PYTHONPATH
import rvscaffold as scaffold

class Project(scaffold.Java):
    def script_path_text(self): return __file__
    def repository_name(self): return 'hookless-collections'
    def pretty_name(self): return 'Reactive collections for Hookless'
    def pom_description(self): return 'Hookless reactive adapter for Java collections.'
    def inception_year(self): return 2015
    def jdk_version(self): return 17
    def stagean_annotations(self): return True
    def complete_javadoc(self): return False
    
    def dependencies(self):
        yield from super().dependencies()
        yield self.use_hookless()
        yield self.use_junit()
        yield self.use_hamcrest()
    
    def javadoc_links(self):
        yield from super().javadoc_links()
        yield 'https://hookless.machinezoo.com/javadocs/core/'

Project().generate()
