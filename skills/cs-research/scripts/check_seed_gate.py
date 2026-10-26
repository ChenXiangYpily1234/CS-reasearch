"""Compute the strict seed-42 metric gate; never launch training."""
import argparse
import json
from decimal import Decimal, InvalidOperation, localcontext


def qualifies(candidate, competitor, direction, minimum_improvement="0"):
    if direction not in ("maximize", "minimize"):
        raise ValueError("direction must be maximize or minimize")
    try:
        values = [Decimal(str(v)) for v in (candidate, competitor, minimum_improvement)]
    except InvalidOperation as exc:
        raise ValueError("scores and threshold must be finite decimal numbers") from exc
    if not all(v.is_finite() for v in values):
        raise ValueError("scores and threshold must be finite decimal numbers")
    candidate, competitor, threshold = values
    if threshold < 0:
        raise ValueError("minimum improvement cannot be negative")
    # Preserve the supplied decimal precision at a strict threshold boundary.
    with localcontext() as ctx:
        ctx.prec = max(28, max(v.adjusted() for v in values) - min(v.as_tuple().exponent for v in values) + 3)
        improvement = candidate - competitor if direction == "maximize" else competitor - candidate
        return improvement > threshold


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", required=True)
    parser.add_argument("--competitor", required=True)
    parser.add_argument("--direction", choices=("maximize", "minimize"), required=True)
    parser.add_argument("--minimum-improvement", default="0")
    args = parser.parse_args()
    try:
        eligible = qualifies(args.candidate, args.competitor, args.direction, args.minimum_improvement)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps({"eligible_seed_42": eligible, "decision": "ELIGIBLE" if eligible else "STOPPED_AFTER_41"}))


if __name__ == "__main__":
    main()
