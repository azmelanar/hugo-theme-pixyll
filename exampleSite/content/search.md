+++
date = "2014-11-09T13:49:44+04:00"
draft = false
title = "search"

+++

<div>
<link rel="stylesheet" type="text/css" href="../tipuesearch/tipuesearch.css">
<script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js"></script>
<script type="text/javascript" src="../tipuesearch/tipuesearch_set.js"></script>
<script type="text/javascript" src="../tipuesearch/tipuesearch.min.js"></script>
<script>
$(document).ready(function() {
     $('#tipue_search_input').tipuesearch({
         'mode' : 'json',
         'show': 10,
         'newWindow': true,
         'contentLocation': '../tipuesearch_content.json'
     });
});
</script>
<div class="span8 offset2">
    <div id="tipue_search_content"><div id="tipue_search_loading"></div>
</div>
</div>
