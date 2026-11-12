---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.46 RelatedRemittanceInformation <RltdRmtInf>", "6.4.2.46.1 RemittanceIdentification <RmtId>"]
file_pages: [785]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.46.1 RemittanceIdentification <RmtId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 785 to 785.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 785

```text
RelatedRemittanceInformation <RltdRmtInf> contains the following RemittanceLocation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceIdentification <RmtId> [0..1] Text 785
   RemittanceLocationDetails <RmtLctnDtls> [0..*]  785
     Method <Mtd> [1..1] CodeSet 785
     ElectronicAddress <ElctrncAdr> [0..1] Text 786
     PostalAddress <PstlAdr> [0..1]  786
       Name <Nm> [1..1] Text 786
       Address <Adr> [1..1] ± 786
6.4.2.46.1  RemittanceIdentification <RmtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the initiating party, to unambiguously identify the
remittance information sent separately from the payment instruction, such as a remittance advice.
Datatype: "Max35Text" on page 1246
6.4.2.46.2  RemittanceLocationDetails <RmtLctnDtls>
Presence: [0..*]
Definition: Set of elements used to provide information on the location and/or delivery of the remittance
information.
RemittanceLocationDetails <RmtLctnDtls> contains the following RemittanceLocationData2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Method <Mtd> [1..1] CodeSet 785
   ElectronicAddress <ElctrncAdr> [0..1] Text 786
   PostalAddress <PstlAdr> [0..1]  786
     Name <Nm> [1..1] Text 786
     Address <Adr> [1..1] ± 786
6.4.2.46.2.1  Method <Mtd>
Presence: [1..1]
Definition: Method used to deliver the remittance advice information.
Datatype: "RemittanceLocationMethod2Code" on page 1236
CodeName Name Definition
FAXI Fax Remittance advice information must be
faxed.
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
785 March 2026
```

