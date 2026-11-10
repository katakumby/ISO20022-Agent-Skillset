---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 camt.007.001.10 ModifyTransactionV10", "6.4 Message Building Blocks", "6.4.2 Modification <Mod>", "6.4.2.1 PaymentIdentification <PmtId>"]
file_pages: [332]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.007.001.10"]
---

# 6.4.2.1 PaymentIdentification <PmtId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 332 to 332.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 332

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Priority <Prty> [0..1]  345
{Or       Code <Cd> [1..1] CodeSet 345
Or}       Proprietary <Prtry> [1..1] Text 345
     ProcessingValidityTime <PrcgVldtyTm> [0..1]  345
{Or       FromDateTime <FrDtTm> [1..1] DateTime 346
Or       ToDateTime <ToDtTm> [1..1] DateTime 346
Or}       DateTimeRange <DtTmRg> [1..1] ± 346
6.4.2.1  PaymentIdentification <PmtId>
Presence: [1..1]
Definition: Reference to the instruction related to the payment for which a modification is requested.
Approved by the Payments SEG on 04 February 2025 camt.007.001.10 ModifyTransactionV10
Cash Management - Maintenance 2024 - 2025 332 February 2025
```

