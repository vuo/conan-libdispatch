from conans import ConanFile

class LibdispatchTestConan(ConanFile):
    generators = 'qbs'

    def build(self):
        self.run('qbs -f "%s"' % self.conanfile_directory)

    def imports(self):
        self.copy('*.so', src='lib', dst='bin')

    def test(self):
        self.run('qbs run -f "%s"' % self.conanfile_directory)

        # Ensure we only link to system libraries.
        self.run('! (ldd bin/libdispatch.so | grep "/" | egrep -v "\s/lib64/")')
