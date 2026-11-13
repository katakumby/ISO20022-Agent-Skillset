---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.1.8 InitiationSource <InitnSrc>"]
file_pages: [21]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.1.8 InitiationSource <InitnSrc>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 21 to 21.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 21

```text
ForwardingAgent <FwdgAgt> contains the following elements (see
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
2.4.1.8  InitiationSource <InitnSrc>
Presence: [0..1]
Definition: Source application or software used to initiate the payment.
InitiationSource <InitnSrc> contains the following PaymentInitiationSource1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 21
   Provider <Prvdr> [0..1] Text 21
   Version <Vrsn> [0..1] Text 22
2.4.1.8.1  Name <Nm>
Presence: [1..1]
Definition: Name of the application or software used to initiate the payment.
Datatype: "Max140Text" on page 608
2.4.1.8.2  Provider <Prvdr>
Presence: [0..1]
Definition: Provider of the application or software used to initiate the payment.
Datatype: "Max35Text" on page 609
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 21 March 2026
```

