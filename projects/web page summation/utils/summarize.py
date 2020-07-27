# -*- coding: utf-8 -*-
# load Dependancies

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import sys


def summarize(url=None, LANGUAGE='English', SENTENCES_COUNT=2):
        parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
        # or for plain text files
        # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        result = ''
        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            result = result + ' ' + str(sentence)
            try:
                result = result + ' ' + str(sentence)

            except:
                print(
                    '\n\n Invalid Entry!, please Ensure you enter a valid web link \n\n')
                sys.stdout.flush()
                return (
                    '\n\n Invalid Entry!, please Ensure you enter a valid web link \n\n')
        print('\n\n'+str(url)+'\n\n'+str(result))
        sys.stdout.flush()
        return result
