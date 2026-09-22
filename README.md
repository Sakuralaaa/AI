# AI Agent 上路指南

[English](README.en.md) · 中文为本仓库的权威版本

> 把 Agent 想象成一辆车：Codex、Claude Code、PI-Desktop 是不同的车，模型是驱动车辆的油。好油能让车跑得更快、更稳；普通油也能完成整理文件、改格式之类的轻任务。Prompt 是目的地，MCP 是车载扩展接口，而你始终是负责选择路线和验收结果的人。

这是一份面向普通用户、研究生和知识工作者的 AI Agent 实用经验库。它不要求你先学会编程，也不会把工具包装成“按一下就自动完成一切”。我们从 Codex 出发，逐步讲清安装、模型、供应商、路由、权限、文件、表格、PPT，以及如何让 Agent 调用 Stata 等专业软件。

## 先看哪一条路线？

- **完全小白：** 从[上车之前](docs/zh-CN/00-before-driving.md)开始，先用10分钟完成一次只读练习。
- **已经装好 Codex：** 直接学习[怎样说清目的地](docs/zh-CN/05-learn-to-drive.md)，再做[日常任务](docs/zh-CN/06-daily-workflows.md)。
- **想配置多模型或中转：** 先理解[模型与供应商](docs/zh-CN/03-models-and-providers.md)，再看[CC-Switch 与 CLIProxyAPI](docs/zh-CN/04-routing-and-proxy.md)。
- **只关心科研软件：** Stata 是一个独立案例，见[完整案例库](docs/zh-CN/08-case-studies.md)。

## 一张图看懂

```text
你（决定目的地并验收）
│
├─ Codex / Claude Code / PI-Desktop     ← 车
│  ├─ 文件、终端、浏览器                 ← 车载能力
│  ├─ MCP / Skills                      ← 扩展接口与驾驶手册
│  └─ 权限、沙箱、审批                   ← 护栏
│
└─ 模型配置                              ← 油路
   ├─ 官方登录或官方 API                 ← 官方加油站
   ├─ CC-Switch                         ← 配置切换面板
   └─ CLIProxyAPI（可选）                ← 本地中转站
```

这个比喻只是入门地图。到了具体操作，我们会回到准确术语：Agent 框架负责组织上下文、工具与执行循环；模型负责理解和生成；供应商负责提供访问与计费。

## 章节目录

1. [上车之前：先完成一次安全体验](docs/zh-CN/00-before-driving.md)
2. [认车：Agent、模型和人的分工](docs/zh-CN/01-know-your-agent.md)
3. [选车与安装：以 Codex 为主线](docs/zh-CN/02-choose-and-install.md)
4. [给车加油：模型、供应商与成本](docs/zh-CN/03-models-and-providers.md)
5. [切换油路：CC-Switch 与 CLIProxyAPI](docs/zh-CN/04-routing-and-proxy.md)
6. [学会开车：工作区、任务、计划与验收](docs/zh-CN/05-learn-to-drive.md)
7. [日常任务：文件、文档、表格和 PPT](docs/zh-CN/06-daily-workflows.md)
8. [改装车辆：MCP、Skills、多 Agent 与 Computer Use](docs/zh-CN/07-upgrades-and-tools.md)
9. [案例库：办公闭环、Stata-MCP 和批量文件](docs/zh-CN/08-case-studies.md)
10. [安全驾驶：隐私、权限与学术伦理](docs/zh-CN/09-safety-and-ethics.md)
11. [路边救援：常见故障排查](docs/zh-CN/10-troubleshooting.md)

## 三条原则

1. **先看再改。** 第一次接触陌生目录时，先让 Agent 盘点和规划，不要直接批量修改。
2. **重要结果要复核。** 数字抽样复算、引用回到原文、PPT逐页查看，不能把“Agent说完成了”当成验收。
3. **权限够用就好。** 默认保留沙箱和审批；只有在明确需要、来源可信、能够恢复时才扩大权限。

## 来源标签

- **官方：** 产品或项目维护者发布的文档与下载入口。
- **社区项目：** 开源社区维护的工具，不代表 OpenAI、Anthropic 或 StataCorp 官方支持。
- **社区镜像：** 对官方安装包的第三方同步；下载后仍需校验签名和哈希。

工具入口和最后核验日期见[工具地图](resources/tools.md)。本仓库不提供账号凭证导出、账号共享、支付绕行或地区限制规避教程。

## 示例与模板

- [共享案例](examples/)：文件整理、资料到汇报、Stata-MCP。
- [中文模板](templates/zh-CN/) / [English templates](templates/en/)：任务简报、验收表、PPT简报等。
- [术语表](resources/glossary.md)：中英文术语、汽车比喻与准确解释。

## V0.1 状态

V0.1 已完成双语正文、模板、案例和自动同步检查。截图将在后续版本按真实界面逐步补充；当前版本不依赖截图也能完整阅读。更新记录见 [CHANGELOG](CHANGELOG.md)。

## 免责声明

本仓库记录个人学习与使用经验，不构成官方支持、学术、法律、投资或支付建议。工具更新很快，请在操作前查看原项目文档。处理敏感数据、安装第三方扩展或接入代理服务前，请确认学校、单位和服务商政策。详见[免责声明](DISCLAIMER.md)与[安全说明](SECURITY.md)。
