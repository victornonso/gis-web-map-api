from rest_framework.renderers import BrowsableAPIRenderer

class NoPostFormBrowsableAPIRenderer(BrowsableAPIRenderer):
    def get_context(self, data, accepted_media_type, renderer_context):
        context = super().get_context(data, accepted_media_type, renderer_context)
        context['post_form'] = None  # Disable the POST form
        return context