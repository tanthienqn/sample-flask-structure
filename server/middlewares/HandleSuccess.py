from server.constants.FormatReturn import TypeReturn

class HandleSuccess:

    __output = {
            "message": "ECT-00000000",
            "status": "OK",
            "statusCode": 200
        }
    __page = 1
    __maxSize = 1000
    __sort = 1
    __propertiesSort = "_id"

    @classmethod
    def pagination(cls, page, maxSize, sort, propertiesSort):
        cls.__page = page
        cls.__maxSize = maxSize
        cls.__sort = sort
        cls.__propertiesSort = propertiesSort

    @classmethod
    def __return_default(cls):
        return cls.__output

    @classmethod
    def __return_msg(cls, msg):
        cls.__output.update({"object": msg})
        return cls.__output

    @classmethod
    def __return_single_model(cls, models):
        data = models.output()
        cls.__output.update({"object":data})
        return cls.__output

    @classmethod
    def __return_pagination_model(cls, list_models, page, maxSize, sort, propertiesSort):
        length = len(list_models)
        data = {
            "page": page,
            "maxSize": maxSize,
            "sort": sort,
            "propertiesSort": propertiesSort
        }
        if length == 0:
            data.update({
                "data": 0,
                "totalElement": 0
            })
        else:
            data.update({
                "data": [model.output() for model in list_models],
                "totalElement": list_models.count()
            })
        cls.__output.update(object=[model.output() for model in list_models])
        return cls.__output

    @classmethod
    def _build_output(cls, code_format, data):
        if code_format == TypeReturn.MSG:
            return cls.__return_msg(data)
        elif code_format == TypeReturn.SINGLE:
            return cls.__return_single_model(data)
        elif code_format == TypeReturn.PAGINATION:
            return  cls.__return_pagination_model(data)
        return cls.__return_default()
