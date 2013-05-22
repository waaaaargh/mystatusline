mystatusline
============

easily extensible wrapper script for i3status.

How
---

In your ```~/.i3/config```, change your bar section to the following

```
bar {
  status_command i3status | /path/to/mystatusline.py
}
```

You now should see the output from ```plugins/hello.py``` in your statusbar

What
----

Excellent question. At the moment, there is only one "official" plugin which just says "Hello". But you can change that. just copy ```plugins/hello.py``` to ```plugins/whateveryouwant.py``` implement the functionality you need and add the ```whateveryouwant``` to the comma-separated list of enabled plugins in ```config.cfg```

If you think a plugin you wrote might be useful for other people, feel free to contribute it via pull request.

Why
---

Mainly because I can.

But also because py3status cannot into JSON.
