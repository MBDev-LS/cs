#!/usr/bin/env python
# coding: utf-8

# # Trees in Python

# ## Establishing the values of variables

# In[1]:


vars = {
	'x': 4,
	'y': 7
}


# ## Class Declarations

# ### Base Class Declarations
# Creating the base class for expressions.

# In[2]:


class Exprs():
	pass


# Defining the base class for Operators such as + and *.

# In[3]:


class Operators(Exprs):
	def __init__(self, l, r):
		self.l = l
		self.r = r

	def __str__(self):
		return f'({self.l} {self.symb} {self.r})'


# ### Specific Operator Declarations
# Defining specific classes for $+$, $-$, $*$ and /. Each of these classes has a seperate eval function.

# In[4]:


class Plus(Operators):
	def __init__(self, l, r):
		super().__init__(l, r)
		self.symb = '+'
	
	def eval(self, vars):
		return self.l.eval(vars) + self.r.eval(vars)


# In[5]:


class Minus(Operators):
	def __init__(self, l, r):
		super().__init__(l, r)
		self.symb = '-'
	
	def eval(self, vars):
		return self.l.eval(vars) - self.r.eval(vars)


# In[6]:


class Times(Operators):
	def __init__(self, l, r):
		super().__init__(l, r)
		self.symb = '*'
	
	def eval(self, vars):
		return self.l.eval(vars) * self.r.eval(vars)


# In[7]:


class Divide(Operators):
	def __init__(self, l, r):
		super().__init__(l, r)
		self.symb = '/'
	
	def eval(self, vars):
		return self.l.eval(vars) / self.r.eval(vars)


# ### Constant and Variable Class Declarations

# In[8]:


class Const(Exprs):
	def __init__(self, value):
		self.value = value
	
	def __str__(self):
		return str(self.value)
	
	def eval(self, vars):
		return self.value


# In[9]:


class Var(Exprs):
	def __init__(self, name):
		self.name = name
	
	def __str__(self):
		return str(self.name)

	def eval(self, vars):
		return vars[self.name]


# ## Object Creation

# Creates the equation $5*(4+x)$ and display it in the correct form.

# In[10]:


e1 = Times(Const(5), Plus(Const(4), Var('x')))


# In[11]:


print(e1)


# Creates the equation $\frac{9+y}{8-x}$ and display it in the correct form.

# In[12]:


e2 = Divide(Plus(Const(9), Var('y')), Minus(Const(8), Var('x')))


# In[13]:


print(e2)


# ### Evaluating Equations
# Using the object function `eval()`, the equations can be evaluated, with variables taking their values from the `vars` dictionary.

# In[14]:


e1.eval(vars)


# In[15]:


e2.eval(vars)


# ## Final Comments & Outcomes
# This document outlines one use case of the tree abstract data structure and its creation has aided my efforts to improve my understanding of this topic.
# 
# Having implemented trees in Python, the next steps are as follows:\
# - Address the issue of unnecessary brackets, see [here](https://www.youtube.com/watch?v=7tCNu4CnjVc&t=908s)\
# - Explore other uses and aspects of trees (including such information specifically pertaining to binary trees)\
# - Learn about ways to search trees\
# 
# ## Attributions
# **Creator** - [Louis Stevens](https://louisstevens.com)\
# **Video referenced** - [Coding Trees in Python - Computerphile](https://www.youtube.com/watch?v=7tCNu4CnjVc)

# ##
