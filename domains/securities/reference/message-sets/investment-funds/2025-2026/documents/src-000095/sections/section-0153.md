---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Portfolio Transfer Management", "Portfolio Transfer Instruction"]
content_origin: "source-transcription"
---

# Portfolio Transfer Instruction

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Portfolio Transfer Management / Portfolio Transfer Instruction.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P768** Portfolio Transfer Instruction

**P769** A transferee (new plan manager or instructing party) sends the AccountHoldingInformationRequest message to the transferor (old plan manager or executing party) to request information about financial instruments held on behalf of the client.

**P770** The transferor responds by sending an AccountHoldingInformation message, specifying the individual products in the portfolio.

**P771** The transferee now instructs the transfer of the portfolio by sending a PortfolioTransferInstruction message to the transferor. This instructs the transfer of the individual products in the portfolio, such as fund units, cash, equities and other assets such as property. For each individual asset, the transferee will instruct one of the following:

**P772** transfer 'as is' (in specie)

**P773** liquidate and transfer as cash

**P774** convert to another instrument and then transfer 'as is' (in specie).

**P775** The transferor sends a PortfolioTransferConfirmation message to confirm its intent to transfer the assets. The actual transfer and confirmation of the individual assets, if fund units, is carried out using the transfer out instruction and confirmation. If the portfolio contains cash, then there will be a payment flow. If an asset is to be liquidated and transferred as cash, there will be a redemption flow and a payment flow.

**P776** Once all individual asset transfers are executed and settled, a PortfolioTransferCompletion message is sent by the transferor, to the transferee, to confirm that the transfer of financial instruments from the client’s account at the transferor to the clients account at the transferee has been completed.

[fig-0108 - original figure evidence](../diagrams/fig-0108.md)

