#!/usr/bin/env python

from bs4 import BeautifulSoup
from urllib import parse
import requests
from selenium.webdriver.firefox.webdriver import WebDriver
import json
import sys

from get_categories_lineo import get_soup, get_absoute_url


def extract_title( page ):
    return page.h1.text

def extract_price( page ):
    result = {}
    spans = page.find( 'div', {
        'class': 'price-bundle padding-medium-bottom'
        } ).find_all('span', recursive=False)
    if len( spans ) == 1:
        result[ 'price' ] = spans[0]
    else:
        result[ 'previous_price' ] = spans[ 0 ]
        result[ 'price' ] = spans[ 2 ]
    return result

def extract_short_descript( page ):
    try:
        descript = page.find( 'div', { 'class': 'short-description' } )
        lis = descript.ul.find_all( 'li' )
        return [ l.text for l in lis ]
    except:
        return [ descript.text.strip() ]

def extract_description( page ):
    descrips = page.find( 'div', { 'id': 'productDetails' } )\
                    .find_all( 'div', recursive=False )
    try:
        spec = descrips[1]
    except:
        spec = descrips[0]
    # pude que no tenga este dato
    try:
        contain_box = spec.find_all( 'table', recursive=False )[ 1 ]
        contain_box = contain_box.text.strip().split( '\n' )
    except Exception:
        contain_box = []
    try:
        spec = spec.table.tbody.find_all( 'tr', recursive=False )
        specs = [ s.text.strip().split( '\n' ) for s in spec ]
    except:
        specs = []

    descriptions = descrips[0].text.strip().split( '\n' )
    descriptions = [ d for d in descriptions if d ]
    return {
        'description': descriptions,
        'features': specs,
        'box_contents': contain_box,
    }

def extract_brand( page ):
    return page.find( 'div', { 'id': 'startZoom' } ).a.text.strip()

def extract_review( page ):
    reviews = page.find(
            'div', { 'id': 'rowrating' } ).div.find_all( 'div',
                                                         recursive=False )
    try:
        clients_reviews = reviews[2].find_all( 'div', recursive=False )[1]\
                                    .find_all( 'div', { 'class': 'customer-review' } )
    except:
        return []
    total = 5
    reviews = []
    for client in clients_reviews:
        puntuation = len( client.span.find_all( 'i', { 'class': 'star active' } ) )
        try:
            data = client.div.div.find_all( 'span' )
            client_name = data[0].text
            date = data[1].text
        except:
            date = data[0].text
            client_name = ''
        review = client.find_all( 'div' )[2].text.strip()

        reviews.append( {
            'score': puntuation,
            'total_score': total,
            'name': client_name,
            'date': date,
            'review': review,
        } )

    return reviews

def extract_article( parent, url ):
    url = get_absoute_url( parent, url )
    page = get_soup( url )

    try:
        title = extract_title( page )
    except:
        return None
    short_description = extract_short_descript( page )
    details = extract_description( page )
    reviews = extract_review( page )
    brand = extract_brand( page )
    return {
        'short_description': short_description,
        'details': details,
        'reviews': reviews,
        'title': title,
        'brand': brand,
    }


def extract_categories( categories, parent=None ):
    result = []
    if parent is None:
        parent = []
    for category, value in categories.items():
        print( parent + [ category ])
        if 'sub_categories' in value:
            tmp_articles = extract_categories( value[ 'sub_categories' ],
                                               parent + [ category ] )
            result.append( tmp_articles )
        if 'articles' in value:
            url_parent = value[ 'url' ]
            for article in value[ 'articles' ]:
                tmp_articles = extract_article( url_parent, article )
                if tmp_articles is None:
                    continue
                tmp_articles[ 'categorie' ] = parent + [ category ]
                result.append( tmp_articles )
    return result




if __name__ == '__main__':
    if len( sys.argv ) >= 2:
        file_name = sys.argv[ 1 ]
    else:
        file_name = 'result.json'
    file_categories = open( file_name )
    categories = json.load( file_categories )
    file_categories.close()

    final = extract_categories( categories )
    articles_file = open( 'articles_result.json', 'w' )
    json.dump( final, articles_file )
    articles_file.close()
