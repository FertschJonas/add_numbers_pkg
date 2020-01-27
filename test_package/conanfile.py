from conans import ConanFile, CMake, tools
import os


class Add2Numbers_test(ConanFile):
    # TBD settings = "os", "compiler", "build_type", "arch", "os_build", "arch_build"
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is in "test_package"
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy('*.so*', dst='bin', src='lib')
       # "Nur statische Lib wird verwendet"


    def test(self):
            os.chdir("bin")
            self.run(".%sarg_printer 5.5 10.5" % os.sep)