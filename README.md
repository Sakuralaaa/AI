# AI Agent 上路指南

[English](README.en.md) · 中文为本仓库的权威版本

> 把 Agent 想象成一辆车：Codex、Claude Code、PI-Desktop 是不同的车，模型是驱动车辆的油。好油能让车跑得更快、更稳；普通油也能完成整理文件、改格式之类的轻任务。Prompt 是目的地，MCP 是车载扩展接口，而你始终是负责选择路线和验收结果的人。

这是一份面向普通用户、研究生和知识工作者的 AI Agent 实用经验库。你不必先学会编程，也不必把所有工具装一遍。首页先把完整主线讲清楚；需要逐步截图级操作、配置细节或排错时，再进入对应文档。

## 先给结论：最稳的起步组合

```text
Codex Desktop                         ← 先装好一辆车
  └─ OpenAI 登录或你有权使用的 API     ← 先接一条能独立验证的油路
      └─ CC-Switch（可选）              ← 有多个供应商时再加切换面板
          └─ CLIProxyAPI（可选）         ← 确实需要协议兼容或本地网关时再加
              └─ MCP / Skills（进阶）    ← 主线稳定后再安装车载扩展
```

第一次使用时，只安装 **Codex Desktop**，保留沙箱和审批，用官方登录或一条可信 API 完成一个小任务。CC-Switch、CLIProxyAPI（下文简称 CPA）、MCP 和多 Agent 都不是起步必需品。

## 先认清车、油和油路

| 比喻 | 准确术语 | 它负责什么 | 常见选择 |
|---|---|---|---|
| 车 | Agent 客户端/框架 | 组织上下文、调用工具、执行任务、展示差异 | Codex、Claude Code、PI-Desktop |
| 油 | 模型 | 理解指令、推理、生成文字或代码 | 不同能力、价格和上下文长度的模型 |
| 加油站 | 模型供应商 | 提供模型访问、认证、额度和计费 | 官方登录、官方 API、合规第三方供应商 |
| 油路切换面板 | CC-Switch | 保存并切换客户端的供应商与相关配置 | 一个客户端连接多个合法来源时使用 |
| 本地中转站 | CLIProxyAPI | 把其支持的上游整理为兼容 API | 有协议适配或统一入口需求时使用 |
| 车载接口 | MCP | 让 Agent 连接文件、浏览器或专业软件 | 按任务逐个安装 |
| 驾驶手册 | Skills / `AGENTS.md` | 保存可复用流程和项目规则 | 验收标准、命名规则、操作边界 |

这套比喻只负责建立直觉。技术上，**模型强不等于 Agent 一定好用**：同一个模型放进不同 Agent，工具、上下文管理、权限和执行循环不同，表现也会不同；同一辆“车”换不同“油”，速度、准确率和成本也会变化。

## 核心工具安装与基础配置

本指南的桌面安装路线**直接使用 GitHub Releases，不把 Microsoft Store 或 `winget ... -s msstore` 作为教程步骤**。不过要说清来源：下面两个 Codex 下载仓库都不是 OpenAI 官方 GitHub 分发渠道。OpenAI 官方文档仍用于核对功能、登录、沙箱和权限行为。

### 1. Codex Desktop：首选社区镜像

首推：[Wangnov/codex-app-mirror 最新版](https://github.com/Wangnov/codex-app-mirror/releases/latest)

按设备选择资产：

- Windows x64：文件名含 `x64` 的 `.Msix`。
- Windows ARM64：文件名含 `arm64` 的 `.Msix`。
- Apple Silicon Mac：`Codex-mac-arm64.dmg`。
- Intel Mac：`Codex-mac-x64.dmg`。

Windows 可先在 PowerShell 查看架构：

```powershell
Get-CimInstance Win32_OperatingSystem | Select-Object OSArchitecture
```

下载后，把发布页中的 `SHA256SUMS.txt` 一并下载并核对。下面的路径和哈希都是占位值：

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath "C:\Downloads\OpenAI.Codex_<version>_x64__2p2nqsd0c76g0.Msix"
Get-AuthenticodeSignature -LiteralPath "C:\Downloads\OpenAI.Codex_<version>_x64__2p2nqsd0c76g0.Msix"
```

确认哈希与发布页一致、签名信息没有异常后安装：

```powershell
Add-AppxPackage -Path "C:\Downloads\OpenAI.Codex_<version>_x64__2p2nqsd0c76g0.Msix"
```

macOS 下载对应 DMG，打开后将应用拖入 `Applications`。不要在不明下载站寻找所谓“破解版”。

> 这是**社区镜像**。仓库声明其同步而不修改上游安装包，并提供校验和与 manifest；使用者仍应自己核对文件。如果学校或单位策略禁止侧载 MSIX，请联系管理员，不要绕过设备策略。

### 2. Codex Desktop：Windows x64 便携备选

备选：[WSGsety/rebuild-codex-desktop Releases](https://github.com/WSGsety/rebuild-codex-desktop/releases)

这个项目提供 Windows x64 免安装 ZIP。下载 `Codex-win-x64-<版本>.zip` 和 `SHA256SUMS.txt`，核对哈希后解压，运行目录中的 `ChatGPT.exe`。

它与首选镜像的区别很重要：这是**非官方重打包**，会解包上游 MSIX、修改 `app.asar` 并重新生成便携 ZIP；当前不支持 Windows ARM64 或 macOS。因为供应链边界更宽，只把它作为 MSIX 无法正常安装时的备选，不要把它称作“官方便携版”。

### 3. 首次启动只做基础配置

1. 登录你自己的合法账号，或配置一条你有权使用的 API。
2. 新建一个练习目录，不要直接打开论文原始数据、财务文件或同步盘根目录。
3. 保留沙箱与“执行前审批”；不要为了省一次确认就长期使用完全访问。
4. 选择熟悉的终端；Windows 新手先用 PowerShell 即可。
5. 让 Codex **只读列出目录内容**，确认工作区和权限正常。

完整的架构判断、安装、哈希校验、便携版差异和首次验收见[选车与安装](docs/zh-CN/02-choose-and-install.md)。

### 4. CC-Switch：需要多条油路时再装

下载：[farion1231/cc-switch 最新版](https://github.com/farion1231/cc-switch/releases/latest)

- Windows：优先下载 `.msi`；不想安装可选 `Windows-Portable.zip`。
- macOS：下载 `.dmg` 并拖入 `Applications`。
- ARM64 设备要选择文件名带 `arm64` 的制品。

Windows下载完成后可双击MSI，或用占位路径执行：

```powershell
msiexec.exe /i "C:\Downloads\CC-Switch-<version>-Windows.msi"
```

第一次切换前先备份 `%USERPROFILE%\.codex` 及目标客户端配置。只添加一个可以独立验证的供应商，用占位结构理解字段：

```text
Name: My Provider
Base URL: https://example.invalid/v1
API Key: YOUR_API_KEY
Model: YOUR_MODEL_NAME
```

切换后重启客户端，用无敏感数据的小任务测试；然后练习恢复到原来的直连配置。不要一次同步全部 MCP、Skills 和 Prompts。完整路径图、CPA 与 Sub2API 的区别见[切换油路](docs/zh-CN/04-routing-and-proxy.md)。

### 安装阶段最常见的四个问题

| 现象 | 先检查什么 | 不要怎么做 |
|---|---|---|
| MSIX 无法安装 | x64/ARM64、App Installer、数字签名、设备策略 | 不要找来源不明的修改包 |
| 提示管理员已阻止 | 是否为学校/单位受管设备，是否禁止侧载 | 不要绕过组织策略 |
| 便携版打不开 | 是否完整解压、是否为 x64、杀毒软件是否给出明确告警 | 不要直接关闭全部安全防护 |
| CC-Switch 切换无效 | 目标客户端、配置文件、Base URL、是否需要重启 | 不要同时改网关、模型和多个配置 |

继续排查请直接看[路边救援](docs/zh-CN/10-troubleshooting.md)。

## 给车加油：模型和供应商怎么选

先问三个问题：任务难不难、出错代价多高、数据能不能交给该供应商。

- 文件改名、格式转换、初步分类：普通模型通常够用，重点是权限和可恢复性。
- 多文件推理、复杂表格、长文档整合：需要更稳定的模型和更大的上下文，但仍要抽样复核。
- 论文结论、公开数据、合同或高风险决策：模型只做助手，必须回到原文、公式和人工审核。

订阅、API 额度和第三方转售通常是不同计费体系。不要默认“买了聊天订阅就自动包含所有 API”。第一次先跑通官方登录或官方 API，再增加 CC-Switch 或 CPA，这样出错时才知道是哪一层。详见[模型、供应商与成本](docs/zh-CN/03-models-and-providers.md)。

## 真正的主线：从一句需求到可验收结果

Agent 不是“发一句话，然后相信它”。一个稳定工作流有六步：

```text
选工作区 → 写任务简报 → 让 Agent 先盘点 → 确认计划与权限
        → 小步执行并查看差异 → 按验收标准复核
```

可以直接复制这个最小任务简报：

```text
目标：把练习目录中的文件按类型整理到新文件夹。
输入：当前目录；不要访问目录外内容。
输出：先给预演清单和移动映射，确认后再执行。
约束：不删除、不覆盖；文件重名时停止并报告。
验收：文件数前后一致，每个旧路径都有新路径，提供恢复映射。
授权：本轮只允许读取和规划，不执行移动。
```

第一次永远先做“只读盘点”或“预演”。当计划正确后，再明确授权执行；执行后检查差异、文件数量和恢复路径。更完整的 Plan、项目记忆与交接方法见[学会开车](docs/zh-CN/05-learn-to-drive.md)，现成模板见[中文模板](templates/zh-CN/)。

## 日常能做什么

| 场景 | Agent 适合做 | 你必须验收 |
|---|---|---|
| 文件整理 | 盘点、分类建议、批量改名预演、恢复映射 | 数量、重名、遗漏、能否恢复 |
| 文档报告 | 提纲、格式统一、资料摘要、草稿整合 | 引用是否回到原文，事实是否准确 |
| 表格 | 清洗方案、公式草稿、合并与异常检查 | 单位、键、缺失值、抽样复算 |
| PPT | 故事线、逐页简报、素材清单、生成初稿 | 每页视觉、数字、字体、演讲逻辑 |
| 专业软件 | 通过 MCP 调用获授权的软件流程 | 软件版本、日志、参数和结果复核 |

Stata-MCP 只是“连接专业软件”的一个案例，不是主线依赖。三个完整案例见[案例库](docs/zh-CN/08-case-studies.md)：资料到报告/表格/PPT、批量文件整理、合成数据上的 Stata-MCP。

## 什么时候再加 MCP、Skills 和多 Agent

- **MCP：** 只有任务确实需要外部工具时再装；安装前看权限、维护状态、日志和卸载方式。
- **Skills：** 当你反复做同一流程时，把步骤和验收标准固化成可复用驾驶手册。
- **多 Agent：** 任务能清楚拆分、输出能合并时才并行；否则沟通成本可能高于收益。
- **Computer Use：** 适合没有 API 的界面操作，但更需要截图、状态确认和人工验收。

详见[改装车辆](docs/zh-CN/07-upgrades-and-tools.md)。

## 你现在该走哪条路线

- **完全小白：** 做[10分钟只读体验](docs/zh-CN/00-before-driving.md)，再按本页安装主线前进。
- **已经装好 Codex：** 跳到[学会开车](docs/zh-CN/05-learn-to-drive.md)，然后做[日常工作流](docs/zh-CN/06-daily-workflows.md)。
- **需要多模型：** 先读[模型与供应商](docs/zh-CN/03-models-and-providers.md)，确认计费和数据边界，再配置[CC-Switch/CPA](docs/zh-CN/04-routing-and-proxy.md)。
- **遇到报错：** 不要叠加“修复”，按[路边救援](docs/zh-CN/10-troubleshooting.md)一次排一层。
- **只关心科研软件：** 直接看[案例库](docs/zh-CN/08-case-studies.md)中的 Stata-MCP；它不会贯穿其他章节。

## 详细章节

1. [上车之前：先完成一次安全体验](docs/zh-CN/00-before-driving.md)
2. [认车：Agent、模型和人的分工](docs/zh-CN/01-know-your-agent.md)
3. [选车与安装：Codex、便携版与 CC-Switch](docs/zh-CN/02-choose-and-install.md)
4. [给车加油：模型、供应商与成本](docs/zh-CN/03-models-and-providers.md)
5. [切换油路：CC-Switch 与 CLIProxyAPI](docs/zh-CN/04-routing-and-proxy.md)
6. [学会开车：工作区、任务、计划与验收](docs/zh-CN/05-learn-to-drive.md)
7. [日常任务：文件、文档、表格和 PPT](docs/zh-CN/06-daily-workflows.md)
8. [改装车辆：MCP、Skills、多 Agent 与 Computer Use](docs/zh-CN/07-upgrades-and-tools.md)
9. [案例库：办公闭环、Stata-MCP 和批量文件](docs/zh-CN/08-case-studies.md)
10. [安全驾驶：隐私、权限与学术伦理](docs/zh-CN/09-safety-and-ethics.md)
11. [路边救援：常见故障排查](docs/zh-CN/10-troubleshooting.md)

## 三条底线

1. **先看再改。** 第一次接触陌生目录时先盘点和规划，不直接批量修改。
2. **重要结果要复核。** 数字抽样复算、引用回到原文、PPT 逐页查看；“Agent 说完成了”不等于验收通过。
3. **权限够用就好。** 默认保留沙箱和审批；只有需求清楚、来源可信且能够恢复时才扩大权限。

## 来源标签与项目边界

- **官方：** 产品或项目维护者发布的文档与下载入口。
- **社区项目：** 开源社区维护的工具，不代表 OpenAI、Anthropic 或 StataCorp 官方支持。
- **社区镜像：** 对上游安装包的第三方同步，仍需校验签名、哈希和 manifest。
- **社区重打包：** 解包并修改后重新发布的制品，供应链边界比镜像更宽。

所有入口、来源类型和最后核验日期见[工具地图](resources/tools.md)。本仓库不提供凭证导出、账号共享、支付绕行或地区限制规避教程。

## 示例、模板与版本状态

- [共享案例](examples/)：文件整理、资料到汇报、Stata-MCP。
- [中文模板](templates/zh-CN/) / [English templates](templates/en/)：任务简报、验收表、PPT 简报等。
- [术语表](resources/glossary.md)：中英文术语、汽车比喻与准确解释。
- [安全说明](SECURITY.md) / [免责声明](DISCLAIMER.md)。

V0.1 已完成双语正文、模板、案例和自动同步检查。截图将在核验真实界面后逐步补充；当前版本不依赖截图也能完整阅读。更新记录见 [CHANGELOG](CHANGELOG.md)。

本仓库记录个人学习与使用经验，不构成官方支持、学术、法律、投资或支付建议。工具更新很快，操作前请复核原项目文档，并确认学校、单位和服务商政策。
