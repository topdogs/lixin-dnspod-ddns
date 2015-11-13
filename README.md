#说明 
该脚本使用`python`编写，利用`dnspod api`开发的一个ddns。
##字段说明
`public_dic["login_email"]`这个是你在dnspod.cn上的账号

`public_dic["login_password"]`这个是你在dnspod.cn上的密码

`domain`需要操作的域名，例如 baidu.com 、lixin.me 、lixin.info

`record`需要解析的记录,例如 www

`isCron`如果脚本由一个定时触发的任务执行的话，值为`True`，否则脚本将在循环不会停止

#使用方法
##1 不需要提供参数执行脚本
首先打开文件，为`public_dic["login_email"]`、`public_dic["login_password"]`、`domain`、`record`这4个参数填写对应的数据。
以后只需要执行<code>python LixinDDNS.py</code>即可
##2不修改文件带参数执行
需要向脚本提供4个参数，分别是dnsp登陆账号，密码，操作的域名，和操作的记录

<code>
python LixinDDNS.py &lt;email&gt; &lt;password&gt; &lt;domain&gt; &lt;record&gt;
</code>
##3通过读取配置文件执行
其中`option` 作为配置文件的节点保存在文件`ddns.cfg`中,这样就可以同时使用管理多个域名记录。

<code>
python LixinDDNS.py &lt;option&gt;
</code>



----
###联系我
website：[我的网站](http://www.lixin.me  '李鑫的网站')

email: lixin@lixin.me