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

    $ python rewrite.py "John Doe <john@localhost>" "John Doe <dearjohn@example.com>"

Enjoy!
