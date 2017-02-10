from conans import ConanFile, CMake, tools

class LibCharsetDetectConan(ConanFile):
    name = "libcharsetdetect"
    version = "1.0"
    license = "LGPL"
    url = "https://github.com/sunxfancy/conan-libcharsetdetect"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    # No exports_sources necessary

    def source(self):
        # this will create a hello subfolder, take it into account
        self.run("git clone https://github.com/elite-lang/libcharsetdetect.git")
        conan_magic_lines = '''PROJECT(charsetdetect)
        include(../conanbuildinfo.cmake)
        CONAN_BASIC_SETUP()
        '''
        tools.replace_in_file("libcharsetdetect/CMakeLists.txt", "PROJECT(charsetdetect)", conan_magic_lines)

    def build(self):
        cmake = CMake(self.settings)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        self.run('cmake %s/libcharsetdetect %s %s' % (self.conanfile_directory, cmake.command_line, shared))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="libcharsetdetect")
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)
        self.copy("*.a", dst="lib", src="lib", keep_path=False)
        self.copy("*.dll", dst="bin", src="lib", keep_path=False)
        self.copy("*.so*", dst="lib", src="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", src="lib", keep_path=False)
    def package_info(self):
        self.cpp_info.libs = ["charsetdetect"]
