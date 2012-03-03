Rewrite author/committer history of a git repository
====================================================

Have you ever accidentally committed to a git repository with a broken
user config?  No?  But your co-workers have?

So, you're stuck with commits like this::

    Author: root <root@localhost>

        Hotfix on the production server.  This was urgent!

Nasty.  Or::

    Author: John Doe <john@localhost>

        Fixed bug #1.  Committed on my laptop.

Would it be nice to rewrite history?  And take care of committers, as
well as of authors?  Without all the hassle?  Now, you can!

Usage::

    $ python git-rewrite-author.py "John Doe <john@localhost>" "John Doe <dearjohn@example.com>"

You're not sure which authors/committers are hidden in your repository?
What about::

    $ git log --pretty=full|grep "^Author\|^Commit"|cut -d " " -f 2-|sort|uniq

Tags are rewritten automagically, too!

Enjoy!
