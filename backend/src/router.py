from contextlib import asynccontextmanager
from fastapi import APIRouter, FastAPI
from .http_client import CMCHTTPClient
from .config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    global cmc_client
    cmc_client = CMCHTTPClient(
        base_url="https://pro-api.coinmarketcap.com",
        api_key=settings.CMC_API_KEY
        )
    yield
    await cmc_client._session.close()


router = APIRouter(
    prefix='/cryptocurrencies',
    lifespan=lifespan
)

@router.get("")
async def get_cryptocurrencies():
    return await cmc_client.get_listings()


@router.get("/{currency_id}")
async def get_cryptocurrency(currency_id: int):
    return await cmc_client.get_currency(currency_id)
