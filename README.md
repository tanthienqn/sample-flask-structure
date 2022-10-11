

Infrastrure folder:
```
├── run.py 						        run project
├── server 						        folder server app
│   ├── app.py 					      init app and 3rd app
│   ├── extensions.py 			  store all connect 3rd app: db, storage
│   ├── config.py 				    config env
│   ├── constants 				    store constant variable
│   │   ├── FormatReturn.py 	store format to return api (now support single object and list objects with pagtination)
│   │   ├── ErrorMessage.py 	store error code to handle error
│   ├── utils					        store functions that are used many times
│   ├── controllers 			    store controller layer
│   │   ├── VQCcontroller.py  store route API for business VQC
│   ├── services 				      store service layer
│   │   ├── BaseService.py    base service
│   │   ├── VQCService.py     store fuctions for business VQC
│   ├── models 					      store model layer
│   ├── middlewares 			    store middleware layer
│   │   ├── Authority.py 		  store functions to check authen
│   │   ├── HandleError.py 		store functions to handle output error api
│   │   ├── HandleSuccess.py 	store functions to handle output success api
```
