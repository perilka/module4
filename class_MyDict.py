class MyDict:
    def __init__(self):
        self.lst_keys = []
        self.lst_values = []

    def __getitem__(self, key):
        if key not in self.lst_keys:
            return None
        return self.lst_values[self.lst_keys.index(key)]

    def __setitem__(self, key, value):
        if not isinstance(key, list|set|dict):
            self.lst_keys.append(key)
            self.lst_values.append(value)
        else:
            raise KeyError

    def __delitem__(self, key):
        if key in self.lst_keys:
            self.lst_values.remove(self.lst_values[self.lst_keys.index(key)])
            self.lst_keys.remove(key)

    def __contains__(self, item):
        return self.lst_keys.__contains__(item)

    def keys(self):
        return self.lst_keys

    def values(self):
        return self.lst_values

    def items(self):
        list_items = []
        for i in range(len(self.lst_keys)):
            cor = (self.lst_keys[i], self.lst_values[i])
            list_items.append(cor)
        return list_items

    def clear(self):
        self.lst_keys = []
        self.lst_values = []

    def pop(self, key):
        if key in self.lst_keys:
            removed_value = self.lst_values.pop(self.lst_values[self.lst_keys.index(key)])
            self.lst_keys.pop(key)
            return removed_value
        else:
            return None

    def popitem(self):
        crt = (self.lst_keys[-1], self.lst_values[-1])
        return crt

    def __str__(self):
        s_open = '{'
        for i in range(len(self.lst_keys)):
            if isinstance(self.lst_keys[i], str):
                s_key = f"'{self.lst_keys[i]}': "
            else:
                s_key = f'{self.lst_keys[i]}: '
            if isinstance(self.lst_values[i], str):
                s_value = f"'{self.lst_values[i]}', "
            else:
                s_value = f"{self.lst_values[i]}, "
            s_mid = s_key + s_value
            s_open += s_mid
        s = s_open[:-2] + '}'
        return s



my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
print(my_dict)
print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']
print(my_dict.popitem())