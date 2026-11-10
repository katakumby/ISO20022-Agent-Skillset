---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.7.6 RequestedSettlementDate <ReqdSttlmDt>"]
file_pages: [627]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.7.6 RequestedSettlementDate <ReqdSttlmDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 627 to 627.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 627

```text
RequestedTransferDate <ReqdTrfDt> contains one of the following elements (see
"DateFormat1Choice" on page 4407 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4407
Or   Code <Cd> [1..1] CodeSet 4408
Or}   DateTime <DtTm> [1..1] DateTime 4408
28.4.7.6  RequestedSettlementDate <ReqdSttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are to be exchanged at the International Central
Securities Depository (ICSD) or Central Securities Depository (CSD).
Datatype: "ISODate" on page 5388
28.4.7.7  TransferOrderDateForm <TrfOrdrDtForm>
Presence: [0..1]
Definition: Date on which the investor signed the transfer order form.
Datatype: "ISODate" on page 5388
28.4.7.8  TransferReason <TrfRsn>
Presence: [0..1]
Definition: Reason for the transfer.
TransferReason <TrfRsn> contains one of the following elements (see "TransferReason1Choice" on
page 5265 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5266
Or}   Proprietary <Prtry> [1..1] ± 5266
28.4.7.9  HoldingsPlanType <HldgsPlanTp>
Presence: [0..3]
Definition: Specifies information about investment plans included in the holding.
Datatype: "HoldingsPlanType1Code" on page 5309
CodeName Name Definition
INVP InvestmentPlan Holding to be transferred belongs to an
investment plan.
SWIP SwitchPlan Holding to be transferred belongs to a
switch plan.
PLAR WithdrawalPlan Holding to be transferred belongs to a
withdrawal plan.
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 627 May 2026
```

