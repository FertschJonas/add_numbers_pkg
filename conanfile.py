from conans import ConanFile, CMake


class OldCmakeCompilation(ConanFile):
    name = "Add_2_Numbers"
    version = "1.0"
    description = "Using_old_CMake"
    license = None
    url = None
    #TBD settings = "os", "compiler", "build_type", "arch", "os_build", "arch_build"
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake"
#source einzelne über conan source aus Konsole aufrufbar
    def source(self):
        self.run("git clone https://github.com/FertschJonas/add_numbers")
        self.run("cd add_numbers && git checkout")
    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="add_numbers")
        cmake.build()
#Kopiert Artefakte in Local Cache
    def package(self):
         self.copy("*.h", dst="include", src="add_numbers")
         self.copy("*.lib", dst="lib", keep_path=False)
         self.copy("*.dll", dst="bin", keep_path=False)
         self.copy("*.so", dst="lib", keep_path=False)
         self.copy("*.dylib", dst="lib", keep_path=False)
         self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        #Über diese Info weiß conan dass 
        self.cpp_info.libs = ["addnumbers"]
