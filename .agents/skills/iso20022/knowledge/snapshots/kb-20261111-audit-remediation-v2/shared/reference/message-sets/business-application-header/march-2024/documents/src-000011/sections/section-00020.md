---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["2 head.001.001.04 BusinessApplicationHeaderV04", "2.4 Message Building Blocks", "2.4.14 Related <Rltd>", "2.4.14.4 BusinessMessageIdentifier <BizMsgIdr>"]
file_pages: [22]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.04"]
---

# 2.4.14.4 BusinessMessageIdentifier <BizMsgIdr>

Source: [src-000011](../../../../../../../../evidence/omitted/b1a725a8c57af20c03e238c2.md). Locator: one-based file pages 22 to 22.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 22

```text
FinancialInstitutionIdentification <FIId> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 26 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  27
     BICFI <BICFI> [0..1] IdentifierSet C2 27
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 28
     LEI <LEI> [0..1] IdentifierSet 28
     Name <Nm> [0..1] Text 28
     PostalAddress <PstlAdr> [0..1] ± 28
     Other <Othr> [0..1] ± 29
   BranchIdentification <BrnchId> [0..1]  30
     Identification <Id> [0..1] Text 30
     LEI <LEI> [0..1] IdentifierSet 30
     Name <Nm> [0..1] Text 30
     PostalAddress <PstlAdr> [0..1] ± 30
2.4.14.4  BusinessMessageIdentifier <BizMsgIdr>
Presence: [1..1]
Definition: Unambiguously identifies the Business Message to the MessagingEndpoint that has created
the Business Message.
Datatype: "Max35Text" on page 57
2.4.14.5  MessageDefinitionIdentifier <MsgDefIdr>
Presence: [1..1]
Definition: The Message Definition Identifier of the Business Message instance with which this Business
Application Header instance is associated.
Datatype: "Max35Text" on page 57
2.4.14.6  BusinessService <BizSvc>
Presence: [0..1]
Definition: Specifies the business service agreed between the two MessagingEndpoints under which
rules this Business Message is exchanged.
To be used when there is a choice of processing services or processing service levels.
Example:
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 head.001.001.04 BusinessApplicationHeaderV04
Business Application Header - Version 4 22 March 2024
```

