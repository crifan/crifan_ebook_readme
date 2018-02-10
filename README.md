# Crifan的电子书的使用说明

## 为何要有：Crifan的电子书

我之前折腾过很多方面的内容，包括技术类的，非技术类的。

关于技术类中又分很多种，其中都放到了我的网站 crifan.com 上，目前已有7000+的技术帖子，但多数都是零散的某个细节的知识点。

当我在某个技术领域有了一定的心得和经验后，就会抽空整理成相对成系统的内容，用(`Docbook`、`Gitbook`等)工具去变成电子书，方便别人参考。

## 为何要有：Crifan的电子书的使用说明

对于这些电子书，之前虽然已经分类列出来了，但是缺少了基本的介绍，所以对于很多人来说，不方便快速找到自己所需要看哪些。

现在加上必要的简介，重新整理如下：

目前所写电子书：

* 内容上：主要分两类
  * 一方面是计算机方面的相关的，技术相关的
  * 另一方面属于非技术，比如生活类的，学习类的
* 制作工具上：也分两类
  * 一类是用`Docbook`制作的
    * 主入口在：http://www.crifan.com/files/doc/docbook/
  * 另一类是用`Gitbook`制作的
    * 弄了2份一样的，分别放在了
      * 自己的 crifan.com 的网站上
        * 入口都在：http://book.crifan.com/books/
      * 和 https://crifan.github.io 上
        * 对应源码是：https://github.com/crifan/crifan.github.io

下面就来详细介绍一下，都有哪些方面的电子书，以及大概的内容分类如何，便于每人找到自己想要的内容：

## 技术类

计算机的技术，从大的概念上，可以大致分为：

* **上层：纯软件**
  * 涉及到在PC（Windows/Mac/Linux）上，用各种编辑器/IDE，去编写各种代码，实现各种工具/软件/脚本等内容
  * 包括PC桌面端软件，Web领域网页开发，移动端APP开发等等
* **中间：**（软硬件结合的）**嵌入式**
  * 涉及到在某某开发板上，写嵌入式代码，驱动硬件工作
  * 包括给别人的芯片或开发板，去写某BSP，某个模块（蓝牙，USB，FM，Nand Flash等）的驱动
* **底层：纯硬件**
  * 涉及PCB Layout，设计和生产开发版
  * 涉及到各种芯片的涉及，包括CPU，内存，显示屏等，涉及到流水线，代工厂等等内容

此处目前折腾的领域主要是：

**中间的嵌入式** 和 **上层的纯软件**

### 技术类通用知识

不论哪方面的技术，都有一些通用的学习方面，逻辑概念，总结如下：

* 关于如何利用工具和脚本提供工作效率的：
  * [如何提高工作效率](https://crifan.github.io/improve_work_efficiency/website)
* 关于要有良好的编程习惯和逻辑，才能写出高质量代码：
  * [编程习惯和代码风格](https://crifan.github.io/program_code_style/website)
  * [计算机语言编程规范](http://crifan.com/files/doc/docbook/lan_coding_rule/release/html/lan_coding_rule.html)
* 对于不同领域的技术，都有一些通用的概念需要了解，才能更好的开发：
  * [计算机编程通用逻辑知识概念](https://crifan.github.io/program_common_logic/website)
* 以及都有一些通知的基础知识：
  * [软件开发基础知识](http://www.crifan.com/files/doc/docbook/soft_dev_basic/release/html/soft_dev_basic.html)
  * [软件技术开发通用知识](http://crifan.com/files/doc/docbook/soft_tech_common/release/html/soft_tech_common.html)
* 想要能用google搜索技术资料，可以使用shadowsocks：
  * [科学上网相关知识总结](https://crifan.github.io/scientific_network_summary/website)

### 推荐的工具或软件

折腾技术或非技术期间，会用到很多软件和工具，此处把觉得不错的，整理出来，推荐之：

* [【crifan推荐】轻量级文本编辑器，Notepad最佳替代品：Notepad++](http://www.crifan.com/files/doc/docbook/rec_soft_npp/release/html/rec_soft_npp.html)
* [【crifan推荐】支持多种协议的串口开发工具：SecureCRT](http://crifan.com/files/doc/docbook/rec_soft_securecrt/release/html/rec_soft_securecrt.html)

### 硬件类

折腾嵌入式期间，其实也想去了解硬件方面的知识，只不过没有深入。

只整理了点和硬件相关的皮毛：

* [硬件电路基础知识](http://www.crifan.com/files/doc/docbook/hardware_basic/release/html/hardware_basic.html)

### 嵌入式软件

下面是之前折腾的嵌入式开发相关的内容：

#### 嵌入式通用知识

嵌入式领域内有些通用的，基本知识：

关于CPU方面的：

* [ARM与MIPS的详细对比](http://www.crifan.com/files/doc/docbook/arm_vs_mips/release/html/arm_vs_mips.html)

和技术和概念相关的，比如：

* [【详解】中断相关的知识](http://www.crifan.com/files/doc/docbook/interrupt_related/release/html/interrupt_related.html)

#### 开发环境+交叉编译器

在折腾嵌入式相关开发前，往往要先去搭建开发环境，其中就要先去搞懂：交叉编译

先去搞清楚什么是交叉编译：

* [交叉编译详解](http://www.crifan.com/files/doc/docbook/cross_compile/release/html/cross_compile.html)

然后再去了解相关的GNU方面的工具：

* [GNU Binutils详解](http://www.crifan.com/files/doc/docbook/binutils_intro/release/html/binutils_intro.html)

然后再去用具体的某个工具，去搭建交叉编译环境（和相关的工具链、rootfs等内容）：

* [Buildroot详解](http://crifan.com/files/doc/docbook/buildroot_intro/release/html/buildroot_intro.html)
* [crosstool-ng详解](http://www.crifan.com/files/doc/docbook/crosstool_ng/release/html/crosstool_ng.html)

关于开发环境的：

在Windows上折腾Linux方面的开发，用Cygiwn：

* [Cygwin详解](http://www.crifan.com/files/doc/docbook/cygwin_intro/release/html/cygwin_intro.html)

#### 嵌入式Linux+嵌入式Linux驱动

如果对于嵌入式软件的整体概念不了解，可以去看：

* [嵌入式软件开发](https://www.crifan.com/files/doc/docbook/embedded_soft_dev/release/html/embedded_soft_dev.html)

如果想要了解嵌入式软件中关于驱动开发的事情，可以去看：

* [嵌入式驱动开发](http://www.crifan.com/files/doc/docbook/embedded_drv_dev/release/html/embedded_drv_dev.html)

而关于嵌入式Linux方面的软件和软件中的驱动，可以去看：

* [嵌入式Linux软件开发](http://www.crifan.com/files/doc/docbook/embedded_linux_dev/release/html/embedded_linux_dev.html)
* [嵌入式Linux驱动开发](http://www.crifan.com/files/doc/docbook/embedded_linux_drv_dev/release/html/embedded_linux_drv_dev.html)

关于嵌入式Linux开发期间的，有：

* [【详解】嵌入式开发中固件的烧录方式](http://www.crifan.com/files/doc/docbook/firmware_download/release/html/firmware_download.html)
* [在Linux运行期间升级Linux系统（Uboot+kernel+Rootfs）](http://www.crifan.com/files/doc/docbook/runtime_upgrade_linux/release/html/runtime_upgrade_linux.html)

而关于典型的Uboot+Kernel+Rootfs的嵌入式Linux中的Uboot：

其中的最开始的启动代码相关的Start.S的汇编代码，实现了启动硬件的功能。

而关于启动的逻辑的具体分析：

* [Uboot中start.S源码的指令级的详尽解析](http://www.crifan.com/files/doc/docbook/uboot_starts_analysis/release/html/uboot_starts_analysis.html)

而关于具体的某个模块/功能方面的驱动有：

关于DMA的驱动：

* [详解ARM的AMBA设备中的DMA设备PL08X的Linux驱动](http://www.crifan.com/files/doc/docbook/dma_pl08x_analysis/release/html/dma_pl08x_analysis.html)

关于无线网卡的驱动：

* [如何在Linux下写无线网卡的驱动](http://www.crifan.com/files/doc/docbook/linux_wireless/release/html/linux_wireless.html)

关于Nand Flash方面的驱动和介绍：

* [【详解】如何编写Linux下Nand Flash驱动](http://www.crifan.com/files/doc/docbook/linux_nand_driver/release/html/linux_nand_driver.html)

而其中Linux中关于Nand Flash的是MTD层，MTD中关于如何识别Nand Flash和启动过程的解析是：

* [Linux MTD下获取Nand flash各个参数的过程的详细解析](http://www.crifan.com/files/doc/docbook/nand_get_type/release/html/nand_get_type.html)

而关于USB方面的协议介绍和相关驱动开发总结是：

* [USB基础知识概论](http://www.crifan.com/files/doc/docbook/usb_basic/release/html/usb_basic.html)
* [如何实现Linux下的U盘（USB Mass Storage）驱动](http://www.crifan.com/files/doc/docbook/usb_disk_driver/release/html/usb_disk_driver.html)
* [USB HID Learning Record](http://www.crifan.com/files/doc/docbook/usb_hid/release/html/usb_hid.html)

#### 具体模块或领域

##### 大的方向=嵌入式的不同应用领域

* [现场总线Fieldbus简析](http://www.crifan.com/files/doc/docbook/fieldbus_intro/release/html/fieldbus_intro.html)

条形码Symbology相关的，各种不同类型的条形码的总结：

* [Code 128 Symbology Introduction](http://www.crifan.com/files/doc/docbook/symbology_code128/release/html/symbology_code128.html)
* [GS1-128条形码和相关的AI及FNC1的详解](http://www.crifan.com/files/doc/docbook/symbology_gs1128/release/html/symbology_gs1128.html)
* [Plessey & MSI Symbology Introduction](http://www.crifan.com/files/doc/docbook/symbology_plessey/release/html/symbology_plessey.html)
* [UPC/UPC-A/UPC-E & EAN Barcode Symbology](http://www.crifan.com/files/doc/docbook/symbology_upc/release/html/symbology_upc.html)

##### 小方面来说=关于具体的模块/硬件/协议方面

关于蓝牙的：

* [蓝牙协议详解](http://crifan.com/files/doc/docbook/bluetooth_intro/release/html/bluetooth_intro.html)

关于串口/RS232的：

* [RS232串口协议详解](http://crifan.com/files/doc/docbook/rs232_serial_intro/release/html/rs232_serial_intro.html)

关于音频领域的：

关于MPEG和MP3的知识：

* [MPEG简介 + 如何计算CBR和VBR的MP3的播放时间](http://www.crifan.com/files/doc/docbook/mpeg_vbr/release/html/mpeg_vbr.html)

### 上层软件

对于上层纯软件方面，也有一些总结：

#### 上层软件的通用知识

关于后台开发和设计接口，移动端调用后台接口，测试人员测试接口和网页等相关的：

和HTTP方面的知识：

* [HTTP知识总结](https://crifan.github.io/http_summary/website)

以及后台人员设计RESTFul的API接口需要了解的：

* [HTTP后台端：RESTful API接口设计](https://crifan.github.io/http_restful_api/website)

以及后台人员开发调试接口时，移动端调用接口时，测试人员测试接口时，可以用到的Postman工具：

* [API开发利器：Postman](https://crifan.github.io/api_tool_postman/website)

各种计算机语言通用的的方面的知识总结：

* [计算机编程语言基础知识](http://www.crifan.com/files/doc/docbook/programming_language_basic/release/html/programming_language_basic.html)
* [各种计算机语言简介和总结](http://www.crifan.com/files/doc/docbook/language_summary/release/html/language_summary.html)

在涉及到前台和后台数据交互，往往都是用JSON：

* [JSON详解](http://www.crifan.com/files/doc/docbook/json_tutorial/release/html/json_tutorial.html)

不同的语言和工具中，都支持用正则表达式去实现复杂的规则去提取想要的数据：

* [正则表达式学习心得](http://www.crifan.com/files/doc/docbook/regular_expression/release/html/regular_expression.html)

而用不同的编辑器或IDE，以及处理文件相关的内容时，往往会涉及到文件的字符编码，可参考：

* [字符编码详解](http://www.crifan.com/files/doc/docbook/char_encoding/release/html/char_encoding.html)

而上面的教程内容太多太杂，如果只是想要简单的使用编码方面的知识，可以直接去看：

* [字符编码应用](http://www.crifan.com/files/doc/docbook/char_encoding_usage/release/html/char_encoding_usage.html)

#### PC桌面端软件

在写Windows平台的桌面端软件时，可以使用C#：

* [C#学习心得](http://www.crifan.com/files/doc/docbook/csharp_summary/release/html/csharp_summary.html)

#### 网页Web领域开发

在涉及到Web网页自动化测试，写爬虫等，会涉及到Selenium：

* [Selenium知识总结](https://crifan.github.io/selenium_summary/website)

而在Web和上层领域内，对于html类的内容提取常会涉及到Xpath：

* [XPath知识总结](https://crifan.github.io/xpath_summary/website)

关于如何搭建网站，以及如何给网站搬家的话，可以参考：

* [建设网站详细教程](http://www.crifan.com/files/doc/docbook/build_website/release/html/build_website.html)
* [网站搬家详解](http://www.crifan.com/files/doc/docbook/website_transfer/release/html/website_transfer.html)

#### 移动端APP开发

在涉及到移动端开发时，可以参考：

* [移动端APP开发总结](https://crifan.github.io/mobiel_app_summary/website)

#### 上层软件的其他领域

比如想要开发自己特定领域内的语言的解析器，即实现自己的编译器，可以使用ANTLR：

* [ANTLR教程](http://www.crifan.com/files/doc/docbook/antlr_tutorial/release/html/antlr_tutorial.html)

想要和我一样，制作出复杂的电子书，可以用相关的工具，比如：

* [Docbook开发手记](http://www.crifan.com/files/doc/docbook/docbook_dev_note/release/html/docbook_dev_note.html)

折腾网络爬虫（和模拟登录）领域的话，可以参考：

* 去了解整个的逻辑和相关的技术：
  * [详解抓取网站，模拟登陆，抓取动态网页的原理和实现（Python，C#等）](http://www.crifan.com/files/doc/docbook/web_scrape_emulate_login/release/html/web_scrape_emulate_login.html)
* 用Python去实现爬虫：
  * [Python专题教程：抓取网站，模拟登陆，抓取动态网页](http://www.crifan.com/files/doc/docbook/python_topic_web_scrape/release/html/python_topic_web_scrape.html)

#### Python语言

折腾折腾Pyton期间，单独整理了一系列的内容，供参考：

用于入门级的介绍的：

* [python初级教程：入门详解](http://www.crifan.com/files/doc/docbook/python_beginner_tutorial/release/html/python_beginner_tutorial.html)

关于整体的Python的心得和总结：

* [python中级教程：开发总结](http://www.crifan.com/files/doc/docbook/python_intermediate_tutorial/release/html/python_intermediate_tutorial.html)
* [Python语言总结](http://www.crifan.com/files/doc/docbook/python_summary/release/html/python_summary.html)

关于某个特定的模块的总结：
* [Python专题教程：BeautifulSoup详解](http://www.crifan.com/files/doc/docbook/python_topic_beautifulsoup/release/html/python_topic_beautifulsoup.html)
* [Python专题教程：正则表达式re模块详解](http://www.crifan.com/files/doc/docbook/python_topic_re/release/html/python_topic_re.html)
* [Python专题教程：字符串和字符编码](http://www.crifan.com/files/doc/docbook/python_topic_str_encoding/release/html/python_topic_str_encoding.html)

#### 我个人=自己=Crifan相关的内容

在折腾技术方面，整理出一些，相对通用的库，整理出来，供参考：

目前最新的代码，都放到 [crifan的Github](https://github.com/crifan)上了：

其中关于自己的库函数，各种语言都有：

https://github.com/crifan/crifanLib

其中关于C#和Python，分别写了专门的电子书解释如何使用：

* [详解crifan的C#库：crifanLib.cs](http://www.crifan.com/files/doc/docbook/crifanlib_csharp/release/html/crifanlib_csharp.html)
* [详解crifan的Python库：crifanLib.py](http://www.crifan.com/files/doc/docbook/crifanlib_python/release/html/crifanlib_python.html)

## 非技术类

### 电脑计算机使用类

和电脑/计算机使用方面的知识，比如有哪些常见的操作系统，以及如何安装软件和驱动等知识的：

* [电脑基础知识教程](http://www.crifan.com/files/doc/docbook/compute_basic/release/html/compute_basic.html)

以及觉得很多好用的工具和软件，也进行了推荐：

* [crifan推荐软件](http://www.crifan.com/files/doc/docbook/crifan_rec_soft/release/html/crifan_rec_soft.html)

和技术开发有点关系，但是更主要是属于电脑使用方面的，虚拟机：

在Windows/Mac中，按照Mac或Windows的系统，而用到的工具，比如VMWare或VirtualBox：

* [虚拟机教程](http://www.crifan.com/files/doc/docbook/virutal_machine_tutorial/release/html/virutal_machine_tutorial.html)
* [VirtualBox教程](http://www.crifan.com/files/doc/docbook/virtualbox_tutorial/release/html/virtualbox_tutorial.html)
* [VMWare教程](http://www.crifan.com/files/doc/docbook/vmware_tutorial/release/html/vmware_tutorial.html)

### 工作类

而开始了工作后，需要了解的各种基本概念和常识，包括招聘和应聘，薪资待遇，股票和期权，创业和公司等：

* [工作和职业相关知识](https://crifan.github.io/work_job_summary/website)

而和别人合作时，往往涉及到文件共享，资料共享，协同编辑等内容，可以使用有道云协作：

* [有道云笔记和云协作使用总结](https://crifan.github.io/youdao_note_summary/website)

而工作后，会遇到具体的某个商业领域相关的知识，比如：

和汽车销售行业，售前和售后，整车厂和经销商，经销商和客户等相关内容：

* [汽车销售领域知识总结](https://crifan.github.io/automobile_sales_summary/website)

## 生活类

和买房前后需要注意哪些事项，具体买房的过程的内容：

* [买房详细教程](http://www.crifan.com/files/doc/docbook/buy_house/release/html/buy_house.html)
