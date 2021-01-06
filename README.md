# FIDAL (Financial Instrument Data Access Library)

Raw access to various financial data APIs

## Usage

Fetch symbols

```python
import fidal.iex.ref_data.symbols
import fidal.alpaca.assets

iex_symbols = fidal.iex.ref_data.symbols.fetch()
alpaca_symbols = fidal.alpaca.assets.fetch()
```
