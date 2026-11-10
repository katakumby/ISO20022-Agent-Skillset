---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.4 MovementPreliminaryAdviceIdentification <MvmntPrlimryAdvcId>"]
file_pages: [559]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.4 MovementPreliminaryAdviceIdentification <MvmntPrlimryAdvcId>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 559 to 559.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 559

```text
Definition: Identification of a previously sent notification document.
NotificationIdentification <NtfctnId> contains the following elements (see "DocumentIdentification31"
on page 860 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 861
   LinkageType <LkgTp> [0..1] ± C22 861
8.4.4 MovementPreliminaryAdviceIdentification
<MvmntPrlimryAdvcId>
Presence: [0..1]
Definition: Identification of a previously sent movement preliminary advice document.
MovementPreliminaryAdviceIdentification <MvmntPrlimryAdvcId> contains the following elements
(see "DocumentIdentification31" on page 860 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 861
   LinkageType <LkgTp> [0..1] ± C22 861
8.4.5 InstructionIdentification <InstrId>
Presence: [0..1]
Definition: Identification of a related instruction document.
InstructionIdentification <InstrId> contains the following elements (see "DocumentIdentification9" on
page 877 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 877
8.4.6 OtherDocumentIdentification <OthrDocId>
Presence: [0..*]
Definition: Identification of other documents as well as the document number.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 559 February 2026
```

