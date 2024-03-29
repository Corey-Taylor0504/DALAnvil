from anvil import *
from _anvil_designer.common_structures import attr_getter, attr_setter, ClassDict

link_name = dict(
    col_widths='{}',
    parent=Container(),
)
label_email = dict(
)
databindings = [
    dict( item='self.item["name"]', element='link_name.text', writeback=False,),
    dict( item='self.item["phone"]', element='label_email.text', writeback=False,),
]

class ContactDisplayFormTemplate(ColumnPanel):
    def __init__(self, **properties):
        super(ContactDisplayFormTemplate, self).__init__()
        self.link_name = Link(**link_name)
        self.label_email = Label(**label_email)
        self._bindings = databindings
        self._item = ClassDict()

        if properties.get('item', None) is not None:
            self.item = properties['item']

    @property
    def item(self):
        return attr_getter(self, 'item')

    @item.setter
    def item(self, some_dict):
        attr_setter(self, some_dict, 'item')
        return

    def init_components(self, **properties):
        ContactDisplayFormTemplate.__init__(self, **properties)
