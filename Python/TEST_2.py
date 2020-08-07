import ui 

def text_field_action(sender):
    print('Text was entered:')
    # `sender` is the text field that caused the action.
    print(sender.text)

v = ui.load_view('TEST_2.pyui') # load the view
tf = v['textfield1'] # Access subview by name
tf.action = text_field_action # Important: No parentheses here!
# ...
v.present('sheet')
