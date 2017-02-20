from __future__ import print_function, division
import cmd


class Mycmd(cmd.Cmd):
      prompt = 'mycmd >>> '
      intro = 'My Command Prompt.'

      def do_deploy(self, line):
              print('deploy')
      def do_kill(self, line):
              print('kill')
      def do_benchmark(self, line):
              print('benchmark')
      def do_report(self, line):
              print('report')
      def do_EOF(self, line):
              print('bye, bye')
              return True

if __name__ == '__main__':
      Mycmd().cmdloop()
