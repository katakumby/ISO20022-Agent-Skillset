---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.34 RelatedRemittanceInformation <RltdRmtInf>", "3.4.2.34.1 RemittanceIdentification <RmtId>"]
file_pages: [201]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.34.1 RemittanceIdentification <RmtId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 201 to 201.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 201

```text
RelatedRemittanceInformation <RltdRmtInf> contains the following RemittanceLocation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceIdentification <RmtId> [0..1] Text 201
   RemittanceLocationDetails <RmtLctnDtls> [0..*]  201
     Method <Mtd> [1..1] CodeSet 201
     ElectronicAddress <ElctrncAdr> [0..1] Text 202
     PostalAddress <PstlAdr> [0..1]  202
       Name <Nm> [1..1] Text 202
       Address <Adr> [1..1] ± 202
3.4.2.34.1  RemittanceIdentification <RmtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the initiating party, to unambiguously identify the
remittance information sent separately from the payment instruction, such as a remittance advice.
Datatype: "Max35Text" on page 1246
3.4.2.34.2  RemittanceLocationDetails <RmtLctnDtls>
Presence: [0..*]
Definition: Set of elements used to provide information on the location and/or delivery of the remittance
information.
RemittanceLocationDetails <RmtLctnDtls> contains the following RemittanceLocationData2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Method <Mtd> [1..1] CodeSet 201
   ElectronicAddress <ElctrncAdr> [0..1] Text 202
   PostalAddress <PstlAdr> [0..1]  202
     Name <Nm> [1..1] Text 202
     Address <Adr> [1..1] ± 202
3.4.2.34.2.1  Method <Mtd>
Presence: [1..1]
Definition: Method used to deliver the remittance advice information.
Datatype: "RemittanceLocationMethod2Code" on page 1236
CodeName Name Definition
FAXI Fax Remittance advice information must be
faxed.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
201 March 2026
```

