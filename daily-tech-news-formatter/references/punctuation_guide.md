# Chinese Punctuation Guide

> **Complete reference for Chinese/English punctuation usage in mixed-language content**

## Punctuation Conversion Table

### Basic Punctuation

| English | Chinese | Unicode | Name | Usage Context |
|---------|---------|---------|------|---------------|
| , | ，| U+FF0C | Comma | In Chinese sentences |
| . | 。| U+3002 | Period | End of Chinese sentence |
| : | ：| U+FF1A | Colon | Before Chinese explanation/quote |
| ; | ；| U+FF1B | Semicolon | Between Chinese clauses |
| ! | ！| U+FF01 | Exclamation | In Chinese exclamation |
| ? | ？| U+FF1F | Question | In Chinese question |
| ( ) | （ ）| U+FF08 U+FF09 | Parentheses | Around Chinese text |
| " " | " "| U+201C U+201D | Double quotes | Outer quotes in Chinese |
| ' ' | ' '| U+2018 U+2019 | Single quotes | Inner quotes in Chinese |

### Special Punctuation

| Symbol | Usage | Example |
|--------|-------|---------|
| · | Separator in Chinese | 乔布斯·史蒂夫 |
| — | Em dash in Chinese | 这是重点——非常重要 |
| … | Ellipsis | 持续增长… |
| ～ | Wavy dash | 2020～2025年 |
| 、 | Chinese comma (enumeration) | 苹果、谷歌、微软 |

## Context-Specific Rules

### Rule 1: Chinese Text Uses Chinese Punctuation

```markdown
✅ Correct:
OpenAI宣布，GPT-5将在2025年发布。

❌ Wrong:
OpenAI宣布, GPT-5将在2025年发布.
```

### Rule 2: English Text Uses English Punctuation

```markdown
✅ Correct:
According to TechCrunch, OpenAI raised $10B.

❌ Wrong:
According to TechCrunch， OpenAI raised $10B。
```

### Rule 3: Mixed Content

```markdown
✅ Correct:
OpenAI的CEO Sam Altman表示："GPT-5将改变AI行业。"

❌ Wrong:
OpenAI的CEO Sam Altman表示:"GPT-5将改变AI行业."
```

**Logic**:
- "OpenAI的CEO Sam Altman表示" → Chinese context → use Chinese colon ：
- Quoted text is Chinese → use Chinese period 。

### Rule 4: Preserve Technical Terms

```markdown
✅ Correct:
该模型名为GPT-4.5 Turbo，性能提升显著。

❌ Wrong:
该模型名为GPT-4。5 Turbo，性能提升显著。
```

**Logic**: "GPT-4.5" is a technical identifier → preserve English period

### Rule 5: URLs and Email

```markdown
✅ Correct:
访问https://openai.com了解详情。

❌ Wrong:
访问https：//openai。com了解详情。
```

### Rule 6: Nested Quotes

```markdown
✅ Correct:
他说："她回答'我不确定'，然后离开了。"

❌ Wrong:
他说："她回答"我不确定"，然后离开了。"
```

**Logic**: Outer quotes use " ", inner quotes use ' '

## Decision Tree for Punctuation Selection

```
Is the character inside a URL/email?
├─ YES → Use English punctuation
└─ NO → Continue

Is the character part of a technical identifier (product name, version)?
├─ YES → Use English punctuation
└─ NO → Continue

Is the surrounding text primarily Chinese (>70% Chinese characters)?
├─ YES → Use Chinese punctuation
└─ NO → Continue

Is the surrounding text primarily English (>70% ASCII)?
├─ YES → Use English punctuation
└─ NO → Use Chinese punctuation (default for mixed content)
```

## Edge Cases

### Case 1: Company Names with Possessive

```markdown
✅ Correct:
OpenAI的模型、Microsoft的Azure、Google的Gemini

✅ Also Acceptable:
OpenAI 的模型、Microsoft 的 Azure、Google 的 Gemini

❌ Wrong:
OpenAI's 模型 (mixing English possessive with Chinese)
```

**Best Practice**: Use Chinese "的" instead of English "'s" when followed by Chinese text.

### Case 2: Abbreviations in Chinese Context

```markdown
✅ Correct:
美国（U.S.）政府宣布新政策。

❌ Wrong:
美国（U。S。）政府宣布新政策。
```

**Logic**: "U.S." is English abbreviation → preserve English periods even in Chinese parentheses

### Case 3: Numbers with Decimal Points

```markdown
✅ Correct:
模型参数达到3.5万亿，性能提升了2.5倍。

❌ Wrong:
模型参数达到3。5万亿，性能提升了2。5倍。
```

**Logic**: Decimal points in numbers are mathematical notation → always use English period

### Case 4: Dates and Timestamps

```markdown
✅ Correct:
2025年11月20日14:30发布

❌ Wrong:
2025年11月20日14：30发布
```

**Logic**: Time format uses colon as separator → use English colon for ISO standard

### Case 5: Prices and Currency

```markdown
✅ Correct:
价格为$99.99美元，约合¥700元。

❌ Wrong:
价格为$99。99美元，约合¥700元。
```

### Case 6: Ratios and Ranges

```markdown
✅ Correct:
性能比为3:1，时间范围为2020-2025年。

❌ Wrong:
性能比为3：1，时间范围为2020-2025年。
```

**Logic**: Mathematical ratios use English colon for international standard

## Implementation Logic

### Python Example

```python
import re
from typing import Tuple

def should_use_chinese_punctuation(text: str, position: int, char: str) -> bool:
    """
    Determine if position should use Chinese punctuation

    Args:
        text: Full text content
        position: Character position
        char: The punctuation character to check

    Returns:
        True if should use Chinese punctuation, False otherwise
    """
    # Extract context window
    start = max(0, position - 20)
    end = min(len(text), position + 20)
    context = text[start:end]

    # Check for preserved contexts
    if is_url_context(text, position):
        return False

    if is_email_context(text, position):
        return False

    if is_technical_term(text, position):
        return False

    if is_number_context(text, position, char):
        return False

    if is_time_format(text, position):
        return False

    # Check language context
    chinese_ratio = sum(1 for c in context if '\u4e00' <= c <= '\u9fff') / len(context)

    return chinese_ratio > 0.7

def is_url_context(text: str, position: int) -> bool:
    """Check if position is inside URL"""
    # Look backwards and forwards for URL patterns
    start = max(0, position - 100)
    end = min(len(text), position + 100)
    snippet = text[start:end]

    url_pattern = r'https?://[^\s\u4e00-\u9fff]+'
    matches = re.finditer(url_pattern, snippet)

    for match in matches:
        if start + match.start() <= position <= start + match.end():
            return True

    return False

def is_technical_term(text: str, position: int) -> bool:
    """Check if position is part of technical identifier"""
    # Look for patterns like "GPT-4.5", "v3.2", "iOS 17.1"
    start = max(0, position - 10)
    end = min(len(text), position + 10)
    snippet = text[start:end]

    tech_patterns = [
        r'[A-Z]+\-?\d+(\.\d+)?',  # GPT-4, GPT-4.5
        r'v\d+\.\d+',              # v3.2
        r'[A-Z][a-z]+\s+\d+(\.\d+)?',  # iOS 17.1
        r'\d+\.\d+\s?[A-Z]+',      # 3.5T, 10.5B
    ]

    for pattern in tech_patterns:
        if re.search(pattern, snippet):
            # Check if position is within match
            for match in re.finditer(pattern, snippet):
                if start + match.start() <= position <= start + match.end():
                    return True

    return False

def is_number_context(text: str, position: int, char: str) -> bool:
    """Check if punctuation is part of number (decimal point, thousands separator)"""
    if char not in '.,':
        return False

    before = text[position-1] if position > 0 else ''
    after = text[position+1] if position < len(text)-1 else ''

    # Decimal point: 3.14, 99.99
    if before.isdigit() and after.isdigit():
        return True

    return False

def is_time_format(text: str, position: int) -> bool:
    """Check if colon is part of time format"""
    start = max(0, position - 5)
    end = min(len(text), position + 5)
    snippet = text[start:end]

    time_pattern = r'\d{1,2}:\d{2}(:\d{2})?'
    return re.search(time_pattern, snippet) is not None

def normalize_punctuation(text: str) -> Tuple[str, list]:
    """
    Convert English punctuation to Chinese in Chinese context

    Returns:
        (normalized_text, changes_log)
    """
    PUNCT_MAP = {
        ',': '，',
        '.': '。',
        ':': '：',
        ';': '；',
        '!': '！',
        '?': '？',
        '(': '（',
        ')': '）',
    }

    result = []
    changes = []

    for i, char in enumerate(text):
        if char in PUNCT_MAP and should_use_chinese_punctuation(text, i, char):
            chinese_char = PUNCT_MAP[char]
            result.append(chinese_char)
            changes.append({
                'position': i,
                'before': char,
                'after': chinese_char,
                'context': text[max(0, i-10):min(len(text), i+10)]
            })
        else:
            result.append(char)

    return ''.join(result), changes
```

## Testing Examples

### Test Case 1: Mixed Content Article

```markdown
Input:
OpenAI宣布, GPT-5将在2025年Q2发布. CEO Sam Altman表示:"这是AI历史上的重大突破."该模型参数达到10.5T,支持多模态能力(文本、图像、视频).

Expected Output:
OpenAI宣布，GPT-5将在2025年Q2发布。CEO Sam Altman表示："这是AI历史上的重大突破。"该模型参数达到10.5T，支持多模态能力（文本、图像、视频）。

Changes:
1. Position 6: , → ，(Chinese comma after 宣布)
2. Position 25: . → 。(Chinese period after 发布)
3. Position 48: : → ：(Chinese colon before quote)
4. Position 49: " → "(Chinese left quote)
5. Position 61: . → 。(Chinese period in quote)
6. Position 62: " → "(Chinese right quote)
7. Position 73: , → ，(Chinese comma after 10.5T)
8. Position 83: ( → （(Chinese left paren)
9. Position 93: ) → ）(Chinese right paren)
10. Position 94: . → 。(Chinese period at end)
```

### Test Case 2: Technical Content Preservation

```markdown
Input:
访问https://openai.com或发送邮件至support@openai.com了解GPT-4.5 Turbo的详情.

Expected Output:
访问https://openai.com或发送邮件至support@openai.com了解GPT-4.5 Turbo的详情。

Changes:
1. Position 67: . → 。(Only end-of-sentence period changed)

Preserved:
- https://openai.com (URL kept with English punctuation)
- support@openai.com (Email kept with English punctuation)
- GPT-4.5 (Version number decimal point preserved)
```

### Test Case 3: Nested Quotes

```markdown
Input:
他说:"她问'你确定吗?',然后我回答'是的'."

Expected Output:
他说："她问'你确定吗？'，然后我回答'是的'。"

Changes:
1. Position 3: : → ：
2. Position 4: " → "
3. Position 11: ? → ？
4. Position 13: ' → '
5. Position 14: , → ，
6. Position 24: ' → '
7. Position 26: . → 。
8. Position 27: " → "
```

## Common Mistakes and Fixes

### Mistake 1: Over-Normalization

```markdown
❌ Wrong:
请访问 https：//openai。com 了解详情。

✅ Correct:
请访问https://openai.com了解详情。

Issue: URLs should preserve English punctuation
```

### Mistake 2: Under-Normalization

```markdown
❌ Wrong:
OpenAI发布GPT-5, 性能提升显著.

✅ Correct:
OpenAI发布GPT-5，性能提升显著。

Issue: Chinese text should use Chinese punctuation
```

### Mistake 3: Inconsistent Quote Matching

```markdown
❌ Wrong:
他说："这很重要"。

✅ Correct:
他说："这很重要。"

Issue: Period should be inside quotes
```

### Mistake 4: Number Formatting

```markdown
❌ Wrong:
价格为$99。99美元。

✅ Correct:
价格为$99.99美元。

Issue: Decimal point in numbers is not a sentence period
```

## Quality Checklist

- [ ] All commas in Chinese context converted to ，
- [ ] All periods ending Chinese sentences converted to 。
- [ ] All colons before Chinese text converted to ：
- [ ] All parentheses around Chinese text converted to （）
- [ ] All quotes around Chinese text converted to " " or ' '
- [ ] URLs preserved with English punctuation
- [ ] Email addresses preserved
- [ ] Technical identifiers (GPT-4.5) preserved
- [ ] Number decimal points preserved (3.14)
- [ ] Time formats preserved (14:30)
- [ ] Nested quotes properly matched
- [ ] No stray punctuation artifacts

---

**Version**: 4.0.0
**Character Encoding**: UTF-8
**Tested with**: daily-tech-news-formatter v4.0.0
**Locale**: zh_CN + en_US mixed content
