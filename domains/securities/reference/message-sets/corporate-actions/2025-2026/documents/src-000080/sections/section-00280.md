---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.5 MovementConfirmationIdentification <MvmntConfId>"]
file_pages: [388]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.5 MovementConfirmationIdentification <MvmntConfId>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 388 to 388.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 388

```text
NotificationIdentification <NtfctnId> contains the following elements (see "DocumentIdentification31"
on page 860 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 861
   LinkageType <LkgTp> [0..1] ± C22 861
7.4.5 MovementConfirmationIdentification <MvmntConfId>
Presence: [0..1]
Definition: Identification of a previously sent movement confirmation document.
MovementConfirmationIdentification <MvmntConfId> contains the following elements (see
"DocumentIdentification31" on page 860 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 861
   LinkageType <LkgTp> [0..1] ± C22 861
7.4.6 InstructionIdentification <InstrId>
Presence: [0..1]
Definition: Identification of a related instruction document.
InstructionIdentification <InstrId> contains the following elements (see "DocumentIdentification9" on
page 877 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 877
7.4.7 OtherDocumentIdentification <OthrDocId>
Presence: [0..*]
Definition: Identification of other documents as well as the document number.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 388 February 2026
```

