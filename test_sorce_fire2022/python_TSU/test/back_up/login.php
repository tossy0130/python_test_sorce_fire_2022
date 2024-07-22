<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja"><head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>
    いつくしみの杜予約システム
</title>
<meta http-equiv="Content-Script-Type" content="text/javascript">
<meta http-equiv="Content-Style-Type" content="text/css"><meta name="author" content="oriental.co.jp"><meta name="keywords" content="oriental.co.jp">
<link rel="stylesheet" href="/yoyaku/css/pc/import.css" type="text/css" media="all">
<script type="text/javascript" src="/yoyaku/js/pc/jquery-1.4.2.min.js"></script>
<script type="text/javascript" src="/yoyaku/js/pc/main.js"></script>
<script type="text/javascript">//<![CDATA[
    
    $(function(){
        var str = String.fromCharCode(111,114,105,101,110,116,97,108, 46,99,111, 46,106,112); 
$('meta:last').after('<meta name="author" content="' + str + '" />'); 
$('meta:last').after('<meta name="keywords" content="' + str + '" />'); 

    });
//]]></script>
</head><!-- ▼BODY部 スタート -->
<body class="frame_outer"><noscript><p>JavaScript を有効にしてご利用下さい.</p></noscript><div id="header"><!--▼HEADER-->
<div id="header_wrap"><div id="header_line"><a href="https://www.itsukushiminomori.jp/yoyaku/index.php">いつくしみの杜予約システム</a></div></div><!--/#header_wrap-->
<!--▲HEADER-->
</div><div id="main"><div id="login-wrap"><div class="btn"><a class="btn_default" href="javascript:;" onclick="main.setModeAndSubmit('form1', 'top'); return false;">TOP</a><a class="btn_default" href="javascript:;" onclick="main.setModeAndSubmit('form1', 'view_list'); return false;">空き状況確認</a></div><div id="login-form" class="clearfix"><span class="attention">利用するには、津市斎場への業者登録が必要です。</span><br><br><div id="input-form"><form name="form1" id="form1" method="post" action="?"><input type="hidden" name="transactionid" value=""><input type="hidden" name="mode" value="login"><div class="inline"><label for="user_id">ユーザーID：</label><input type="text" name="user_id" size="20" class="box25"></div><div class="inline clearfix"><label for="password">パスワード：</label><input type="password" name="password" size="20" class="box25"></div><div class="btn_area"><ul><li><a class="btn_default" href="javascript:;" onclick="document.form1.submit(); return false;"><span>OK</span></a></li><li><a class="btn_default" href="javascript:;" onclick="document.form1.reset(); return false;"><span>キャンセル</span></a></li><li><a class="btn_default" href="/yoyaku/view_list.php?">戻る</a></li></ul></div></form></div><br><span class="strong">注）ID及びパスワードを忘れた場合は、斎場へ問合せください。</span></div></div></div><div id="footer">
<!--▼FOOTER-->
<div id="footer_wrap"><div id="footer_line" class="clearfix"><div id="copyright">Copyright ©&nbsp;2014-2023&nbsp;Jim Computer Service All rights reserved.</div></div></div>
<!--▲FOOTER--></div>

</body><!-- ▲BODY部 エンド --></html>