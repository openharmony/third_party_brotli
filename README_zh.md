# third_party_brotli

#### 介绍
Brotli是基于LZ77算法，霍夫曼编码以及二阶上下文建模的开源数据压缩算法。
OpenHarmony 引入该算法用于curl支持处理使用brotli算法压缩的http请求。

#### 软件架构
'''
LICENSE    #版权声明
v.1.0.9.tar.gz    #源码压缩包
install.sh    #解压缩以及打补丁脚本
patch    #补丁
BUILD.gn    #编译程序
'''


#### 安装教程

1.  在使用该库的编译程序中加入依赖
'''
deps = ["//third_party/brotli:brotli"]
'''
2.  预处理
'''
./build/prebuilts_download.sh
'''
3.  编译
'''
./build.sh --product-name rk3568 --ccache
'''
编译生成物对应路径： 'out/rk3568/thirdparty/brotli/libbrotli.z.so'

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


