---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.2 IndividualOrderDetailsReport <IndvOrdrDtlsRpt>", "56.4.3.2.7 OrderStatus <OrdrSts>", "56.4.3.2.7.4 Rejected <Rjctd>", "56.4.3.2.7.4.1 Reason <Rsn>", "56.4.3.2.7.4.1.2 Proprietary <Prtry>"]
file_pages: [4145]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.2.7.4.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4145 to 4145.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4145

```text
CodeName Name Definition
ADEA AfterDeadline Instruction was received after the
Receiver's deadline.
DTRD TradeDate Unrecognised or invalid trade date or
requested trade date or future trade
date.
FEEE FeeOrCommission Unrecognised or invalid fee or
commission.
IEXE SubscriberOrRedeemer Unrecognised or invalid subscriber or
redeemer.
NCRR SettlementAmountCurrency Unrecognised or invalid Settlement
Amount Currency.
PHYS PhysicalSettlement Physical Settlement Impossible.
PLCE PlaceOfTrade Unrecognised or invalid Place of Trade.
SETR SettlementTransaction Unrecognised or invalid Settlement
Transaction.
RTGS RTGSSystem Impossible to use RTGS System.
CASH InvalidCashAccount Cash account is not recognised or
invalid.
DMON InvalidSettlementAmount Unrecognised or invalid settlement
amount.
BMIN BelowMinimumInitialInvestmentAmount Amount of subscription is below the
minimum initial investment amount.
INSU InsufficientCapacity Insufficient capacity.
PRCT PercentageHoldingBreach Percentage holding breach, for example,
PPM rules; taxation rules (ERISA).
BMRA BelowMinimumRedemptionAmount Amount is below the minimum
redemption amount.
BMRV BelowMinimumRetainedAmount Holding will be below the minimum
retained value.
LOCK LockUp Lock-up period is in place.
ILLI AssetsIlliquid Assets are illiquid.
CLOS FundClosed Fund is closed and will not take in any
more investments.
UNSC UnacceptableSwitchCombination Instruction specifies an unacceptable
combination for the financial instruments
in the switch order.
56.4.3.2.7.4.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Rejected reason expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4145 May 2026
```

