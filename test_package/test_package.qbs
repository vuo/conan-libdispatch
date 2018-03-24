import qbs 1.0

Project {
	minimumQbsVersion: '1.6'
	references: [ buildDirectory + '/../conanbuildinfo.qbs' ]
	Product {
		type: 'application'
		consoleApplication: true

		Depends { name: 'ConanBasicSetup' }

		Depends { name: 'cpp' }
		cpp.compilerPathByLanguage: ({
			c: '//usr/bin/clang-5.0',
			cpp: '/usr/bin/clang++-5.0',
		})
		cpp.cxxFlags: [ '-fblocks' ]
		cpp.cxxStandardLibrary: 'libstdc++'
		cpp.linkerPath: '/usr/bin/clang++-5.0'
		cpp.rpaths: [ buildDirectory + '/../../lib' ]
		cpp.target: 'x86_64-unknown-linux-gnu'

		files: [ 'test_package.cc' ]
	}
}
