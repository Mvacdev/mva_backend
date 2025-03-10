import json
import os
import re
import sys

import requests
from rest_framework import status, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import DataHistorySerializer, PotentialFranchiseSerializer


class DataHistoryAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = DataHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PotentialFranchiseAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = PotentialFranchiseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchCarsAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: Request):
        return self.handle_request(
            auto_mark=request.query_params.get('auto_mark'),
            auto_model=request.query_params.get('auto_model'),
            auto_year=request.query_params.get('auto_year'),
            auto_km=request.query_params.get('auto_km')
        )

    def post(self, request: Request):
        data = request.data
        return self.handle_request(
            auto_mark=data.get('auto_mark'),
            auto_model=data.get('auto_model'),
            auto_year=data.get('auto_year'),
            auto_km=data.get('auto_km')
        )

    def handle_request(self, auto_mark, auto_model, auto_year, auto_km):
        try:
            if not all([auto_mark, auto_model, auto_year, auto_km]):
                return Response({"error": "Missing parameters"}, status=status.HTTP_400_BAD_REQUEST)

            result = self.search_cars(auto_mark, auto_model, auto_year, auto_km)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            exc_type, _, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            return Response(
                {"error": [str(e), str(exc_type), str(fname), str(exc_tb.tb_lineno)]},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def search_cars(self, auto_mark, auto_model, auto_year, auto_km):
        # PATH = os.path.dirname(os.path.abspath(__file__))
        # date_file = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p").replace(":", "-")

        # RESULT_FOLDER = "PARSE_CARS_occasion_largus"
        # FILE_LOG_RES = f"{auto_mark}_{auto_model}_{auto_year}_{auto_km}_LOG_{date_file}.log"
        # FILE_LOG_RES_ERROR = f"{auto_mark}_{auto_model}_{auto_year}_{auto_km}_LOG_ERROR_{date_file}.log"

        # PATH_RESULT_FILE = os.path.join(PATH, RESULT_FOLDER)
        # os.makedirs(PATH_RESULT_FILE, exist_ok=True)

        # PATH_SAVE = os.path.join(PATH_RESULT_FILE, "")

        res_cars = []
        res_lacentrale = {}

        # cookies = {
        #     "datadome": "qwRRFd3HdMPuXWO6w8dHAR8uY~J2GR7a7f4hd1HglmkAr4AIHjkphi_BmINomOpLEAycXPzaa8UWo9dBfG3D9e~Bbo47iNOarSImB5KX~~CO_NEDhg6OzRFlZyJovFc1",
        # }
        #
        # headers = {
        #     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        #     "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        # }
        cookies = {
            'datadome': 'qwRRFd3HdMPuXWO6w8dHAR8uY~J2GR7a7f4hd1HglmkAr4AIHjkphi_BmINomOpLEAycXPzaa8UWo9dBfG3D9e~Bbo47iNOarSImB5KX~~CO_NEDhg6OzRFlZyJovFc1',
        }

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # 'priority': 'u=0, i',
            # 'sec-ch-device-memory': '8',
            # 'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            # 'sec-ch-ua-arch': '"x86"',
            # 'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6834.83"',
            # 'sec-ch-ua-mobile': '?0',
            # 'sec-ch-ua-model': '""',
            # 'sec-ch-ua-platform': '"Linux"',
            # 'sec-fetch-dest': 'document',
            # 'sec-fetch-mode': 'navigate',
            # 'sec-fetch-site': 'none',
            # 'sec-fetch-user': '?1',
            # 'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            # 'user-agent': random.choice(user_agent_list),
        }

        params = {
            "km[max]": str(int(auto_km) + 15000),
            "km[min]": str(int(auto_km) - 15000),
            "year[max]": str(int(auto_year) + 1),
            "year[min]": str(int(auto_year) - 1),
        }

        try:
            url = f"https://occasion.largus.fr/auto/{auto_mark}/{auto_model}/"
            response = requests.get(url, params=params, cookies=cookies, headers=headers)

            if response.status_code == 200:
                match = re.search(r'"list_products":\s*(\[\{.*?\}\])', response.text, re.DOTALL)
                if match:
                    list_products_json = match.group(1)
                    try:
                        list_products = json.loads(list_products_json)
                        for car in list_products:
                            res_cars.append({
                                "car_name": car["list_product_name"],
                                "car_price": car["list_product_unitprice_ati"],
                                "car_url": "https://occasion.largus.fr" + car["list_product_url_page"],
                            })
                        prices = [int(car["car_price"]) for car in res_cars[:10]]
                        if prices:
                            res_lacentrale["average_price"] = sum(prices) / len(prices)
                            res_lacentrale["cars"] = res_cars[:10]
                            return res_lacentrale
                        else:
                            return {"error": "No cars found."}
                    except Exception as e:
                        return {"error": f"Failed to parse list_products JSON. {e}"}
                else:
                    return {"error": "list_products not found in the response."}
            else:
                print(response.text)
                return {"error": f"Failed to fetch data, status code: {response.status_code}"}
        except Exception as e:
            return {"error": str(e)}


# def index(request):
#     return render(request, 'form.html')


# def index_1(request):
#     return render(request, 'form_with_alarm.html')
