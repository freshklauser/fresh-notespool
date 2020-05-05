# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-05-03 13:07:13
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-05-03 13:07:33


class ClassTreeAttributesDisplay:
    """类树+属性树
    Mix-in that returns an __str__ trace of the entire class tree and all its
    objects' attrs at and above self; run by print() or str() returns constructed string;
    use __x attr names to avoid impacting clients;
    use generator expr to recurse to superclasses;
    use str.format() to make substitutions clearer
    """

    def __str__(self):
        self.__visited = {}
        return '<Instance of {}, address {}:\n{}{}>'.format(
            self.__class__.__name__,
            id(self),
            self.__gatherAttrs(self, 0),
            self.__gatherClass(self.__class__, 4))

    def __gatherClass(self, aClass, indent):
        dot_prefix = '.' * (indent + 4)
        if aClass in self.__visited.keys():
            return '\n{0}<Class {1}, address {2}: (see above)>\n'.format(
                dot_prefix,
                aClass.__name__,
                id(aClass))
        else:
            self.__visited[aClass] = 1              # 1: 访问过
            supercls_iter = (self.__gatherClass(c, indent + 4) for c in aClass.__bases__)
            return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}\n>'.format(
                dot_prefix,
                aClass.__name__,
                id(aClass),
                self.__gatherAttrs(aClass, indent),
                ''.join(supercls_iter),
                dot_prefix)

    def __gatherAttrs(self, obj, indent):
        '''
        获取并返回每个obj中的属性 key=value
        Arguments:
            obj {class or instance} -- 类或实例
            indent {int} -- 缩进
        '''
        space_prefix = ' ' * (indent + 4)
        attrs = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                attrs += space_prefix + '{}=<>\n'.format(attr)
            else:
                attrs += space_prefix + '{}={}\n'.format(attr, getattr(obj, attr))
        return attrs
