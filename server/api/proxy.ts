/**
 * Web Proxy API Route
 * Forwards requests to target URLs, useful for bypassing CORS restrictions.
 *
 * Usage:
 *   GET /api/proxy?url=https://api.example.com/data
 *   POST /api/proxy?url=https://api.example.com/data (with JSON body)
 */

export default defineEventHandler(async (event) => {
  const query = getQuery(event)
  const targetUrl = query.url as string

  if (!targetUrl) {
    throw createError({
      statusCode: 400,
      message: 'Missing "url" query parameter'
    })
  }

  const method = event.method

  // Handle CORS preflight
  if (method === 'OPTIONS') {
    setResponseHeaders(event, {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
      'Access-Control-Allow-Headers': '*'
    })
    return null
  }

  try {
    // Get request body for non-GET requests
    let body: any = undefined
    if (method !== 'GET' && method !== 'HEAD') {
      body = await readBody(event)
    }

    // Forward headers (excluding problematic ones)
    const excludedHeaders = ['host', 'connection', 'content-length']
    const headers: Record<string, string> = {}
    const requestHeaders = getHeaders(event)

    for (const [key, value] of Object.entries(requestHeaders)) {
      if (!excludedHeaders.includes(key.toLowerCase()) && value) {
        headers[key] = value as string
      }
    }

    // Build URL with additional query params (excluding 'url')
    const url = new URL(targetUrl)
    for (const [key, value] of Object.entries(query)) {
      if (key !== 'url' && value) {
        url.searchParams.set(key, value as string)
      }
    }

    // Make the request
    const response = await $fetch.raw(url.toString(), {
      method: method as any,
      headers,
      body: body ? JSON.stringify(body) : undefined,
      redirect: 'follow'
    })

    // Set CORS headers on response
    setResponseHeaders(event, {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
      'Access-Control-Allow-Headers': '*'
    })

    return response._data

  } catch (error: any) {
    console.error('Proxy error:', error)

    throw createError({
      statusCode: error.statusCode || 502,
      message: `Proxy error: ${error.message || 'Unknown error'}`
    })
  }
})
