from lxml import etree

text = '''
<div>
    <ul>
        <li class="item li-first" name="li">
            <a href="link.html">item_1</a>
            <a class="item">item_2</a>
        </li>
    </ul>
</div>
'''

html = etree.HTML(text)
result_1 = html.xpath('//li/a[last()]/text()')
result_2 = html.xpath('//li/a[position()=1]/text()')
print(result_1)
print(result_2)
