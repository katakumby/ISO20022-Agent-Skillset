---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.14 RelatedRemittanceInformation <RltdRmtInf>", "4.4.2.14.18.2.14.1 RemittanceIdentification <RmtId>"]
file_pages: [682]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.14.1 RemittanceIdentification <RmtId>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 682 to 682.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 682

```text
RelatedRemittanceInformation <RltdRmtInf> contains the following RemittanceLocation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceIdentification <RmtId> [0..1] Text 682
   RemittanceLocationDetails <RmtLctnDtls> [0..*]  682
     Method <Mtd> [1..1] CodeSet 682
     ElectronicAddress <ElctrncAdr> [0..1] Text 683
     PostalAddress <PstlAdr> [0..1]  683
       Name <Nm> [1..1] Text 683
       Address <Adr> [1..1] ± 683
4.4.2.14.18.2.14.1  RemittanceIdentification <RmtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the initiating party, to unambiguously identify the
remittance information sent separately from the payment instruction, such as a remittance advice.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.14.2  RemittanceLocationDetails <RmtLctnDtls>
Presence: [0..*]
Definition: Set of elements used to provide information on the location and/or delivery of the remittance
information.
RemittanceLocationDetails <RmtLctnDtls> contains the following RemittanceLocationData2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Method <Mtd> [1..1] CodeSet 682
   ElectronicAddress <ElctrncAdr> [0..1] Text 683
   PostalAddress <PstlAdr> [0..1]  683
     Name <Nm> [1..1] Text 683
     Address <Adr> [1..1] ± 683
4.4.2.14.18.2.14.2.1  Method <Mtd>
Presence: [1..1]
Definition: Method used to deliver the remittance advice information.
Datatype: "RemittanceLocationMethod2Code" on page 904
CodeName Name Definition
FAXI Fax Remittance advice information must be
faxed.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
682 March 2026
```

