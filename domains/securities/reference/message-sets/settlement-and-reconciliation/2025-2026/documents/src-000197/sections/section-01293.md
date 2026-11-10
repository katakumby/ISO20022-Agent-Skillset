---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.23 Safekeeping Place", "35.1.23.1 SafeKeepingPlace5", "35.1.23.1.2 LEI <LEI>"]
file_pages: [1750]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.23.1.2 LEI <LEI>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1750 to 1750.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1750

```text
SafekeepingPlaceFormat <SfkpgPlcFrmt> contains one of the following elements (see
"SafekeepingPlaceFormat41Choice" on page 1648 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  1649
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1649
     Identification <Id> [0..1] Text 1649
Or   Country <Ctry> [1..1] CodeSet C7 1649
Or   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1650
Or   TypeAndIdentification <TpAndId> [1..1]  1650
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1650
     Identification <Id> [1..1] IdentifierSet C5 1650
Or}   Proprietary <Prtry> [1..1] ± 1651
35.1.23.1.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a place of safekeeping.
Datatype: "LEIIdentifier" on page 2187
35.1.24 Securities Quantity
35.1.24.1  OriginalAndCurrentQuantities1
Definition: Original and current value of an asset-back instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FaceAmount <FaceAmt> [1..1] Amount 1750
   AmortisedValue <AmtsdVal> [1..1] Amount 1750
35.1.24.1.1  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, that is, the principal of a
debt instrument.
Datatype: "ImpliedCurrencyAndAmount" on page 2042
35.1.24.1.2  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Datatype: "ImpliedCurrencyAndAmount" on page 2042
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1750 March 2026
```

