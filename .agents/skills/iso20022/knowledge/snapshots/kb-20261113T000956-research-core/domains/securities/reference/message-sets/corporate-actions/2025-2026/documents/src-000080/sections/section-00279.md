---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.2 MovementPreliminaryAdviceGeneralInformation <MvmntPrlimryAdvcGnlInf>", "7.4.2.1 MovementPreliminaryAdviceIdentification <MvmntPrlimryAdvcId>"]
file_pages: [387]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.2.1 MovementPreliminaryAdviceIdentification <MvmntPrlimryAdvcId>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 387 to 387.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 387

```text
7.4.2.1  MovementPreliminaryAdviceIdentification <MvmntPrlimryAdvcId>
Presence: [0..1]
Definition: Unique identification of the group of corporate action movement preliminary advice
messages when the preliminary advice is split in multiple (paginated) messages.
Datatype: "Max35Text" on page 1251
7.4.2.2  Type <Tp>
Presence: [1..1]
Definition: Type of movement preliminary advice, for example. new or replacement.
Datatype: "CorporateActionPreliminaryAdviceType1Code" on page 1203
CodeName Name Definition
NEWM New New movement preliminary advice.
REPL Replacement Movement preliminary advice replacing a
previously sent preliminary advice.
7.4.2.3  Function <Fctn>
Presence: [1..1]
Definition: Specifies whether the message advises about the final eligible balance and entitlements or
about an upcoming posting or reversal of securities and/or cash postings.
Datatype: "CorporateActionMovementPreliminaryAdviceFunction1Code" on page 1195
CodeName Name Definition
ENTL Entitlement Message is an entitlement.
CAPA PreadviceOfMovement Message is a preadvice of movement.
7.4.3 PreviousMovementPreliminaryAdviceIdentification
<PrvsMvmntPrlimryAdvcId>
Presence: [0..1]
Definition: Identification of the previously sent movement preliminary advice document.
PreviousMovementPreliminaryAdviceIdentification <PrvsMvmntPrlimryAdvcId> contains the
following elements (see "DocumentIdentification31" on page 860 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 861
   LinkageType <LkgTp> [0..1] ± C22 861
7.4.4 NotificationIdentification <NtfctnId>
Presence: [0..1]
Definition: Identification of a previously sent notification document.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 387 February 2026
```

