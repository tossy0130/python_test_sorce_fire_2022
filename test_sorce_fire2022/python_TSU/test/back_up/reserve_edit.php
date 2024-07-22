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
<body class="frame_outer"><noscript><p>JavaScript を有効にしてご利用下さい.</p></noscript><script type="text/javascript" src="/yoyaku/js/pc/ajaxzip3-https.js"></script><div id="header"><!--▼HEADER-->
<div id="header_wrap"><div id="header_line"><a href="https://www.itsukushiminomori.jp/yoyaku/index.php">いつくしみの杜予約システム</a></div></div><!--/#header_wrap-->
<!--▲HEADER-->
</div><div id="main"><span class="strong">新規登録</span><br><form name="form1" id="form1" method="post" action="?"><input type="hidden" name="transactionid" value="4677e61e721eb33cc16f76f1ddae13ce77035b6b"><input type="hidden" name="mode" value=""><div class="btn"><a class="btn_default" href="javascript:;" onclick="main.setModeAndSubmit('form1', 'logout'); return false;">ログアウト</a><a class="btn_default" href="javascript:;" onclick="main.setModeAndSubmit('form1', 'view_list'); return false;">空き状況確認</a><a class="btn_default" href="javascript:;" onclick="main.setModeAndSubmit('form1', 'reserve_list'); return false;">予約状況確認</a></div><table class="list"><caption class="strong">■予約情報</caption><colgroup><col width="25%"><col width="75%"></colgroup><tbody><tr><th class="alignL">火葬予約日時</th><td class="alignL"><input type="hidden" name="yoyakubi_date" value="23-04-05 15:00">2023年04月05日(水) 15:00</td></tr><tr><th class="alignL">待合室利用</th><td class="alignL"><span class="attention"></span><span style=""><label><input type="radio" name="room_type" value="0" checked="checked">利用する</label>
<label><input type="radio" name="room_type" value="1">洋室</label>
<label><input type="radio" name="room_type" value="2">和室</label>
<label><input type="radio" name="room_type" value="3">利用しない</label></span></td></tr><tr><th class="alignL">霊柩車利用</th><td class="alignL"><span class="attention"></span><span style=""><label><input type="radio" name="car_type" value="0" checked="checked">利用しない</label>
<label><input type="radio" name="car_type" value="1">特別車</label>
<label><input type="radio" name="car_type" value="2">普通車</label></span><span style="margin-left:20px;"></span>出棺時刻：<select name="car_dtkb" id="car_dtkb" style=""><option value="" selected="">未選択</option><option label="前日" value="-1">前日</option>
<option label="当日" value="0">当日</option>
</select><select name="car_time" id="car_time" style=""><option value="" selected="">未選択</option><option label="7:00" value="7:00">7:00</option>
<option label="7:10" value="7:10">7:10</option>
<option label="7:20" value="7:20">7:20</option>
<option label="7:30" value="7:30">7:30</option>
<option label="7:40" value="7:40">7:40</option>
<option label="7:50" value="7:50">7:50</option>
<option label="8:00" value="8:00">8:00</option>
<option label="8:10" value="8:10">8:10</option>
<option label="8:20" value="8:20">8:20</option>
<option label="8:30" value="8:30">8:30</option>
<option label="8:40" value="8:40">8:40</option>
<option label="8:50" value="8:50">8:50</option>
<option label="9:00" value="9:00">9:00</option>
<option label="9:10" value="9:10">9:10</option>
<option label="9:20" value="9:20">9:20</option>
<option label="9:30" value="9:30">9:30</option>
<option label="9:40" value="9:40">9:40</option>
<option label="9:50" value="9:50">9:50</option>
<option label="10:00" value="10:00">10:00</option>
<option label="10:10" value="10:10">10:10</option>
<option label="10:20" value="10:20">10:20</option>
<option label="10:30" value="10:30">10:30</option>
<option label="10:40" value="10:40">10:40</option>
<option label="10:50" value="10:50">10:50</option>
<option label="11:00" value="11:00">11:00</option>
<option label="11:10" value="11:10">11:10</option>
<option label="11:20" value="11:20">11:20</option>
<option label="11:30" value="11:30">11:30</option>
<option label="11:40" value="11:40">11:40</option>
<option label="11:50" value="11:50">11:50</option>
<option label="12:00" value="12:00">12:00</option>
<option label="12:10" value="12:10">12:10</option>
<option label="12:20" value="12:20">12:20</option>
<option label="12:30" value="12:30">12:30</option>
<option label="12:40" value="12:40">12:40</option>
<option label="12:50" value="12:50">12:50</option>
<option label="13:00" value="13:00">13:00</option>
<option label="13:10" value="13:10">13:10</option>
<option label="13:20" value="13:20">13:20</option>
<option label="13:30" value="13:30">13:30</option>
<option label="13:40" value="13:40">13:40</option>
<option label="13:50" value="13:50">13:50</option>
<option label="14:00" value="14:00">14:00</option>
<option label="14:10" value="14:10">14:10</option>
<option label="14:20" value="14:20">14:20</option>
<option label="14:30" value="14:30">14:30</option>
<option label="14:40" value="14:40">14:40</option>
<option label="14:50" value="14:50">14:50</option>
<option label="15:00" value="15:00">15:00</option>
<option label="15:10" value="15:10">15:10</option>
<option label="15:20" value="15:20">15:20</option>
<option label="15:30" value="15:30">15:30</option>
<option label="15:40" value="15:40">15:40</option>
<option label="15:50" value="15:50">15:50</option>
<option label="16:00" value="16:00">16:00</option>
<option label="16:10" value="16:10">16:10</option>
<option label="16:20" value="16:20">16:20</option>
<option label="16:30" value="16:30">16:30</option>
<option label="16:40" value="16:40">16:40</option>
<option label="16:50" value="16:50">16:50</option>
<option label="17:00" value="17:00">17:00</option>
<option label="17:10" value="17:10">17:10</option>
<option label="17:20" value="17:20">17:20</option>
<option label="17:30" value="17:30">17:30</option>
<option label="17:40" value="17:40">17:40</option>
<option label="17:50" value="17:50">17:50</option>
<option label="18:00" value="18:00">18:00</option>
<option label="18:10" value="18:10">18:10</option>
<option label="18:20" value="18:20">18:20</option>
<option label="18:30" value="18:30">18:30</option>
<option label="18:40" value="18:40">18:40</option>
<option label="18:50" value="18:50">18:50</option>
<option label="19:00" value="19:00">19:00</option>
<option label="19:10" value="19:10">19:10</option>
<option label="19:20" value="19:20">19:20</option>
<option label="19:30" value="19:30">19:30</option>
<option label="19:40" value="19:40">19:40</option>
<option label="19:50" value="19:50">19:50</option>
<option label="20:00" value="20:00">20:00</option>
<option label="20:10" value="20:10">20:10</option>
<option label="20:20" value="20:20">20:20</option>
<option label="20:30" value="20:30">20:30</option>
<option label="20:40" value="20:40">20:40</option>
<option label="20:50" value="20:50">20:50</option>
</select><br>出棺場所：<input type="text" name="car_place" value="" maxlength="200" style=";" class="box300"><span class="alignL attention">※住所、会館名等を入力します。</span></td></tr><tr><th class="alignL">通夜式利用</th><td class="alignL"><span class="attention"></span><span style=""><label><input type="radio" name="tsuya_type" value="0" checked="checked">利用しない</label>
<label><input type="radio" name="tsuya_type" value="1">利用する</label></span><span style="margin-left:20px;"></span>開始時刻：<select name="tsuya_dtkb" id="tsuya_dtkb" style=""><option label="前日" value="-1" selected="selected">前日</option>
<option label="当日" value="0">当日</option>
</select><select name="tsuya_time" id="tsuya_time" style=""><option value="" selected="">未選択</option><option label="7:00" value="7:00">7:00</option>
<option label="7:10" value="7:10">7:10</option>
<option label="7:20" value="7:20">7:20</option>
<option label="7:30" value="7:30">7:30</option>
<option label="7:40" value="7:40">7:40</option>
<option label="7:50" value="7:50">7:50</option>
<option label="8:00" value="8:00">8:00</option>
<option label="8:10" value="8:10">8:10</option>
<option label="8:20" value="8:20">8:20</option>
<option label="8:30" value="8:30">8:30</option>
<option label="8:40" value="8:40">8:40</option>
<option label="8:50" value="8:50">8:50</option>
<option label="9:00" value="9:00">9:00</option>
<option label="9:10" value="9:10">9:10</option>
<option label="9:20" value="9:20">9:20</option>
<option label="9:30" value="9:30">9:30</option>
<option label="9:40" value="9:40">9:40</option>
<option label="9:50" value="9:50">9:50</option>
<option label="10:00" value="10:00">10:00</option>
<option label="10:10" value="10:10">10:10</option>
<option label="10:20" value="10:20">10:20</option>
<option label="10:30" value="10:30">10:30</option>
<option label="10:40" value="10:40">10:40</option>
<option label="10:50" value="10:50">10:50</option>
<option label="11:00" value="11:00">11:00</option>
<option label="11:10" value="11:10">11:10</option>
<option label="11:20" value="11:20">11:20</option>
<option label="11:30" value="11:30">11:30</option>
<option label="11:40" value="11:40">11:40</option>
<option label="11:50" value="11:50">11:50</option>
<option label="12:00" value="12:00">12:00</option>
<option label="12:10" value="12:10">12:10</option>
<option label="12:20" value="12:20">12:20</option>
<option label="12:30" value="12:30">12:30</option>
<option label="12:40" value="12:40">12:40</option>
<option label="12:50" value="12:50">12:50</option>
<option label="13:00" value="13:00">13:00</option>
<option label="13:10" value="13:10">13:10</option>
<option label="13:20" value="13:20">13:20</option>
<option label="13:30" value="13:30">13:30</option>
<option label="13:40" value="13:40">13:40</option>
<option label="13:50" value="13:50">13:50</option>
<option label="14:00" value="14:00">14:00</option>
<option label="14:10" value="14:10">14:10</option>
<option label="14:20" value="14:20">14:20</option>
<option label="14:30" value="14:30">14:30</option>
<option label="14:40" value="14:40">14:40</option>
<option label="14:50" value="14:50">14:50</option>
<option label="15:00" value="15:00">15:00</option>
<option label="15:10" value="15:10">15:10</option>
<option label="15:20" value="15:20">15:20</option>
<option label="15:30" value="15:30">15:30</option>
<option label="15:40" value="15:40">15:40</option>
<option label="15:50" value="15:50">15:50</option>
<option label="16:00" value="16:00">16:00</option>
<option label="16:10" value="16:10">16:10</option>
<option label="16:20" value="16:20">16:20</option>
<option label="16:30" value="16:30">16:30</option>
<option label="16:40" value="16:40">16:40</option>
<option label="16:50" value="16:50">16:50</option>
<option label="17:00" value="17:00">17:00</option>
<option label="17:10" value="17:10">17:10</option>
<option label="17:20" value="17:20">17:20</option>
<option label="17:30" value="17:30">17:30</option>
<option label="17:40" value="17:40">17:40</option>
<option label="17:50" value="17:50">17:50</option>
<option label="18:00" value="18:00">18:00</option>
<option label="18:10" value="18:10">18:10</option>
<option label="18:20" value="18:20">18:20</option>
<option label="18:30" value="18:30">18:30</option>
<option label="18:40" value="18:40">18:40</option>
<option label="18:50" value="18:50">18:50</option>
<option label="19:00" value="19:00">19:00</option>
<option label="19:10" value="19:10">19:10</option>
<option label="19:20" value="19:20">19:20</option>
<option label="19:30" value="19:30">19:30</option>
<option label="19:40" value="19:40">19:40</option>
<option label="19:50" value="19:50">19:50</option>
<option label="20:00" value="20:00">20:00</option>
<option label="20:10" value="20:10">20:10</option>
<option label="20:20" value="20:20">20:20</option>
<option label="20:30" value="20:30">20:30</option>
<option label="20:40" value="20:40">20:40</option>
<option label="20:50" value="20:50">20:50</option>
</select></td></tr><tr><th class="alignL">葬儀式場利用</th><td class="alignL"><span class="attention"></span><span style=""><label><input type="radio" name="shiki_type" value="0" checked="checked">利用しない</label>
<label><input type="radio" name="shiki_type" value="1">利用する</label></span><span style="margin-left:20px;"></span>開始時刻：<select name="shiki_dtkb" id="shiki_dtkb" style=""><option label="前日" value="-1">前日</option>
<option label="当日" value="0" selected="selected">当日</option>
</select><select name="shiki_time" id="shiki_time" style=""><option value="" selected="">未選択</option><option label="7:00" value="7:00">7:00</option>
<option label="7:10" value="7:10">7:10</option>
<option label="7:20" value="7:20">7:20</option>
<option label="7:30" value="7:30">7:30</option>
<option label="7:40" value="7:40">7:40</option>
<option label="7:50" value="7:50">7:50</option>
<option label="8:00" value="8:00">8:00</option>
<option label="8:10" value="8:10">8:10</option>
<option label="8:20" value="8:20">8:20</option>
<option label="8:30" value="8:30">8:30</option>
<option label="8:40" value="8:40">8:40</option>
<option label="8:50" value="8:50">8:50</option>
<option label="9:00" value="9:00">9:00</option>
<option label="9:10" value="9:10">9:10</option>
<option label="9:20" value="9:20">9:20</option>
<option label="9:30" value="9:30">9:30</option>
<option label="9:40" value="9:40">9:40</option>
<option label="9:50" value="9:50">9:50</option>
<option label="10:00" value="10:00">10:00</option>
<option label="10:10" value="10:10">10:10</option>
<option label="10:20" value="10:20">10:20</option>
<option label="10:30" value="10:30">10:30</option>
<option label="10:40" value="10:40">10:40</option>
<option label="10:50" value="10:50">10:50</option>
<option label="11:00" value="11:00">11:00</option>
<option label="11:10" value="11:10">11:10</option>
<option label="11:20" value="11:20">11:20</option>
<option label="11:30" value="11:30">11:30</option>
<option label="11:40" value="11:40">11:40</option>
<option label="11:50" value="11:50">11:50</option>
<option label="12:00" value="12:00">12:00</option>
<option label="12:10" value="12:10">12:10</option>
<option label="12:20" value="12:20">12:20</option>
<option label="12:30" value="12:30">12:30</option>
<option label="12:40" value="12:40">12:40</option>
<option label="12:50" value="12:50">12:50</option>
<option label="13:00" value="13:00">13:00</option>
<option label="13:10" value="13:10">13:10</option>
<option label="13:20" value="13:20">13:20</option>
<option label="13:30" value="13:30">13:30</option>
<option label="13:40" value="13:40">13:40</option>
<option label="13:50" value="13:50">13:50</option>
<option label="14:00" value="14:00">14:00</option>
<option label="14:10" value="14:10">14:10</option>
<option label="14:20" value="14:20">14:20</option>
<option label="14:30" value="14:30">14:30</option>
<option label="14:40" value="14:40">14:40</option>
<option label="14:50" value="14:50">14:50</option>
<option label="15:00" value="15:00">15:00</option>
<option label="15:10" value="15:10">15:10</option>
<option label="15:20" value="15:20">15:20</option>
<option label="15:30" value="15:30">15:30</option>
<option label="15:40" value="15:40">15:40</option>
<option label="15:50" value="15:50">15:50</option>
<option label="16:00" value="16:00">16:00</option>
<option label="16:10" value="16:10">16:10</option>
<option label="16:20" value="16:20">16:20</option>
<option label="16:30" value="16:30">16:30</option>
<option label="16:40" value="16:40">16:40</option>
<option label="16:50" value="16:50">16:50</option>
<option label="17:00" value="17:00">17:00</option>
<option label="17:10" value="17:10">17:10</option>
<option label="17:20" value="17:20">17:20</option>
<option label="17:30" value="17:30">17:30</option>
<option label="17:40" value="17:40">17:40</option>
<option label="17:50" value="17:50">17:50</option>
<option label="18:00" value="18:00">18:00</option>
<option label="18:10" value="18:10">18:10</option>
<option label="18:20" value="18:20">18:20</option>
<option label="18:30" value="18:30">18:30</option>
<option label="18:40" value="18:40">18:40</option>
<option label="18:50" value="18:50">18:50</option>
<option label="19:00" value="19:00">19:00</option>
<option label="19:10" value="19:10">19:10</option>
<option label="19:20" value="19:20">19:20</option>
<option label="19:30" value="19:30">19:30</option>
<option label="19:40" value="19:40">19:40</option>
<option label="19:50" value="19:50">19:50</option>
<option label="20:00" value="20:00">20:00</option>
<option label="20:10" value="20:10">20:10</option>
<option label="20:20" value="20:20">20:20</option>
<option label="20:30" value="20:30">20:30</option>
<option label="20:40" value="20:40">20:40</option>
<option label="20:50" value="20:50">20:50</option>
</select></td></tr><tr><th class="alignL">火葬区分</th><td class="alignL"><span class="attention"></span><span style=""><label><input type="radio" name="kasou_type" value="0" checked="checked">大人(12歳以上)</label>
<label><input type="radio" name="kasou_type" value="1">小人(12歳未満)</label></span></td></tr><tr><th class="alignL">死亡者の居住地</th><td class="alignL"><span class="attention"></span><span style=""><label><input type="radio" name="region_type" value="0" checked="checked">市内</label>
<label><input type="radio" name="region_type" value="1">市外</label></span></td></tr><tr><th class="alignL">受付番号</th><td class="alignL">6174</td></tr></tbody></table><table class="list"><caption class="strong">■申請者情報</caption><colgroup><col width="25%"><col width="75%"></colgroup><tbody><tr><th class="alignL">申請者氏名</th><td class="alignL"><span class="attention"></span>姓：<input type="text" name="applicant_name01" value="" maxlength="50" style=";" class="box30">　名：<input type="text" name="applicant_name02" value="" maxlength="50" style=";" class="box30"></td></tr><tr><th class="alignL">申請者カナ</th><td class="alignL"><span class="attention"></span>姓：<input type="text" name="applicant_kana01" value="" maxlength="50" style=";" class="box30">　名：<input type="text" name="applicant_kana02" value="" maxlength="50" style=";" class="box30"><br><span class="alignL attention">※カナは、全角カタカナで入力します。</span></td></tr><tr><th class="alignL">連絡先TEL</th><td class="alignL"><span class="attention"></span><input type="text" name="applicant_tel01" value="" maxlength="6" size="6" class="box6" style=";">- <input type="text" name="applicant_tel02" value="" maxlength="6" size="6" class="box6" style=";">- <input type="text" name="applicant_tel03" value="" maxlength="6" size="6" class="box6" style=";"></td></tr><tr><th class="alignL">故人との続柄</th><td class="alignL"><span class="attention"></span><span style=""><label><input type="radio" name="applicant_rel" value="0" checked="checked">親族</label>
<label><input type="radio" name="applicant_rel" value="1">その他</label></span></td></tr><tr><th class="alignL">郵便番号</th><td class="alignL"><span class="attention"></span>〒 <input type="text" name="applicant_zip01" value="" maxlength="3" size="6" class="box6" style="ime-mode:disabled;">- <input type="text" name="applicant_zip02" value="" maxlength="4" size="6" class="box6" style="ime-mode:disabled;"><input type="button" value="郵便→住所" onclick="main.chkCode('applicant_zip01');main.chkCode('applicant_zip02');AjaxZip3.zip2addr('applicant_zip01','applicant_zip02','applicant_address1','applicant_address1');"></td></tr><tr><th class="alignL">住所</th><td class="alignL"><span class="attention"></span>町名まで：<input type="text" name="applicant_address1" value="" maxlength="200" style=";" class="box240"><span style="margin-left:20px;"></span>番地以降：<input type="text" name="applicant_address2" value="" maxlength="200" style=";" class="box240"></td></tr></tbody></table><table class="list"><caption class="strong">■死亡者情報</caption><colgroup><col width="25%"><col width="75%"></colgroup><tbody><tr><th class="alignL">死亡者氏名</th><td class="alignL"><span class="attention"></span>姓：<input type="text" name="dead_name01" value="" maxlength="50" style=";" class="box30">　名：<input type="text" name="dead_name02" value="" maxlength="50" style=";" class="box30"></td></tr><tr><th class="alignL">死亡者カナ</th><td class="alignL"><span class="attention"></span>姓：<input type="text" name="dead_kana01" value="" maxlength="50" style=";" class="box30">　名：<input type="text" name="dead_kana02" value="" maxlength="50" style=";" class="box30"><br><span class="alignL attention">※カナは、全角カタカナで入力します。</span></td></tr><tr><th class="alignL">性別</th><td class="alignL"><span class="attention"></span><span style=""><label><input type="radio" name="dead_sex" value="0">男性</label>
<label><input type="radio" name="dead_sex" value="1">女性</label>
<label><input type="radio" name="dead_sex" value="2">不詳</label></span></td></tr><tr><th class="alignL">生年月日</th><td class="alignL"><select name="dead_birth_koyomi_type" style=""><option value="" selected="">未選択</option><option label="西暦" value="-1">西暦</option>
<option label="令和" value="4">令和</option>
<option label="平成" value="3">平成</option>
<option label="昭和" value="2">昭和</option>
<option label="大正" value="1">大正</option>
<option label="明治" value="0">明治</option>
</select><input type="text" name="dead_birth_year" value="" maxlength="50" style=";" size="6" class="box6">年&nbsp;<select name="dead_birth_month" style=""><option value="" selected="">未選択</option><option label="1" value="1">1</option>
<option label="2" value="2">2</option>
<option label="3" value="3">3</option>
<option label="4" value="4">4</option>
<option label="5" value="5">5</option>
<option label="6" value="6">6</option>
<option label="7" value="7">7</option>
<option label="8" value="8">8</option>
<option label="9" value="9">9</option>
<option label="10" value="10">10</option>
<option label="11" value="11">11</option>
<option label="12" value="12">12</option>
</select>月&nbsp;<select name="dead_birth_day" style=""><option value="" selected="">未選択</option><option label="1" value="1">1</option>
<option label="2" value="2">2</option>
<option label="3" value="3">3</option>
<option label="4" value="4">4</option>
<option label="5" value="5">5</option>
<option label="6" value="6">6</option>
<option label="7" value="7">7</option>
<option label="8" value="8">8</option>
<option label="9" value="9">9</option>
<option label="10" value="10">10</option>
<option label="11" value="11">11</option>
<option label="12" value="12">12</option>
<option label="13" value="13">13</option>
<option label="14" value="14">14</option>
<option label="15" value="15">15</option>
<option label="16" value="16">16</option>
<option label="17" value="17">17</option>
<option label="18" value="18">18</option>
<option label="19" value="19">19</option>
<option label="20" value="20">20</option>
<option label="21" value="21">21</option>
<option label="22" value="22">22</option>
<option label="23" value="23">23</option>
<option label="24" value="24">24</option>
<option label="25" value="25">25</option>
<option label="26" value="26">26</option>
<option label="27" value="27">27</option>
<option label="28" value="28">28</option>
<option label="29" value="29">29</option>
<option label="30" value="30">30</option>
<option label="31" value="31">31</option>
</select>日</td></tr><tr><th class="alignL">死亡年月日</th><td class="alignL"><select name="dead_koyomi_type" style=""><option value="" selected="">未選択</option><option label="西暦" value="-1">西暦</option>
<option label="令和" value="4">令和</option>
<option label="平成" value="3">平成</option>
<option label="昭和" value="2">昭和</option>
<option label="大正" value="1">大正</option>
<option label="明治" value="0">明治</option>
</select><input type="text" name="dead_year" value="" maxlength="50" style=";" size="6" class="box6">年&nbsp;<select name="dead_month" style=""><option value="" selected="">未選択</option><option label="1" value="1">1</option>
<option label="2" value="2">2</option>
<option label="3" value="3">3</option>
<option label="4" value="4">4</option>
<option label="5" value="5">5</option>
<option label="6" value="6">6</option>
<option label="7" value="7">7</option>
<option label="8" value="8">8</option>
<option label="9" value="9">9</option>
<option label="10" value="10">10</option>
<option label="11" value="11">11</option>
<option label="12" value="12">12</option>
</select>月&nbsp;<select name="dead_day" style=""><option value="" selected="">未選択</option><option label="1" value="1">1</option>
<option label="2" value="2">2</option>
<option label="3" value="3">3</option>
<option label="4" value="4">4</option>
<option label="5" value="5">5</option>
<option label="6" value="6">6</option>
<option label="7" value="7">7</option>
<option label="8" value="8">8</option>
<option label="9" value="9">9</option>
<option label="10" value="10">10</option>
<option label="11" value="11">11</option>
<option label="12" value="12">12</option>
<option label="13" value="13">13</option>
<option label="14" value="14">14</option>
<option label="15" value="15">15</option>
<option label="16" value="16">16</option>
<option label="17" value="17">17</option>
<option label="18" value="18">18</option>
<option label="19" value="19">19</option>
<option label="20" value="20">20</option>
<option label="21" value="21">21</option>
<option label="22" value="22">22</option>
<option label="23" value="23">23</option>
<option label="24" value="24">24</option>
<option label="25" value="25">25</option>
<option label="26" value="26">26</option>
<option label="27" value="27">27</option>
<option label="28" value="28">28</option>
<option label="29" value="29">29</option>
<option label="30" value="30">30</option>
<option label="31" value="31">31</option>
</select>日</td></tr><tr><th class="alignL">郵便番号</th><td class="alignL"><span class="attention"></span>〒 <input type="text" name="dead_zip01" value="" maxlength="3" size="6" class="box6" style="ime-mode:disabled;;">- <input type="text" name="dead_zip02" value="" maxlength="4" size="6" class="box6" style="ime-mode:disabled;;"><input type="button" value="郵便→住所" onclick="main.chkCode('dead_zip01');main.chkCode('dead_zip02');AjaxZip3.zip2addr('dead_zip01','dead_zip02','dead_address1','dead_address1');"></td></tr><tr><th class="alignL">住所</th><td class="alignL"><span class="attention"></span>町名まで：<input type="text" name="dead_address1" value="" maxlength="200" style=";" class="box240"><span style="margin-left:20px;"></span>番地以降：<input type="text" name="dead_address2" value="" maxlength="200" style=";" class="box240"></td></tr><tr><th class="alignL">郵便番号（本籍）</th><td class="alignL"><span class="attention"></span>〒 <input type="text" name="dead_honseki_zip01" value="" maxlength="3" size="6" class="box6" style="ime-mode:disabled;;">- <input type="text" name="dead_honseki_zip02" value="" maxlength="4" size="6" class="box6" style="ime-mode:disabled;;"><input type="button" value="郵便→住所" onclick="main.chkCode('dead_honseki_zip01');main.chkCode('dead_honseki_zip02');AjaxZip3.zip2addr('dead_honseki_zip01','dead_honseki_zip02','dead_honseki_address1','dead_honseki_address1');"></td></tr><tr><th class="alignL">本籍</th><td class="alignL"><span class="attention"></span>町名まで：<input type="text" name="dead_honseki_address1" value="" maxlength="200" style=";" class="box240"><span style="margin-left:20px;"></span>番地以降：<input type="text" name="dead_honseki_address2" value="" maxlength="200" style=";" class="box240"></td></tr></tbody></table><table class="list"><caption class="strong">■業者情報</caption><colgroup><col width="25%"><col width="75%"></colgroup><tbody><tr><th class="alignL">担当者</th><td class="alignL">ジム・コンピュータ・サービス 夏目</td></tr><tr><th class="alignL">メールアドレス</th><td class="alignL">natsume@jimnet.co.jp</td></tr><tr><th class="alignL">FAX送付</th><td class="alignL"><span class="attention"></span><span style=""><label><input type="radio" name="stuff_fax_flg" value="0" checked="checked">送信しない</label>
<label><input type="radio" name="stuff_fax_flg" value="1">送信する</label></span></td></tr><tr><th class="alignL">FAX番号</th><td class="alignL"><span class="attention"></span><input type="text" name="stuff_fax01" value="0256" maxlength="6" size="6" class="box6" style=";">- <input type="text" name="stuff_fax02" value="34" maxlength="6" size="6" class="box6" style=";">- <input type="text" name="stuff_fax03" value="2795" maxlength="6" size="6" class="box6" style=";"></td></tr><tr><th class="alignL">連絡事項</th><td class="alignL"><span class="attention"></span><textarea name="stuff_info" cols="50" rows="5" style=";"></textarea></td></tr></tbody></table><div class="btn"><a class="btn_default" href="javascript:;" onclick="main.setModeAndSubmit('form1', 'entry_confirm'); return false;">予約を登録する</a></div></form></div><div id="footer">
<!--▼FOOTER-->
<div id="footer_wrap"><div id="footer_line" class="clearfix"><div id="copyright">Copyright ©&nbsp;2014-2023&nbsp;Jim Computer Service All rights reserved.</div></div></div>
<!--▲FOOTER--></div>

</body><!-- ▲BODY部 エンド --></html>