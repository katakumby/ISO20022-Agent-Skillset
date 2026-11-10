---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "7.4 Message Building Blocks", "7.4.3 Cancellations <Cxls>", "7.4.3.4 Cancellation <Cxl>", "7.4.3.4.7 Underlying <Undrlyg>", "7.4.3.4.7.1 IntraPositionMovement <IntraPosMvmnt>", "7.4.3.4.7.1.2 SettlementQuantity <SttlmQty>"]
file_pages: [162]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
---

# 7.4.3.4.7.1.2 SettlementQuantity <SttlmQty>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 162 to 162.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 162

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
7.4.3.4.7.1.2  SettlementQuantity <SttlmQty>
Presence: [1..1]
Definition: Total quantity of securities to be settled.
SettlementQuantity <SttlmQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 220 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 221
Or   FaceAmount <FaceAmt> [1..1] Amount 221
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 221
7.4.3.4.7.1.3  SettlementDate <SttlmDt>
Presence: [1..1]
Definition: Date and time at which the securities are to be moved.
SettlementDate <SttlmDt> contains one of the following elements (see "DateAndDateTime2Choice"
on page 204 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 204
Or}   DateTime <DtTm> [1..1] DateTime 204
7.4.3.4.7.1.4  BalanceFrom <BalFr>
Presence: [0..1]
Definition: Balance from which the securities are moving.
Approved by the Securities SEG on 21 August 2025 semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities - Settlement Restrictions 162 September 2025
```

