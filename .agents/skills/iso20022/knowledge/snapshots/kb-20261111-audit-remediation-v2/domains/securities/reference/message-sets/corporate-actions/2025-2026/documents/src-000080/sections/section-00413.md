---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks"]
file_pages: [558]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
preceding_topic_continuations: [{"constraint_ids": ["C75", "C76", "C77"], "until_heading": "8.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 558, "topic": "8.3 Constraints", "reference_path": "domains/securities/reference/message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00412.md"}]
---

# 8.4 Message Building Blocks

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 558 to 558.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 558, C75–C77 before **8.4 Message Building Blocks** continue [8.3 Constraints](section-00412.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 558

```text
(MT 566 NVR C4).
C75 WithholdingTaxRate2Rule
Only a single occurrence of either WithholdingTaxRate/Amount or WithholdingTaxRate/Rate or
WithholdingTaxRate/NotSpecifiedRate may be present, only one of these elements may be
present.
(MT 564 NVR C7).
C76 WithholdingTaxRate2Rule
Only a single occurrence of either WithholdingTaxRate/Amount or WithholdingTaxRate/Rate or
WithholdingTaxRate/NotSpecifiedRate may be present, only one of these elements may be
present.
(MT 566 NVR C3).
C77 WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and
which must be executed together. Even if one single transactions/instructions/notifications can
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.
8.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
8.4.1 Pagination <Pgntn>
Presence: [0..1]
Definition: Page number of the message and continuation indicator to indicate that the multi-part
notification is to continue or that the message is the last page of the multi-part notification.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 889 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 889
   LastPageIndicator <LastPgInd> [1..1] Indicator 889
8.4.2 MovementConfirmationIdentification <MvmntConfId>
Presence: [0..1]
Definition: Unique Identification of the group of corporate action movement confirmation messages
when the movement confirmation is split in multiple (paginated) messages.
Datatype: "Max35Text" on page 1251
8.4.3 NotificationIdentification <NtfctnId>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 558 February 2026
```

