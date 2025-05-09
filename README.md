# Internet Prices

This repo contains code for plotting the price of home internet subscriptions over time.
Currently, it is focussed on Switzerland.

For each speed, only the lowest known base price (at that point in time) is included.
Reductions from the base price are not considered (temporary promotions, combining home internet with a mobile subscription, ...).

Note that price is only one factor when choosing your internet.
E.g., you may want to consider:
the physical architecture (P2P/AON vs. P2MP/PON),
the backhaul capacity of the POP you are connected to,
the connectivity of the ISP towards other ASes (good peering and internet exchange capacity),
or the quality of customer support.

Please let me know if there is any data that I missed!

## Usage

```bash
# Setup
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt

# Use
python3 plot.py
```

## License

This repo is published under the [MIT License][LICENSE].
