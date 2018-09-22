+++
date = "2014-11-09T13:49:44+04:00"
draft = false
title = "Search"
slug = "search"

+++

<div>
<link rel="stylesheet" type="text/css" href="../tipuesearch/tipuesearch.css">
<script src="//ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<link href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.0/normalize.min.css">
<script type="text/javascript" src="../tipuesearch/tipuesearch_set.js"></script>
<script type="text/javascript" src="../tipuesearch/tipuesearch.min.js"></script>
<script type="text/javascript" src="../tipuesearch/tipuesearch_content.js"></script>
<script>
$(document).ready(function() {
     $('#tipue_search_input').tipuesearch({
         'mode' : 'json',
         'show': 10,
         'newWindow': true,
         'wholeWords': false
     });
});
</script>
<div class="span8 offset2">
    <div id="tipue_search_content"><div id="tipue_search_loading"></div>
</div>
</div>
