#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Vector:
    # 생성자의 입력값은 벡터 리스트
    def __init__(self, vec_list, dtype):
        self.dtype = dtype
        self.vector = []
        for i, item in enumerate(vec_list):
            if type(item) != dtype:
                print(f"The item {i} isn't same data type...")
                raise ValueError
      
            else:
                self.vector.append(item)
                
    def dtype(self):
        return self.dtype
    
    def push(self, item):
        if self.dtype != type(item):
            print(f"Input item isn't same data type...")
        else:
            self.vector.append(item)
    
    def pop(self):
        return self.vector.pop(-1)
    
    def check_dimension(self, other):
        if len(self.vector) != len(other.vector):
            print(f"The dimension of two vectors are not same")
            return False
        else:
            return True
    
    # 연산자 오버로딩
    def __add__(self, other):
        new_vector = []
        if self.check_dimension(other):
            for elem1, elem2 in zip(self.vector, other.vector):
                new_elem = elem1 + elem2
                new_vector.append(new_elem)
        else:
            raise ValueError
        new_vec = Vector(new_vector, self.dtype)
        return new_vec
    
    def __sub__(self, other):
        new_vector = []
        if self.check_dimension(other):
            for elem1, elem2 in zip(self.vector, other.vector):
                new_elem = elem1 - elem2
                new_vector.append(new_elem)
        else:
            raise ValueError
        new_vec = Vector(new_vector, self.dtype)
        return new_vec
    
    def __mul__(self, other):
        dot_product = 0
        if self.check_dimension(other):
            for elem1, elem2 in zip(self.vector, other.vector):
                dot_product += elem1 * elem2
            return dot_product
        else:
            raise ValueError
            
    def __call__(self):
        return self.vector
    
    def __str__(self):
        msg = f"{self.vector}"
        return msg

