---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.12 CreditorAgentAccount <CdtrAgtAcct>"]
file_pages: [432]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.12 CreditorAgentAccount <CdtrAgtAcct>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 432 to 432.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 432

```text
CreditorAgent <CdtrAgt> contains the following elements (see
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
5.4.2.12  CreditorAgentAccount <CdtrAgtAcct>
Presence: [0..1]
Definition: Unambiguous identification of the account of the creditor agent at its servicing agent in the
payment chain.
Impacted by: C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"
CreditorAgentAccount <CdtrAgtAcct> contains the following elements (see "CashAccount40" on
page 527 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 527
   Type <Tp> [0..1] ± 527
   Currency <Ccy> [0..1] CodeSet C2 528
   Name <Nm> [0..1] Text 528
   Proxy <Prxy> [0..1] ± 528
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 432 March 2026
```

