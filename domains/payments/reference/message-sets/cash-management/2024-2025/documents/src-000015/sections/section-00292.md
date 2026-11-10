---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["10 camt.011.001.08 ModifyLimitV08", "10.2 Structure"]
file_pages: [423]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.011.001.08"]
---

# 10.2 Structure

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 423 to 423.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 423

```text
10.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <ModfyLmt> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 425
   LimitDetails <LmtDtls> [0..*]  C8 425
     LimitIdentification <LmtId> [1..1]  427
{Or       Current <Cur> [1..1]  C3, C4 429
         SystemIdentification <SysId> [0..1] ± 429
         BilateralLimitCounterpartyIdentification <BilLmtCtrPtyId> [0..1] ± 430
         Type <Tp> [1..1]  430
{Or           Code <Cd> [1..1] CodeSet 430
Or}           Proprietary <Prtry> [1..1] Text 432
         AccountOwner <AcctOwnr> [0..1] ± 432
         AccountIdentification <AcctId> [0..1] ± 433
Or       Default <Dflt> [1..1]  C3, C4 433
         SystemIdentification <SysId> [0..1] ± 434
         BilateralLimitCounterpartyIdentification <BilLmtCtrPtyId> [0..1] ± 434
         Type <Tp> [1..1]  435
{Or           Code <Cd> [1..1] CodeSet 435
Or}           Proprietary <Prtry> [1..1] Text 437
         AccountOwner <AcctOwnr> [0..1] ± 437
         AccountIdentification <AcctId> [0..1] ± 438
Or       AllCurrent <AllCur> [1..1]  438
         SystemIdentification <SysId> [0..1] ± 439
         Type <Tp> [1..1]  439
{Or           Code <Cd> [1..1] CodeSet 439
Or}           Proprietary <Prtry> [1..1] Text 441
         AccountOwner <AcctOwnr> [0..1] ± 441
         AccountIdentification <AcctId> [0..1] ± 442
Or}       AllDefault <AllDflt> [1..1]  442
         SystemIdentification <SysId> [0..1] ± 443
         Type <Tp> [1..1]  443
Approved by the Payments SEG on 04 February 2025 camt.011.001.08 ModifyLimitV08
Cash Management - Maintenance 2024 - 2025 423 February 2025
```

