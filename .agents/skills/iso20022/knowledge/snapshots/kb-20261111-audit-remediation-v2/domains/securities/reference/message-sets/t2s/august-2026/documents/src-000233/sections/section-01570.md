---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["48 reda.028.001.01 CollateralDataStatusAdviceV01", "48.4 Message Building Blocks"]
file_pages: [2195]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.028.001.01"]
---

# 48.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2195 to 2195.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2195

```text
C3 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C4 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C5 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C6 StatusReasonAndFinancialInstrumentPresenceRule
If Status Reason And Financial Instrument is present then Status Reason cannot be present
On Condition
    /StatusReasonAndFinancialInstrument is present
Following Must be True
    /StatusReason Must be absent
This constraint is defined at the MessageDefinition level.
C7 StatusReasonPresenceRule
If Status Reason is present then Status Reason And Financial Instrument cannot be present
On Condition
    /StatusReason is present
Following Must be True
    /StatusReasonAndFinancialInstrument Must be absent
This constraint is defined at the MessageDefinition level.
C8 StatusReasonRule
If Status equals 'Rejected' then Reason must be present.
C9 StatusReasonRule
If Status equals 'Rejected' then Reason must be present.
C10 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
48.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
48.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.028.001.01 CollateralDataStatusAdviceV01
Target2-Securities 2195 August 2026
```

