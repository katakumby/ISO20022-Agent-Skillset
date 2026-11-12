---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "78.4 Message Building Blocks", "78.4.3 Cancellations <Cxls>", "78.4.3.4 Cancellation <Cxl>", "78.4.3.4.7 Underlying <Undrlyg>", "78.4.3.4.7.1 IntraPositionMovement <IntraPosMvmnt>", "78.4.3.4.7.1.2 SettlementQuantity <SttlmQty>"]
file_pages: [2717]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
---

# 78.4.3.4.7.1.2 SettlementQuantity <SttlmQty>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2717 to 2717.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2717

```text
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
78.4.3.4.7.1.2  SettlementQuantity <SttlmQty>
Presence: [1..1]
Definition: Total quantity of securities to be settled.
SettlementQuantity <SttlmQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
78.4.3.4.7.1.3  SettlementDate <SttlmDt>
Presence: [1..1]
Definition: Date and time at which the securities are to be moved.
SettlementDate <SttlmDt> contains one of the following elements (see "DateAndDateTime2Choice"
on page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
78.4.3.4.7.1.4  BalanceFrom <BalFr>
Presence: [0..1]
Definition: Balance from which the securities are moving.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities 2717 August 2026
```

