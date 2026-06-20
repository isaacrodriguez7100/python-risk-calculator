# python-risk-calculator

A small Python tool that calculates position sizing and risk exposure. Given the lower and upper limits of a price candle, the calculator outputs values per contract, recommended contract amount, recommended stop loss line, and recommended gain lines based on the ORB (Opening Range Breakout) day-trading strategy.

## Requirements

- Python 3.14+ (no external packages required)

## Usage

Run the script and follow the interactive prompts:

```bash
python Risk_Calculator_ORB.py
```

Example session:
- Input:
  - Lower limit: 100
  - Upper limit: 120
- Output:
  - Stop Loss is: 110.0
  - Value Per Market is: 20.0
  - Sell Gain Line is: 80.0
  - Buy Gain Line is: 140.0
  - Recommended Amount Of Mrkt/S is: 11
  - Recommended Exposure is: 220.0

Notes:
- The script currently accepts integer input; consider using float inputs if you want fractional prices.
- The calculator searches for an integer multiplier near the target risk (default target 220) and reports the closest match.

## Files

- `Risk_Calculator_ORB.py` — main script
- `LICENSE` — MIT License

## Suggestions / Next steps

- Add `requirements.txt` or `pyproject.toml` if you add dependencies.
- Convert the script to accept CLI arguments for non-interactive use.
- Add unit tests and a short example script or sample data.

## License

MIT License — see the `LICENSE` file in this repository.
