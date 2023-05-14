# ShunTong-2023
# streamlit主页搭建
参考 https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app  

在项目下新建pages文件夹，在里面新建文件，文件名称即是小标签页名称  

本项目中给出了一般新页面的模板，包含音频，视频，图片引入方式，包含链接导入方式，其余页面描述可以用markdown完成。  

模板地址：ShunTong-2023 streamlitMainPage/pages/template.py  

要新加入页面，就在pages文件夹下面继续新建py文件并仿照模板进行即可  

#
# streamlit 云服务器部署
可以参考 powerpoint 里面 streamlit 云服务器部署部分进行。 

首先购买相应云服务器，然后进行云服务器root密码修改等操作，随后使用远程终端连接云服务器，依据项目所需的环境进行部署，部署完成后可以使用后台启动命令来启动项目。部署完成后的项目可以通过云服务器的公网ip+端口进行访问。 

这里部署完成的网站是：  
47.120.40.60:8501  

或者采用streamlit cloud的方式进行部署，即部署完成链接形式是：  
https://presiton-streamlitmainpage-main-page-pffie7.streamlit.app/  
  

#
# streamlit 本地服务器做云服务器部署
本地服务器做云服务器部署主要是为了处理需要使用到gpu的情况，直接租用带gpu的云服务器价格高昂。 

首先保证项目在本地跑起来，随后要做的就是内网穿透，这里使用了一个叫做cpolar的内网穿透进行，可以免费使用也可以付费使用，免费使用的域名会每24小时更换一次，付费试用则可以固定二级域名。  

本地测试使用了windows + ubuntu 20.04 双系统的台式机，部署在ubuntu 20.04下完成，教程使用根据下面参考视频部署即可完成。

参考教程网站：
https://www.bilibili.com/video/BV1dg4y1373q/?spm_id_from=333.337.search-card.all.click

文章参考教程：
https://www.bilibili.com/read/cv22820592?spm_id_from=333.999.0.0

#
# streamlit-webrtc-example-main 修正
修正requirements.txt里面不正确的依赖  
安装requirements.txt时，注意使用conda 新创建一个 虚拟环境 env，并切换到env环境下进行操作，尤其是同一服务器想部署多个项目一定要这样做，否则依赖冲突。    
安装依赖时，可以直接将报错google，依赖版本替换完成后，注意最新问题是验证当前这个库的依赖还是解决下一个依赖，不要反复去修改同一个依赖。  
