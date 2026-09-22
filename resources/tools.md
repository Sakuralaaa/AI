# 工具地图

[English](tools.en.md) · 最后核验：2026-09-22

“官方”表示产品或项目维护者的入口；“社区项目”表示独立开源项目；“社区镜像”和“社区重打包”都不是官方分发渠道。

| 工具 | 类型 | 本教程中的用途 | 入口 | 使用前注意 |
|---|---|---|---|---|
| ChatGPT desktop app / Codex | OpenAI官方 | 主线Agent与工作区的功能、登录和权限参考 | [Windows文档](https://learn.chatgpt.com/docs/windows/windows-app) | 本指南的安装步骤使用下列GitHub社区渠道；不要把社区下载写成OpenAI官方发布 |
| Codex App Mirror | 社区镜像 | 本指南首选的GitHub直装来源；Windows MSIX与macOS DMG | [最新Release](https://github.com/Wangnov/codex-app-mirror/releases/latest) | 非OpenAI官方仓库；核对架构、SHA256、manifest与数字签名 |
| Rebuild Codex Desktop | 社区重打包 | Windows x64免安装ZIP备选 | [GitHub Releases](https://github.com/WSGsety/rebuild-codex-desktop/releases) | 会解包和修改后重打包；仅限Windows x64，供应链边界比镜像更宽 |
| Claude Code | Anthropic官方 | 替代Agent车型 | [官方文档](https://docs.anthropic.com/en/docs/claude-code/getting-started) | 安装、登录、地区和方案资格以Anthropic说明为准 |
| PI-Desktop | 社区项目 | 可扩展、模型无关的桌面Agent工作区 | [vastsa/PI-Desktop](https://github.com/vastsa/PI-Desktop) | 处于早期迭代期；下载、权限和功能以Releases及README为准 |
| CC-Switch | 社区项目 | 管理不同Agent的供应商、MCP、Skills与配置 | [最新Release](https://github.com/farion1231/cc-switch/releases/latest) | Windows优先MSI、macOS优先DMG；切换前备份配置 |
| CLIProxyAPI | 社区项目 | 可选的本地统一兼容API网关 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | 默认只向本机提供服务；不要把管理接口和凭证暴露到公网 |
| Sub2API | 社区项目 | 团队、用户和计费型网关的对比参考 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | 本仓库不提供商用部署教程；运营者需自行处理合规与数据责任 |
| MCP-for-Stata | 社区项目 | Stata专业软件调用案例 | [SepineTam/mcp-for-stata](https://github.com/SepineTam/mcp-for-stata) | 与StataCorp无隶属关系；Stata及许可证需用户自行准备 |

## 更新规则

- 正文不使用“永远最新”“官方GitHub镜像”等容易过期或误导的表述。
- 入口、安装命令或项目归属变化时，先更新本表，再同步相关章节。
- 无法确认维护状态时，保留历史说明并标为“待核验”，不猜测替代地址。
