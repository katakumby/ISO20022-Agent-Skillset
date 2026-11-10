---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.18 OriginalTransactionReference <OrgnlTxRef>", "2.4.3.18.10 MandateRelatedInformation <MndtRltdInf>", "2.4.3.18.10.1 DirectDebitMandate <DrctDbtMndt>", "2.4.3.18.10.1.4 AmendmentInformationDetails <AmdmntInfDtls>", "2.4.3.18.10.1.4.7 OriginalDebtorAgent <OrgnlDbtrAgt>"]
file_pages: [70]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.18.10.1.4.7 OriginalDebtorAgent <OrgnlDbtrAgt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 70 to 70.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 70

```text
OriginalDebtorAccount <OrgnlDbtrAcct> contains the following elements (see "CashAccount40" on
page 1161 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 1161
   Type <Tp> [0..1] ± 1161
   Currency <Ccy> [0..1] CodeSet C2 1162
   Name <Nm> [0..1] Text 1162
   Proxy <Prxy> [0..1] ± 1162
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
2.4.3.18.10.1.4.7  OriginalDebtorAgent <OrgnlDbtrAgt>
Presence: [0..1]
Definition: Original debtor agent that has been modified.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
70 March 2026
```

