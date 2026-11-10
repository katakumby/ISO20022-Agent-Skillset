---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["9 reda.042.001.01 PartyAuditTrailQueryV01", "9.3 Constraints"]
file_pages: [112]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.042.001.01"]
---

# 9.3 Constraints

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 112 to 112.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 112

```text
9.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
9.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
9.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 161 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 161
   CreationDateTime <CreDtTm> [0..1] DateTime 161
9.4.2 SearchCriteria <SchCrit>
Presence: [1..1]
Definition: Defines the criteria to be used to query the party audit trail by the executing system.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.042.001.01 PartyAuditTrailQueryV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
112 March 2024
```

