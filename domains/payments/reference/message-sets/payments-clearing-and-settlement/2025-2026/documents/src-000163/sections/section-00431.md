---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.2 OriginalGroupInformation <OrgnlGrpInf>"]
file_pages: [590]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.2 OriginalGroupInformation <OrgnlGrpInf>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 590 to 590.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 590

```text
InstructedAgent <InstdAgt> contains the following elements (see
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
5.4.2 OriginalGroupInformation <OrgnlGrpInf>
Presence: [0..1]
Definition: Information concerning the original group of transactions, to which the message refers.
OriginalGroupInformation <OrgnlGrpInf> contains the following OriginalGroupHeader20 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMessageIdentification <OrgnlMsgId> [1..1] Text 590
   OriginalMessageNameIdentification <OrgnlMsgNmId> [1..1] Text 591
   OriginalCreationDateTime <OrgnlCreDtTm> [0..1] DateTime 591
   ReversalReasonInformation <RvslRsnInf> [0..*]  591
     Originator <Orgtr> [0..1] ± 591
     Reason <Rsn> [0..1]  592
{Or       Code <Cd> [1..1] CodeSet 593
Or}       Proprietary <Prtry> [1..1] Text 593
     AdditionalInformation <AddtlInf> [0..*] Text 593
5.4.2.1  OriginalMessageIdentification <OrgnlMsgId>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
590 March 2026
```

