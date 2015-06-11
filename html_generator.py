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
        title = '<h3>' + section[0] + '</h3>'
        bullets = section[1]
        html_2 += '\n' + get_section_html(title, bullets)
    return html_1 + html_2

# Helper function for get_recursive_stage

def recursive(mylist, spaces = ''):
    if not any(isinstance(e, list) for e in mylist): # If no more lists inside any element of list, create the ul.
        html_ul = '<ul>' + '\n' + spaces
        for e in mylist:
            html_ul += '<li>' + e + '</li>'
        return html_ul + '\n' + spaces + '</ul>'
    else:
        spaces += '    '
        html = '<ul>'
        for e in mylist:
            if isinstance(e, str): # There are lists but string element is the parent bullet.
                html += '<li>' + e + '</li>'
            else:
                html += '\n' + spaces + recursive(e, spaces)
        return html + '</ul>'

# Call this to generate recursive notes for stage on the fly.
# Allows infinite number of nested unordered lists.
# Use with new data structure, ie stage5 and higher.

def get_recursive_stage(stage_dict):
    html = '<div class="stage"><h1>' + stage_dict['title'] + '</h1>'
    for e in stage_dict['sections']:
        sec_title = '<h3>' + e['sec_title'] + '</h3>'
        sec_notes = recursive(e['notes'])
        html += '<div class="section">\n' + sec_title + '\n' + sec_notes + '\n</div>'
    return html + '\n</div>'