---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks"]
file_pages: [386]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4 Message Building Blocks

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 386 to 386.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 386

```text
(MT 564 NVR C7).
C83 WithholdingTaxRate2Rule
Only a single occurrence of either WithholdingTaxRate/Amount or WithholdingTaxRate/Rate or
WithholdingTaxRate/NotSpecifiedRate may be present, only one of these elements may be
present.
(MT 564 NVR C7).
C84 WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and
which must be executed together. Even if one single transactions/instructions/notifications can
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.
7.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
7.4.1 Pagination <Pgntn>
Presence: [0..1]
Definition: Page number of the message and continuation indicator to indicate that the multi-part
preliminary advice is to continue or that the message is the last page of the multi-part preliminary
advice.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 889 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 889
   LastPageIndicator <LastPgInd> [1..1] Indicator 889
7.4.2 MovementPreliminaryAdviceGeneralInformation
<MvmntPrlimryAdvcGnlInf>
Presence: [1..1]
Definition: General information about the movement preliminary advice document.
MovementPreliminaryAdviceGeneralInformation <MvmntPrlimryAdvcGnlInf> contains the
following CorporateActionPreliminaryAdviceType4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MovementPreliminaryAdviceIdentification
<MvmntPrlimryAdvcId>
[0..1] Text 387
   Type <Tp> [1..1] CodeSet 387
   Function <Fctn> [1..1] CodeSet 387
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 386 February 2026
```

