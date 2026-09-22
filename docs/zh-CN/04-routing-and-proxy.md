<!-- lang: zh-CN | status: source | last_updated: 2026-09-22 | last_verified: 2026-09-22 -->

# 04｜切换油路：CC-Switch与CLIProxyAPI

[English](../en/04-routing-and-proxy.md) · [返回首页](../../README.md)

## 先记住一句话

CC-Switch主要管理客户端配置，CLIProxyAPI主要提供本地兼容网关；先让官方直连跑通，再逐层增加复杂度。

## 为什么你会需要它

同时使用多个Agent或供应商时，手工修改JSON、TOML和环境变量容易出错。CC-Switch提供可视化管理；CLIProxyAPI（下文简称CPA）则可以把其支持的上游接入整理成兼容API。两者可以配合，也可以单独使用。

```text
Codex等客户端
   ↓ 读取配置
CC-Switch（保存、切换并同步配置）
   ↓ 可选的Base URL
CLIProxyAPI（本地兼容API网关）
   ↓
你有权使用的上游服务
```

CPA在这里是项目简称，不是`.cpa`文件格式。

## CC-Switch安全上手

1. 从 [farion1231/cc-switch](https://github.com/farion1231/cc-switch) 声明的官方渠道下载。
2. 第一次切换前备份Codex及其他客户端配置。
3. 先添加一个你能够独立验证的供应商。
4. 使用占位结构理解字段：

```text
Name: My Provider
Base URL: https://example.invalid/v1
API Key: YOUR_API_KEY
Model: YOUR_MODEL_NAME
```

5. 切换后重新打开客户端，做一个短小、无敏感数据的连通性任务。
6. 记录CC-Switch修改了哪些文件，练习恢复到原配置。

CC-Switch还可以管理MCP、Skills和Prompts；不要一次同步全部内容，先验证单个客户端。

## CLIProxyAPI安全上手原则

- 从 [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) 查看当前文档和Releases。
- 首次部署只绑定回环地址，例如 `127.0.0.1`，不要直接开放公网。
- 为客户端使用单独的本地访问密钥，不要在教程、日志或截图中暴露上游认证。
- 启用前确认配置目录、日志位置、模型映射、停止方法和升级回退方式。
- 只接入你有权使用且符合服务条款的账号或API。

本仓库不提供认证提取、账号共享或绕过限制的步骤。具体配置格式更新很快，应以项目当前文档为准。

## Sub2API放在哪里

[Sub2API](https://github.com/Wei-Shaw/sub2api) 更偏向多用户、Key分发、计费和运营管理。个人本地自用不必为了“功能更多”引入数据库、后台和公网服务。本仓库只做概念对比，不提供商用部署教程。

## 跟着做一次：逐层定位

1. 不经过CC-Switch和CPA，确认官方登录或官方API能完成短任务。
2. 只加入CC-Switch，切换一次再恢复。
3. 确有需要时再加入本地CPA，并保持回环监听。
4. 每增加一层，都记录请求路径、配置文件和日志位置。

## 我踩过的坑

- 官方直连都没跑通，就同时调CC-Switch、CPA和模型映射。
- Base URL多写或少写路径，导致认证成功但接口404。
- 将本地管理端口映射到公网。
- 切换失败后忘记恢复客户端原配置。

## 正常结果与验收

- [ ] 能画出自己的请求路径。
- [ ] 知道CC-Switch修改了哪些客户端配置。
- [ ] CPA只监听本机或受控网络，管理接口未公开。
- [ ] 能恢复官方直连。
- [ ] 示例和日志不含真实凭证。

## 来源与核验

- [CC-Switch](https://github.com/farion1231/cc-switch)
- [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI)
- [Sub2API](https://github.com/Wei-Shaw/sub2api)
- 最后核验：2026-09-22

[上一章](03-models-and-providers.md) · [下一章：学会开车](05-learn-to-drive.md)
