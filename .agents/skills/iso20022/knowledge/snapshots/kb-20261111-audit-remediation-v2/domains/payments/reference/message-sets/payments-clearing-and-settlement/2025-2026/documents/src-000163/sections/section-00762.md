---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "8.4 Message Building Blocks", "8.4.1 GroupHeader <GrpHdr>", "8.4.1.6 InstructedAgent <InstdAgt>"]
file_pages: [1022]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.010.001.06"]
---

# 8.4.1.6 InstructedAgent <InstdAgt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1022 to 1022.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1022

```text
InstructingAgent <InstgAgt> contains the following elements (see
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
8.4.1.6  InstructedAgent <InstdAgt>
Presence: [0..1]
Definition: Agent that is instructed by the previous party in the chain to carry out the (set of)
instruction(s).
Approved by the Payments SEG on 12 January 2026 pacs.010.001.06 FinancialInstitutionDirectDebitV06
Payments Clearing and Settlement - Maintenance 2025 -
2026
1022 March 2026
```

