from conans import ConanFile

class LibdispatchTestConan(ConanFile):
    generators = 'qbs'

    def build(self):
        self.run('qbs -f "%s"' % self.source_folder)

    def imports(self):
        self.copy('*', src='lib', dst='lib')

    def test(self):
        self.run('qbs run')

        # Ensure we only link to system libraries.
        self.run('! (ldd lib/libdispatch.so | grep "/" | egrep -v "\s/lib64/")')
