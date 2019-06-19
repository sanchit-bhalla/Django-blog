from django import forms
from blog.models import Comment,Post

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('text','title','author')

        widgets = {'title':forms.TextInput(attrs={'class':'textinputclass'}),
                    'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
                    }


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
                    'author':forms.TextInput(attrs={'class':'textinputclass'})
                    }
