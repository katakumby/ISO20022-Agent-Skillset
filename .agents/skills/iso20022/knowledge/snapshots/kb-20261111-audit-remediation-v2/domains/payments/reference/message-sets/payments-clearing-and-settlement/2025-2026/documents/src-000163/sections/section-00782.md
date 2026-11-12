---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "8.4 Message Building Blocks", "8.4.2 CreditInstruction <CdtInstr>", "8.4.2.21 DirectDebitTransactionInformation <DrctDbtTxInf>", "8.4.2.21.11 DebtorAgent <DbtrAgt>"]
file_pages: [1045]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.010.001.06"]
---

# 8.4.2.21.11 DebtorAgent <DbtrAgt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1045 to 1045.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1045

```text
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
8.4.2.21.11  DebtorAgent <DbtrAgt>
Presence: [0..1]
Definition: Financial institution servicing an account for the debtor.
DebtorAgent <DbtrAgt> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 1173 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  1174
     BICFI <BICFI> [0..1] IdentifierSet C5 1174
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1175
     LEI <LEI> [0..1] IdentifierSet 1175
     Name <Nm> [0..1] Text 1175
     PostalAddress <PstlAdr> [0..1] ± 1175
     Other <Othr> [0..1] ± 1176
   BranchIdentification <BrnchId> [0..1]  1177
     Identification <Id> [0..1] Text 1177
     LEI <LEI> [0..1] IdentifierSet 1177
     Name <Nm> [0..1] Text 1177
     PostalAddress <PstlAdr> [0..1] ± 1177
8.4.2.21.12  DebtorAgentAccount <DbtrAgtAcct>
Presence: [0..1]
Definition: Unambiguous identification of the account of the debtor agent at its servicing agent in the
payment chain.
Impacted by: C9 "IdentificationOrProxyPresenceRule", C8 "IdentificationAndProxyGuideline"
Approved by the Payments SEG on 12 January 2026 pacs.010.001.06 FinancialInstitutionDirectDebitV06
Payments Clearing and Settlement - Maintenance 2025 -
2026
1045 March 2026
```

