﻿import config as cf
import model
import csv
from DISClib.ADT import list as lt

# Inicialización de los Catálogos


def initCatalogVideos():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog


def initCatalogCategories():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    category = model.newCategory()
    return category

# Funciones para la carga de datos


def loadDataVideos(catalog):
    """
    Carga los archivos y los datos en la estructura de datos
    """
    catalogList = loadVideos(catalog)
    return catalogList


def loadDataCategories(categories):
    """
    Carga los archivos y los datos en la estructura de datos
    """
    categoryList = loadCategory(categories)
    return categoryList


def loadVideos(catalog):
    videosfile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    catalogList = model.newCatalogList()
    for video in input_file:
        cg = model.addVideoInfo(catalog, video)
        model.addVideo(catalogList, cg)

    return catalogList


def loadCategory(catalog):
    categoriesfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(categoriesfile, encoding='utf-8'),
                                delimiter='\t')
    categoryList = model.newCategoryList()
    for category in input_file:
        cl = model.addCategoryInfo(catalog, category)
        model.addCategory(categoryList, cl)

    return categoryList


def loadDays(catalog):

    catalogDays = model.loadDays(catalog)

    i = 0
    while i < lt.size(catalogDays):

        model.addDays(catalog, catalogDays['elements'][i])
        i += 1

# Funciones de ordenamiento


def sortVideos(categoryList, catalogList, category_name, country, size):
    return model.sortVideos(categoryList, catalogList, category_name,
                            country, size)


def sortVideosCountry(catalogList, country):
    return model.sortVideosCountry(catalogList, country)


def sortVideosCategory(categoryList, catalogList, category_name):
    return model.sortVideosCategory(categoryList, catalogList, category_name)


def sortVideosTags(catalogList, tag, country):
    return model.sortVideosTags(catalogList, tag, country)

# Funciones de consulta sobre el catálogo
