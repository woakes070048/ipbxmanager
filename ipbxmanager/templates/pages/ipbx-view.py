import pprint
import frappe

def get_context(context):
	print('here')
	pprint.pprint(frappe)
	pprint.pprint(context)
	context['custom_content'] = 'Hub featured page custom content'
	context.show_sidebarar = 1
