---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["6 acmt.006.001.07 AccountManagementStatusReportV07", "6.4 Message Building Blocks"]
file_pages: [88]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.006.001.07"]
---

# 6.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 88 to 88.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 88

```text
C6 ClosedStatus5Rule
If Closed is present then Proforma is not allowed.
C7 ClosedStatus6Rule
If Closed is present then ClosurePending is not allowed.
C8 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C9 EnabledDisabledStatus1Rule
If Enabled is present, then Disabled is not allowed.
C10 EnabledDisabledStatus2Rule
If Disabled is present, then Enabled is not allowed.
C11 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C12 StatusElementRule
One of the elements (Enabled, Disabled, Pending, PendingOpening, Proforma, Closed,
ClosurePending, Other) must be present.
6.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
6.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
6.4.2 RelatedReference <RltdRef>
Presence: [1..2]
Definition: Reference to a linked message that was previously received.
Approved by the Securities SEG on 27 January 2026 acmt.006.001.07
AccountManagementStatusReportV07
Investment Funds - Maintenance 2025 - 2026 88 May 2026
```

