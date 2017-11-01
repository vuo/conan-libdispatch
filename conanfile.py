from conans import ConanFile, tools, AutoToolsBuildEnvironment
import os

class LibdispatchConan(ConanFile):
    name = 'libdispatch'
    version = '4.0'
    settings = 'os', 'compiler', 'build_type', 'arch'
    url = 'https://github.com/vuo/conan-libdispatch'
    license = 'https://github.com/apple/swift-corelibs-libdispatch/blob/master/LICENSE'
    description = 'A library for concurrency on multicore hardware'
    source_dir = 'swift-corelibs-libdispatch-swift-%s-RELEASE' % version
    build_dir = '_build'

    def source(self):
        self.output.info(self.package_folder)
        tools.get('https://github.com/apple/swift-corelibs-libdispatch/archive/swift-%s-RELEASE.tar.gz' % self.version,
                  # sha256='9e63da11de3e05482411c169f5055bafa7ab08f7319e91bf8819601900f29732'
                  )
        with tools.chdir(self.source_dir):
            tools.patch(patch_string='''
--- dispatch/dispatch.h	2017-10-31 02:44:42.330119073 -0400
+++ dispatch/dispatch.h	2017-10-31 02:46:52.155032542 -0400
@@ -36,7 +36,14 @@
 #include <stdbool.h>
 #include <stdarg.h>
 #if !defined(HAVE_UNISTD_H) || HAVE_UNISTD_H
+
+// https://sourceware.org/bugzilla/show_bug.cgi?id=11157
+#undef __block
+#define __block __glibc_block
 #include <unistd.h>
+#undef __block
+#define __block __attribute__((__blocks__(byref)))
+
 #endif
 #include <fcntl.h>
            ''')
            self.run('sh autogen.sh')

    def build(self):
        tools.mkdir(self.build_dir)
        with tools.chdir(self.build_dir):
            autotools = AutoToolsBuildEnvironment(self)
            autotools.cxx_flags.append('-Oz')

            env_vars = {
                'CC' : '/opt/llvm-3.8.0/bin/clang',
                'CXX': '/opt/llvm-3.8.0/bin/clang++',
            }
            with tools.environment_append(env_vars):
                autotools.configure(configure_dir='../%s' % self.source_dir,
                                    args=['--quiet',
                                          '--enable-shared',
                                          '--disable-static',
                                          '--disable-build-tests',
                                          '--prefix=%s' % os.getcwd()])
                autotools.make(args=['install'])

    def package(self):
        self.copy('*.h', src='%s/include' % self.build_dir, dst='include')
        self.copy('libdispatch.so', src='%s/lib' % self.build_dir, dst='lib')

    def package_info(self):
        self.cpp_info.libs = ['dispatch']
