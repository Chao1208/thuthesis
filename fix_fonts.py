#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复BibTeX文件中的特殊字符，替换为LaTeX兼容的字符
"""

import re

def fix_bibtex_chars(input_file, output_file=None):
    """修复BibTeX文件中的特殊字符"""
    if output_file is None:
        output_file = input_file
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 记录替换信息
    replacements = []
    
    # 替换各种连字符为标准连字符
    hyphen_replacements = [
        ('\u2010', '-'),  # HYPHEN
        ('\u2011', '-'),  # NON-BREAKING HYPHEN
        ('\u2012', '-'),  # FIGURE DASH
        ('\u2013', '--'), # EN DASH
        ('\u2014', '---'),# EM DASH
        ('\u2015', '---'),# HORIZONTAL BAR
    ]
    
    for old_char, new_char in hyphen_replacements:
        count = content.count(old_char)
        if count > 0:
            replacements.append(f"替换 {repr(old_char)} -> {repr(new_char)}: {count}处")
            content = content.replace(old_char, new_char)
    
    # 替换其他特殊字符
    other_replacements = [
        ('\u00A0', ' '),  # NO-BREAK SPACE
        ('\u2018', '`'),  # LEFT SINGLE QUOTATION MARK
        ('\u2019', "'"),  # RIGHT SINGLE QUOTATION MARK
        ('\u201C', "``"), # LEFT DOUBLE QUOTATION MARK
        ('\u201D', "''"), # RIGHT DOUBLE QUOTATION MARK
        ('\u2026', '...'),# HORIZONTAL ELLIPSIS
    ]
    
    for old_char, new_char in other_replacements:
        count = content.count(old_char)
        if count > 0:
            replacements.append(f"替换 {repr(old_char)} -> {repr(new_char)}: {count}处")
            content = content.replace(old_char, new_char)
    
    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return replacements

if __name__ == '__main__':
    import sys
    
    input_file = 'myref/refs.bib'
    
    print("="*60)
    print("开始修复BibTeX文件中的特殊字符...")
    print("="*60)
    
    try:
        replacements = fix_bibtex_chars(input_file)
        
        if replacements:
            print("\n完成以下替换：")
            for r in replacements:
                print(f"  • {r}")
            print(f"\n✓ 文件已更新: {input_file}")
        else:
            print("\n✓ 没有发现需要替换的特殊字符")
        
        print("="*60)
        
    except Exception as e:
        print(f"\n✗ 错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

