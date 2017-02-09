from conans import ConanFile, CMake

class LibCharsetDetectConan(ConanFile):
    name = "libcharsetdetect"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    # No exports_sources necessary

    def source(self):
        # this will create a hello subfolder, take it into account
        self.run("git clone https://github.com/elite-lang/libcharsetdetect.git")

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake %s/libcharsetdetect %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="libcharsetdetect")
        self.copy("*.lib", dst="lib", src="build")
        self.copy("*.a", dst="lib", src="build")

    def package_info(self):
        self.cpp_info.libs = ["charsetdetect"]