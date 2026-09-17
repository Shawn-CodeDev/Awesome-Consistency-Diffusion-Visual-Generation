from pathlib import Path

path = Path('README.md')
text = path.read_text(encoding='utf-8')

# Preserve critical survey content.
required = [
    'paper/Cons_01.png',
    'paper/Eval_01.png',
    'paper/Optimize_01.png',
    'https://doi.org/10.20944/preprints202606.0870.v1',
    'visitor-badge.laobi.icu',
    'img.shields.io/github/stars',
    '<!-- BEGIN GENERATED RECENT PAPERS -->',
    '<!-- BEGIN ADDITIONAL-200-2026-09-16 -->',
    'docs/additional-papers-200.md',
]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit(f'Refusing README update; missing expected content: {missing}')

# Repair and complete the centered navigation.
old_nav = '''<p>
  <a href="#overview">Overview</a> ·
  <a href="#taxonomy">Taxonomy</a> ·
  <a href="#evaluation-and-optimization">Evaluation & Optimization</a> ·
  <a href="#resource-collection">Resources</a> ·
  <a href="#machine-readable-resources">Data Files</a> ·
  <a href="#contribution-guide">Contribute</a> ·
  <a href="#citation">Citation</a>
</p>'''
new_nav = '''<p>
  <a href="#overview">Overview</a> ·
  <a href="#taxonomy">Taxonomy</a> ·
  <a href="#evaluation-and-optimization">Evaluation & Optimization</a> ·
  <a href="#recent-literature">Recent papers</a> ·
  <a href="#additional-200-papers">Additional 200</a> ·
  <a href="#resource-collection">Resources</a> ·
  <a href="#machine-readable-resources">Data Files</a> ·
  <a href="#contribution-guide">Contribute</a> ·
  <a href="#citation">Citation</a>
</p>'''
if old_nav not in text and new_nav not in text:
    raise SystemExit('Could not identify the centered navigation block safely.')
text = text.replace(old_nav, new_nav, 1)

# Repair the statistics/badge row. This also removes the stray closing </a>.
old_badges = '''<p align="center">
  <a href="https://github.com/Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation/stargazers"><img src="https://img.shields.io/github/stars/Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation?style=flat-square&amp;label=Stars&amp;color=E3B341" alt="GitHub stars"></a>
  <a href="https://github.com/Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation"><img src="https://visitor-badge.laobi.icu/badge?page_id=Shawn-CodeDev.Awesome-Consistency-Diffusion-Visual-Generation" alt="Visitor badge requests"></a>
  <a href="#recent-literature"><img src="https://img.shields.io/badge/Recent%20papers-81-2563EB?style=flat-square" alt="81 recent papers"></a>
 </a>
</p>'''
new_badges = '''<p align="center">
  <a href="https://github.com/Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation/stargazers"><img src="https://img.shields.io/github/stars/Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation?style=flat-square&amp;label=Stars&amp;color=E3B341" alt="GitHub stars"></a>
  <a href="https://github.com/Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation"><img src="https://visitor-badge.laobi.icu/badge?page_id=Shawn-CodeDev.Awesome-Consistency-Diffusion-Visual-Generation" alt="Visitor badge requests"></a>
  <a href="#recent-literature"><img src="https://img.shields.io/badge/Recent%20papers-81-2563EB?style=flat-square" alt="81 recent papers"></a>
  <a href="#additional-200-papers"><img src="https://img.shields.io/badge/Additional%20papers-200-7C3AED?style=flat-square" alt="200 additional papers"></a>
</p>'''
if old_badges not in text and new_badges not in text:
    raise SystemExit('Could not identify the statistics badge block safely.')
text = text.replace(old_badges, new_badges, 1)

# Sanity checks after the edit.
checks = [
    '<a href="#recent-literature">Recent papers</a>',
    '<a href="#additional-200-papers">Additional 200</a>',
    'Additional%20papers-200-7C3AED',
]
for item in checks:
    if item not in text:
        raise SystemExit(f'Post-edit README check failed: {item}')
if '\n </a>\n</p>' in text:
    raise SystemExit('Stray closing anchor remains in README header.')

path.write_text(text, encoding='utf-8')
