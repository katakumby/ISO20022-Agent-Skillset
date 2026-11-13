---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.36 ReferredAgent3"]
file_pages: [5027]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.36 ReferredAgent3

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5027 to 5027.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5027

```text
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress4" on
page 5100 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 5100
   Address <Adr> [1..1] ± 5100
66.1.30.36  ReferredAgent3
Definition: Provides the placement agent identification for a hedge fund if the investor was referred by
one.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Referred <Rfrd> [1..1] CodeSet 5027
   ReferredPlacementAgent <RfrdPlcmntAgt> [0..1] ± 5027
Constraints
• ReferredPlacementAgentRule
ReferredPlacementAgent may only be present if Referred is REFR (Referred).
66.1.30.36.1  Referred <Rfrd>
Presence: [1..1]
Definition: Indicates if the investor was referred by a placement agent.
Datatype: "Referred1Code" on page 5346
CodeName Name Definition
REFR Referred The investor was referred to the fund by
a placement agent.
NRFR NotReferred The investor was not referred to the fund
by a placement agent.
UKNW NotKnown It is not known whether the investor was
referred to the fund by a placement
agent.
66.1.30.36.2  ReferredPlacementAgent <RfrdPlcmntAgt>
Presence: [0..1]
Definition: Placement agent that referred the investor.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5027 May 2026
```

