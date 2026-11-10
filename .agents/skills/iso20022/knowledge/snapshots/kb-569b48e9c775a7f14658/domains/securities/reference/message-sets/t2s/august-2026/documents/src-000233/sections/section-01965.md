---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "76.4 Message Building Blocks", "76.4.3 Modifications <Mods>", "76.4.3.4 Modification <Mod>", "76.4.3.4.7 Underlying <Undrlyg>", "76.4.3.4.7.2 SettlementTransaction <SttlmTx>", "76.4.3.4.7.2.2 SettlementQuantity <SttlmQty>"]
file_pages: [2685]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 76.4.3.4.7.2.2 SettlementQuantity <SttlmQty>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2685 to 2685.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2685

```text
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
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
76.4.3.4.7.2.2  SettlementQuantity <SttlmQty>
Presence: [1..1]
Definition: Total quantity of securities to be settled.
SettlementQuantity <SttlmQty> contains one of the following elements (see "Quantity6Choice" on
page 2954 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 2954
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 2954
76.4.3.4.7.2.3  SettlementAmount <SttlmAmt>
Presence: [0..1]
Definition: Total amount of money to be paid or received in exchange for the securities.
SettlementAmount <SttlmAmt> contains the following elements (see "AmountAndDirection51" on
page 2837 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C4 2838
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 2838
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C1, C5 2838
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2685 August 2026
```

