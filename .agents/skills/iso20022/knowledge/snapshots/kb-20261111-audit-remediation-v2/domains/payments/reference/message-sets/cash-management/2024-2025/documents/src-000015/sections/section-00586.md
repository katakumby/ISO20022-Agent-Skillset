---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["34 camt.102.001.03 CreateStandingOrderV03", "34.4 Message Building Blocks", "34.4.3 ValueSet <ValSet>", "34.4.3.3 CreditorAccount <CdtrAcct>"]
file_pages: [761]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.102.001.03"]
---

# 34.4.3.3 CreditorAccount <CdtrAcct>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 761 to 761.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 761

```text
Definition: Party to which an amount of money is due.
Creditor <Cdtr> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on
page 803 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  804
     BICFI <BICFI> [0..1] IdentifierSet C2 804
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 805
     LEI <LEI> [0..1] IdentifierSet 805
     Name <Nm> [0..1] Text 805
     PostalAddress <PstlAdr> [0..1] ± 805
     Other <Othr> [0..1] ± 806
   BranchIdentification <BrnchId> [0..1]  807
     Identification <Id> [0..1] Text 807
     LEI <LEI> [0..1] IdentifierSet 807
     Name <Nm> [0..1] Text 807
     PostalAddress <PstlAdr> [0..1] ± 807
34.4.3.3  CreditorAccount <CdtrAcct>
Presence: [0..1]
Definition: Cash account credited from a standing order mechanism.
Impacted by: C8 "IdentificationOrProxyPresenceRule", C7 "IdentificationAndProxyGuideline"
CreditorAccount <CdtrAcct> contains the following elements (see "CashAccount40" on page 783 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 783
   Type <Tp> [0..1] ± 783
   Currency <Ccy> [0..1] CodeSet C1 784
   Name <Nm> [0..1] Text 784
   Proxy <Prxy> [0..1] ± 784
Approved by the Payments SEG on 04 February 2025 camt.102.001.03 CreateStandingOrderV03
Cash Management - Maintenance 2024 - 2025 761 February 2025
```

