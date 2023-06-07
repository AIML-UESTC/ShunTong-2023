# app/Dockerfile
#此处设置使用的python版本
FROM python:3.8
#此处设置在docker容器里面运行的项目文件夹
WORKDIR /app
#此处为ubuntu依赖安装,如果需要安装系统依赖,则添加到此处,并添加-y参数表明确认安装
RUN apt-get update && apt-get install -y && apt-get install libgl1 -y
#此Dockerfile是将本地目录里面所有文件复制到docker镜像里面对应位置,是本地项目的部署
COPY . .
#此处是安装要打包成docker镜像的python项目需要用到的所有依赖,导出requirements.txt在上面给了教程
RUN pip3 install -r requirements.txt
#暴露对外访问端口
EXPOSE 8503
#curl健康检查,可有可无
#HEALTHCHECK CMD curl --fail http://localhost:8503/_stcore/health
#设置入口和运行streamlit命令,当启动docker容器运行镜像时,会自动执行该命令
#该命令等效为 streamlit run main.py --server.port=8503, --server.address=0.0.0.0
#在编写Dockerfile时,streamlit的访问端口与上面EXPOSE的端口一致即可,以及部署的docker及每个同学分配的端口我会给出
ENTRYPOINT ["streamlit", "run", "main_page.py", "--server.port=8503", "--server.address=0.0.0.0"]
