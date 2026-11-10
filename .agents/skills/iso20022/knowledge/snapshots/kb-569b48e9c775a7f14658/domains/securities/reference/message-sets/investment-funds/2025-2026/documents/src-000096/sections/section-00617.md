---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.6 TransferStatus <TrfSts>", "34.4.4.6.5 Rejected <Rjctd>", "34.4.4.6.5.1 Reason <Rsn>", "34.4.4.6.5.1.2 Proprietary <Prtry>"]
file_pages: [847]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.6.5.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 847 to 847.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 847

```text
CodeName Name Definition
NCON NotConvertable The two share classes are not part of the
same fund.
ACLO AssetClosed Asset instructed for transfer is closed.
NASS AssetNotSupported Asset does not support reregistration.
NQTY QuantityBelowMinimum Transfer quantity is too small.
BLTR AccountBlockedForTransfer Investment account is blocked due to a
transfer out of investment funds.
COSE AlreadyExecuted Order or transfer has already been
executed and confirmation has been
sent.
ILLI AssetsIlliquid Assets are illiquid.
BMRV BelowMinimumRetainedAmount Holding will be below the minimum
retained value.
DINV DataInvalid Data in the order or transfer instruction is
invalid.
ICAG DeliveringAgent Delivering agent is not recognised or is
invalid.
IPAC InstructingPartyNotAllowedForAccount Instructing party is not allowed to instruct
for this investment account.
INTE Intermediary Intermediary is not recognised or is
invalid.
DMON InvalidSettlementAmount Unrecognised or invalid settlement
amount.
PRCT PercentageHoldingBreach Percentage holding breach, for example,
PPM rules; taxation rules (ERISA).
IVAG ReceivingAgent Receiving agent is not recognised or is
invalid.
NCRR SettlementAmountCurrency Unrecognised or invalid Settlement
Amount Currency.
DTRD TradeDate Unrecognised or invalid trade date or
requested trade date or future trade
date.
UPAY UnacceptedPaymentMethod Payment method, for example, cheque
or payment card, is not accepted.
URSC UnacceptedRequestedSettlementCurrency Settlement currency requested is not
supported.
NCMP NotCompliantWithMarketPractice Instruction is not compliant with the
relevant market practice.
34.4.4.6.5.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Rejected reason expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 847 May 2026
```

