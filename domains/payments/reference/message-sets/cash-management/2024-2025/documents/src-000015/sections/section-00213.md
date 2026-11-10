---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 camt.007.001.10 ModifyTransactionV10", "6.3 Constraints"]
file_pages: [329]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.007.001.10"]
---

# 6.3 Constraints

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 329 to 329.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 329

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       Instruction <Instr> [0..1] CodeSet 342
       Type <Tp> [0..1]  342
{Or         Code <Cd> [1..1] CodeSet 343
Or}         Proprietary <Prtry> [1..1] Text 344
       Priority <Prty> [0..1]  345
{Or         Code <Cd> [1..1] CodeSet 345
Or}         Proprietary <Prtry> [1..1] Text 345
       ProcessingValidityTime <PrcgVldtyTm> [0..1]  345
{Or         FromDateTime <FrDtTm> [1..1] DateTime 346
Or         ToDateTime <ToDtTm> [1..1] DateTime 346
Or}         DateTimeRange <DtTmRg> [1..1] ± 346
   SupplementaryData <SplmtryData> [0..*] ± C3 346
6.3 Constraints
C1 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C4 TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
C5 TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
6.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
6.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Approved by the Payments SEG on 04 February 2025 camt.007.001.10 ModifyTransactionV10
Cash Management - Maintenance 2024 - 2025 329 February 2025
```

