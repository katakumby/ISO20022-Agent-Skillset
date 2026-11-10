---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "2.4 Message Building Blocks", "2.4.14 Related <Rltd>", "2.4.14.4 BusinessMessageIdentifier <BizMsgIdr>"]
file_pages: [20]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.001.001.03", "head.001.001.02"]
---

# 2.4.14.4 BusinessMessageIdentifier <BizMsgIdr>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 20 to 20.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 20

```text
FinancialInstitutionIdentification <FIId> contains the following elements (see
"BranchAndFinancialInstitutionIdentification6" on page 867 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1] ± 867
   BranchIdentification <BrnchId> [0..1] ± 868
2.4.14.4  BusinessMessageIdentifier <BizMsgIdr>
Presence: [1..1]
Definition: Unambiguously identifies the Business Message to the MessagingEndpoint that has created
the Business Message.
Datatype: "Max35Text" on page 1251
2.4.14.5  MessageDefinitionIdentifier <MsgDefIdr>
Presence: [1..1]
Definition: Contains the MessageIdentifier that defines the BusinessMessage.
It must contain a MessageIdentifier published on the ISO 20022 website.
example camt.001.001.03.
Datatype: "Max35Text" on page 1251
2.4.14.6  BusinessService <BizSvc>
Presence: [0..1]
Definition: Specifies the business service agreed between the two MessagingEndpoints under which
rules this Business Message is exchanged.
To be used when there is a choice of processing services or processing service levels.
Example: E&I.
Datatype: "Max35Text" on page 1251
2.4.14.7  CreationDate <CreDt>
Presence: [1..1]
Definition: Date and time when this Business Message (header) was created.
Note Times must be normalized, using the "Z" annotation.
Datatype: "ISODateTime" on page 1243
2.4.14.8  CopyDuplicate <CpyDplct>
Presence: [0..1]
Definition: Indicates whether the message is a Copy, a Duplicate or a copy of a duplicate of a previously
sent ISO 20022 Message.
Approved by the Securities SEG on 27 January 2026 head.001.001.02 BusinessApplicationHeaderV02
Corporate Actions - Maintenance 2025 - 2026 20 February 2026
```

