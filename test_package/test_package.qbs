import qbs

Project {
	minimumQbsVersion: 1.6
	references: [ buildDirectory + '/../conanbuildinfo.qbs' ]
	Product {
		type: 'application'
		consoleApplication: true

		Depends { name: 'ConanBasicSetup' }

		Depends { name: 'cpp' }
		cpp.compilerPath: '/opt/llvm-3.8.0/bin/clang++'
		cpp.compilerPathByLanguage: {}
		cpp.cxxFlags: [ '-fblocks' ]
		cpp.cxxStandardLibrary: 'libstdc++'
		cpp.linkerPath: '/opt/llvm-3.8.0/bin/clang++'
		cpp.rpaths: [ buildDirectory + '/../../bin' ]
		cpp.target: 'x86_64-unknown-linux-gnu'

		files: [ 'test_package.cc' ]
	}
}
