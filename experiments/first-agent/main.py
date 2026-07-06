import os

import anthropic
from web3 import Web3

SEPOLIA_RPC = "https://ethereum-sepolia-rpc.publicnode.com"
w3 = Web3(Web3.HTTPProvider(SEPOLIA_RPC))


def get_contract_info(address: str) -> dict:
    checksum = Web3.to_checksum_address(address)
    code = w3.eth.get_code(checksum)
    balance_wei = w3.eth.get_balance(checksum)
    return {
        "address": checksum,
        "has_code": len(code) > 0,
        "balance_eth": str(w3.from_wei(balance_wei, "ether")),
    }


TOOLS = [
    {
        "name": "get_contract_info",
        "description": (
            "Reads basic on-chain info about a Sepolia address: whether it has "
            "deployed contract code, and its ETH balance."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "address": {
                    "type": "string",
                    "description": "The address to inspect (0x...)",
                }
            },
            "required": ["address"],
        },
    }
]


def run_agent(user_question: str, address: str) -> str:
    client = anthropic.Anthropic()
    messages = [
        {"role": "user", "content": f"{user_question}\nAddress: {address}"}
    ]

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        tools=TOOLS,
        messages=messages,
    )

    if response.stop_reason == "tool_use":
        tool_use = next(b for b in response.content if b.type == "tool_use")
        result = get_contract_info(**tool_use.input)

        messages.append({"role": "assistant", "content": response.content})
        messages.append(
            {
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": tool_use.id,
                        "content": str(result),
                    }
                ],
            }
        )

        final = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            tools=TOOLS,
            messages=messages,
        )
        return final.content[0].text

    return response.content[0].text


if __name__ == "__main__":
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise SystemExit("Set ANTHROPIC_API_KEY before running this script.")

    weth_sepolia = "0xfFf9976782d46CC05630D1f6eBAb18b2324d6B14"
    answer = run_agent(
        "Check this address and tell me what you find, in plain language.",
        weth_sepolia,
    )
    print(answer)
