---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.14 RelatedRemittanceInformation <RltdRmtInf>", "2.4.2.15.18.2.14.1 RemittanceIdentification <RmtId>"]
file_pages: [164]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.14.1 RemittanceIdentification <RmtId>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 164 to 164.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 164

```text
RelatedRemittanceInformation <RltdRmtInf> contains the following RemittanceLocation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceIdentification <RmtId> [0..1] Text 164
   RemittanceLocationDetails <RmtLctnDtls> [0..*]  164
     Method <Mtd> [1..1] CodeSet 164
     ElectronicAddress <ElctrncAdr> [0..1] Text 165
     PostalAddress <PstlAdr> [0..1]  165
       Name <Nm> [1..1] Text 165
       Address <Adr> [1..1] ± 165
2.4.2.15.18.2.14.1  RemittanceIdentification <RmtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the initiating party, to unambiguously identify the
remittance information sent separately from the payment instruction, such as a remittance advice.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.14.2  RemittanceLocationDetails <RmtLctnDtls>
Presence: [0..*]
Definition: Set of elements used to provide information on the location and/or delivery of the remittance
information.
RemittanceLocationDetails <RmtLctnDtls> contains the following RemittanceLocationData2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Method <Mtd> [1..1] CodeSet 164
   ElectronicAddress <ElctrncAdr> [0..1] Text 165
   PostalAddress <PstlAdr> [0..1]  165
     Name <Nm> [1..1] Text 165
     Address <Adr> [1..1] ± 165
2.4.2.15.18.2.14.2.1  Method <Mtd>
Presence: [1..1]
Definition: Method used to deliver the remittance advice information.
Datatype: "RemittanceLocationMethod2Code" on page 904
CodeName Name Definition
FAXI Fax Remittance advice information must be
faxed.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
164 March 2026
```

