---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.1 OriginalMessageIdentification <OrgnlMsgId>"]
file_pages: [288]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.2.1 OriginalMessageIdentification <OrgnlMsgId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 288 to 288.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 288

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
4.4.2 OriginalGroupInformation <OrgnlGrpInf>
Presence: [0..1]
Definition: Information concerning the original group of transactions, to which the message refers.
OriginalGroupInformation <OrgnlGrpInf> contains the following OriginalGroupHeader19 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMessageIdentification <OrgnlMsgId> [1..1] Text 288
   OriginalMessageNameIdentification <OrgnlMsgNmId> [1..1] Text 289
   OriginalCreationDateTime <OrgnlCreDtTm> [0..1] DateTime 289
   ReturnReasonInformation <RtrRsnInf> [0..*]  C62 289
     Originator <Orgtr> [0..1] ± 289
     Reason <Rsn> [0..1]  290
{Or       Code <Cd> [1..1] CodeSet 291
Or}       Proprietary <Prtry> [1..1] Text 291
     AdditionalInformation <AddtlInf> [0..*] Text 291
4.4.2.1  OriginalMessageIdentification <OrgnlMsgId>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
288 March 2026
```

