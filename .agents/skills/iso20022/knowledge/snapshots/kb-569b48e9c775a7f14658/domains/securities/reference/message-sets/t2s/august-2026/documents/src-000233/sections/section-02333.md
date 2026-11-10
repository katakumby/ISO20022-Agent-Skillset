---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.26 Safekeeping Place", "82.1.26.1 SafeKeepingPlace3", "82.1.26.1.2 LEI <LEI>"]
file_pages: [3114]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.26.1.2 LEI <LEI>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3114 to 3114.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3114

```text
SafekeepingPlaceFormat <SfkpgPlcFrmt> contains one of the following elements (see
"SafekeepingPlaceFormat29Choice" on page 3039 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  3039
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 3040
     Identification <Id> [0..1] Text 3040
Or   Country <Ctry> [1..1] CodeSet C3 3040
Or   TypeAndIdentification <TpAndId> [1..1]  3040
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 3040
     Identification <Id> [1..1] IdentifierSet C2 3041
Or}   Proprietary <Prtry> [1..1] ± 3041
82.1.26.1.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a place of safekeeping.
Datatype: "LEIIdentifier" on page 3322
82.1.27 Securities Quantity
82.1.27.1  OriginalAndCurrentQuantities1
Definition: Original and current value of an asset-back instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FaceAmount <FaceAmt> [1..1] Amount 3114
   AmortisedValue <AmtsdVal> [1..1] Amount 3114
82.1.27.1.1  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, that is, the principal of a
debt instrument.
Datatype: "ImpliedCurrencyAndAmount" on page 3210
82.1.27.1.2  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Datatype: "ImpliedCurrencyAndAmount" on page 3210
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3114 August 2026
```

