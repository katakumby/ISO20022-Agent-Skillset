---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.10 MandateRelatedInformation <MndtRltdInf>", "4.4.3.8.9.10.1 DirectDebitMandate <DrctDbtMndt>", "4.4.3.8.9.10.1.4 AmendmentInformationDetails <AmdmntInfDtls>", "4.4.3.8.9.10.1.4.4 OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct>"]
file_pages: [338]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.10.1.4.4 OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 338 to 338.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 338

```text
OriginalCreditorAgent <OrgnlCdtrAgt> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 539 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  540
     BICFI <BICFI> [0..1] IdentifierSet C4 540
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 541
     LEI <LEI> [0..1] IdentifierSet 541
     Name <Nm> [0..1] Text 541
     PostalAddress <PstlAdr> [0..1] ± 541
     Other <Othr> [0..1] ± 542
   BranchIdentification <BrnchId> [0..1]  543
     Identification <Id> [0..1] Text 543
     LEI <LEI> [0..1] IdentifierSet 543
     Name <Nm> [0..1] Text 543
     PostalAddress <PstlAdr> [0..1] ± 543
4.4.3.8.9.10.1.4.4  OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct>
Presence: [0..1]
Definition: Original creditor agent account that has been modified.
Impacted by: C18 "IdentificationOrProxyPresenceRule", C17 "IdentificationAndProxyGuideline"
OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> contains the following elements (see
"CashAccount40" on page 527 for details)
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
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 338 March 2026
```

