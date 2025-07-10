# SpiderAVPro

## 项目介绍
蜘蛛AV - 只有老司机才懂的资源聚合网站，专为资深用户设计的高效资源管理系统。

**核心优势：**
- 完全免费无限制使用
- 无任何隐形消费
- 纯净无广告体验
- 本地数据安全存储

## 支持线路
| 线路名称 | 状态 | 特点 |
|----------|------|------|
| com_piwivbd_h5frz1   | ✅    | 高速稳定 |

> 注：线路信息会不定期更新，具体以实际使用为准。

## 功能特点
- 资源自动收集与整理
- 本地收藏管理系统
- 简洁高效的用户界面
- 数据加密与安全存储

## 下载地址
```bash
git clone https://github.com/YyCloud2024/SpiderAVPro.git
cd SpiderAVPro
```

## 部署流程
### 方法一：使用uv（推荐）
1. 安装uv包管理器
   ```bash
   # Windows系统
   powershell -ExecutionPolicy Bypass -c "irm https://github.com/astral-sh/uv/releases/download/0.7.12/uv-installer.ps1 | iex"
   ```
2. 安装依赖
   ```bash
   uv install
   ```
3. 启动应用
   ```bash
   uv run manage.py runserver
   ```

### 方法二：使用requirements.txt
1. 创建虚拟环境
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
2. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```
3. 启动应用
   ```bash
   python manage.py runserver
   ```

## 联系方式(如果需要定制开发可联系我)
- 微信号：duyanbz

## 常见问题解决
### 线路无法打开
如果遇到线路无法打开的情况，请按照以下步骤操作：
1. 打开 `SpiderAvPro/settings.py` 文件
2. 将 `DEBUG = True` 修改为 `DEBUG = False`
3. 运行项目让系统更新数据
4. 更新完成后，开发环境可改回 `DEBUG = True` 以获得更快的运行速度和正确的静态资源加载
5. 线上环境请保持 `DEBUG = False`
6. 爬虫文件使用
   项目根目录下的 `firing range.zip` 包含爬虫相关文件，用于问题复现和解决：
   -  解压 `firing range.zip` 获取爬虫源代码
   -  当线上环境遇到问题时，可使用这些爬虫文件自定义复现问题
   -  修复问题后，将最新代码更新到 `av_spider` 目录下对应的线路代码中
7. 模块缺失
如果遇到提示找不到名为 `BloodSpiderModel` 的模块：
   - 解压项目根目录下的 `firing range.zip` 文件
   - 从解压后的文件中获取所需模块
   - 将模块放置在项目的对应venv环境下
8. 其他问题
如果遇到其他问题，请联系我获取支持

## 注意事项
- 本项目仅供学习交流使用
- 本项目没有限制范围
- 本项目不承担任何法律责任,因使用本项目而导致的任何损失,本项目概不负责
- 本项目提供任何技术支持,如遇问题请联系我