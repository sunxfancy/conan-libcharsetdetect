from conans import ConanFile, CMake, tools
import os

class LibCharsetDetectConan(ConanFile):
    name = "libcharsetdetect"
    version = "1.1.1"
    license = "LGPL"
    url = "https://github.com/sunxfancy/conan-libcharsetdetect"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    # No exports_sources necessary

    def source(self):
        # this will create a hello subfolder, take it into account
        tools.download("https://github.com/elite-lang/libcharsetdetect/archive/master.zip", "master.zip")
        tools.unzip("master.zip")
        os.unlink("master.zip")
        conan_magic_lines = '''PROJECT(charsetdetect)
        include(../conanbuildinfo.cmake)
        CONAN_BASIC_SETUP()
        '''
        tools.replace_in_file("libcharsetdetect-master/CMakeLists.txt", "PROJECT(charsetdetect)", conan_magic_lines)

    def build(self):
        cmake = CMake(self)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        self.run('cmake %s/libcharsetdetect-master %s %s' % (self.conanfile_directory, cmake.command_line, shared))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="libcharsetdetect-master")
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)
        self.copy("*.a", dst="lib", src="lib", keep_path=False)
        self.copy("*.dll", dst="bin", src="lib", keep_path=False)
        self.copy("*.so*", dst="lib", src="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", src="lib", keep_path=False)
    def package_info(self):
        self.cpp_info.libs = ["charsetdetect"]
