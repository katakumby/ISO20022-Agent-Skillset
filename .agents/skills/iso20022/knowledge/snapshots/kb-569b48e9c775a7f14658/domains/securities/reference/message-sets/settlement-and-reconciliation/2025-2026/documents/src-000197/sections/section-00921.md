---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.3 Amount", "35.1.3.1 OtherAmounts46", "35.1.3.1.26 CollateralMonitorAmount <CollMntrAmt>"]
file_pages: [1357]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.3.1.26 CollateralMonitorAmount <CollMntrAmt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1357 to 1357.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1357

```text
BookValue <BookVal> contains the following elements (see "AmountAndDirection44" on page 1375
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1375
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1376
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1376
   ForeignExchangeDetails <FXDtls> [0..1] ± 1376
35.1.3.1.26  CollateralMonitorAmount <CollMntrAmt>
Presence: [0..1]
Definition: Value of the collateral available for the delivery settlement process at the account level.
CollateralMonitorAmount <CollMntrAmt> contains the following elements (see
"AmountAndDirection44" on page 1375 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1375
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1376
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1376
   ForeignExchangeDetails <FXDtls> [0..1] ± 1376
35.1.3.1.27  ResearchFee <RsrchFee>
Presence: [0..1]
Definition: Charge or commission paid by the investor to a distributor/intermediary or other service
provider for the provision of financial research.
ResearchFee <RsrchFee> contains the following elements (see "AmountAndDirection44" on
page 1375 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1375
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1376
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1376
   ForeignExchangeDetails <FXDtls> [0..1] ± 1376
35.1.3.1.28  NetworkFee <NtwkFee>
Presence: [0..1]
Definition: Network fee assigned to a transaction on a DLT network.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1357 March 2026
```

