
from __future__ import print_function
import types

class RecursionDetectedError(Exception):
    pass

def norecurse(func):
    '''Decoratore che lancia una eccezione se la funzione è ricorsiva'''
    func.called = False
    def f(*args, **kwargs):
        if func.called:
            print("Recursion detected! in " + func.__name__)
            func.called = False # if you are going to continue execution
            raise RecursionDetectedError
        func.called = True
        result = func(*args, **kwargs)
        func.called = False
        return result
    return f

def isRecursiveP(func):
    '''Decoratore che setta l'attributo della funzione recursive=True se scopre la ricorsione nella sua esecuzione.'''
    func.called    = False
    func.recursive = False
    def f(*args, **kwargs):
        if func.called:
            #print "Recursion detected!"
            func.recursive = True
        func.called = True
        result = func(*args, **kwargs)
        func.called = False
        return result
    return f

def decorate_function(f, dec):
    '''applica il decoratore dec alla funzione f e ricorda la vecchia funzione'''
    newf = dec(f)
    newf.oldf = f
    return newf

def undecorate_function(f):
    '''rimuove il decoratore dec dalla funzione f, se presente'''
    return getattr(f, 'oldf', f)

# TODO usare il modulo decorator

DEBUG=True
DEBUG=False

def decorate_module(module, decorator=norecurse):
    '''decora le funzioni ed i metodi delle classi definite nel modulo, per default con norecurse'''
    for f in dir(module):
        ff = getattr(module,f)
        if getattr(ff, '__module__', None) == module.__name__:
            if isinstance(ff, types.FunctionType):
                if DEBUG: print('decorating', f)
                ff = decorate_function(ff,decorator)
                setattr(module,f,ff)
            elif isinstance(ff, type):
                if DEBUG: print('decorating', f, 'methods')
                for m in dir(ff):
                    if DEBUG: print('   decorating',m)
                    mm = getattr(ff, m)
                    if isinstance(mm, types.FunctionType):
                        mm = decorate_function(mm, decorator)
                        setattr(ff, m, mm)

def undecorate_module(module):
    '''elimina le decorazioni messe prima'''
    for f in dir(module):
        ff = getattr(module,f)
        if isinstance(ff, types.FunctionType):
            if DEBUG: print('undecorating', f)
            ff = undecorate_function(ff)
            setattr(module,f,ff)
        elif isinstance(ff, type):
            if DEBUG: print('undecorating', f, 'methods')
            for m in dir(ff):
                if DEBUG: print('   undecorating',m)
                mm = getattr(ff, m)
                if isinstance(mm, types.FunctionType):
                    mm = undecorate_function(mm)
                    setattr(ff, m, mm)


