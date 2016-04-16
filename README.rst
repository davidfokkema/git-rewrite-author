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

    $ git rewrite-author -w "John Doe <john@localhost>" "John Doe <dearjohn@example.com>"

Then, to push your changes to the default remote::

    $ git push --force

Not using --force may duplicate the commits on origin, not replace them, so be careful with that.

You're not sure which authors/committers are hidden in your repository?
What about::

    $ git rewrite-author -l

Tags are rewritten automagically, too!

After you've checked everything is okay, you may wish to remove the original refs backed up by git --filter-branch::

    $ git for-each-ref --format="%(refname)" refs/original/ | xargs -r -n 1 git update-ref -d


Enjoy!


Installation
------------

Clone or download this repository and run::

    $ python setup.py install
