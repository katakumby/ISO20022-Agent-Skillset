---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["36 camt.104.001.01 CreateMemberV01", "36.4 Message Building Blocks"]
file_pages: [775]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.104.001.01"]
---

# 36.4 Message Building Blocks

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 775 to 775.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 775

```text
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 StreetNameAndOrPostOfficeBoxRule
If StreetName is not present, then PostOfficeBox is mandatory. If StreetName is present, then
PostOfficeBox is optional.
C4 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
36.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
36.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 811 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 812
   CreationDateTime <CreDtTm> [0..1] DateTime 812
36.4.2 MemberIdentification <MmbId>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a system member, as assigned by the system, or the
system administrator.
MemberIdentification <MmbId> contains one of the following MemberIdentification3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICFI <BICFI> [1..1] IdentifierSet C1 775
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 776
Or}   Other <Othr> [1..1] ± 776
36.4.2.1  BICFI <BICFI>
Presence: [1..1]
Definition: Business identification code of the member financial institution.
Impacted by: C1 "BICFI"
Approved by the Payments SEG on 04 February 2025 camt.104.001.01 CreateMemberV01
Cash Management - Maintenance 2024 - 2025 775 February 2025
```

