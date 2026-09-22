<!-- lang: zh-CN | status: source | last_updated: 2026-09-22 | last_verified: 2026-09-22 -->

# 02｜选车与安装：以Codex为主线

[English](../en/02-choose-and-install.md) · [返回首页](../../README.md)

## 先记住一句话

先选一辆能稳定上路的车，不要同时安装一排工具；本教程以Codex为主，Claude Code和PI-Desktop只在需求确实不同的时候作为替代。

## 三种常见选择

| Agent | 适合谁 | 特点 | 需要注意 |
|---|---|---|---|
| Codex | 希望在桌面工作区中管理文件、任务和审查结果的用户 | Windows原生、项目工作区、沙箱、MCP、Skills、内置审查 | 以OpenAI官方文档中的功能和入口为准 |
| Claude Code | 偏好终端工作流或Anthropic生态的用户 | 终端优先、项目内执行、可扩展 | 安装与账号资格以Anthropic官方说明为准 |
| PI-Desktop | 希望在独立桌面工作区组合模型、项目和扩展的用户 | 本地优先、模型无关、插件化的社区桌面项目 | 处于早期迭代期，功能、权限与安装方式以当前README和Releases为准 |

PI-Desktop适合愿意跟随早期项目迭代、重视独立桌面工作区和模型自由度的用户，但不是本教程的必要组件。

## 安装前检查

- 在Windows设置中确认系统版本和“系统类型”（x64或ARM64）。
- 判断电脑是否由学校或单位管理；受管设备可能禁止侧载MSIX。
- 准备一个普通练习目录，不要直接使用论文原始数据或同步盘根目录。
- 记录已有Codex配置；不确定时先备份 `%USERPROFILE%\.codex`。
- Git有助于查看和撤销修改；Node、Python、.NET是否需要取决于任务，不必一次装齐。

## Codex官方安装

OpenAI官方Windows文档提供Microsoft Store下载，并给出命令行入口：

```powershell
winget install --id 9PLM9XGG6VKS -s msstore
```

安装后登录，在设置中确认Agent运行环境、终端和审批选项。第一次使用保留默认权限，打开练习目录完成第00章。

## Microsoft Store不可用时

[Wangnov/codex-app-mirror](https://github.com/Wangnov/codex-app-mirror/releases) 是**社区镜像，不是OpenAI官方GitHub仓库**。确需使用时：

1. 先确认x64或ARM64。
2. 只从该仓库Releases或其明确列出的镜像入口下载。
3. 使用发布页附带的SHA256清单和Manifest核对文件。
4. 查看Windows数字签名；来源或签名异常时停止安装。
5. 如果设备策略阻止侧载，联系管理员，不要尝试绕过策略。

社区镜像解决的是下载渠道，不会替你绕过系统策略、账号登录或产品资格。

## 跟着做一次

安装完成后：

1. 新建并打开练习目录。
2. 选择要求审批的权限模式。
3. 让Codex只读列出目录内容。
4. 打开审查或文件预览确认结果。
5. 记录版本、安装渠道和日期，便于以后排错。

## 我踩过的坑

- 下载ARM64包到x64电脑，或反过来。
- 把社区镜像写成“官方GitHub版”。
- 为解决脚本错误直接用管理员身份长期运行整个应用。
- 在Windows原生和WSL之间切换后，以为两边自动共享全部配置与会话。

## 正常结果与验收

- [ ] Codex能打开练习目录并准确列出文件。
- [ ] 知道自己的架构、安装渠道和配置目录。
- [ ] 默认保留沙箱与审批。
- [ ] 若使用社区镜像，已核对哈希、Manifest和数字签名。
- [ ] 没有为了安装绕过组织设备策略。

## 来源与核验

- [OpenAI Docs：Windows应用](https://learn.chatgpt.com/docs/windows/windows-app)
- [Anthropic：Claude Code入门](https://docs.anthropic.com/en/docs/claude-code/getting-started)
- [PI-Desktop](https://github.com/vastsa/PI-Desktop)
- 最后核验：2026-09-22

[上一章](01-know-your-agent.md) · [下一章：模型与供应商](03-models-and-providers.md)
