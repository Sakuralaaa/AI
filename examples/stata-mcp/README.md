# Stata-MCP合成案例

[English](README.en.md)

本目录演示“Agent通过MCP调用专业软件”的可重复流程。数据完全合成，共5个单位、4年、20行。样本太小，不能用于真实因果推断。

文件：

- `synthetic_panel.csv`：合成面板数据。
- `analysis.do`：仅使用Stata基础命令的示例脚本。
- `verification.md`：人工核验清单。

使用前准备有效的Stata安装和许可证，并按 [MCP-for-Stata](https://github.com/SepineTam/mcp-for-stata) 当前文档安装。先独立确认Stata能启动，再让Codex测试MCP。不要把个人或受限数据替换进案例，除非已经完成授权、环境和隐私评估。
