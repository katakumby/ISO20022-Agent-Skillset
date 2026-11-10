---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.5 DirectDebitTransaction <DrctDbtTx>", "5.4.2.18.5.1 MandateRelatedInformation <MndtRltdInf>", "5.4.2.18.5.1.4 AmendmentInformationDetails <AmdmntInfDtls>", "5.4.2.18.5.1.4.7 OriginalDebtorAgent <OrgnlDbtrAgt>"]
file_pages: [456]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.5.1.4.7 OriginalDebtorAgent <OrgnlDbtrAgt>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 456 to 456.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 456

```text
OriginalDebtorAccount <OrgnlDbtrAcct> contains the following elements (see "CashAccount40" on
page 527 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 527
   Type <Tp> [0..1] ± 527
   Currency <Ccy> [0..1] CodeSet C2 528
   Name <Nm> [0..1] Text 528
   Proxy <Prxy> [0..1] ± 528
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
5.4.2.18.5.1.4.7  OriginalDebtorAgent <OrgnlDbtrAgt>
Presence: [0..1]
Definition: Original debtor agent that has been modified.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 456 March 2026
```

