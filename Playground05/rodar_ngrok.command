#!/bin/bash
cd "$(dirname "$0")"

cd extra/binarios/ngrok/mac

./ngrok authtoken 2EfqmJJC7tZQx0a555cVehvuymt_E3tvShD9gRnGmZp2tYfV

./ngrok http 5000
