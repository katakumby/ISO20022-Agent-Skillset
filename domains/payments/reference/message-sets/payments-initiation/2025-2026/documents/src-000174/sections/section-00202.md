---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.1.10 CreditorAgent <CdtrAgt>"]
file_pages: [288]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.1.10 CreditorAgent <CdtrAgt>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 288 to 288.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 288

```text
4.4.1.10  CreditorAgent <CdtrAgt>
Presence: [0..1]
Definition: Financial institution servicing an account for the creditor.
CreditorAgent <CdtrAgt> contains the following elements (see
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
4.4.2 OriginalGroupInformation <OrgnlGrpInf>
Presence: [1..1]
Definition: Information concerning the original group of transactions, to which the message refers.
OriginalGroupInformation <OrgnlGrpInf> contains the following OriginalGroupHeader20 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMessageIdentification <OrgnlMsgId> [1..1] Text 289
   OriginalMessageNameIdentification <OrgnlMsgNmId> [1..1] Text 289
   OriginalCreationDateTime <OrgnlCreDtTm> [0..1] DateTime 289
   ReversalReasonInformation <RvslRsnInf> [0..*]  289
     Originator <Orgtr> [0..1] ± 289
     Reason <Rsn> [0..1]  290
{Or       Code <Cd> [1..1] CodeSet 291
Or}       Proprietary <Prtry> [1..1] Text 291
     AdditionalInformation <AddtlInf> [0..*] Text 291
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 288 March 2026
```

