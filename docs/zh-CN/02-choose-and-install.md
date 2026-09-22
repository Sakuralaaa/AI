<!-- lang: zh-CN | status: source | last_updated: 2026-09-22 | last_verified: 2026-09-22 -->

# 02｜选车与安装：以Codex为主线

[English](../en/02-choose-and-install.md) · [返回首页](../../README.md)

## 先记住一句话

先装一辆能稳定上路的车，再考虑换油和改装；本教程用GitHub Releases直装Codex Desktop，不把Microsoft Store作为操作步骤。

## 为什么需要先选一条主线

同时安装几套Agent、切换多个供应商，出错时很难判断是客户端、账号、模型还是网关的问题。先用Codex完成一次可验收的小任务，后面比较Claude Code或PI-Desktop才有基准。

| Agent | 适合谁 | 特点 | 需要注意 |
|---|---|---|---|
| Codex | 希望在桌面工作区管理文件、任务和审查结果的用户 | Windows原生工作流、项目、沙箱、MCP、Skills、审查 | 本教程主线；功能与权限行为以OpenAI官方文档为准 |
| Claude Code | 偏好终端工作流或Anthropic生态的用户 | 终端优先、项目内执行、可扩展 | 安装和账号资格以Anthropic官方说明为准 |
| PI-Desktop | 希望在独立桌面工作区组合模型、项目和插件的用户 | 本地优先、模型无关的社区桌面项目 | 早期迭代较快，以当前README和Releases为准 |

PI-Desktop是可选车型，不是本教程的必要组件。

## 安装前检查

- 确认Windows版本和系统类型（x64或ARM64）；macOS确认Intel或Apple Silicon。
- 判断电脑是否由学校或单位管理；受管设备可能禁止侧载MSIX。
- 准备普通练习目录，不要直接使用论文原始数据或同步盘根目录。
- 已经用过Codex时，先备份 `%USERPROFILE%\.codex`。
- Git有助于查看和撤销修改；Node、Python、.NET按任务需要安装，不必一次装齐。

Windows可在PowerShell查看架构：

```powershell
Get-CimInstance Win32_OperatingSystem | Select-Object OSArchitecture
```

## Codex Desktop：首选GitHub社区镜像

打开 [Wangnov/codex-app-mirror 最新Release](https://github.com/Wangnov/codex-app-mirror/releases/latest)。这是社区镜像，不是OpenAI官方GitHub仓库。仓库声明它同步而不修改上游安装包，并随Release提供校验和与manifest。

| 系统 | 选择的资产 |
|---|---|
| Windows x64 | 文件名含 `x64` 的 `.Msix` |
| Windows ARM64 | 文件名含 `arm64` 的 `.Msix` |
| Apple Silicon Mac | `Codex-mac-arm64.dmg` |
| Intel Mac | `Codex-mac-x64.dmg` |

### Windows：校验并安装MSIX

将安装包、`SHA256SUMS.txt`和发布页提供的manifest下载到同一临时目录。下面的文件名和路径是占位示例，不要照抄版本号：

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath "C:\Downloads\OpenAI.Codex_<version>_x64__2p2nqsd0c76g0.Msix"
Get-AuthenticodeSignature -LiteralPath "C:\Downloads\OpenAI.Codex_<version>_x64__2p2nqsd0c76g0.Msix"
```

把第一条输出与`SHA256SUMS.txt`中的对应行逐字比较，并确认签名信息没有异常。然后执行：

```powershell
Add-AppxPackage -Path "C:\Downloads\OpenAI.Codex_<version>_x64__2p2nqsd0c76g0.Msix"
```

也可以双击MSIX，使用系统的App Installer完成安装。若系统提示管理员阻止、禁止侧载或部署服务不可用，受管设备应联系管理员；不要通过修改策略或下载破解版绕过限制。

### macOS：安装DMG

下载与处理器对应的DMG，打开后将应用拖入`Applications`。首次打开若出现安全提示，先核对下载来源与文件校验，不要为了启动未知制品而整体关闭系统保护。

OpenAI的[Windows官方文档](https://learn.chatgpt.com/docs/windows/windows-app)仍是功能、登录、沙箱和运行环境的权威参考；其当前下载入口与本指南选择的GitHub直装路线不同。

## Windows x64便携备选

[WSGsety/rebuild-codex-desktop Releases](https://github.com/WSGsety/rebuild-codex-desktop/releases) 提供Windows x64免安装ZIP：

1. 下载 `Codex-win-x64-<版本>.zip` 和 `SHA256SUMS.txt`。
2. 用 `Get-FileHash` 核对ZIP。
3. 完整解压到普通目录，不要直接在压缩包预览中运行。
4. 启动解压目录中的 `ChatGPT.exe`。

这个项目会解包上游MSIX、修改`app.asar`并重新打包，因此属于**非官方社区重打包**，不是单纯镜像，也不是OpenAI官方便携版。当前仅支持Windows x64。它的供应链边界更宽，只在MSIX无法正常安装且你理解差异时作为备选。

## CC-Switch：GitHub Releases直装

只有需要管理多个供应商或多套客户端配置时才安装CC-Switch。打开 [farion1231/cc-switch 最新Release](https://github.com/farion1231/cc-switch/releases/latest)：

- Windows优先选择 `.msi`；免安装需求选 `Windows-Portable.zip`。
- macOS选择 `.dmg` 并拖入`Applications`。
- ARM64设备选择文件名明确包含`arm64`的制品。

Windows可双击MSI，或用占位路径安装：

```powershell
msiexec.exe /i "C:\Downloads\CC-Switch-<version>-Windows.msi"
```

第一次启动后不要立刻同步所有配置。先备份Codex配置，只添加一个可以独立验证的供应商，切换后重启客户端并完成一个无敏感数据的小任务。CC-Switch的字段、恢复方法和CPA组合方式见[第04章](04-routing-and-proxy.md)。

## 跟着做一次：第一次安全启动

1. 启动Codex并使用你自己的合法账号登录，或配置一条有权使用的API。
2. 在设置中确认Agent运行环境、终端、沙箱和审批选项。
3. 保留默认沙箱与执行前审批。
4. 新建并打开练习目录。
5. 输入：“只读列出当前目录内容，不创建、修改或删除任何文件。”
6. 核对列出的文件，记录应用版本、安装来源、架构和日期。
7. 只有确实需要多供应商时，才安装CC-Switch并完成一次“切换—验证—恢复”。

## 我踩过的坑

- 下载ARM64包到x64电脑，或反过来。
- 把社区镜像或社区重打包写成“官方GitHub版”。
- 没有核对哈希、manifest和签名就安装第三方下载的制品。
- 在压缩包窗口里直接运行便携版，导致资源文件找不到。
- 为解决一次脚本错误，长期以管理员身份运行整个应用。
- 官方直连尚未跑通，就同时配置CC-Switch、CPA和多个模型。

## 正常结果

Codex能打开练习目录，准确列出文件，没有发生写入；你知道安装包来源、设备架构、应用版本和配置目录。若安装了CC-Switch，还应能恢复到原来的直连配置。

## 验收清单

- [ ] 下载资产与设备架构一致。
- [ ] 社区镜像已核对SHA256、manifest和数字签名。
- [ ] 便携备选被正确识别为Windows x64社区重打包。
- [ ] Codex能完成只读目录盘点。
- [ ] 默认保留沙箱与审批。
- [ ] 没有为了安装绕过组织设备策略。
- [ ] 若使用CC-Switch，已备份并能恢复原配置。

## 来源与核验

- [OpenAI Docs：Windows应用](https://learn.chatgpt.com/docs/windows/windows-app)
- [Wangnov/codex-app-mirror Releases](https://github.com/Wangnov/codex-app-mirror/releases/latest)（社区镜像）
- [WSGsety/rebuild-codex-desktop Releases](https://github.com/WSGsety/rebuild-codex-desktop/releases)（社区重打包）
- [CC-Switch Releases](https://github.com/farion1231/cc-switch/releases/latest)（社区项目）
- [Anthropic：Claude Code入门](https://docs.anthropic.com/en/docs/claude-code/getting-started)
- [PI-Desktop](https://github.com/vastsa/PI-Desktop)（社区项目）
- 最后核验：2026-09-22

[上一章](01-know-your-agent.md) · [下一章：模型与供应商](03-models-and-providers.md)
