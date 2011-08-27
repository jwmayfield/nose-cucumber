from os import environ, getcwd, path, sep, walk
from subprocess import Popen, PIPE, STDOUT
from sys import stdout

from nose.plugins.base import Plugin
from nose.config import ConfigError


class Cucumber(Plugin):
    # TODO: add options for specifying an rvm to use so you don't have to
    # install cucumber to system ruby if you don't want to
    name = 'cucumber'

    def configure(self, options, config):
        Plugin.configure(self, options, config)
        if not self.enabled:
            return
        self.cucumber_dirs = []

    def wantDirectory(self, dirpath):
        possible = path.join(dirpath, 'features')
        if path.exists(possible):
            self.cucumber_dirs.append(dirpath)
            return True
        return False

    def report(self, stream):
        for d in self.cucumber_dirs:
            cmd = ['cucumber', d]

            p = Popen(
                cmd, env={'PATH': environ.get('PATH', None)},
                stdout=PIPE, stderr=STDOUT,
            )

            stream.write(p.stdout.read())
            returncode = p.wait()
            print >> stream, ""
            if returncode != 0:
                print >> stream, "FAIL"
            else:
                print >> stream, "OK"
