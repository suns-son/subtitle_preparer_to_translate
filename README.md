# subtitle_preparer_to_translate
## This program prepare your AI generated subtitle to translate.
If you've ever tried to have the AI generate subtitles as SRT file, you've probably come across something like this:

```
1
00:00:10,810 --> 00:00:14,490
The great gift of man over beasts has been his ability

2
00:00:14,570 --> 00:00:18,314
to craft and use tools. A simple stone

3
00:00:18,362 --> 00:00:21,710
axe gave man the power to shape the world around

4
00:00:21,780 --> 00:00:25,254
him. A spear could mean a difference between

5
00:00:25,292 --> 00:00:27,750
a family eating or starving.

```

This Python code turns it to that:

```
1
00:00:10,810 --> 00:00:16,394
The great gift of man over beasts has been his ability to craft and use tools.

2
00:00:16,458 --> 00:00:23,474
A simple stone axe gave man the power to shape the world around him.

3
00:00:23,528 --> 00:00:27,750
A spear could mean a difference between a family eating or starving.

```

It also changes the times properly.

**The main goal of this program is to prepare subtitles for translation.
Translation apps often fail to translate split sentences.
It makes subtitle files ready for translation by joining sentences, editing them and adjusting their timing.
Apart from translation, it can also be used to provide more complete sentences and to improve readability.**
