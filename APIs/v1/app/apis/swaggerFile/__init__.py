#!/usr/bin/python3
""" All swagger dec for the endpoints """
from .activationSwagger import activiationDoc
from .signinSwagger import siginDoc
from .siginupSwagger import signuDoc
from .resendSwagger import resendDoc
from .optCodeSwagger import optCodeDoc
from .storeRegistration import createStoreDoc, updateStoreDoc, deleteStoreDoc
from .otpVerifySwagger import verifyDoc
from .passwordResetSwagger import resetDoc
from .accountSwagger import accountDoc
from .accountUpdateSwagger import accountUpdateDoc
from .accountPasswordSwagger import accountUpdatePasswordDoc
from .productSwagger import productDoc
from .productUpdateSwagger import productUpdateDoc
from .productDeleteSwagger import productDeleteDoc
from .storesSwagger import getAllStoresDoc
from .allProductsSwagger import getAllProductsByCategoryDoc
from .storesInfoSwagger import getStoresDoc
from .ordersSwagger import createOrderDoc, updateOrderDoc, deleteOrderDoc
from .ordesInfoSwagger import getAllOrdersDoc, getOrderDoc
