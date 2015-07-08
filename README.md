# Pixyll

Pixyll is a simple, beautiful theme for [Hugo](http://gohugo.io/).
Based on [Pixyll for Jekyll](https://github.com/johnotander/pixyll)

## Features

- Basic tag support.
- Disqus comments supported.
- Google Analytics supported.
- Social links (currently only for twitter).
- [Formspree](http://formspree.io/) for contanct form.
- Pagination support.

Example config:

```toml
languageCode = "en-us"
contentdir = "content"
publishdir = "public"
builddrafts = false
baseUrl = ""
canonifyurls = true
title = "Pixyll"
author = "admin"
theme = "pixyll"

[indexes]
  category = "categories"
  tag = "tags"

[params]
  search_engine = true
  google_analytics_id = "XX-XXXXXXXX-X"
  twitter_username = "username"
  disqus_shortname = "sitename"
  paginate = true
```

![Pixyll Screenshot](https://raw.githubusercontent.com/azmelanar/hugo-theme-pixyll/master/images/tn.png)
