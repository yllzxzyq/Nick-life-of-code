**Jupyter Lab常用快捷键**

 熟悉vim编辑器的开发者应该都知道命令模式和编辑模式，jupyter同样继承了这两种模式。1）编辑模式，允许你往单元中键入代码或文本；这时的单元框线是绿色的。2）命令模式，键盘输入运行程序命令；这时的单元框线是灰色。

快捷键

\1. 命令模式 (esc开启)

转入编辑模式：Enter

查看快捷键帮助文档：h

打开命令调色板：cmd+shift+p

保存文件：s or cmd+s

在上方插入cell：a

在下方插入cell：b

剪切当前cell：x

删除当前cell：dd

撤销删除：u

上下：方向键 or jk (同vim)

扩展选中上下左右：shift+jk

当前cell转入markdown状态：m

当前cell转入代码状态：y

当前cell装入raw文本状态：r

设置第2级标题：2

复制当前所选：c

粘贴所选到下方：v

转换行号：l

\2. 编辑模式 (enter开启)

转入命令模式：esc

复制、粘贴、全选、撤销等：同系统

代码提示：tab

删除前一个字符：back

删除后一个字符：ctrl+d

删除前一个单词：option+back

删除后一个单词：option+d

删除当前行光标前所有：cmd+back

运行选中的cells：ctrl+enter

运行当前以上的cells: 可自行设置快捷键或通过调用命令调色板

\3. 其他命令：

牢记命令调色板cmd+shift+p，便于查询，有时比快捷键好用

可自行设置增减快捷键，比如熟悉vim可用vim风格控制