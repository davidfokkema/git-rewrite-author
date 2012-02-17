import argparse
import re
import subprocess
import textwrap


description = "Rewrite author/committer in git history"
author_help = "'Full Name <email@domain>'"

git_rewrite_command = """git filter-branch --env-filter 'if [ "$GIT_AUTHOR_NAME" == "%s" -a "$GIT_AUTHOR_EMAIL" == "%s" ]; then GIT_AUTHOR_NAME="%s"; GIT_AUTHOR_EMAIL="%s"; fi; export GIT_AUTHOR_NAME; export GIT_AUTHOR_EMAIL' -f -- --all"""


def parse_args():
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('old', type=str, help=author_help)
    parser.add_argument('new', type=str, help=author_help)
    return parser.parse_args()

def main(args):
    old_name, old_email = parse_author_arg(args.old)
    new_name, new_email = parse_author_arg(args.new)

    rewrite_git_author(old_name, old_email, new_name, new_email)
    rewrite_git_committer(old_name, old_email, new_name, new_email)

def parse_author_arg(arg):
    name, email = re.match("([A-Za-z\(\) ]+) <(.*)>", arg).groups()
    return name, email

def rewrite_git_author(old_name, old_email, new_name, new_email):
    command = git_rewrite_command % (old_name, old_email, new_name, new_email)
    subprocess.call(command, shell=True)

def rewrite_git_committer(old_name, old_email, new_name, new_email):
    command = git_rewrite_command.replace('AUTHOR', 'COMMITTER') % (old_name, old_email, new_name, new_email)
    subprocess.call(command, shell=True)


if __name__ == '__main__':
    args = parse_args()
    main(args)
