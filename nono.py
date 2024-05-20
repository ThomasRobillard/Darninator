import re

nono_words_mapping = {
    '8={1,}D': 'darn',
    r'[a@4][s$]{2,}': 'darn',
    'abortion': 'darnortion',
    'ahole': 'darnhole',
    'aids': 'darns',
    'anal': 'darnal',
    'anus': 'darnus',
    'arse': 'darn',
    'auschwitz': 'darnwitz',
    r'b[o0]{2,}b': 'darn',
    'ball': 'darn',
    r'b[a@4]st[a@4]rd': 'darnard',
    "beaner": 'darner',
    r'b([ie13]+)?[iaoy1@0]*tch': 'darnch',
    'blowjob': 'darnjob',
    r'blow[ ]?me': 'darn me',
    r'bon[3e]r': 'darner',
    r'b[o0]ll[o0]cks': 'darnocks',
    'bukakke': 'darnne',
    'bung': 'darn',
    'butthead': 'darnhead',
    r'butt?h[o0]l[e3]': 'darnhole',
    'buttplug': 'darnplug',
    'c[0o]ck': 'cock',
    r'c[a@4]str[a@4]t[e3]': 'darnate',
    r'ch[i1!]nk': 'darn',
    'chinga': 'darna',
    'chode': 'darne',
    'chonga': 'darna',
    'circlejerk': 'darn',
    r'cl[1i!]t': 'darn',
    r'c[0o]ck': 'darn',
    r'c[o0]{2,}n': 'daarn',
    r'c[o0]{2,}ter': 'darner',
    r'cotton[ -]?pi(ck|c|k)': 'darnage collect',
    'crackhead': 'darnhead',
    'cum': 'darn',
    r'c[uv]n[t7]': 'darnt',
    r'd[i1!](ck|kc)': 'darn',
    'dildo': 'darn',
    r'd[o0]ng': 'darn',
    'douche': 'darn',
    'dyke': 'darn',
    'Ejaculate': 'darn',
    'f3lch': 'darn',
    r'(ph|f)[a@4]+gg?': 'darn',
    'fckn': 'darn',
    'felch': 'darn',
    'fellatio': 'darn',
    'fetish': 'darnish',
    'fgt': 'darnt',
    'foreskin': 'darn',
    r'(ph|f)[uvx]+(ck|q|c|k)': 'darn',
    'fxuxcxk': 'darn',
    r'g[o0]{2,}k': 'darn',
    'goddamn': 'darnam',
    r'golden[ ]?shower': 'darn shower',
    'Gooch': 'darn',
    r'h[o0]m[o0]': 'darno',
    r'h[i1]tl[e3]?r': 'darner',
    'Herpes': 'darn',
    'hooker': 'darn',
    'hymen': 'darn',
    r'inc[e3]st': 'darnest',
    'intercourse': 'darn',
    r'j[i1]gg?[a@4]b[o0]{2,}': 'darnaboo',
    r'j[i1]gg?[a@4]b[o0]{,1}': 'darnabo',
    # need to fix: Right now, this will censor "Japan"
    # 'jap': 'darn',
    r'j([a@4]|[e3]r)k[ ]?[o0]ff': 'darn off',
    'jizz': 'darn',
    r'k[i1!]k[e3]': 'darn',
    r'k[i1!]ll': 'darnify',
    'kkk': 'ddd(darn darn darn)',
    'manshaft': 'darnshaft',
    r'm[a@4]sturb[a@4][i1!]?t[e3]?': 'darn',
    r'm3th': 'darn',
    r'm[i1!]lf': 'darnf',
    'molest': 'darn',
    'molester': 'darn',
    'molestor': 'darn',
    r'n+[i1!]+[gq6]+[e3a@]*r?[s$]*': 'darner',
    r'n[a@4]t?z[i1!]': 'darni',
    r'n[i1!]ppl[e3]': 'darn',
    r'nut[sz]': 'darns',
    r'[o0]rgy': 'darny',
    r'p[e3]+nn?[i1]+[s$5]+': 'darnis',
    r'p[a@4]nt[i1y][e3]?s': 'darnies',
    r'p[e3]d[o0]': 'darno',
    r'p[o0]rn': 'darn',
    r'pr[i1]ck': 'darn',
    r'p[uv]+[s$z]{2,}([i1]+)?[e|y]+': 'darny',
    r'pub[i1]c': "darnic",
    r'qu[e3]{2,}f': 'darnf',
    r'r[a@4]+[i1!]?p[e3]': 'darn',
    r'r[a@4]+[i1l]?p[e3]?[i1!][s$5]t': 'darnist',
    'raghead': 'darn',
    r'r[a@4][i1!]?p[i1!]ng?': 'darning',
    r'r[a@4][i1!]p': 'darn',
    r'r[a@4][i1!]?p[a@4]g[e3]': 'darnage',
    r'r[e3]ctum': 'darnum',
    'reggin': 'darnin',
    r'r[e3]t[a@4]rd': 'darnard',
    r'r[i!1]mj[o0]b': 'darnjob',
    'rimming': 'darn',
    'schlong': 'darn',
    'scrote': 'darn',
    r's[e3](x|cks)': 'darn',
    r'[s$c][e3]+m[e3]n': 'darnen',
    r'[s$5]h[i1\|][t+7]': 'darn',
    r'[s$5]h[a@]r?t': 'darnt',
    r'sk[a@4]nk': 'darnk',
    r'sl[uv]t': 'darnt',
    'taint': 'darn',
    'teabag': 'darn',
    'teebag': 'darn',
    r't[e3][s$]t[i1!]cl[e3]s': 'darnicles',
    r't[i1!]tt?[sz]?': 'darnt',
    'towelhead': 'darn',
    'trannie': 'darnie',
    'tranny': 'darny',
    r'tw[a@4]t': 'darnt',
    r'v[a#4][g6][i1!]n[a@4]': "darna",
    r'(w|vv)h[i1!]t[e3][ -]?p[o0](w|vv)[e3]r': "darn power",
    r'w[e3]t[ ]?b[a@4]ck': 'darnback',
    r'w[a@4]nk': 'darn',
    r'wh[o0]r[e3]': "darnore",
}