﻿<%@ Page Language="C#" AutoEventWireup="true" CodeFile="index.aspx.cs" Inherits="index" %>

<html>
<!-- Author: Michael Feather -->
<head>
 <title> Cube Solver </title>
 <meta name="robots" content="nofollow">
 <link rel=icon href=mini_cube.png type=image/png>
 <link rel="stylesheet" type="text/css" href="style2.css">
 <meta name=viewport content="width=device-width, initial-scale=1">

    <script src="./jquery.js"></script>
    <script src="./Cube.js"></script>

 <script src=rch.js></script>
 <script src=rclib.js></script>
 <script src=solve.js></script>
 <script src=verify.js></script>
 <script src=readfiles.js></script>



    
    <link rel="stylesheet" href="css/ystep.css" />
    <script type="text/javascript" src="js/jquery.min.js"></script>
    <script type="text/javascript" src="js/setStep.js"></script>



 <style> 
  div.wrap {
    height:100%;
    overflow:auto;
    padding:0px 5%; }
  .sbtn {
    height:28px;
    width:74px;
    border-radius:15px;
    background-color:#ffffff;
    padding:0px;
    border:none;
    outline:none;
  }
 </style>

    <script src="js/jquery.qrcode.min.js"></script>

    <!-- Add fancyBox main JS and CSS files -->
	<script type="text/javascript" src="../source/jquery.fancybox.js?v=2.1.5"></script>
	<link rel="stylesheet" type="text/css" href="../source/jquery.fancybox.css?v=2.1.5" media="screen" />
    <script type="text/javascript">
        $(document).ready(function () {
            $('.fancybox').fancybox();
        });
	</script>
</head>
<body>
<div class=wrap>
<center>
<style> input { height:22px; width:22px;} </style>
<table>
    
<tr><td height=50></tr>
<tr><td valign=top>
<font size=+2> Cube Solver </font>
<table border=0 style=line-height:0>
  <tr height=8>
  <tr>
    <!--
    <td>
      <input id=b1 type=button onclick="switch_style()" style="opacity:0">
      <input id=b1 type=button style="opacity:0"> 
    </td>
    -->
    <td colspan=4></td>
    <td> <input id=f0 type=button onclick=set_color(this)> </td>
    <td> <input id=f1 type=button onclick=set_color(this)> </td>
    <td> <input id=f2 type=button onclick=set_color(this)> </td>
    <td colspan=2>
    <td colspan=5 rowspan=3 align=center>
      <table border=0>
        <tr height=5> </tr>
        <tr>
          <td width=3>
          <td> <input type=button id=R onclick=select_color(this) style="background-color:red;"> </td>
          <td> <input type=button id=Y onclick=select_color(this) style="background-color:yellow;"> </td>
          <td> <input type=button id=B onclick=select_color(this) style="background-color:blue;"> </td>
        </tr>
        <tr>
          <td>
          <td> <input type=button id=O onclick=select_color(this) style="background-color:orange"> </td>
          <td> <input type=button id=W onclick=select_color(this) style="background-color:white"> </td>
          <td> <input type=button id=G onclick=select_color(this) style="background-color:green"> </td>
        </tr>
      </table>
    </td>
  </tr>
  <tr> 
    <td colspan=4></td>
    <td> <input id=f3 type=button onclick=set_color(this)> </td>
    <td> <input id=f4 type=button onclick=set_color(this)> </td> 
    <td> <input id=f5 type=button onclick=set_color(this)> </td>
  </tr>
  <tr> 
    <td colspan=4></td>
    <td> <input id=f6 type=button onclick=set_color(this)> </td>
    <td> <input id=f7 type=button onclick=set_color(this)> </td>
    <td> <input id=f8 type=button onclick=set_color(this)> </td>
  </tr>
  <tr height=10> </tr>
  <tr>
    <td> <input id=f9 type=button onclick=set_color(this)> </td>
    <td> <input id=f10 type=button onclick=set_color(this)> </td>
    <td> <input id=f11 type=button onclick=set_color(this)> </td>
    <td width=12> </td>
    <td> <input id=f12 type=button onclick=set_color(this)> </td>
    <td> <input id=f13 type=button onclick=set_color(this)> </td>
    <td> <input id=f14 type=button onclick=set_color(this)> </td>
    <td width=12> </td>
    <td> <input id=f15 type=button onclick=set_color(this)> </td>
    <td> <input id=f16 type=button onclick=set_color(this)> </td>
    <td> <input id=f17 type=button onclick=set_color(this)> </td>
    <td width=12> </td>
    <td> <input id=f18 type=button onclick=set_color(this)> </td>
    <td> <input id=f19 type=button onclick=set_color(this)> </td>
    <td> <input id=f20 type=button onclick=set_color(this)> </td>
  </tr>
  <tr>
    <td> <input id=f21 type=button onclick=set_color(this)> </td>
    <td> <input id=f22 type=button onclick=set_color(this)> </td>
    <td> <input id=f23 type=button onclick=set_color(this)> </td>
    <td> </td>
    <td> <input id=f24 type=button onclick=set_color(this)> </td>
    <td> <input id=f25 type=button onclick=set_color(this)> </td>
    <td> <input id=f26 type=button onclick=set_color(this)> </td>
    <td> </td>
    <td> <input id=f27 type=button onclick=set_color(this)> </td>
    <td> <input id=f28 type=button onclick=set_color(this)> </td>
    <td> <input id=f29 type=button onclick=set_color(this)> </td>
    <td> </td>
    <td> <input id=f30 type=button onclick=set_color(this)> </td>
    <td> <input id=f31 type=button onclick=set_color(this)> </td>
    <td> <input id=f32 type=button onclick=set_color(this)> </td>
  </tr>
  <tr>
    <td> <input id=f33 type=button onclick=set_color(this)> </td>
    <td> <input id=f34 type=button onclick=set_color(this)> </td>
    <td> <input id=f35 type=button onclick=set_color(this)> </td>
    <td> </td>
    <td> <input id=f36 type=button onclick=set_color(this)> </td>
    <td> <input id=f37 type=button onclick=set_color(this)> </td>
    <td> <input id=f38 type=button onclick=set_color(this)> </td>
    <td> </td>
    <td> <input id=f39 type=button onclick=set_color(this)> </td>
    <td> <input id=f40 type=button onclick=set_color(this)> </td>
    <td> <input id=f41 type=button onclick=set_color(this)> </td>
    <td> </td>
    <td> <input id=f42 type=button onclick=set_color(this)> </td>
    <td> <input id=f43 type=button onclick=set_color(this)> </td>
    <td> <input id=f44 type=button onclick=set_color(this)> </td>
  </tr>
  <tr height=10> </tr>
  <tr>
    <td colspan=4></td>
    <td> <input id=f45 type=button onclick=set_color(this)> </td>
    <td> <input id=f46 type=button onclick=set_color(this)> </td>
    <td> <input id=f47 type=button onclick=set_color(this)> </td>
  </tr>
  <tr>
    <td colspan=4></td>
    <td> <input id=f48 type=button onclick=set_color(this)> </td>
    <td> <input id=f49 type=button onclick=set_color(this)> </td>
    <td> <input id=f50 type=button onclick=set_color(this)> </td>
  </tr>
  <tr>
    <td colspan=4></td>
    <td> <input id=f51 type=button onclick=set_color(this)> </td>
    <td> <input id=f52 type=button onclick=set_color(this)> </td>
    <td> <input id=f53 type=button onclick=set_color(this)> </td>
  </tr>
</table>

<table border=0>
  <tr height=14>
  <tr>
    <td> <button class="btn svw1" onclick="home()">Home</button> </td>
    <td width=5>
    <td> <button class="btn svw1" onclick="show()">Show</button> </td>
    <td width=5>
    <td> <button class="btn svw2" onclick="rand()">Random</button> </td>
    <td width=5>
<!--
    <td> <button id=sbtn class=sbtn onclick="solve()">Solve</button> </td>
-->
    <td> <button id=sbtn class="btn svw1" onclick="solve()">Solve</button> </td>
  </tr>
  <tr height=10>
  <tr>
    <td> <button class="btn svw1" onclick="clear()" style="visibility:hidden">Clear</button> </td>
    <td width=5> </td>
    <td> <button class="btn svw1" onclick="help()" style="visibility:hidden">Help</button> </td>
    <td width=5> </td>
    <td valign=top colspan=3 style=text-align:right>


        <!--这里的search time是搜索次数 设为隐藏-->
        <!--Search Time-->
        <input type=text name=stl id=stl maxlength=5 style="font-size:.9em; height:24px; width:40px; border:none; border-radius:10px; padding-left:8px; border-radius:15px; visibility:hidden" value=5>



    </td>
  </tr>
  <tr height=10>
  <tr> 
    <td colspan=8>
      <div id=btn>
      </div>
     </td>
  </tr>
</table>

</td><td width=5%><td id=tdc valign=top>
    <!--<iframe id="cube"></iframe>-->
    
<div style=width:300px>
                    <div id="mf" style="margin: 40px auto 80px;"></div>

                    <div id="btns">
                        <!--<input type="button" class="btn" value="u" id="u" />
                        <input type="button" class="btn" value="e" id="e" />
                        <input type="button" class="btn" value="d" id="d'" />
                        <input type="button" class="btn" value="l" id="l'" />
                        <input type="button" class="btn" value="m" id="m" />
                        <input type="button" class="btn" value="r" id="r" />
                        <input type="button" class="btn" value="f" id="f" />
                        <input type="button" class="btn" value="s" id="s" />
                        <input type="button" class="btn" value="b" id="b'" />
                        <input type="button" class="btn" value="u'" id="u'" />
                        <input type="button" class="btn" value="e'" id="e'" />
                        <input type="button" class="btn" value="d'" id="d" />
                        <input type="button" class="btn" value="l'" id="l" />
                        <input type="button" class="btn" value="m'" id="m'" />
                        <input type="button" class="btn" value="r'"  id="r'"/>
                        <input type="button" class="btn" value="f'" id="f'" />
                        <input type="button" class="btn" value="s'" id="s'" />
                        <input type="button" class="btn" value="b'" id="b" />-->

                        <input type="button" class="btn" value="U" id="u" />
                        <input type="button" class="btn" value="E" id="e'" />
                        <input type="button" class="btn" value="D" id="d" />
                        <input type="button" class="btn" value="L" id="l" />
                        <input type="button" class="btn" value="M" id="m'" />
                        <input type="button" class="btn" value="R" id="r" />
                        <input type="button" class="btn" value="F" id="f" />
                        <input type="button" class="btn" value="S" id="s" />
                        <input type="button" class="btn" value="B" id="b" />
                        <input type="button" class="btn" value="U'" id="u'" />
                        <input type="button" class="btn" value="E'" id="e" />
                        <input type="button" class="btn" value="D'" id="d'" />
                        <input type="button" class="btn" value="L'" id="l'" />
                        <input type="button" class="btn" value="M'" id="m" />
                        <input type="button" class="btn" value="R'"  id="r'"/>
                        <input type="button" class="btn" value="F'" id="f'" />
                        <input type="button" class="btn" value="S'" id="s'" />
                        <input type="button" class="btn" value="B'" id="b'" />


                        <input type="button" class="btn svw1" onclick="resetCubeLocation()" value="Relocate" />
                    </div>

                    <script type="text/javascript">
                        var cube = new Cube('mf', { borderLength: 200 });

                        var aInt = document.getElementById('btns').getElementsByTagName('input');
                        for (var i = 0; i < aInt.length - 1; i++) {
                            aInt[i].onclick = function () {
                                //cube.turn3(this.value);
                                cube.turn3(this.id);
                            }
                        }
                        function resetCubeLocation() {
                            cube.initL();
                        };
                        function executeAll() {
                            var value = $("#solinput").val();
                            cube.turn3s(value);
                        };
                        function setColorForCube() {
                            colorslist = [$("#f0").css("backgroundColor"), $("#f1").css("backgroundColor"), $("#f2").css("backgroundColor"), $("#f3").css("backgroundColor"), $("#f4").css("backgroundColor"), $("#f5").css("backgroundColor"), $("#f6").css("backgroundColor"), $("#f7").css("backgroundColor"), $("#f8").css("backgroundColor"),
                                $("#f9").css("backgroundColor"), $("#f10").css("backgroundColor"), $("#f11").css("backgroundColor"), $("#f12").css("backgroundColor"), $("#f13").css("backgroundColor"), $("#f14").css("backgroundColor"), $("#f15").css("backgroundColor"), $("#f16").css("backgroundColor"), $("#f17").css("backgroundColor"),
                                $("#f18").css("backgroundColor"), $("#f19").css("backgroundColor"), $("#f20").css("backgroundColor"), $("#f21").css("backgroundColor"), $("#f22").css("backgroundColor"), $("#f23").css("backgroundColor"), $("#f24").css("backgroundColor"), $("#f25").css("backgroundColor"), $("#f26").css("backgroundColor"),
                                $("#f27").css("backgroundColor"), $("#f28").css("backgroundColor"), $("#f29").css("backgroundColor"), $("#f30").css("backgroundColor"), $("#f31").css("backgroundColor"), $("#f32").css("backgroundColor"), $("#f33").css("backgroundColor"), $("#f34").css("backgroundColor"), $("#f35").css("backgroundColor"),
                                $("#f36").css("backgroundColor"), $("#f37").css("backgroundColor"), $("#f38").css("backgroundColor"), $("#f39").css("backgroundColor"), $("#f40").css("backgroundColor"), $("#f41").css("backgroundColor"), $("#f42").css("backgroundColor"), $("#f43").css("backgroundColor"), $("#f44").css("backgroundColor"),
                                $("#f45").css("backgroundColor"), $("#f46").css("backgroundColor"), $("#f47").css("backgroundColor"), $("#f48").css("backgroundColor"), $("#f49").css("backgroundColor"), $("#f50").css("backgroundColor"), $("#f51").css("backgroundColor"), $("#f52").css("backgroundColor"), $("#f53").css("backgroundColor")]

                            for (i = 0; i < colorslist.length; i++) {
                                if (colorslist[i] == "rgb(255, 0, 0)") {
                                    colorslist[i] = "red";
                                }
                                else if (colorslist[i] == "rgb(255, 255, 0)") {
                                    colorslist[i] = "yellow";
                                }
                                else if (colorslist[i] == "rgb(0, 0, 255)") {
                                    colorslist[i] = "blue";
                                }
                                else if (colorslist[i] == "rgb(255, 165, 0)") {
                                    colorslist[i] = "orange";
                                }
                                else if (colorslist[i] == "rgb(255, 255, 255)") {
                                    colorslist[i] = "white";
                                }
                                else if (colorslist[i] == "rgb(0, 128, 0)") {
                                    colorslist[i] = "green";
                                }
                            }

                            //    右边边魔方的编码规律
                            //
                            //               00 01 02
                            //               03 04 05
                            //               06 07 08
                            //               
                            //    18 21 24   36 37 38   33 30 27    47 46 45
                            //    19 22 25   39 40 41   34 31 28    50 49 48
                            //    20 23 26   42 43 44   35 32 29    53 52 51
                            //
                            //               15 16 17
                            //               12 13 14
                            //               09 10 11
                            //
                            //
                            //    左边魔方的编码规律
                            //
                            //               00 01 02
                            //               03 04 05
                            //               06 07 08
                            //
                            //     09 10 11  12 13 14   15 16 17    18 19 20
                            //     21 22 23  24 25 26   27 28 29    30 31 32
                            //     33 34 35  36 37 38   39 40 41    42 43 44
                            //
                            //               45 46 47
                            //               48 49 50
                            //               51 52 53

                            colorslistTop = [];
                            colorslistBottom = [];
                            colorslistLeft = [];
                            colorslistRight = [];
                            colorslistFront = [];
                            colorslistBack = [];
                            colorslistTop.push(colorslist[0]);
                            colorslistTop.push(colorslist[1]);
                            colorslistTop.push(colorslist[2]);
                            colorslistTop.push(colorslist[3]);
                            colorslistTop.push(colorslist[4]);
                            colorslistTop.push(colorslist[5]);
                            colorslistTop.push(colorslist[6]);
                            colorslistTop.push(colorslist[7]);
                            colorslistTop.push(colorslist[8]);

                            colorslistBottom.push(colorslist[51]);
                            colorslistBottom.push(colorslist[52]);
                            colorslistBottom.push(colorslist[53]);
                            colorslistBottom.push(colorslist[48]);
                            colorslistBottom.push(colorslist[49]);
                            colorslistBottom.push(colorslist[50]);
                            colorslistBottom.push(colorslist[45]);
                            colorslistBottom.push(colorslist[46]);
                            colorslistBottom.push(colorslist[47]);

                            colorslistLeft.push(colorslist[09]);
                            colorslistLeft.push(colorslist[21]);
                            colorslistLeft.push(colorslist[33]);
                            colorslistLeft.push(colorslist[10]);
                            colorslistLeft.push(colorslist[22]);
                            colorslistLeft.push(colorslist[34]);
                            colorslistLeft.push(colorslist[11]);
                            colorslistLeft.push(colorslist[23]);
                            colorslistLeft.push(colorslist[35]);

                            colorslistRight.push(colorslist[17]);
                            colorslistRight.push(colorslist[29]);
                            colorslistRight.push(colorslist[41]);
                            colorslistRight.push(colorslist[16]);
                            colorslistRight.push(colorslist[28]);
                            colorslistRight.push(colorslist[40]);
                            colorslistRight.push(colorslist[15]);
                            colorslistRight.push(colorslist[27]);
                            colorslistRight.push(colorslist[39]);

                            colorslistFront.push(colorslist[12]);
                            colorslistFront.push(colorslist[13]);
                            colorslistFront.push(colorslist[14]);
                            colorslistFront.push(colorslist[24]);
                            colorslistFront.push(colorslist[25]);
                            colorslistFront.push(colorslist[26]);
                            colorslistFront.push(colorslist[36]);
                            colorslistFront.push(colorslist[37]);
                            colorslistFront.push(colorslist[38]);

                            colorslistBack.push(colorslist[20]);
                            colorslistBack.push(colorslist[19]);
                            colorslistBack.push(colorslist[18]);
                            colorslistBack.push(colorslist[32]);
                            colorslistBack.push(colorslist[31]);
                            colorslistBack.push(colorslist[30]);
                            colorslistBack.push(colorslist[44]);
                            colorslistBack.push(colorslist[43]);
                            colorslistBack.push(colorslist[42]);

                            colors = [colorslistTop, colorslistBottom, colorslistLeft, colorslistRight, colorslistFront, colorslistBack];
                            cube.setColor(colors);
                        }
                    </script>

    <div id=status width="300"></div>

</div>

</tr></table>
<div id=back> </div>
<br />
    <input type="text" style="width:400px" id="solinput" />　<input type="button" class="btn svw1" onclick="executeAll()" value="ExecuteAll" />
    <input type="text" style="width:400px;display:none" id="solinput2" />　<input type="button" class="btn svw1" onclick="qrcode()" value="QR code" />
    <div id="output" class="fancybox" style="display:none"></div>

    <script>
        function qrcode() {
            //$("#output").qrcode($("#solinput2").val());
            $("#output").empty();
            $('#output').qrcode({
                render: "canvas", //也可以替换为table
                width: 400,
                height: 400,
                text: $("#solinput2").val()
            });
            $('#output').click();
        }
    </script>
<br /><br />

    <!-- 菜单及分页容器-->
    <div class="stepCont stepCont3" id="div1">
        <!-- 菜单导航显示-->
        <div class='ystep-container ystep-lg ystep-blue' id="div2"></div>
    </div>
    <script>
        //去左空格;
        function ltrim(s) {
            return s.replace(/(^\s*)/g, "");
        }
        //去右空格;
        function rtrim(s) {
            return s.replace(/(\s*$)/g, "");
        }
        //去左右空格;
        function trim(s) {
            return s.replace(/(^\s*)|(\s*$)/g, "");
        }


        function setSetp(cube) {
            var value = $("#solinput").val();
            value = ' ' + value;
            var steps = rtrim(value).split(' ');

            $("#div2").empty();
            $("#div3").remove();
            var step3 = new SetStep({
                content: '.stepCont3',
                clickAble: false
            }, steps, cube);
        }

    </script>

<script>

    "use strict";

    var logwin;
    var stl;
    var color;
    var style;
    // var config;
    var facelets_arr = [];
    var solve_option = 'none';
    var init_done = 0;
    var stoplen = 0;
    var cloze = 0;
    var fnames = [];
    var dist_loaded = [0, 0, 0];
    var skip_mkdp2 = 0;
    var sbtn_bgcolor_active = "#aaaaaa";    // should match btn:active in style2.css
    var sbtn_bgcolor_inactive = "#ffffff";  // should match btn background-color style2.css

    //var CUBE_HOME = "RRRRRRRRRGGGYYYBBBWWWGGGYYYBBBWWWGGGYYYBBBWWWOOOOOOOOO";
    var CUBE_HOME = "YYYYYYYYYGGGOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRWWWWWWWWW"
    var CUBE_BLANK = "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL";

    var dist_gen_depth = 0;
    var dist3_gen_depth = 0;
    var distp2_gen_depth = 0;
    var load_dist_files = 0;

    var params = location.search.substr(1).split('&');
    for (var i = 0; i < params.length; i++) {
        var p = params[i].split('=');
        if (typeof (p[1]) != 'undefined')
            window[p[0]] = p[1];
    }

    if (typeof (use_dist3) != 'undefined')
        if (use_dist3 == 1) {
            USE_DIST3 = 1;
            dist3_gen_depth = 10;
            load_dist_files = 1;
            dist_loaded = [0, 0, 0, 0];
        }

    /*
    Solve options:    
      Generate Arrays:    range default
        dist_gen_depth     8-9     8 
        dist_p2_gen_depth  8-10    8
      Load Files:
        dist_gen_depth     8-10    9
        dist_p2_gen_depth  8-15    8
    */

    if (isNaN(dist_gen_depth))
        dist_gen_depth = ((load_dist_files == 1) ? 9 : 8)
    else {
        if (dist_gen_depth == 0)
            dist_gen_depth = ((load_dist_files == 1) ? 9 : 8)
        else {
            var gen_max = ((load_dist_files == 1) ? 10 : 9);
            if (dist_gen_depth < 8)
                dist_gen_depth = 8;
            else if (dist_gen_depth > gen_max)
                dist_gen_depth = gen_max;
        }
    }

    if (isNaN(distp2_gen_depth))
        distp2_gen_depth = 8;
    else {
        if (distp2_gen_depth == 0)
            distp2_gen_depth = 8;
        else {
            var gen2_max = ((load_dist_files == 1) ? 15 : 10);
            if (distp2_gen_depth < 8)
                distp2_gen_depth = 8;
            else if (distp2_gen_depth > gen2_max)
                distp2_gen_depth = gen2_max;
        }
    }

    if (load_dist_files == 1) {
        init_fnames();
        document.getElementById('btn').innerHTML =
          '<input type=file id=selectFiles style="display:none;" ' +
          'onchange="readfiles(this.files)" multiple>' +
          '<button class="btn svw4" onclick="document.getElementById(\'selectFiles\').click()">Load Dist Files</button>';
    }

    if (typeof (stl) != 'undefined')
        document.getElementById('stl').value = stl;

    if (typeof (facelets) == 'undefined')
        var facelets = CUBE_HOME;
    else {
        cloze = 1;
        if (facelets.length > 54)
            facelets = facelets.substr(0, 54);
        if (facelets.length < 54)
            facelets = (facelets + CUBE_BLANK).substr(0, 54);
        facelets = facelets.toUpperCase();
        var ftmp = facelets.split('');
        for (var i = 0; i < 54; i++) {
            var f = ftmp[i];
            if ('WYORGB'.indexOf(f) == -1)
                ftmp[i] = 'L';
        }
        facelets = ftmp.join('');
    }

    update_layout();
    show_cube(1);

    //if (cloze == 1)
    //  document.getElementById('back').innerHTML = '<a href="JavaScript:window.close()">Close</a>';
    //else 
    //  document.getElementById('back').innerHTML = '<a href="javascript: history.go(-1)">Back</a>';

    // pre-allocate dist arrays so garbage collector will run now (if needed)
    // instead of when the search button is pressed, use a timeout to allow
    // the screen to paint prior to the alloc
    setTimeout(allocate_dist_arrays, 500);

    function update_layout() {
        facelets_arr = facelets.split('');
        for (var i = 0; i < 54; i++) {
            document.getElementById('f' + i).style.backgroundColor = color_str(facelets_arr[i]);
        }
    }

    function select_color(f) {
        color = f.id;
    }

    function set_color(f) {
        if (typeof (color) != 'undefined') {
            facelets_arr[f.id.substr(1)] = color;
            f.style.backgroundColor = color_str(color);
        }
    }

    function show() {
        if (facelets != facelets_arr.join('')) {
            facelets = facelets_arr.join('');
            show_cube(1);
        }
        else {
            if (msgtxt.length > 0)
                clear_status();
        }
        
        setColorForCube();
    }

    function home() {
        facelets = CUBE_HOME;
        if (CUBE_HOME != facelets_arr.join('')) {
            update_layout();
            show_cube(1);
        }
        else {
            if (msgtxt.length > 0)
                clear_status();
        }
        setColorForCube();
        $("#solinput").val("");
        $("#div1").empty();
        $("#div2").empty();
        $("#div3").empty();
    }

    function rand() {
        facelets = randcube();
        update_layout();
        show_cube(1);
        setColorForCube();
    }

    function clear() {
        facelets = CUBE_BLANK;
        if (CUBE_BLANK != facelets_arr.join('')) {
            update_layout();
            show_cube(1);
        }
        else {
            if (msgtxt.length > 0)
                clear_status();
        }
    }

    function help() {
        if (style == 'dark')
            window.open('solver_help.html?style=dark');
        else
            window.open('solver_help.html');
    }

    function solve() {
        sbtn_active();
        setTimeout(solve2, 100);
    }

    function solve2() {
        if (load_dist_files == 1) {
            if (dist_files_loaded == 0) {
                var need = '';
                // var n = 0;
                for (var i = 0, n = 0; i < fnames.length; i++) {
                    if (dist_loaded[i] == 0) {
                        need += fnames[i] + '<br>';
                        n++;
                    }
                }
                var str = (n == 1) ? "this file" : "these files";
                document.getElementById('status').innerHTML = 'Load ' + str + ' before solving:<br>' + need;
                sbtn_inactive();
                return;
            }
        }
        stl = document.getElementById('stl').value + '';
        stl = stl.toLowerCase();
        var stlr = stl.replace(/ /g, '');
        if (stlr.length != stl.length) {
            document.getElementById('stl').value = stlr;
            stl = stlr;
        }
        if (stl == '') {
            stl = '5';
            document.getElementById('stl').value = 5;
        }
        msgtxt.length = 0;
        document.getElementById('status').style.textAlign = 'left';
        if (facelets != facelets_arr.join('')) {
            facelets = facelets_arr.join('');
            show_cube(1);
        }
        var verif = verify_main(facelets);
        if (verif == 0) {
            gtime0 = new Date().getTime();
            logtxt.length = 0;
            show_cube_layout(facelets);
            var v = stl.substr(stl.length - 1);
            if (v == 's' || v == 't') {
                stoplen = (v == 's') ? 20 : 0;
                stl = stl.substr(0, stl.length - 1);
            }
            if (v == 'd') {
                solve_option = v;
                stl = stl.substr(0, stl.length - 1);
                if (dist_gen_depth < 9) {
                    dist_gen_depth = 9;
                    first_time = 1;
                }
            }
            if (first_time) {
                if (init_done == 0) {
                    document.getElementById('status').innerHTML = "Initializing";
                    setTimeout(step1, 100);
                }
                else
                    if (dist_files_loaded == 0) {
                        if (dist_gen_depth == 9) {
                            skip_mkdp2 = 1;
                            document.getElementById('status').innerHTML =
                              'Making Search Arrays<br>Generating to Depth 9';
                        }
                        setTimeout(step2, 100);
                    }
            }
            else {
                document.getElementById('status').innerHTML = "Searching for Solution";
                setTimeout(step4, 100);
            }
        }
        else {
            sbtn_inactive();
            document.getElementById('status').innerHTML = msgtxt.join('');
        }
    }

    function step1() {
        sbtn_active();
        init();
        init_done = 1;
        if (dist_files_loaded == 1)
            step3();
        else {
            var str = (dist_gen_depth == 9) ? '<br>Generating to Depth 9' : '';
            document.getElementById('status').innerHTML = 'Making Search Arrays' + str;
            setTimeout(step2, 100);
        }
    }

    function step2() {
        sbtn_active();
        mkd();
        if (skip_mkdp2 == 0) {
            document.getElementById('status').innerHTML = "Making Search Arrays (P2)";
            setTimeout(step3, 100);
        }
        else
            step3();
    }

    function step3() {
        sbtn_active();
        document.getElementById('sbtn').style.backgroundColor = sbtn_bgcolor_active;
        if (dist_files_loaded == 0 && skip_mkdp2 == 0)
            mkdp2();
        document.getElementById('status').innerHTML = "Searching for Solution";
        setTimeout(step4, 100);
    }

    function step4() {
        solver_main();
        show_solution();
        first_time = 0;
        sbtn_inactive();
    }

    function show_solution() {
        var af = cvt_to_anim(facelets);
        var sol = solution.join('');


        var sols = "";
        for (i = 0 ; i < solution.length; i++) {
            if (solution[i][1] == ' ') {
                sols += solution[i];
            }
            else {
                sols += solution[i] + ' ';
            }
        }

        document.getElementById("solinput").value = sols;
        
        
        setSetp(cube);//设置进度条



        /*document.getElementById('cube').outerHTML =
        "<iframe id=cube width=290 height=290 scrolling=no frameborder=0\
   src=\"cube.html?config=AnimCube.cfg&move=" + sol + "&facelets=" + af + "&edit=0\">\
  </iframe>";*/

        sol = sol.replace(/\s*/g, "");
        sol = sol.replace(/\'/g, "%27");
        document.getElementById("solinput2").value = "http://47.95.217.17/" + "cube.html?config=AnimCube.cfg&move=" + sol + "&facelets=" + af + "&edit=0";






        document.getElementById('status').style.textAlign = 'center';
        if (stoplen == 0)
            document.getElementById('status').innerHTML =
              '<button class="btn svw3" onclick="show_log()">Solve Log</button> </td>'
        else
            document.getElementById('status').innerHTML =
              '<button class="btn svw3" onclick="show_log()">Solve Log</button> </td>' +
              '<table><tr height=10><td></table>' + search_time;
    }

    function show_cube(n) {
        if (n)
            clear_status();
        var af = cvt_to_anim(facelets);
        /*document.getElementById('cube').outerHTML =
        "<iframe id=cube width=290 height=290 scrolling=no frameborder=0\
   src=\"cube.html?config=AnimCube.cfg&facelets=" + af + "&edit=0\">\
  </iframe>";*/
    }

    function clear_status() {
        document.getElementById('status').innerHTML = '';
        msgtxt.length = 0;
        solution.length = 0;
    }

    function cvt_to_anim(c) {
        var ca = new Array(54);

        var to_anim = [
          6, 7, 8, 3, 4, 5, 0, 1, 2, 45, 48, 51, 46, 49, 52, 47, 50, 53, 12, 24,
          36, 13, 25, 37, 14, 26, 38, 18, 30, 42, 19, 31, 43, 20, 32, 44, 11,
          10, 9, 23, 22, 21, 35, 34, 33, 15, 27, 39, 16, 28, 40, 17, 29, 41];

        for (var i = 0; i < 54; i++)
            ca[i] = c[to_anim[i]];

        return (ca.join(''));
    }

    function randcube() {
        var cs = [];

        init_conv();
        copy(untwc, "021", 3, 0);  // for make_cubestr

        for (var i = 0; i < 20; i++) {
            var ep = Math.floor(Math.random() * 479001600);
            var et = Math.floor(Math.random() * 2048);
            var cp = Math.floor(Math.random() * 40320);
            var ct = Math.floor(Math.random() * 2187);

            int_to_perm(cp, cps, 8);
            int_to_perm(ep, eps, 12);
            int_to_strp(ct, cts, 7, 3);
            int_to_strp(et, ets, 11, 2);

            if (parity(eps, 12) == parity(cps, 8))
                break;
        }
        make_cubestr();
        assign_centers_6c();
        colorize(cs);
        return (cs.join(''));
    }

    function colorize(cs) {
        for (var i = 0; i < 54; i++)
            if (cubestr[i] == 0) cs[i] = 'B';
            else if (cubestr[i] == 1) cs[i] = 'Y';
            else if (cubestr[i] == 2) cs[i] = 'R';
            else if (cubestr[i] == 3) cs[i] = 'G';
            else if (cubestr[i] == 4) cs[i] = 'W';
            else if (cubestr[i] == 5) cs[i] = 'O';
    }

    function readfiles_done() {
        document.getElementById('status').innerHTML =
          'All Dist Files Loaded<br>Ready to Solve';
        document.getElementById('btn').innerHTML = '';
    }

    function sbtn_active() {
        document.getElementById('sbtn').style.backgroundColor = sbtn_bgcolor_active;
    }
    function sbtn_inactive() {
        document.getElementById('sbtn').style.backgroundColor = sbtn_bgcolor_inactive;
    }
</script>
</center>
</div>
</body>
</html>
