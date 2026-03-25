import { apiClient } from '../client';

describe('apiClient', () => {
  beforeEach(() => {
    vi.stubGlobal(
      'fetch',
      vi.fn(() =>
        Promise.resolve({
          ok: true,
          json: () => Promise.resolve({ success: true }),
        }),
      ) as unknown as typeof fetch,
    );
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  it('calls fetch with the correct URL', async () => {
    await apiClient('/api/v1/health');

    expect(fetch).toHaveBeenCalledWith(
      expect.stringContaining('/api/v1/health'),
      expect.any(Object),
    );
  });

  it('sets Content-Type to application/json by default', async () => {
    await apiClient('/test');

    expect(fetch).toHaveBeenCalledWith(
      expect.any(String),
      expect.objectContaining({
        headers: expect.objectContaining({ 'Content-Type': 'application/json' }),
      }),
    );
  });

  it('allows custom headers to override defaults', async () => {
    await apiClient('/test', {
      headers: { Authorization: 'Bearer token' },
    });

    // options spread comes after the headers merge, so options.headers overwrites
    expect(fetch).toHaveBeenCalledWith(
      expect.any(String),
      expect.objectContaining({
        headers: expect.objectContaining({
          Authorization: 'Bearer token',
        }),
      }),
    );
  });

  it('returns the parsed JSON body on success', async () => {
    const data = await apiClient<{ success: boolean }>('/test');
    expect(data).toEqual({ success: true });
  });

  it('throws an error when the response is not ok', async () => {
    vi.stubGlobal(
      'fetch',
      vi.fn(() =>
        Promise.resolve({
          ok: false,
          status: 500,
          json: () => Promise.resolve({}),
        }),
      ) as unknown as typeof fetch,
    );

    await expect(apiClient('/fail')).rejects.toThrow('API error: 500');
  });

  it('forwards request options to fetch', async () => {
    await apiClient('/test', { method: 'POST', body: JSON.stringify({ a: 1 }) });

    expect(fetch).toHaveBeenCalledWith(
      expect.any(String),
      expect.objectContaining({
        method: 'POST',
        body: JSON.stringify({ a: 1 }),
      }),
    );
  });
});
