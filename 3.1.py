# Share By @HgAnh_7

import os
import sys
import ast
import random
import zlib
import marshal
import traceback
import base64
import bz2
import re
from pystyle import *
if sys.version_info < (3, 10):
    print("\033[1;91mCài đặt Python Phiên bản = 3.10 hoặc > 3.10 Để Sử dụng Mã này\033[0m")
    sys.exit()

def _rd():
    return "".join(__import__("random").sample(
        [chr(i) for i in range(97, 122)], k=5))


def _rd1():
    return "".join(__import__("random").sample(
        [chr(i) for i in range(97, 122)], k=1))


def rd():
    return "_" + "".join(__import__("random").sample([str(i) for i in range(1, 20)], k=2))


def randomint():
    return "".join(__import__("random").sample([str(i) for i in range(1, 20)], k=2))


def _chrobf(x):
    return ord(x) + 0xFF78FF

def obfstr(v):
    global _join
    global _hexrun
    global obfint
    if v == "":
        return f"''"
    else:
        x = []
        r = list(v)
        for i in range(len(r)):
            x.append(_chrobf(r[i]))
        _str_ = f"(lambda  : (lambda : (lambda : {_join}(( {_list}({_map}({_hexrun}, {x})) )))())())()"
        return _str_

def _byte(v):
    byte_array = bytearray()
    byte_array.extend(v.to_bytes((v.bit_length() + 7) // 8, 'big'))
    return b"enherlyswar/" + byte_array

def obfint(v):
    n = rd()
    if 'bool' in str(type(v)):
        if str(v)=='True':
            return f'(lambda: (lambda {n}: {n} + (lambda : H2SbF7({(1+0x7777)}))())(0) == 1)()'
        else:
            return f'(lambda: (lambda {n}: {n} - (lambda : H2SbF7(({(1+0x7777)} ) ) )())(0) == 1)()'
    else:
        return f'(lambda: c2h6({_byte(int(v))}))()'

def varsobf(v):
    return f"""({(v)}) if bool(bool(bool({(v)}))) < bool(type(int({randomint()})>int({randomint()})<int({randomint()})>int({randomint()}))) and bool(str(str({randomint()})>int({randomint()})<int({randomint()})>int({randomint()}))) > 2 else {v}"""

_join = "h2o"
_lambda = "ᅠ"
_int = "h2so4"
_str = "co2"
_bool = "mol"
_type = "feo2"
_bytes = "feso4"
_vars = "agno3"
_ip = "hno3"
ngoac = "{"
_ngoac = "}"
___import__ = "ch2oh4p2so4"
_movdiv = "h2"
_hexrun = "o2"
_argshexrun = "h2so3"
__print = r"tryᅠ"
__input = r"exceptᅠ"
_eval = "h2o3"
_list = "agno4"
_map = "h3o"
def unicodeobf(x):
    b = []
    for i in x:
        j = ord(i) + 0xFF78FF
        b.append(j)
    return b

def _uni(x):
    return unicodeobf(x)

__bool = rd()
__exx = rd()
_temp = rd()
_temp1 = rd()
_wt = rd()
_exp = rd()

var = fr"""

globals()['{_bool}'] = {varsobf('bool')}
globals()['{_str}'] =  {varsobf('str')}
globals()['{_type}'] =  {varsobf('type')}
globals()['{_int}'] =  {varsobf('int')}
globals()['{_bytes}'] =  {varsobf('bytes')}
globals()['{_vars}'] =  {varsobf('vars')}
globals()['{_movdiv}'] =  {varsobf('callable')}
globals()['{_eval}'] =  {varsobf('eval')}
globals()['{_list}'] =  {varsobf('list')}
globals()['{_map}'] =  {varsobf('map')}
globals()['{___import__}'] =  {varsobf('__import__')}
globals()['tryᅠ'] =  {varsobf('print')}
globals()['exceptᅠ'] =  {varsobf('input')}
def {_join}(herlys,*k):
    if k:
        enherlyswar = '+'
        op = "+"
    else:
        enherlyswar = ''
        op = ''
    globals()['{__exx}'] = {obfint(True)}
    globals()['{_join}'] = {_join}
    globals()['{_str}'] = {_str}
    globals()['herlys'] = herlys
    for globals()['enherlyswar_'] in globals()['herlys']:
        if not {__exx}:globals()['enherlyswar_'] += (lambda : '')()
        enherlyswar += {_str}(enherlyswar_);f = {obfint(True)}
    return enherlyswar
def H2SbF7(x):
    return {_int}(x-0x7777)
def c2h6(e):
    br = bytearray(e[len(b"enherlyswar/"):])
    r = 0
    for b in br:
        r = r * 256 + b
    return r
def longlongint(x):
    ar = []
    for i in x:
        ar.append({_eval}(i))
    return ar
if {obfint(True)}:
    def {_hexrun}({_argshexrun}):
        {_argshexrun} = {_argshexrun}-0xFF78FF
        if {_argshexrun} <= 0x7F:
                    return {_str}({_bytes}([{_argshexrun}]),"utf8")
        elif {_argshexrun} <= 0x7FF:
                    if 1<2:
                            b1 = 0xC0 | ({_argshexrun} >> 6)
                    b2 = 0x80 | ({_argshexrun} & 0x3F)
                    return {_str}({_bytes}([b1, b2]),"utf8")
        elif {_argshexrun} <= 0xFFFF:
                b1 = 0xE0 | ({_argshexrun} >> 12)
                if 2>1:
                    b2 = 0x80 | (({_argshexrun} >> 6) & 0x3F)
                b3 = 0x80 | ({_argshexrun} & 0x3F)
                return {_str}({_bytes}([b1, b2, b3]),"utf8")
        else:
            b1 = 0xF0 | ({_argshexrun} >> 18)
            if 2==2:
                b2 = 0x80 | (({_argshexrun} >> 12) & 0x3F)
            if 1<2<3:
                b3 = 0x80 | (({_argshexrun} >> 6) & 0x3F)
            b4 = 0x80 | ({_argshexrun} & 0x3F)
            return {_str}({_bytes}([b1, b2, b3, b4]),"utf8")
    def _hex(j):
        {_argshexrun} = ''
        for _hex in j:
            {_argshexrun} += ({_hexrun}(_hex))
        return {_argshexrun}
else:"enherlyswar"
"""

def _moreobf(tree):
    def rd():
        return str(random.randint(0x1E000000000, 0x7E000000000))

    def junk(en, max_value):
        cases = []
        line = max_value + 1
        for i in range(random.randint(1, 5)):
            case_name = "__"+rd()
            case_body = [
                ast.If(
                    test=ast.Compare(
                        left=ast.Subscript(
                            value=ast.Attribute(
                                value=ast.Name(id=en), 
                                attr='args'
                            ), 
                            slice=ast.Constant(value=0)
                        ), 
                        ops=[ast.Eq()], 
                        comparators=[ast.Constant(value=line)]
                    ), 
                    body=[
                        ast.Assign(
                            targets=[ast.Name(id=case_name)], 
                            value=ast.Constant(value=random.randint(0xFFFFF, 0xFFFFFFFFFFFF)), 
                            lineno=None
                        )
                    ], 
                    orelse=[]
                )
            ]
            cases.extend(case_body)
            line += 1
        return cases

    def bl(body):
        var = "__"+rd()
        en = "__"+rd()
        tb = [
            ast.AugAssign(
                target=ast.Name(id=var), 
                op=ast.Add(), 
                value=ast.Constant(value=1)
            ),
            ast.Try(
                body=[
                    ast.Raise(
                        exc=ast.Call(func=ast.Name(id='MemoryError'), 
                                     args=[ast.Name(id=var)], 
                                     keywords=[])
                    )
                ],
                handlers=[
                    ast.ExceptHandler(
                        type=ast.Name(id='MemoryError'), 
                        name=en, 
                        body=[]
                    )
                ],
                orelse=[],
                finalbody=[]
            )
        ]
        for i in body:
            tb[1].handlers[0].body.append(
                ast.If(
                    test=ast.Compare(
                        left=ast.Subscript(
                            value=ast.Attribute(
                                value=ast.Name(id=en), 
                                attr='args'
                            ), 
                            slice=ast.Constant(value=0)
                        ), 
                        ops=[ast.Eq()], 
                        comparators=[ast.Constant(value=1)]
                    ), 
                    body=[i], 
                    orelse=[]
                )
            )
        tb[1].handlers[0].body.extend(junk(en, len(body) + 1))
        node = ast.Assign(
            targets=[ast.Name(id=var)], 
            value=ast.Constant(value=0), 
            lineno=None
        )
        return [node] + tb

    def _bl(node):
        olb = node.body
        var = "__"+rd()
        en = "__"+rd()
        tb = [
            ast.AugAssign(
                target=ast.Name(id=var), 
                op=ast.Add(), 
                value=ast.Constant(value=1)
            ),
            ast.Try(
                body=[
                    ast.Raise(
                        exc=ast.Call(func=ast.Name(id='MemoryError'), 
                                     args=[ast.Name(id=var)], 
                                     keywords=[])
                    )
                ],
                handlers=[
                    ast.ExceptHandler(
                        type=ast.Name(id='MemoryError'), 
                        name=en, 
                        body=[]
                    )
                ],
                orelse=[],
                finalbody=[]
            )
        ]
        for i in olb:
            tb[1].handlers[0].body.append(
                ast.If(
                    test=ast.Compare(
                        left=ast.Subscript(
                            value=ast.Attribute(
                                value=ast.Name(id=en), 
                                attr='args'
                            ), 
                            slice=ast.Constant(value=0)
                        ), 
                        ops=[ast.Eq()], 
                        comparators=[ast.Constant(value=1)]
                    ), 
                    body=[i], 
                    orelse=[]
                )
            )
        tb[1].handlers[0].body.extend(junk(en, len(olb) + 1))
        node.body = [
            ast.Assign(
                targets=[ast.Name(id=var)], 
                value=ast.Constant(value=0), 
                lineno=None
            )
        ] + tb
        return node

    def on(node):
        if isinstance(node, ast.FunctionDef):
            return _bl(node)
        return node
    nb = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            nb.append(on(node))
        elif isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
            nb.extend(bl([node]))
        elif isinstance(node, ast.Expr):
            nb.extend(bl([node]))
        else:
            nb.append(node)
    tree.body = nb
    return tree

def __moreobf(x):
    return ast.unparse(_moreobf(ast.parse(x)))

def fm(node: ast.JoinedStr) -> ast.Call:
    return ast.Call(
        func=ast.Attribute(
            value=ast.Constant(value="{}" * len(node.values)),
            attr="format",
            ctx=ast.Load(),
        ),
        args=[
            value.value if isinstance(value, ast.FormattedValue) else value
            for value in node.values
        ],
        keywords=[],
    )

def _syntax(x):
    def v(node):
        if node.name:
            for statement in node.body:
                ten = ast.Try(
                    body=[ast.parse(f"{_eval}('0/0')"),ast.parse(f"""if "quanhau" == "deptrai":{rd()},{rd()},{rd()},{rd()}\nelse:pass""")],
                    handlers=[
                        ast.ExceptHandler(
                            type=ast.Name(id='ZeroDivisionError', ctx=ast.Load()),
                            name=None,
                            body=[z(statement)]
                        )
                    ],
                    orelse=[],
                    finalbody=[]
                )
                node.body[node.body.index(statement)] = ten
            return node

    def z(statement):
        return ast.Try(
            body=[ast.parse(f"{_eval}('0/0')")],
            handlers=[
                ast.ExceptHandler(
                    type=ast.Name(id='ZeroDivisionError', ctx=ast.Load()),
                    name=None,
                    body=[statement]
                )
            ],
            orelse=[ast.Pass()],
            finalbody=[ast.parse("str(100)")]
        )
    tree = ast.parse(x)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            v(node)
    st = ast.unparse(tree)
    return st

def obfuscate(node):
    for i in ast.walk(node):
        if isinstance(i, ast.Global):
            continue
        for f, v in ast.iter_fields(i):
            if isinstance(v, list):
                ar = []
                for j in v:
                    try:
                        if isinstance(j, ast.Constant) and isinstance(j.value, str):
                            ar.append(ast.parse(obfstr(j.value)).body[0].value)
                        elif isinstance(j, ast.Constant) and isinstance(j.value, int):
                            ar.append(ast.parse(obfint(j.value)).body[0].value)
                        elif isinstance(j, ast.JoinedStr):
                            ar.append(fm(j))
                        elif isinstance(j, ast.AST):
                            ar.append(j)
                    except Exception as e:
                        print(f"Error processing node {j}: {e}")
                        ar.append(j)
                setattr(i, f, ar)
            else:
                try:
                    if isinstance(v, ast.Constant) and isinstance(v.value, str):
                        setattr(i, f, ast.parse(obfstr(v.value)).body[0].value)
                    elif isinstance(v, ast.Constant) and isinstance(v.value, int):
                        setattr(i, f, ast.parse(obfint(v.value)).body[0].value)
                    elif isinstance(v, ast.JoinedStr):
                        setattr(i, f, fm(v))
                except Exception as e:
                    print(f"Error processing field {f} with value {v}: {e}")

def rename_function(node, ol, nn):
    for i in ast.walk(node):
        if isinstance(i, ast.FunctionDef) and i.name == ol:
            i.name = nn
        elif isinstance(i, ast.Attribute) and isinstance(i.value, ast.Name) and i.value.id == ol:
            i.value.id = nn
        elif isinstance(i, ast.Call) and isinstance(i.func, ast.Name) and i.func.id == ol:
            i.func.id = nn
        elif isinstance(i, ast.Name) and i.id == ol:
            i.id = nn
    return node

def random_match_case():
    var1 = ast.Constant(value=randomint(), kind=None)
    var2 = ast.Constant(value=randomint(), kind=None)
    return ast.Match(
        subject=ast.Compare(
            left=var1,
            ops=[ast.Eq()],
            comparators=[var2],
        ),
        cases=[
            ast.match_case(
                pattern=ast.MatchValue(value=ast.Constant(value=True, kind=None)),
                body=[
                    ast.Assign(
                        lineno=0,
                        col_offset=0,
                        targets=[],
                        value=[ast.Raise(
                    exc=ast.Call(
                        func=ast.Name(id="MemoryError", ctx=ast.Load()),
                        args=[],
                        keywords=[ast.Str(s=[True])],
                    ),)],
                    )
                ],
            ),
            ast.match_case(
                pattern=ast.MatchValue(value=ast.Constant(value=False, kind=None)),
                body=[
                    ast.Assign(
                        lineno=0,
                        col_offset=0,
                        targets=[ast.Name(id=rd(), ctx=ast.Store())],
                        value=ast.Constant(value=[[True], [False]], kind=None),
                    ),
                    ast.Expr(
                        lineno=0,
                        col_offset=0,
                        value=ast.Call(
                            func=ast.Name(id=_str, ctx=ast.Load()),
                            args=[ast.Constant(value=[rd()], kind=None)],
                            keywords=[],
                        ),
                    ),
                ],
            ),
        ],
    )

def trycatch(body, loop):
    ar = []
    for x in body:
        j = x
        for _ in range(1): 
            j = ast.Try(
                body=[random_match_case(),

                ],
                handlers=[
                    ast.ExceptHandler(
                        type=ast.Name(id="MemoryError", ctx=ast.Load()),
                        name=rd(),
                        body=[j],
                    )
                ],
                orelse=[],
                finalbody=[],
            )
            j.body.append(
                ast.Raise(
                    exc=ast.Call(
                        func=ast.Name(id="MemoryError", ctx=ast.Load()),
                        args=[],
                        keywords=[ast.Str(s=[True])],
                    ),
                    cause=None,
                )
            )
        ar.append(j)
    return ar

def obf(code):
    def ps(x):
        return ast.parse(x)
    code = rename_function(ps(code),"print",__print)
    code = rename_function(ps(code),"input",__input)
    tree = ps(code)
    obfuscate(tree)
    tbd = trycatch(tree.body, 1)
    def ast_to_code(node):
        return ast.unparse(node)
    j = ast_to_code(tbd)
    return j

print("\033[1;97m╔═══════════════════════╗")         
print("║ \033[1;96mCông Cụ Mã Hóa PYTHON \033[97m║")
print("╚═══════════════════════╝")
print("""
ENHERLYS OBFUSCATOR
AST MẠNH MẼ
CHUỖI SỬ DỤNG BIỂU THỨC LAMBDA
INT VÀ BOOL SỬ DỤNG BIỂU THỨC TENARY
THỬ CATCH, MATCH CASE [THÊM RÁC VAR VÀ HÀM KHÔNG XÁC ĐỊNH]

CHỐNG HOOKING: BLOCK HOOKING
BIÊN DỊCH: VỚI MARSHAL(TRÌNH BIÊN DỊCH KHÁC PYC), ZLIB, BZ2, BASE64

\033[97m[\033[96m*\033[97m] \033[1;96mCHẾ ĐỘ 1\033[97m: \033[1;32mOBF THẤP \033[1;97m(DÀNH CHO TẤT CẢ TỆP) (DỄ DÀNG ĐẾN DEOBF)
\033[97m[\033[96m*\033[97m] \033[1;96mCHẾ ĐỘ 2\033[97m: \033[1;32mTRUNG BÌNH \033[1;97m(LỰA CHỌN TỐT NHẤT) (CHUỖI ĐẦY ĐỦ, INT, OBF BOOL)
\033[97m[\033[96m*\033[97m] \033[1;96mCHẾ ĐỘ 3\033[97m: \033[1;32mCAO \033[1;97m(KHÔNG KHUYẾN NGHỊ) (ĐÂY LÀ CHẾ ĐỘ TRUNG BÌNH NHƯNG X2 SPAM)
════════════════════════════════════════════════════════\033[0m
""")

_file = input("\033[97m[\033[96m*\033[97m] \033[1;96mFile cần mã hóa\033[97m:\033[0m ")

while True:
    try:
        with open(_file, "r", encoding="utf8") as file:
            code = file.read()
        break
    except FileNotFoundError:
        _file = input("\033[97m[\033[96m*\033[97m] \033[1;96mNhập Lại Tệp \033[1;32m(không tìm thấy tệp)\033[97m:\033[0m ")
        
while True:
    try:
        mode = int(input("\033[97m[\033[96m*\033[97m] \033[1;96mChọn Chế Độ Mã Hóa\033[97m:\033[0m "))
        if mode < 4:
            break
    except ValueError:
        pass
moreobf = input("\033[97m[\033[96m*\033[97m] \033[1;96mBạn Có Muốn Thêm OBF Không? \033[1;92m(y/n)\033[97m: ")

antidebug = input("\033[97m[\033[96m*\033[97m] \033[1;96mBạn Có Muốn Thêm Chống Gỡ Lỗi Không? \033[1;92m(y/n)\033[97m: ")

method = input("\033[97m[\033[96m*\033[97m] \033[1;96mBạn Có Muốn Biên Dịch Không? \033[1;92m(y/n)\033[97m: ")

check = 0
code = _syntax(code)
if moreobf.upper() == "Y":
    code = __moreobf(code)
    check = 5
checkver = f"""

if '{sys.version[0]+sys.version[1]+sys.version[2]+sys.version[3]}' not in sys.version:
    input("Your python version does not work on this code, please install {sys.version[0]+sys.version[1]+sys.version[2]+sys.version[3]}")
    __import__("sys").exit()
"""

author = "# Share By @HgAnh_7"
anti = r"""
import traceback, marshal

ch = set()
am = {'builtins', '__main__'}

def vv():
    raise MemoryError('>> GOOD LUCK!! DITCUMAY') from None

def cb(fn):
    if callable(fn) and fn.__module__ not in am:
        ch.add(fn.__module__)
        vv()

def ba(fn):
    def hi(*args, **kwargs):
        if args and args[0] in ch:
            vv()
        return fn(*args, **kwargs)
    return hi

def bh():
    stack = traceback.extract_stack()
    for frame in stack[:-2]:
        if frame.filename != __file__:
            vv()

def ck(fn, md):
    if callable(fn) and fn.__module__ != md:
        ch.add(md)
        raise ImportError(f'>> Detect [{fn.__name__}] call [{md}] ! <<') from None

def ic(md, nf):
    module = __import__(md)
    funcs = nf if isinstance(nf, list) else [nf]
    [ck(getattr(module, func, None), md) for func in funcs]

def lf(val, xy):
    return callable(val) and xy and val.__module__ != xy.__name__

def kt(lo):
    if any(lf(val, xy) for val, xy in lo):
        vv()

def ct(md, nf):
    module = __import__(md)
    func = getattr(module, nf, None)
    if func is None:
        vv()
    tg = type(func)
    def cf(func):
        if type(func) != tg:
            vv()
    cf(func)
    return func

def ic_type(md, nf):
    func = ct(md, nf)
    ck(func, md)

def nc():
    __import__('sys').settrace(lambda *args, **keys: None)
    __import__('sys').modules['marshal'] = None
    __import__('sys').modules['marshal'] = type(__import__('sys'))('marshal')
    __import__('sys').modules['marshal'].loads = marshal.loads

def sc():
    nk = {
        'marshal': 'loads'
    }
    [ic_type(md, nf) for md, nf in nk.items()]

    lo = [
        (__import__('marshal').loads, marshal)
    ]
    kt(lo)
    nc()

sc()
bh()
"""
if antidebug.upper() == "Y":
    code = anti+code

for i in range(mode):
    code = obf(code)

if method.upper() != "Y":
    code = var + code
    if check == 5:
        try:
            code = __moreobf(code)
        except:
            code = __moreobf(code)

else:
    if check == 5:
        try:
            code = __moreobf(code)
        except:
            code = __moreobf(code)
    code = code
    code = marshal.dumps(compile(code, "", "exec"))
    code = zlib.compress(code)
    code = bz2.compress(code)
    code = base64.b85encode(code)
    l = len(code)
    part1 = code[: l // 4]
    part2 = code[l // 4: l // 2]
    part3 = code[l // 2: 3 * l // 4]
    part4 = code[3 * l // 4:]
    _f = "for"
    _i = "in"
    _t = rd()
    code = author + var + f"""

def bytecode():
    herlyswar = globals().update
    if True:
        herlyswar({ngoac}**{ngoac} _hex({_uni("en")}): {_temp} {_f} {_temp1}, {_temp} {_i} {_vars}({___import__}(_hex({_uni("marshal")}))).items() if {_movdiv}({_temp}) and {_temp1} == _hex({_uni("loads")}){_ngoac}, **{ngoac}{_temp1}: {_temp} {_f} {_temp1}, {_temp} {_i} {_vars}({___import__}(_hex({_uni("marshal")}))).items() if {_movdiv}({_temp}) and {_temp1} != _hex({_uni("loads")}){_ngoac}{_ngoac})
    else:"herlyswar"
    if 1>2:
        {obfint(3)}
    else:
        herlyswar({ngoac}**{ngoac}_hex({_uni("herlys")}): {_temp} {_f} {_temp1}, {_temp} {_i} {_vars}({___import__}(_hex({_uni("zlib")}))).items() if {_movdiv}({_temp}) and {_temp1} == _hex({_uni("decompress")}){_ngoac}, **{ngoac}{_temp1}: {_temp} {_f} {_temp1}, {_temp} {_i} {_vars}({___import__}(_hex({_uni("zlib")}))).items() if {_movdiv}({_temp}) and {_temp1} != _hex({_uni("decompress")}){_ngoac}{_ngoac})
    herlyswar({ngoac}**{ngoac}_hex({_uni("birth")}): {_temp} {_f} {_temp1}, {_temp} {_i} {_vars}({___import__}(_hex({_uni("bz2")}))).items() if {_movdiv}({_temp}) and {_temp1} == _hex({_uni("decompress")}){_ngoac}, **{ngoac}{_temp1}: {_temp} {_f} {_temp1}, {_temp} {_i} {_vars}({___import__}(_hex({_uni("bz2")}))).items() if {_movdiv}({_temp}) and {_temp1} != _hex({_uni("decompress")}){_ngoac}{_ngoac})
    herlyswar()
    herlyswar({ngoac}**{ngoac}_hex({_uni("_war")}): {_t} {_f} {_temp1}, {_t} {_i} {_vars}({___import__}(_hex({_uni("base64")}))).items() if {_movdiv}({_t}) and {_temp1} == _hex({_uni("b85decode")}){_ngoac}, **{ngoac}{_temp1}: {_t} {_f} {_temp1}, {_t} {_i} {_vars}({___import__}(_hex({_uni("base64")}))).items() if {_movdiv}({_t}) and {_temp1} != _hex({_uni("b85decode")}){_ngoac}{_ngoac})
    herlyswar()
    herlyswar({ngoac}**{ngoac}_hex({_uni("herlyswar")}): {_t} {_f} {_temp1}, {_t} {_i} {_vars}({___import__}(_hex({_uni("builtins")}))).items() if {_movdiv}({_t}) and {_temp1} == _hex({_uni("exec")}){_ngoac}, **{ngoac}{_temp1}: {_t} {_f} {_temp1}, {_t} {_i} {_vars}({___import__}(_hex({_uni("builtins")}))).items() if {_movdiv}({_t}) and {_temp1} != _hex({_uni("eval")}){_ngoac}{_ngoac})
bytecode()

_en  {'  '* 999}={part1}
_herlys  {'  '* 999}={part2}
_birth  {'  '* 999}={part3}
__war  {'  '* 999}={part4}
try:
    herlyswar(
    en(
    herlys(
    birth(
    _war(
    _en+_herlys+_birth+__war)))))
except Exception as e:
    print(e)

"""
open("hganh7-" + _file, "w", encoding="utf8").write(str(code))
print(" Save in", "hganh7-" + _file)
