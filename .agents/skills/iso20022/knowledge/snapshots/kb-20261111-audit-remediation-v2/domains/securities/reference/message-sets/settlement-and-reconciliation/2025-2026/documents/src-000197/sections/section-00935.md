---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.3 Amount", "35.1.3.9 OtherAmounts32", "35.1.3.9.6 LocalBrokerCommission <LclBrkrComssn>"]
file_pages: [1371]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.3.9.6 LocalBrokerCommission <LclBrkrComssn>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1371 to 1371.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1371

```text
LocalTax <LclTax> contains the following elements (see "AmountAndDirection47" on page 1359 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1359
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1359
   ForeignExchangeDetails <FXDtls> [0..1] ± 1359
35.1.3.9.6  LocalBrokerCommission <LclBrkrComssn>
Presence: [0..1]
Definition: Amount of commission paid to a local broker.
LocalBrokerCommission <LclBrkrComssn> contains the following elements (see
"AmountAndDirection47" on page 1359 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1359
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1359
   ForeignExchangeDetails <FXDtls> [0..1] ± 1359
35.1.3.9.7  Other <Othr>
Presence: [0..1]
Definition: An amount that is not indicated by a known business denomination.
Other <Othr> contains the following elements (see "AmountAndDirection47" on page 1359 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1359
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1359
   ForeignExchangeDetails <FXDtls> [0..1] ± 1359
35.1.3.9.8  StampDuty <StmpDty>
Presence: [0..1]
Definition: Amount of stamp duty.
StampDuty <StmpDty> contains the following elements (see "AmountAndDirection47" on page 1359
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1359
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1359
   ForeignExchangeDetails <FXDtls> [0..1] ± 1359
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1371 March 2026
```

