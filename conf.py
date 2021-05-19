# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Blog/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
    # "name": "Prism",
    # "type": "git",
    # "url": "https://github.com/Reedo0910/Maverick-Theme-Prism.git",
    # "branch": "deploy"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "LSQsjtu/Blog@gh-pages"
}

# 站点设置
site_name = "我的个人博客"
site_logo = "${static_prefix}f-logo.png"
site_build_date = "2021-05-04T22:46+08:00"
author = "LSQ"
email = "1959376918@qq.com"
author_homepage = "https://lsqsjtu.github.io/Blog/"
description = "记录生活美好"
key_words = ['Maverick', 'LSQ', 'Galileo', 'blog']
language = 'zh-CN'
locale = 'Asia/Shanghai'
# background_img = "${static_prefix}logo.jpg"
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/lsq15",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/LSQsjtu",
        "icon": "gi gi-github"
    },
    # {
    #     "name": "Weibo",
    #     "url": "https://weibo.com/5245109677/",
    #     "icon": "gi gi-weibo"
    # }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="shortcut icon" href="${static_prefix}Arley.png">
<script type='text/javascript' src="https://cdn.jsdelivr.net/gh/LSQsjtu/Blog@gh-pages/assets/jquery-3.4.1.min.js"></script>
<!-- szgotop -->
<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/gh/LSQsjtu/Blog/gotop/css/szgotop.css" />
<!-- FancyBox -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/LSQsjtu/Blog@gh-pages/assets/jquery.fancybox.min.css" />
<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/LSQsjtu/Blog@gh-pages/assets/jquery.fancybox.min.js"></script>
<script>
$(function() {
   $(".yue figure img").each(function(i) {
      if (!this.parentNode.href) {
         $(this).wrap("<a href='" + this.src + "' data-fancybox='images' data-caption='" + this.alt + "'></a>")
      }
   })
});
</script>
<script type="text/javascript">
$( '[data-fancybox]' ).fancybox({
	protect:true,
	caption : function( instance, item ) {
	return $(this).find('figcaption').html();
	}
});
</script>
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?d69b9b23082b2143a5bce14c4c459baa";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>
'''

footer_addon = ''

body_addon = r'''
<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/LSQsjtu/Blog/gotop/js/szgotop.js"></script>
<div class="back-to-top cd-top faa-float animated cd-is-visible" style="top: -999px;"></div>
'''

