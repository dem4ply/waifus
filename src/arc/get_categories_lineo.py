#!/usr/bin/env python
from bs4 import BeautifulSoup
from urllib import parse
import requests
from selenium.webdriver.firefox.webdriver import WebDriver

#firefox = WebDriver()


def get_absoute_url( parent, url ):
    return parse.urljoin( parent, url )

def get_soup( url ):
    try:
        html = requests.get( url, headers={
        } ).text
        soup = BeautifulSoup( html, 'html.parser'  )
    except Exception as e:
        print( e )
        print( url )
    return soup

def get_categories_parents():
    url_directory = "https://www.linio.com.mx/directorio"
    page = get_soup( url_directory )
    categories = page.find_all( 'a', { 'class': 'category-link' } )
    categories = filter( lambda x: x.text not in ( 'Moda', 'Viajes', 'Tiendas Oficiales' ),
                         categories )
    categories = { cat.text: get_absoute_url( url_directory, cat.get( 'href' ) )
                   for cat in categories }
    return categories

def get_first_subcategory( cat, url ):
    page = get_soup( url )
    banners = page.find_all( 'div', { 'class': 'cms-banner-menu' } )
    for banner in banners:
        links = banner.find_all( 'a' )
        for link in links:
            if link.has_attr( 'href' ):
                return link.get( 'href' )

def get_all_categories( url ):
    page = get_soup( url )
    categories = page.find( 'ul', { 'class': 'sidebar-category-tree list-unstyled' } )
    li = categories.find_all( 'li', recursive=False )
    result = {}
    for item in li:
        sub_list = item.find( 'ul' )
        if sub_list:
            sub_list.replace_with( '' )
        link = item.find_next( 'a' )
        link.find( 'span' ).replace_with( '' )
        result[ link.text.strip() ] = get_absoute_url( url, link.get( 'href' ) )
    return result

def extract_sub_categorie( categories ):
    li = categories.find_all( 'li', recursive=False )
    result = {}
    for item in li:
        sub_list = item.find( 'ul' )
        if sub_list:
            sub_list.replace_with( '' )
        link = item.find_next( 'a' )
        link.find( 'span' ).replace_with( '' )
        result[ link.text.strip() ] = get_absoute_url( url, link.get( 'href' ) )
    return result


def get_subcategorie( page ):
    if page:
        return page.find( 'ul', { 'class': 'sidebar-category-tree list-unstyled' } )

#from pprint import pprint as print
import json

def extract_articles( page, parent ):
    grid_articles = page.find( 'div', { 'class': 'products-collection grid-view' } )
    articles = grid_articles.find_all( 'div', recursive=False )
    list_links_articles = []
    for article in articles:
        link = article.find( 'a' )
        link = link.get( 'href' )
        list_links_articles.append( get_absoute_url( parent, link ) )
    #subcategories[ sub_cat ] = { 'url': url, 'articles': list_links_articles }
    return list_links_articles

if __name__ == '__main__':
    categories = get_categories_parents()
    for cat, url in categories.items():
        firts_subcategorie = get_first_subcategory( cat, url )
        all_categories = get_all_categories( firts_subcategorie )
        categories[ cat ] = { 'sub_categories': all_categories, 'url': url }
    for cat, value in categories.items():
        subcategories = value[ 'sub_categories' ]
        for sub_cat, url in subcategories.items():
            page = get_soup( url )
            sub = get_subcategorie( page )
            sub = get_subcategorie( sub )
            if sub:
                sub_sub_categories = extract_sub_categorie( sub )
                subcategories[ sub_cat ] = {
                        'url': url,
                        'sub_categories': sub_sub_categories }
                for sub_sub, sub_url in sub_sub_categories.items():
                    page = get_soup( sub_url )
                    sub = get_subcategorie( page )
                    sub = get_subcategorie( sub )
                    sub = get_subcategorie( sub )
                    if sub:
                        sub_sub_sub = extract_sub_categorie( sub )
                        sub_sub_categories[ sub_sub ] = {
                                'url': url,
                                'sub_categories': sub_sub_sub }
                        for sub_sub_cat, url in sub_sub_sub.items():
                            page = get_soup( sub_url )
                            sub = get_subcategorie( page )
                            sub = get_subcategorie( sub )
                            sub = get_subcategorie( sub )
                            sub = get_subcategorie( sub )
                            if sub:
                                import pdb
                                pdb.set_trace()

                            print( cat, '>', sub_cat, '>', sub_sub, '>', sub_sub_cat)
                            list_articles = extract_articles( page, url )
                            sub_sub_sub[ sub_sub_cat ] = {
                                    'url': url,
                                    'articles': list_articles, }
                        continue
                    print( cat, '>', sub_cat, '>', sub_sub )
                    list_articles = extract_articles( page, url )
                    if isinstance( sub_sub_categories[ sub_sub ], dict ):
                        sub_sub_categories[ sub_sub ][ 'articles' ] = list_articles
                    else:
                        sub_sub_categories[ sub_sub ] = {
                                'url': url,
                                'articles': list_articles }
                continue
            print( cat, '>', sub_cat )
            list_articles = extract_articles( page, url )
            if isinstance( subcategories[ sub_cat ], dict ):
                subcategories[ sub_cat ][ 'articles' ] = list_articles
            else:
                subcategories[ sub_cat ] = { 'url': url, 'articles': list_articles }
    result_json = open( 'result.json', 'w')
    json.dump( categories, result_json )



