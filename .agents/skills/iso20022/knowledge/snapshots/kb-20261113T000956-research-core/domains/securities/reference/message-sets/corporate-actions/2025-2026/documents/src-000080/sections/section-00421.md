---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.10 AccountDetails <AcctDtls>", "8.4.10.4 SafekeepingPlace <SfkpgPlc>"]
file_pages: [566]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.10.4 SafekeepingPlace <SfkpgPlc>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 566 to 566.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 566

```text
8.4.10.4  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Location where the financial instruments are/will be safekept.
SafekeepingPlace <SfkpgPlc> contains one of the following elements (see
"SafekeepingPlaceFormat42Choice" on page 1130 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  1130
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1130
     Identification <Id> [0..1] Text 1131
Or   Country <Ctry> [1..1] CodeSet C3 1131
Or   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1131
Or   TypeAndIdentification <TpAndId> [1..1]  1131
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1132
     Identification <Id> [1..1] IdentifierSet C1 1132
Or}   Proprietary <Prtry> [1..1] ± 1132
8.4.10.5  Balance <Bal>
Presence: [1..1]
Definition: Provides information about balance related to a corporate action.
Impacted by: C7 "AffectedAndUnaffectedBalanceRule"
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 566 February 2026
```

