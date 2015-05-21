from notes import stage0, stage1, stage2, stage3, stage4


def get_section_html(title, bullets):
    html_1 = '<div class="section">\n\t' + title
    html_2 = '\n\t\t</ul>\n'
    html_3 = ''
    for bull in bullets:
        html_3 += '\t\t\t<li>' + bull + '</li>\n'
    html_4 ='\t\t</ul>\n</div>'
    return html_1 + html_2 + html_3 + html_4


def get_stage_html(stage_list):
    html_1 = '<div class="stage">\n<h1>' + stage_list[0] + '</h1>\n'
    html_2 = ''
    for section in stage_list[1]:
        title = '<h4>' + section[0] + '</h4>'
        bullets = section[1]
        html_2 += '\n' + get_section_html(title, bullets)
    return html_1 + html_2


def get_all_html():
    html = ''
    notes_list = [notes.stage0, notes.stage1, notes.stage2, notes.stage3, notes.stage4]
    for stage in notes_list:
        html += "\n" + get_stage_html(stage) + "\n</div>\n\n\n"
    return html


