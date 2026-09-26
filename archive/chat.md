# User
你知道leetcode吗？leetcode刷题是只能在网页上做吗？我能否在终端，获取指定题目，然后保存到本地，然后在本地写代码测试，然后上传代码去进行测试以及提交，并且获取测试结果，可以做到吗？如果可以的话，会不会需要反复要求登录之类的很麻烦的那种？

# LLM
知道，而且完全可以。LeetCode 不必只在网页上刷；用第三方 CLI 工具可以完成“获取题目 → 本地编码/调试 → 在线测试 → 提交 → 查看结果”的完整流程。

我比较推荐跨平台的 [leetgo](https://github.com/j178/leetgo)。它同时支持 `leetcode.cn` 和 `leetcode.com`，典型流程是：

```powershell
# 初始化刷题目录：中国站 + C++
leetgo init -t cn -l cpp

# 获取第 1 题，生成题目描述、代码模板和测试文件
leetgo pick 1

# 本地编译运行测试
leetgo test last -L

# 调用 LeetCode 服务器运行
leetgo test last

# 正式提交，并等待返回 Accepted / Wrong Answer 等结果
leetgo submit last
```

也可以把本地测试和提交连起来：

```powershell
leetgo test last -L -s
```

登录方面通常不会每次都让你登录：

- 本地测试完全不需要联网或重新登录。
- 在线运行和提交需要 LeetCode 身份，但 CLI 会复用 Cookie。
- 正常情况下配置一次，可以持续使用很久。
- 只有 Cookie 过期、你在网页退出账号、修改密码，或者触发 Cloudflare 验证时，才需要更新。

需要特别注意你现在是 Windows 环境：Chrome/Edge 127 之后启用了 Cookie 的 App-Bound Encryption，leetgo 无法直接解密新版 Chrome/Edge Cookie。可以选择：

- 用 Firefox 登录 LeetCode，让 leetgo 自动读取；
- 或手动配置 `LEETCODE_SESSION` 和 `csrftoken`；
- 国际站还可能需要 `cf_clearance`。

这是 Chromium 的安全机制，不是每次都要操作；手动配好后仍然可以长期复用。[leetgo 的认证说明](https://github.com/j178/leetgo#leetcode-authentication)也特别标注了这个限制，[Google 的相关说明](https://security.googleblog.com/2024/07/improving-security-of-chrome-cookies-on.html)解释了该机制。

几个现实限制：

- 隐藏测试用例只能在 LeetCode 服务器上运行，本地只能跑样例和你自己添加的用例。
- leetgo 当前对 C++、Python、Go、Rust 的本地测试支持最好；其他语言可以获取和提交，但可能需要自己补测试入口。
- 这是第三方工具，依赖 LeetCode 的 GraphQL 接口；网站接口改版时偶尔可能需要升级工具。
- 如果把 Cookie 放进项目的 `.env`，一定要把 `.env` 加入 `.gitignore`，不能提交到 Git。

总的来说：可以做到，而且配置完成后并不麻烦，平时基本不需要打开网页。对于你的 Windows 环境，最省心的组合是“leetgo + Firefox 登录”或者“一次性手动配置 Cookie”。