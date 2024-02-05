import requests
import pandas as pd
from six import string_types

API_URL="http://api.censusreporter.org/1.0/data/show/{release}?table_ids={table_ids}&geo_ids={geoids}"
SEARCH_API_URL="http://api.censusreporter.org/2.1/full-text/search?type=profile&q={query}"

def _clean_list_arg(arg,default):
    if arg is None:
        arg = default
    if isinstance(arg,string_types):
        arg = [arg]
    return arg

def json_data(tables=None, geoids=None, release='latest'):
    geoids = _clean_list_arg(geoids,'040|01000US')
    tables = _clean_list_arg(tables,'B01001')

    url = API_URL.format(table_ids=','.join(tables).upper(),
                         geoids=','.join(geoids),
                         release=release)

    response = requests.get(url)
    return response.json()

def _prep_data_for_pandas(json_data,include_moe=False):
    """Given a dict of dicts as they come from a Census Reporter API call, set it up to be amenable to pandas.DataFrame.from_dict"""
    result = {}
    for geoid, tables in json_data['data'].items():
        flat = {}
        for table,values in tables.items():
            for kind, columns in values.items():
                if kind == 'estimate':
                    flat.update(columns)
                elif kind == 'error' and include_moe:
                    renamed = dict((k+"_moe",v) for k,v in columns.items())
                    flat.update(renamed)
        result[geoid] = flat
    return result

def _prep_headers_for_pandas(json_data,separator=":", level=None, include_moe=False):
    headers = {}
    for table in json_data['tables']:
        stack = [ None ] * 10 # pretty sure no columns are nested deeper than this.
        for column in sorted(json_data['tables'][table]['columns']):
            col_md = json_data['tables'][table]['columns'][column]
            indent = col_md['indent']
            name = col_md['name'].strip(separator)
            stack[indent] = name
            parts = []
            if indent > 0:
                for i in range(1,indent+1):
                    if stack[i] is not None:
                        parts.append(stack[i].strip(separator))
                name = separator.join(parts)
            if level is None or indent <= level:
                headers[column] = name
                if include_moe:
                    moe_col = '{}_moe'.format(column)
                    headers[moe_col] = "{} (error)".format(name)
    return headers

def search_places(q,sumlevel=None,sumlevels=None):
    url = SEARCH_API_URL.format(query=q)
    resp = requests.get(url)
    j = resp.json()
    if sumlevel is not None:
        sumlevels = [ sumlevel ]
    if sumlevels is not None:
        sumlevels = map(str,sumlevels)
        return map(lambda x: x['sumlevel'] in sumlevels, j['results'])
    else:
        return j['results']

def get_dataframe(tables=None, geoids=None, release='latest',level=None,place_names=True,column_names=True, include_moe=False):
    response = json_data(tables, geoids, release)
    if 'error' in response:
        raise Exception(response['error'])
    df = pd.DataFrame.from_dict(_prep_data_for_pandas(response, include_moe=include_moe),orient='index')
    df = df.reindex(sorted(df.columns), axis=1)
    if column_names or level is not None:
        headers = _prep_headers_for_pandas(response, level=level, include_moe=include_moe)
        if level is not None:
            df = df.loc[:, df.columns.map(lambda x: x in headers)]
            #df = df.loc(lambda x: x in headers,axis=1)
        if column_names:
            df = df.rename(columns=headers)
    if place_names:
        name_frame = pd.DataFrame.from_dict(response['geography'],orient='index')
        df.insert(0, 'name', name_frame.name)
    return df