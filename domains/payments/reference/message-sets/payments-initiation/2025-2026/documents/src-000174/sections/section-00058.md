---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.25 RelatedRemittanceInformation <RltdRmtInf>", "2.4.2.19.25.1 RemittanceIdentification <RmtId>"]
file_pages: [85]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.25.1 RemittanceIdentification <RmtId>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 85 to 85.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 85

```text
RelatedRemittanceInformation <RltdRmtInf> contains the following RemittanceLocation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceIdentification <RmtId> [0..1] Text 85
   RemittanceLocationDetails <RmtLctnDtls> [0..*]  85
     Method <Mtd> [1..1] CodeSet 85
     ElectronicAddress <ElctrncAdr> [0..1] Text 86
     PostalAddress <PstlAdr> [0..1]  86
       Name <Nm> [1..1] Text 86
       Address <Adr> [1..1] ± 86
2.4.2.19.25.1  RemittanceIdentification <RmtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the initiating party, to unambiguously identify the
remittance information sent separately from the payment instruction, such as a remittance advice.
Datatype: "Max35Text" on page 609
2.4.2.19.25.2  RemittanceLocationDetails <RmtLctnDtls>
Presence: [0..*]
Definition: Set of elements used to provide information on the location and/or delivery of the remittance
information.
RemittanceLocationDetails <RmtLctnDtls> contains the following RemittanceLocationData2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Method <Mtd> [1..1] CodeSet 85
   ElectronicAddress <ElctrncAdr> [0..1] Text 86
   PostalAddress <PstlAdr> [0..1]  86
     Name <Nm> [1..1] Text 86
     Address <Adr> [1..1] ± 86
2.4.2.19.25.2.1  Method <Mtd>
Presence: [1..1]
Definition: Method used to deliver the remittance advice information.
Datatype: "RemittanceLocationMethod2Code" on page 601
CodeName Name Definition
FAXI Fax Remittance advice information must be
faxed.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 85 March 2026
```

