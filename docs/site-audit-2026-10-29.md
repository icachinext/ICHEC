# 工程检查记录 · 2026-10-29

## 检查范围与结果

- 全站 Jekyll 构建，重点复核 `13/`–`19/` 的 HTML、样式、脚本、图片引用与菜单。
- 首次生成站点检查发现 298 处引用错误（272 处文件引用、26 处锚点引用）；这些是引用次数，同一资源可能被多个页面引用。
- 修复后对 126 个生成 HTML 页面及全站 CSS 执行本地链接检查：0 个缺失文件或锚点。
- `bundle exec jekyll build --strict_front_matter` 成功。验证使用已有 `ichec-jekyll` 容器，Ruby 3.4.11、Bundler 2.6.9；没有修改工程的 Ruby 版本锁定。
- Node.js 对 245 个 JavaScript 文件及生成页面的内联脚本执行语法解析：0 个语法错误。这不代表浏览器运行时交互验证。
- 核查 2023–2027 年生成页面的 248 个去重外部地址：先检查 HEAD，再用 GET 复核 404、405 和连接失败。9 个持续 404 的个人主页替换为官方新地址，均以 GET 确认 200。
- 浏览器自动化被当前 Work 设置禁用，本轮未完成截图及浏览器交互验收。外部站点的 403、412、999、超时不等于链接不存在；没有凭这些结果删除内容。

## 已处理的问题

| 范围 | 处理 |
| --- | --- |
| 2013 | 补充明确标注为恢复样式的 `archive.css`，修复顶部导航布局；图标复用已有会议标识；删除未保存的空主题钩子和过期倒计时依赖，显示历史会议日期。 |
| 2014–2015 | 删除未保存的冗余主题 CSS/JS 引用；2015 图标使用现存主题标识。实际内容样式仍使用各年的 `custom.css`。2015 存档中的 `site.js` 响应为空。 |
| 2014 相册 | 保留 53 张照片的原始存档入口及三页翻页导航；缺失原图和缩略图改为说明和文字链接，不用其他照片冒充。 |
| 2016 | 本地文件及锚点引用未发现缺失；原有 CDN 依赖保留。 |
| 2017 | 日程图缺件改为说明及原页存档入口；注册和找回密码表单加入停用说明，使用禁用的 fieldset 防止提交至不存在的静态后台。 |
| 2018 | 两张分会场日程图缺件改为说明及原页存档入口；保留已有日程总览及论坛资料。2017–2018 所用 Bootstrap CDN CSS/JS 已确认 200。 |
| 2019 | 从 Drupal 官方主题发行包补回 2 个菜单脚本、1 个 HTML5 兼容脚本和 10 张标准装饰图片；补全 Paper、Art、返回顶部锚点；移除访问不存在元素的倒计时示例，显示历史会议日期；修复未闭合的 style 引号；日程及二维码缺件改为明确说明。 |
| 2020 | 清除归档工具栏 CSS 对缺失截图图标的依赖。 |
| 2021–2022 | 移除模板残留 Help/Contacts 死链；2021 附属论坛指向同页真实论坛条目；未保存的视频改为缺件说明。 |
| 2023–2025 | 修复缺少协议头的个人站点和签证外链、错误的 IWHEC 路径，以及 9 个失效个人主页。历史任职和会议正文未因个人主页迁移而改写。 |
| 工具 | 新增 `scripts/check_site.py` 与构建说明，`scripts/`、`docs/` 排除出发布站点。 |

## 仍需要原始资料的归档内容

以下项目没有可确认的完整原件。本轮没有编造日程、照片、付款二维码或历史正文。

1. **2013 原始自定义主题及未本地收录的正文页**：存档索引仅找到根首页、`page/welcome` 和 `page/conference-program` 的早期正文记录。注册、投稿、组委会、赞助、旅游、联系、设计比赛、问卷及部分报告等仍保留原有 Wayback 入口，不能保证这些外部入口有完整存档。恢复样式不是原始主题的逐像素复原。
2. **2014 相册 53 张原图及其缩略图**：精确核查 `chchi2014_(1).JPG` 的存档记录为 404；较大范围的相册索引查询超时，因此不能断言所有照片在任何来源都不存在。文字入口仍可能返回缺件页。
3. **2017 日程图 `pro_0.png`**，**2018 分会场图 `Day1.png`、`Day2.png`**：查到的存档记录虽标为 200，实际类型为 HTML，不是图片，未作为原图引入。
4. **2019 `Program0625.jpg`、`QRcode.png`**：本轮查到的该站存档资源索引未包含这两个文件。
5. **2021 开幕及闭幕录像**：`assets/video/Opening.mp4`、`Closing speech.mp4` 不在工程中。

部分人物头像、2013 标识及 2014 横幅在先前提交中已使用替代素材；本轮没有把它们重新标记为原件。来源可查提交 `1ea19d2`。

## 标准主题资源来源

新增的 2019 标准图片及脚本来自 [Drupal 官方 business 7.x-1.11 发行包](https://ftp.drupal.org/files/projects/business-7.x-1.11.tar.gz)。保留发行包中的 `LICENSE.txt`，脚本保留作者及许可声明。没有覆盖原站的自定义图片和现有脚本。

## 已更新的个人主页

以下新地址均由相应学校官方页面确认姓名，并在本轮 GET 检查返回 200。

| 人物 | 新地址 |
| --- | --- |
| 付心仪 | [清华大学未来实验室](https://thfl.tsinghua.edu.cn/yjdw/jzg/zxjg/rjwrhjqqyts/yjy/fxy.htm) |
| 彭宇 | [清华大学未来实验室](https://thfl.tsinghua.edu.cn/yjdw/xy_bys/zxjg/rjwrhjqqyts/py.htm) |
| 冯元凌 | [清华大学未来实验室](https://thfl.tsinghua.edu.cn/yjdw/xy_bys/zxjg/rjwrhjqqyts/fyl.htm) |
| 张为威 | [清华大学未来实验室](https://thfl.tsinghua.edu.cn/yjdw/xy_bys/zxjg/llyhtyjfwxtsj/zww.htm) |
| 洪昀 | [清华大学未来实验室](https://thfl.tsinghua.edu.cn/yjdw/xy_bys/zxjg/qt/hy.htm) |
| 佟馨 | [昆山杜克大学保存的个人简历](https://newstatic.dukekunshan.edu.cn/globalhealth/2022/05/07145949/CV_XinTong_meta_Mar22.pdf) |
| 张嘉欣 | [南方科技大学](https://sustech.edu.cn/en/faculties/zhangjiaxin.html) |
| 何思倩 | [北京科技大学](https://me.ustb.edu.cn/szdw/xsjs/gysjx1/7e286933f61f41cf97695c1f2883ee30.htm) |
| 王建民 | [同济大学](https://tjdi.tongji.edu.cn/TeacherDetail.do?id=4237) |

本轮持续无法建立连接的近年外链：`anpengcheng.cn`、`molina.imigrasi.go.id`、`taoye.me`（含 `/CV`）、`mirnazordan.com`、`xintong.ca`。保留原址，不把连接失败当作更换人物或改写历史签证说明的依据。EasyChair 与飞书表单的部分 HEAD 响应为 404，但实际 GET 可访问，未改写其入口或保存临时登录令牌。
