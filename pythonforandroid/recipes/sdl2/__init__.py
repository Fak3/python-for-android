from pythonforandroid.recipe import BootstrapNDKRecipe
from pythonforandroid.toolchain import current_directory, shprint
import sh


class LibSDL2Recipe(BootstrapNDKRecipe):
    version = "45b56ed51919"
    url = "https://hg.libsdl.org/SDL/archive/{version}.zip"
    md5sum = "75c3946311a320482609fc2fa68a695d"

    dir_name = 'SDL'

    depends = ['sdl2_image', 'sdl2_mixer', 'sdl2_ttf']

    def get_recipe_env(self,
                       arch=None,
                       with_flags_in_cc=True,
                       with_python=True):
        env = super(LibSDL2Recipe, self).get_recipe_env(
            arch=arch, with_flags_in_cc=with_flags_in_cc,
            with_python=with_python
        )
        env['APP_ALLOW_MISSING_DEPS'] = 'true'
        return env

    def build_arch(self, arch):
        env = self.get_recipe_env(arch)

        with current_directory(self.get_jni_dir()):
            shprint(sh.ndk_build, "V=1", _env=env)


recipe = LibSDL2Recipe()
