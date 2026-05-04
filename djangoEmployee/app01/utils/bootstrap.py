from django import forms

class BootStrap:
    bootstrap_fields = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name in self.bootstrap_fields:
                continue
            # 批量加的 多个属性
            new_attrs = {
                "class": "form-control",
            }

            # 循环挨个设置：只补空缺，绝不覆盖原有！
            for key, value in new_attrs.items():
                field.widget.attrs.setdefault(key, value)

class BootStrapModelForm(BootStrap, forms.ModelForm):
    pass

class BootStrapForm(BootStrap, forms.Form):
    pass