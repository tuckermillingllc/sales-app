"""
Flask Web Proxy Server
Forwards requests to target URLs, useful for bypassing CORS restrictions.
"""

from flask import Flask, request, Response
import requests

app = Flask(__name__)

# Configure allowed headers to forward
EXCLUDED_HEADERS = [
    'content-encoding',
    'content-length',
    'transfer-encoding',
    'connection',
    'host'
]


@app.route('/proxy', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def proxy():
    """
    Proxy endpoint that forwards requests to the target URL.

    Usage:
        GET /proxy?url=https://api.example.com/data
        POST /proxy?url=https://api.example.com/data (with JSON body)
    """
    target_url = request.args.get('url')

    if not target_url:
        return {'error': 'Missing "url" query parameter'}, 400

    # Forward headers (excluding problematic ones)
    headers = {
        key: value for key, value in request.headers
        if key.lower() not in EXCLUDED_HEADERS
    }

    try:
        # Forward the request to the target URL
        resp = requests.request(
            method=request.method,
            url=target_url,
            headers=headers,
            data=request.get_data(),
            params={k: v for k, v in request.args.items() if k != 'url'},
            cookies=request.cookies,
            allow_redirects=False,
            timeout=30
        )

        # Build response headers (excluding problematic ones)
        response_headers = [
            (name, value) for name, value in resp.raw.headers.items()
            if name.lower() not in EXCLUDED_HEADERS
        ]

        # Create response with CORS headers
        response = Response(resp.content, resp.status_code, response_headers)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, PATCH, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = '*'

        return response

    except requests.exceptions.Timeout:
        return {'error': 'Request timed out'}, 504
    except requests.exceptions.RequestException as e:
        return {'error': f'Proxy error: {str(e)}'}, 502


@app.route('/proxy', methods=['OPTIONS'])
def proxy_options():
    """Handle CORS preflight requests."""
    response = Response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, PATCH, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response


@app.route('/health')
def health():
    """Health check endpoint."""
    return {'status': 'ok'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
