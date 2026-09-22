<!-- lang: zh-CN | status: source | last_updated: 2026-09-22 | last_verified: 2026-09-22 -->

# 07｜改装车辆：MCP、Skills、多Agent与Computer Use

[English](../en/07-upgrades-and-tools.md) · [返回首页](../../README.md)

## 先记住一句话

扩展不是装得越多越强：只有当内置能力解决不了明确问题时，才增加MCP、Skill、插件或第二个Agent。

## MCP：车载扩展接口

Model Context Protocol让Agent连接外部工具和上下文。Codex本地客户端支持本地STDIO服务器和远程HTTP服务器；不同传输方式有不同的进程、网络和认证边界。

安装前问：

- 谁维护它，代码和发布包在哪里？
- 它能读取、写入或删除什么？
- 是否访问网络，数据发到哪里？
- 使用什么认证，凭证放在哪里？
- 如何停止、移除和查看日志？

在Codex桌面端中添加服务器后需要按界面提示保存并重启。先用无敏感数据测试单个工具，再扩大范围。

## Skills：驾驶手册

Skill通常是包含 `SKILL.md` 的目录，用于说明何时使用某个工作流、执行步骤和成功标准，也可以附带脚本、参考和模板。它不让模型“升级”，而是减少重复说明和流程漂移。

适合做成Skill的内容：每周报告、固定表格核验、论文图表出口规范。一次性的临时要求继续放在Prompt里；仓库长期约定放在AGENTS.md。

## Plugins：打包的改装套件

在支持的产品中，插件可以组合Skills、MCP服务器和可选界面。安装前把它当作软件供应链，而不是一段无害提示词：核对维护者、版本、权限、网络和更新记录。

## 多Agent：车队而不是分身

适合并行的是互不写同一文件的独立任务，例如“检索来源”“检查表格”“审阅PPT”。需要共享状态或连续决策的任务，单Agent通常更清楚。

推荐角色：执行者产生成果，审查者按明确清单找问题。不要让两个Agent同时修改同一文件；用不同输出目录，最后由一个负责人整合。

## Computer Use与浏览器

它适合需要真实界面、没有稳定API或必须视觉检查的任务。登录、支付、发布、删除、发送消息和最终提交应保留人工确认。网页和文档可能包含针对Agent的恶意指令，不要因为内容出现在页面上就把它当成你的要求。

## 跟着做一次

选择一个重复三次以上的低风险流程，例如“将会议记录整理成摘要和行动项”：

1. 先用普通Prompt跑通。
2. 写下稳定步骤和验收清单。
3. 再决定放进AGENTS.md、模板还是Skill。
4. 只有确实需要外部系统时才添加MCP。

## 我踩过的坑

- 一次安装十几个MCP，却不知道哪个进程能访问哪些文件。
- 把临时偏好写成全局规则，污染其他项目。
- 多Agent并行编辑同一PPT，合并时丢失版本。
- 允许Computer Use直接点击最终提交按钮。

## 正常结果与验收

- [ ] 每个扩展都有明确用途和最小权限。
- [ ] 能说明MCP、Skill、Plugin和AGENTS.md的区别。
- [ ] 多Agent输出互相隔离，有明确整合者。
- [ ] 外部提交和不可逆操作保留人工确认。
- [ ] 知道如何停用或卸载扩展。

## 来源与核验

- [OpenAI Docs：MCP](https://learn.chatgpt.com/docs/extend/mcp)
- [OpenAI Docs：插件架构](https://developers.openai.com/plugins/concepts/plugins)
- [OpenAI Docs：AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- 最后核验：2026-09-22

[上一章](06-daily-workflows.md) · [下一章：案例库](08-case-studies.md)
