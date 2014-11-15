# Pixyll

Pixyll is a simple, beautiful theme for [Hugo](http://gohugo.io/).
Based on [Pixyll for Jekyll](https://github.com/johnotander/pixyll)

## Features

- Disqus comments supported.
  Add DisqusUrl parameter to Site params in config.
- Basic tag support. Add tag = "tags" to Site indexes in config.

Example config
```toml
languageCode = "en-us"
contentdir = "content"
publishdir = "public"
builddrafts = false
baseUrl = "http://localhost"
canonifyurls = true
title = "Pixyll"
author = "admin"

[indexes]
  category = "categories"
  tag = "tags"

[params]
  DisqusUrl = "pixyll"
```

