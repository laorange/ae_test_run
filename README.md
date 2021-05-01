<a href="https://996.icu"><img src="https://img.shields.io/badge/link-996.icu-red.svg" alt="996.icu" /></a>

# aeroengine test run [\[SIAE\]](https://baike.baidu.com/item/%E4%B8%AD%E6%AC%A7%E8%88%AA%E7%A9%BA%E5%B7%A5%E7%A8%8B%E5%B8%88%E5%AD%A6%E9%99%A2/4060853?fr=aladdin)

使用pandas+plotly对2021.03综合实验周的航空发动机试车原理及故障诊断实验的数据分析代码示例

因为生成的结果是动态的，查看示例可访问该网站：https://laorange.github.io/ae_test_run/demo.html

使用python实现，查看源代码可点击![此处](https://github.com/laorange/ae_test_run/blob/main/parse.py)

---------------

如果需要指定某些列，可修改 ``cols``。理论上在204那台设备做实验生成的数据均可用这个程序做可视化。

如果需要套公式对某列进行运算，请参考``numpy``和``pandas``的使用方法。

---------------

requirements.txt:

```python
pandas
numpy
plotly>=4.14.3
```
