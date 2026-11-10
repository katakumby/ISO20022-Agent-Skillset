---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.24 UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf>", "4.4.3.27.24.34 InstructionForCreditorAgent <InstrForCdtrAgt>"]
file_pages: [556]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.24.34 InstructionForCreditorAgent <InstrForCdtrAgt>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 556 to 556.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 556

```text
UltimateCreditor <UltmtCdtr> contains the following elements (see
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
4.4.3.27.24.34  InstructionForCreditorAgent <InstrForCdtrAgt>
Presence: [0..*]
Definition: Further information related to the processing of the payment instruction, provided by the
initiating party, and intended for the creditor agent.
InstructionForCreditorAgent <InstrForCdtrAgt> contains the following elements (see
"InstructionForCreditorAgent3" on page 1203 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [0..1] CodeSet 1203
   InstructionInformation <InstrInf> [0..1] Text 1203
4.4.3.27.24.35  InstructionForNextAgent <InstrForNxtAgt>
Presence: [0..*]
Definition: Further information related to the processing of the payment instruction that may need to be
acted upon by the next agent.
Usage: The next agent may not be the creditor agent.
The instruction can relate to a level of service, can be an instruction that has to be executed by the
agent, or can be information required by the next agent.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
556 March 2026
```

