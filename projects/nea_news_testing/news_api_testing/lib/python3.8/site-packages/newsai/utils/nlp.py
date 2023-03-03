from typing import Union, Optional, List, Any
import math
from collections import Counter
from itertools import combinations
import pandas as pd
import numpy as np
import re
import nltk
from nltk import ngrams
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from .nlogger import Log

log = Log(__name__)


# stop words/nltk - deprecated

stop_words = set()
lemmatizer = WordNetLemmatizer()
symbol_map = {r"[^A-Za-z0-9^,!?.\/'+]": " ",
              r"\+": " plus ",
              r",": " ",
              r"\.": " ",
              r"!": " ! ",
              r"\?": " ? ",
              # r"'": " ",
              r"\"": " ",
              r":": " : ",
              r"\s{2,}": " "}


def activate_nltk() -> set:
    global stop_words
    nltk.download('wordnet')
    nltk.download('stopwords')
    nltk.download('punkt')
    stop_words = set(stopwords.words('english'))
    return stop_words


def get_non_stop_words(text_data: Union[pd.Series, str]):
    if type(text_data) == pd.Series:
        text_data = series_to_string(text_data)
    non_stop_words = [
        lemmatizer.lemmatize(w)
        for w in re.findall(r'\b\S+\b', text_data.casefold())
        if w not in stop_words]
    return non_stop_words


def get_total_word_count(text_data: Union[pd.Series, str]):
    return len(get_non_stop_words(text_data))


def get_top_n_words(text_data: Union[pd.Series, str],
                    n_top_words: Optional[int] = None, ngram: int = 1):
    """
    we can use xgram variable to specify reocurring words
    """
    non_stop_words = get_non_stop_words(text_data)
    xgram = ngrams(non_stop_words, ngram)
    return Counter(xgram).most_common(10)


def text_to_word_list(text, symb_map: dict = symbol_map):
    text = str(text).lower()

    for k, v in symb_map.items():
        text = re.sub(k, v, text)

    def split_words(text_data):
        return \
            [lemmatizer.lemmatize(w)
             for w in re.findall(r'\b\S+\b', text.lower())
             if w not in stop_words]

    return split_words(text)


#

lowercase_words = ['iPhone', 'iPad']


def find_lowercase_words(string_input: str,
                         lowercase_word: str):
    pos = string_input.find(lowercase_word)
    if pos != -1:
        return (pos, pos+len(lowercase_word))
    else:
        return None


def split_on_uppercase(string_input: str,
                       lowercase_words: List = lowercase_words
                       ) -> List:
    exclusion_positions = []
    for e in lowercase_words:
        exl = find_lowercase_words(string_input, e)
        if exl:
            exclusion_positions.append(
                exl)
    matches = [
        match.span()[0]+1 for match in re.finditer(
            # re.compile(r'([\[a-z0-9][A-Z]|[\[a-zA-Z0-9][A-Z][a-z0-9])'),
            re.compile(r'([\[a-z][A-Z]|[\[A-Z0-9][A-Z][a-z0-9])'),
            string_input)]
    if exclusion_positions:
        for m in matches.copy():
            for e in exclusion_positions:
                if m > e[0] and m < e[1]:
                    matches.remove(m)
    matches.insert(0, 0)
    matches.append(len(string_input))
    out = []
    for i in range(len(matches)-1):
        out.append(string_input[matches[i]: matches[i+1]])
    return out


def series_to_string(text_series: pd.Series):
    return text_series.to_string(index=False).replace("\n", "")


def is_null(val) -> bool:
    # try:
    #     return math.isnan(val)
    # except TypeError:
    #     return False
    return val != val


def remove_null_rows(df: pd.DataFrame, columns: list):
    """
    removes rows with all nulls in the columns specified
    """
    null_rows = (df[columns].isna()).all(axis=1)

    log.warning(f'Removing {df[null_rows].size} rows with nulls')
    return df[~null_rows]


def remove_null_columns(df: pd.DataFrame, headers_to_check: list
                        ) -> pd.DataFrame:
    for h in headers_to_check:
        if len(df[df[h].notna()]) == 0:
            log.info(f'Removing column {h}')
            df = df.drop(columns=h)
    return df


def shift_nulls(df: pd.DataFrame, headers: list,
                _remove_null_columns=True) -> pd.DataFrame:
    """
    shifts column values to the left to occupy nulls e.g.
        H0  H1  H2
    1   nan nan a
    2   nan b   c
    becomes
        H0  H1  H2
    1   a   nan nan
    2   b   c   nan
    and if _remove_null_columns is true we are left with:
        H0  H1
    1   a   nan
    2   b   c 
    """
    df = df.T
    for c in df.columns:
        for k, v in enumerate(headers):
            if not is_null(df[c][v]):
                if k > 0:
                    for i in range(len(headers)):
                        if k+i < len(headers):
                            df[c][i] = df[c][k+i]
                break
    if not _remove_null_columns:
        return df.T
    else:
        return remove_null_columns(df.T, headers)


def list_to_str(inp: list) -> str:
    """
    joins list to string
    """
    return ' ' .join(
        ['' if e != e or type(e) is not str
         else str(e) for e in inp])


def remove_short_sentences(df: pd.DataFrame,
                           columns: list,
                           sentence_length: int = 3) -> pd.DataFrame:
    log.info(f'Removing sentences with a length <= {sentence_length}.')
    for col in columns:
        try:
            short_sentences = (df[col].apply(
                lambda x: len(str(x).split(' '))) <= sentence_length)
            df.loc[short_sentences, col] = np.nan
        except Exception as e:
            log.error(e)
    return df


def truncate_long_sentences(df: pd.Series,
                            sentence_length: int = 100) -> pd.Series:
    log.info(f'Truncating sentences with a length > {sentence_length}.')

    def _truncate_str(any_inp: Any):
        try:
            return ' '.join(any_inp.split(' ')[0:sentence_length])
        except AttributeError:
            return any_inp
    try:
        return df.apply(lambda x: _truncate_str(x))
    except Exception as e:
        log.error(e)


def remove_duplicate_rows(df: pd.DataFrame, columns: List):
    duplicate_rows = df[columns].duplicated()
    log.warning(f'Removing {len(duplicate_rows)} duplicates')
    return df[~duplicate_rows]


def remove_duplicate_columns(df: pd.DataFrame,
                             columnA: str, columnB: str):
    df.loc[df[columnA] == df[columnB], columnB] = np.nan
    return df
