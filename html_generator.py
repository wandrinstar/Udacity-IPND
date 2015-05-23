from notes import all_stages

# Helper function for get_stage_html()
# param title, bullets are elements within a stage list
# return html string of one section

def get_section_html(title, bullets):
    html_1 = '<div class="section">\n\t' + title
    html_2 = '\n\t\t</ul>\n'
    html_3 = ''
    for bull in bullets:
        html_3 += '\t\t\t<li>' + bull + '</li>\n'
    html_4 = '\t\t</ul>\n</div>'
    return html_1 + html_2 + html_3 + html_4

# Call this when generating each stage's content on the fly
# param stage_list is a list containing sections which in turn contain titles and bullets
# return html string for entire stage

def get_stage_html(stage_list):
    html_1 = '<div class="stage">\n<h1>' + stage_list[0] + '</h1>\n'
    html_2 = ''
    for section in stage_list[1]:
        title = '<h4>' + section[0] + '</h4>'
        bullets = section[1]
        html_2 += '\n' + get_section_html(title, bullets)
    return html_1 + html_2

# Not actually used in this app because we will only generate one stage at a time
# return html string for all stages

def get_all_html():
    html = ''
    for stage in all_stages:
        html += "\n" + get_stage_html(stage) + "\n</div>\n\n\n"
    return html
