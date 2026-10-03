from __future__ import annotations

import asyncio

from graphvest_datapipe.services.demo import run_demo


def main() -> None:
    print(asyncio.run(run_demo()).model_dump_json(indent=2))


if __name__ == "__main__":
    main()
