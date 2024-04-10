from aiogram import Router


def get_handlers_router() -> Router:
    from . import menu, registration, review

    router = Router()
    router.include_router(registration.router)
    router.include_router(menu.router)
    router.include_router(review.router)

    return router
